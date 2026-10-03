import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def generate_workload(num_tasks=100, horizon=720, min_dur=30, max_dur=120):
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

def pack_slots_ctdm(tasks):
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
    return [len(s) for s in slots]

def pack_slots_edf(tasks):
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
    return [len(s) for s in slots]

def pack_slots_naive(tasks):
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
    return [len(s) for s in slots]

# ==============================================================================
# Simulation Execution Setup
# ==============================================================================

NUM_TASKS = 100
TRIALS = 100
MAX_SLOTS_TRACK = 25  # Limit slot display for clear visualization

ctdm_counts_all, edf_counts_all, naive_counts_all = [], [], []

print("Running Experiment 3: Slot Load Balancing...")
for _ in range(TRIALS):
    task_set = generate_workload(NUM_TASKS)

    ctdm_counts_all.append(pack_slots_ctdm(task_set))
    edf_counts_all.append(pack_slots_edf(task_set))
    naive_counts_all.append(pack_slots_naive(task_set))

# Align matrix shapes across trials by padding with zeros
def average_slot_distribution(counts_list, max_len=25):
    padded = np.zeros((len(counts_list), max_len))
    for i, counts in enumerate(counts_list):
        length = min(len(counts), max_len)
        padded[i, :length] = counts[:length]
    return np.mean(padded, axis=0)

avg_ctdm = average_slot_distribution(ctdm_counts_all, MAX_SLOTS_TRACK)
avg_edf = average_slot_distribution(edf_counts_all, MAX_SLOTS_TRACK)
avg_naive = average_slot_distribution(naive_counts_all, MAX_SLOTS_TRACK)

# ==============================================================================
# Plot Generation
# ==============================================================================

slot_indices = np.arange(1, MAX_SLOTS_TRACK + 1)

plt.figure(figsize=(9, 5), dpi=300)

plt.plot(slot_indices, avg_ctdm,
         marker='s', color='#1f77b4',
         linewidth=2, label='CTDM')

plt.plot(slot_indices, avg_edf,
         marker='^', color='#d62728',
         linewidth=2, label='EDF / Finish-Time First')

plt.plot(slot_indices, avg_naive,
         marker='x', color='#7f7f7f',
         linestyle='--', linewidth=2,
         label='Naive / Randomized')


# X-axis label
plt.xlabel('Slot Index ($l$)',
           fontsize=19,
           fontweight='normal')

# Y-axis label
plt.ylabel('Average Tasks Assigned per Slot',
           fontsize=19,
           fontweight='normal')


# X-axis numbers
plt.xticks(np.arange(1, MAX_SLOTS_TRACK + 1, 2),
           fontsize=15,
           fontweight='normal')

# Y-axis numbers
plt.yticks(fontsize=15,
           fontweight='normal')


plt.grid(True, linestyle=':', alpha=0.7)


# Labels inside the figure
plt.legend(loc='upper right',
           fontsize=18,
           frameon=True,
           facecolor='white',
           framealpha=0.9)


plt.tight_layout()

plt.savefig('experiment3_ctdm_packing_efficiency.eps', dpi=300)

plt.show()