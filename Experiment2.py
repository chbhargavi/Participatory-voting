import time
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def generate_large_workload(num_tasks, horizon=1440, min_dur=30, max_dur=180):
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

def run_ctdm_timed(tasks):
    start_time = time.perf_counter()
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
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000.0  # Convert to ms

def run_edf_timed(tasks):
    start_time = time.perf_counter()
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
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000.0

def run_naive_timed(tasks):
    start_time = time.perf_counter()
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
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000.0

# ==============================================================================
# Simulation Execution
# ==============================================================================

task_counts = np.arange(100, 1001, 100)
trials = 50

ctdm_times, edf_times, naive_times = [], [], []

print("Running Experiment 2: Scalability Benchmarks...")
for N in task_counts:
    c_t, e_t, n_t = [], [], []
    for _ in range(trials):
        task_set = generate_large_workload(N)
        c_t.append(run_ctdm_timed(task_set))
        e_t.append(run_edf_timed(task_set))
        n_t.append(run_naive_timed(task_set))

    ctdm_times.append(np.mean(c_t))
    edf_times.append(np.mean(e_t))
    naive_times.append(np.mean(n_t))

    print(f"Tasks (|F|): {N:4d} | CTDM: {ctdm_times[-1]:6.2f} ms | EDF: {edf_times[-1]:6.2f} ms | Naive: {naive_times[-1]:6.2f} ms")

# ==============================================================================
# Plot Generation
# ==============================================================================

plt.figure(figsize=(8.5, 5), dpi=300)

plt.plot(task_counts, ctdm_times, marker='s', color='#1f77b4',
         linewidth=2, label='CTDM')

plt.plot(task_counts, edf_times, marker='^', color='#d62728',
         linewidth=2, label='EDF / Finish-Time First')

plt.plot(task_counts, naive_times, marker='x', color='#7f7f7f',
         linestyle='--', linewidth=2, label='Naive / Randomized')


# X-axis label
plt.xlabel('Number of Funded Tasks ($|\\mathbb{F}|$)',
           fontsize=19, fontweight='normal')

# Y-axis label
plt.ylabel('Execution Time (milliseconds)',
           fontsize=19, fontweight='normal')


# X-axis numbers
plt.xticks(task_counts, fontsize=14, fontweight='normal')

# Y-axis numbers
plt.yticks(fontsize=14, fontweight='normal')


plt.grid(True, linestyle=':', alpha=0.7)


# Labels inside the figure (legend)
plt.legend(loc='upper left',
           fontsize=16,
           frameon=True,
           facecolor='white',
           framealpha=0.9)


plt.tight_layout()

plt.savefig('experiment2_ctdm_scalability.eps', dpi=300)

plt.show()