import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def generate_duration_workload(num_tasks, min_dur, max_dur, horizon=720):
    """
    Generates synthetic task intervals with specific duration bounds.
    """
    tasks = []
    for t_id in range(num_tasks):
        duration = np.random.randint(min_dur, max_dur + 1)
        start = np.random.randint(0, horizon - duration + 1)
        finish = start + duration
        tasks.append({'id': t_id, 'start': start, 'finish': finish})
    return tasks

def is_compatible(slot, task):
    for t in slot:
        if max(t['start'], task['start']) < min(t['finish'], task['finish']):
            return False
    return True

def run_ctdm(tasks):
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

def run_edf(tasks):
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

def run_naive(tasks):
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

# ==============================================================================
# Simulation Execution
# ==============================================================================

NUM_TASKS = 100
TRIALS = 100

duration_configs = [
    (10, 30, 20),    # (min_dur, max_dur, mean_dur)
    (20, 60, 40),
    (30, 90, 60),
    (40, 120, 80),
    (60, 180, 120),
    (90, 270, 180),
    (120, 360, 240)
]

mean_durations = [config[2] for config in duration_configs]
ctdm_means, edf_means, naive_means = [], [], []

print("Running Experiment 4: Task Duration Variance...")
for min_d, max_d, mean_d in duration_configs:
    c_runs, e_runs, n_runs = [], [], []

    for _ in range(TRIALS):
        task_set = generate_duration_workload(NUM_TASKS, min_d, max_d)
        c_runs.append(run_ctdm(task_set))
        e_runs.append(run_edf(task_set))
        n_runs.append(run_naive(task_set))

    ctdm_means.append(np.mean(c_runs))
    edf_means.append(np.mean(e_runs))
    naive_means.append(np.mean(n_runs))

    print(f"Mean Duration: {mean_d:3d} min | CTDM: {ctdm_means[-1]:.1f} | EDF: {edf_means[-1]:.1f} | Naive: {naive_means[-1]:.1f}")

# ==============================================================================
# Plot Generation
# ==============================================================================

plt.figure(figsize=(8.5, 5), dpi=300)

plt.plot(mean_durations, ctdm_means,
         marker='s', color='#1f77b4',
         linewidth=2, label='CTDM')

plt.plot(mean_durations, edf_means,
         marker='^', color='#d62728',
         linewidth=2, label='EDF / Finish-Time First')

plt.plot(mean_durations, naive_means,
         marker='x', color='#7f7f7f',
         linestyle='--', linewidth=2,
         label='Naive / Randomized')


# X-axis label
plt.xlabel('Mean Task Duration $\\mu_D$ (minutes)',
           fontsize=17,
           fontweight='normal')

# Y-axis label
plt.ylabel('Number of Generated Slots ($l$)',
           fontsize=17,
           fontweight='normal')


# X-axis numbers
plt.xticks(mean_durations,
           fontsize=17,
           fontweight='normal')

# Y-axis numbers
plt.yticks(fontsize=17,
           fontweight='normal')


plt.grid(True, linestyle=':', alpha=0.7)


# Labels inside the figure
plt.legend(loc='upper left',
           fontsize=18,
           frameon=True,
           facecolor='white',
           framealpha=0.9)


plt.tight_layout()

plt.savefig('experiment4_ctdm_duration_variance.eps', dpi=300)

plt.show()