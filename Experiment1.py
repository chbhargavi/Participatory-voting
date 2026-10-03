import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

def generate_tasks(num_tasks, horizon=720, min_dur=30, max_dur=120):
    """
    Generates synthetic task intervals (start_time, finish_time).
    """
    tasks = []
    for i in range(num_tasks):
        duration = np.random.randint(min_dur, max_dur + 1)
        start = np.random.randint(0, horizon - duration + 1)
        finish = start + duration
        tasks.append({'id': i, 'start': start, 'finish': finish})
    return tasks

def is_compatible(slot_tasks, task):
    """
    Checks if a task is compatible (non-overlapping) with all tasks in a slot.
    """
    for t in slot_tasks:
        # Overlap condition: max(start1, start2) < min(finish1, finish2)
        if max(t['start'], task['start']) < min(t['finish'], task['finish']):
            return False
    return True

def schedule_ctdm(tasks):
    """
    CTDM: Sort by non-decreasing start time, greedy first-fit insertion.
    """
    sorted_tasks = sorted(tasks, key=lambda x: x['start'])
    slots = []
    for task in sorted_tasks:
        placed = False
        for slot in slots:
            if is_compatible(slot, task):
                slot.append(task)
                placed = True
                break
        if not placed:
            slots.append([task])
    return len(slots)

def schedule_edf(tasks):
    """
    EDF / Finish-Time First: Sort by non-decreasing finish time, greedy insertion.
    """
    sorted_tasks = sorted(tasks, key=lambda x: x['finish'])
    slots = []
    for task in sorted_tasks:
        placed = False
        for slot in slots:
            if is_compatible(slot, task):
                slot.append(task)
                placed = True
                break
        if not placed:
            slots.append([task])
    return len(slots)

def schedule_naive(tasks):
    """
    Naive / Randomized: Unsorted insertion based on arrival sequence.
    """
    shuffled_tasks = tasks.copy()
    np.random.shuffle(shuffled_tasks)
    slots = []
    for task in shuffled_tasks:
        placed = False
        for slot in slots:
            if is_compatible(slot, task):
                slot.append(task)
                placed = True
                break
        if not placed:
            slots.append([task])
    return len(slots)

# ==========================================
# Monte Carlo Simulation Pipeline
# ==========================================

task_counts = np.arange(20, 201, 20)
num_trials = 100

ctdm_results = []
edf_results = []
naive_results = []

print("Running Monte Carlo Simulations...")

for N in task_counts:
    ctdm_slots, edf_slots, naive_slots = [], [], []

    for _ in range(num_trials):
        tasks = generate_tasks(N)

        ctdm_slots.append(schedule_ctdm(tasks))
        edf_slots.append(schedule_edf(tasks))
        naive_slots.append(schedule_naive(tasks))

    ctdm_results.append(np.mean(ctdm_slots))
    edf_results.append(np.mean(edf_slots))
    naive_results.append(np.mean(naive_slots))

    print(
        f"Tasks: {N:3d} | "
        f"CTDM: {ctdm_results[-1]:.1f} | "
        f"EDF: {edf_results[-1]:.1f} | "
        f"Naive: {naive_results[-1]:.1f}"
    )

# ==========================================
# Plotting Results
# ==========================================

fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)

ax.plot(
    task_counts,
    ctdm_results,
    marker='s',
    color='blue',
    linewidth=3,
    markersize=9,
    label='CTDM'
)

ax.plot(
    task_counts,
    edf_results,
    marker='^',
    color='red',
    linewidth=3,
    markersize=9,
    label='EDF / Finish-Time First'
)

ax.plot(
    task_counts,
    naive_results,
    marker='x',
    color='gray',
    linestyle='--',
    linewidth=3,
    markersize=9,
    label='Naive / Randomized'
)

# ------------------------------------------
# Axis labels - NORMAL FONT
# ------------------------------------------

ax.set_xlabel(
    'Number of Funded Tasks (|F|)',
    fontsize=29,
    fontweight='normal',
    labelpad=15
)

ax.set_ylabel(
    'Number of Generated Slots (l)',
    fontsize=29,
    fontweight='normal',
    labelpad=18
)

# ------------------------------------------
# Tick labels - NORMAL FONT
# ------------------------------------------

ax.set_xticks(task_counts)

ax.tick_params(
    axis='x',
    labelsize=24,
    width=1.5,
    length=6
)

ax.tick_params(
    axis='y',
    labelsize=24,
    width=1.5,
    length=6
)

# ------------------------------------------
# Grid
# ------------------------------------------

ax.grid(
    True,
    linestyle='--',
    linewidth=1.2,
    alpha=0.6
)

# ------------------------------------------
# Legend
# ------------------------------------------

ax.legend(
    loc='upper left',
    fontsize=23,
    frameon=True
)

# ------------------------------------------
# Border
# ------------------------------------------

for spine in ax.spines.values():
    spine.set_linewidth(1.5)

# ------------------------------------------
# Adjust margins
# ------------------------------------------

fig.subplots_adjust(
    left=0.18,
    right=0.98,
    bottom=0.18,
    top=0.98
)

# ------------------------------------------
# Save figure
# ------------------------------------------

plt.savefig(
    'experiment1_ctdm_comparison.eps',
    dpi=300,
    bbox_inches='tight'
)

plt.show()