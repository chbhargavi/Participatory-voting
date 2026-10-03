import random
from datetime import datetime, timedelta
n = int(input("Enter no.of city dwellers:"))
t = int(input("Enter no. of tasks:"))
E= int(input("Enter no. of Executors:"))
budget = int(input("Enter Budget:"))
tasks = []
total_cost = 0
budget1 = budget
executor_cost={j:random.randint(5,35) for j in range(1,E + 1)}
print("\nExecutor bid costs:")
for j in range(1, E + 1):
    print(f"Executor {j} bid cost: {executor_cost[j]}")
# task_costs = {i: random.randint(5, 30) for i in range(1, t + 1)}
# for i in range(1, t + 1):
#     print(f"Task {i} cost: {task_costs[i]}")
task_costs = {i: random.randint(5, 30) for i in range(1, t + 1)}
task_times = {}
for i in range(1, t + 1):
    # Random starting time between 8:00 AM and 6:00 PM
    start_minutes = random.randint(8 * 60, 18 * 60)
    start_time = datetime(2026, 1, 1) + timedelta(minutes=start_minutes)
    # Random duration between 30 minutes and 3 hours
    duration = random.randint(30, 180)
    finish_time = start_time + timedelta(minutes=duration)
    task_times[i] = {
        "start": start_time,
        "finish": finish_time
    }
print("\nTasks costs along with starting and finishing time:")
for i in range(1, t + 1):
    print(
        f"Task {i} | "
        f"Cost: {task_costs[i]} | "
        f"Starting Time: {task_times[i]['start'].strftime('%I:%M %p')} | "
        f"Finishing Time: {task_times[i]['finish'].strftime('%I:%M %p')}"
    )
agent_votes = {}
for agent in range(1, n + 1):
    preferences = random.sample(range(1, t + 1), t)
    selected_tasks = []
    remaining_budget = budget
    for preference in preferences:
        task_cost = task_costs[preference]
        if selected_tasks.append(preference):
            remaining_budget -= task_cost
        else:    
            continue
    agent_votes[agent] = selected_tasks
print("\nPreferences of each city dwellers:")
for agent, preferences in agent_votes.items():
    print(f"city dwellers {agent}: {preferences}")
agents = list(agent_votes.values())
sel_tasks = []
tasks = [i+1 for i in range(t)]
for pref in range(1,t+1):  
    if budget>0:
        first_elements_counts = {}
        for agent_list in agents:
            if (agent_list):  
                if ((len(agent_list))>(pref-1)):
                    first_element = agent_list[pref-1]
                    if first_element in first_elements_counts:
                        first_elements_counts[first_element] += 1
                    else:
                        first_elements_counts[first_element] = 1
        pref_dict =  {k: v for k, v in sorted(first_elements_counts.items(), key=lambda item: item[1],reverse=True)}
        
        pref_dict = {k:v for k,v in pref_dict.items() if k in tasks}
        if pref_dict:
            print(f"\nSorted the Tasks in descending order based on their {pref} preference votes:")
            for task, votes in pref_dict.items():
                print(f"Task {task}: {votes} votes")                
    sel_iter = []
    for k,v in pref_dict.items():
        if (v!=0):
            budget = budget - task_costs[k]
            if budget>=0:
                sel_tasks.append(k)
                sel_iter.append(k)
                tasks.remove(k)
            else:
                budget = budget + task_costs[k]
    if pref_dict:
        print("\nSelected Tasks within the budget:")
        for task in sel_iter:
            print(f"Task {task} selected")

        print("Remaining_budget:", budget)
        print("\nRemaining Tasks:", tasks)
    if budget==0:
        break
    temp = [t for t in tasks if task_costs[t]<=budget]
    if len(temp)==0:
        break

# ---------------------------------------------------------
# OVERALL FINAL RESULT
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("                 OVERALL FINAL RESULT")
print("=" * 60)

# Overall selected tasks
print("\nOverall Selected Tasks:")
if sel_tasks:
    for task in sel_tasks:
        print(
            f"Task {task} | Cost: {task_costs[task]}"
        )
else:
    print("No tasks selected.")

print("\nSelected Tasks Count:", len(sel_tasks))

# Total cost of selected tasks
total_selected_cost = sum(task_costs[task] for task in sel_tasks)

print("Total Cost of Selected Tasks:", total_selected_cost)

# Remaining budget
print("Original Budget:", budget1)
print("Remaining Budget:", budget)

# Remaining tasks
print("\nRemaining Tasks:")
if tasks:
    for task in tasks:
        print(
            f"Task {task} | Cost: {task_costs[task]}"
        )
else:
    print("No remaining tasks.")

print("\nRemaining Tasks Count:", len(tasks))

print("\n" + "=" * 60)   

# ---------------------------------------------------------
# INTERVAL PARTITIONING / COMPATIBLE TASKS DISTRIBUTION
# WITH COMPLETE STEP-BY-STEP CALCULATION
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("       INTERVAL PARTITIONING / SLOT FORMATION")
print("=" * 70)

# Step 1: Consider only selected tasks
selected_task_list = []

for task in sel_tasks:
    selected_task_list.append((
        task,
        task_times[task]["start"],
        task_times[task]["finish"]
    ))

print("\nSTEP 1: SELECTED TASKS")
print("-" * 70)

for task, start, finish in selected_task_list:
    pass
    print(
        f"Task {task} | "
        f"Cost: {task_costs[task]} | "
        f"Start: {start.strftime('%I:%M %p')} | "
        f"Finish: {finish.strftime('%I:%M %p')}"
    )


# Step 2: Sort according to starting time
selected_task_list.sort(key=lambda x: x[1])

print("\nSTEP 2: SORT TASKS IN ASCENDING ORDER OF STARTING TIME")
print("-" * 70)

for position, (task, start, finish) in enumerate(selected_task_list, start=1):
    pass
    print(
        f"{position}. Task {task} | "
        f"Start: {start.strftime('%I:%M %p')} | "
        f"Finish: {finish.strftime('%I:%M %p')}"
    )


# ---------------------------------------------------------
# SLOT FORMATION
# ---------------------------------------------------------

slots = []

# print("\n" + "=" * 70)
# print("STEP 3: SLOT FORMATION")
# print("=" * 70)

for task, start, finish in selected_task_list:

    # print("\n" + "-" * 70)
    # print(
    #     f"CURRENT TASK: Task {task}\n"
    #     f"Cost: {task_costs[task]}\n"
    #     f"Start Time: {start.strftime('%I:%M %p')}\n"
    #     f"Finish Time: {finish.strftime('%I:%M %p')}"
    # )

    placed = False

    # -----------------------------------------------------
    # Check all existing slots
    # -----------------------------------------------------

    if len(slots) == 0:

        # print("\nNo slots exist yet.")
        # print(f"Therefore, creating Slot 1.")

        slots.append([(task, start, finish)])

        # print(f"Task {task} placed in Slot 1.")

        # print("\nCurrent Slot 1:")
        for existing_task, existing_start, existing_finish in slots[0]:
            pass
            # print(
            #     f"  Task {existing_task}: "
            #     f"{existing_start.strftime('%I:%M %p')} - "
            #     f"{existing_finish.strftime('%I:%M %p')}"
            # )

        continue


    # -----------------------------------------------------
    # Check each slot
    # -----------------------------------------------------

    for slot_number, slot in enumerate(slots, start=1):

        # print("\n" + "-" * 50)
        # print(f"Checking Slot {slot_number}")
        # print("-" * 50)

        # print(f"Task {task} must be compatible with ALL tasks in Slot {slot_number}.")

        compatible = True

        # Check current task against every task in slot
        for existing_task, existing_start, existing_finish in slot:

            # print(f"\nChecking Task {task} against Task {existing_task}:" )

            # print(
            #     f"  Current Task {task}: "
            #     f"{start.strftime('%I:%M %p')} - "
            #     f"{finish.strftime('%I:%M %p')}"
            # )

            # print(
            #     f"  Existing Task {existing_task}: "
            #     f"{existing_start.strftime('%I:%M %p')} - "
            #     f"{existing_finish.strftime('%I:%M %p')}"
            # )

            # -------------------------------------------------
            # Overlap condition
            # -------------------------------------------------

            if start < existing_finish and finish > existing_start:

                # print(
                #     f"\n  Result: NOT COMPATIBLE"
                # )

                # print(
                #     f"  Task {task} overlaps with Task {existing_task}."
                # )

                # print(
                #     f"  Therefore, Task {task} CANNOT be placed "
                #     f"in Slot {slot_number}."
                # )

                compatible = False
                break

            else:
                pass
                # print(
                #     f"\n  Result: COMPATIBLE"
                # )

                # print(
                #     f"  Task {task} does not overlap "
                #     f"with Task {existing_task}."
                # )


        # -------------------------------------------------
        # Place task if compatible
        # -------------------------------------------------

        if compatible:

            # print(
            #     f"\nTask {task} is compatible with ALL tasks "
            #     f"in Slot {slot_number}."
            # )

            # print(
            #     f"Therefore, Task {task} is placed in Slot {slot_number}."
            # )

            slot.append((task, start, finish))

            placed = True

            # Show current slot
            # print(f"\nUpdated Slot {slot_number}:")

            for existing_task, existing_start, existing_finish in slot:
                pass
                # print(
                #     f"  Task {existing_task} | "
                #     f"Start: {existing_start.strftime('%I:%M %p')} | "
                #     f"Finish: {existing_finish.strftime('%I:%M %p')}"
                # )

            break

        else:
            pass

            # print(
            #     f"\nTask {task} cannot be placed in Slot {slot_number}."
            # )

            # print("Moving to the next slot...")


    # -----------------------------------------------------
    # Create new slot if task cannot fit anywhere
    # -----------------------------------------------------

    if not placed:

        new_slot_number = len(slots) + 1

        # print("\n" + "-" * 50)
        # print("NO COMPATIBLE SLOT FOUND")
        # print("-" * 50)

        # print(
        #     f"Task {task} is not compatible with "
        #     f"any existing slot."
        # )

        # print(
        #     f"Therefore, creating a NEW Slot {new_slot_number}."
        # )

        slots.append([(task, start, finish)])

        # print(
        #     f"Task {task} placed in Slot {new_slot_number}."
        # )

        # print(f"\nCurrent Slot {new_slot_number}:")

        for existing_task, existing_start, existing_finish in slots[-1]:
            pass
            # print(
            #     f"  Task {existing_task} | "
            #     f"Start: {existing_start.strftime('%I:%M %p')} | "
            #     f"Finish: {existing_finish.strftime('%I:%M %p')}"
            # )


# ---------------------------------------------------------
# FINAL SLOT RESULT
# ---------------------------------------------------------

print("\n\n" + "=" * 70)
print("                 FINAL SLOT FORMATION")
print("=" * 70)

for slot_number, slot in enumerate(slots, start=1):

    print(f"\nSLOT {slot_number}")
    print("-" * 70)

    for task, start, finish in slot:

        print(
            f"Task {task} | "
            f"Cost: {task_costs[task]} | "
            f"Start: {start.strftime('%I:%M %p')} | "
            f"Finish: {finish.strftime('%I:%M %p')}"
        )

    print(f"Number of tasks in Slot {slot_number}: {len(slot)}")


print("\n" + "=" * 70)
print(f"TOTAL NUMBER OF SLOTS: {len(slots)}")
print("=" * 70)

# ---------------------------------------------------------
# ALGORITHM 3
# ALLOCATION AND PRICING RULE
# ---------------------------------------------------------

W = []
p = {}

print("\n\n" + "=" * 80)
print("ALGORITHM 3: ALLOCATION AND PRICING RULE")
print("=" * 80)


# =========================================================
# PROCESS EACH AVAILABLE SLOT
# =========================================================

for slot_number, slot in enumerate(slots, start=1):

    print("\n\n" + "=" * 80)
    print(f"SLOT {slot_number}")
    print("=" * 80)


    # =====================================================
    # SORT TASKS IN THIS SLOT BY INCREASING START TIME
    # =====================================================

    slot_tasks = sorted(
        slot,
        key=lambda x: x[1]
    )


    print("\nTASKS IN SLOT - SORTED BY STARTING TIME")
    print("-" * 80)


    for position, (
        task,
        start,
        finish
    ) in enumerate(
        slot_tasks,
        start=1
    ):

        print(
            f"{position}. Task {task} | "
            f"Start = {start.strftime('%I:%M %p')} | "
            f"Finish = {finish.strftime('%I:%M %p')} | "
            f"Task Cost (B_i) = {task_costs[task]}"
        )


    # =====================================================
    # RANDOMLY SELECT AVAILABLE EXECUTORS FOR THIS SLOT
    # =====================================================

    number_of_executors = random.randint(
        2,
        E
    )


    available_executors = random.sample(
        range(1, E + 1),
        number_of_executors
    )


    print("\nAVAILABLE TASK EXECUTORS")
    print("-" * 80)


    for executor in available_executors:

        print(
            f"Executor {executor} | "
            f"Bid Cost (c_f) = "
            f"{executor_cost[executor]}"
        )


    # =====================================================
    # SORT EXECUTORS BY INCREASING BID COST
    # =====================================================

    sorted_executors = sorted(
        available_executors,
        key=lambda executor: executor_cost[executor]
    )


    print("\nEXECUTORS SORTED BY INCREASING BID COST")
    print("-" * 80)


    for position, executor in enumerate(
        sorted_executors,
        start=1
    ):

        print(
            f"{position}. Executor {executor} | "
            f"Bid Cost (c_f) = "
            f"{executor_cost[executor]}"
        )


    # =====================================================
    # PROCESS EACH TASK IN THE CURRENT SLOT
    # =====================================================

    for task_position, (
        task,
        start,
        finish
    ) in enumerate(
        slot_tasks,
        start=1
    ):


        print("\n\n" + "#" * 80)
        print(
            f"TASK {task} - SLOT {slot_number}"
        )
        print("#" * 80)


        # =================================================
        # B_i IS THE COST OF THIS PARTICULAR TASK
        # =================================================

        B_i = task_costs[task]


        print("\nB_i FOR THIS TASK")
        print("-" * 80)

        print(
            f"Task {task} cost = {B_i}"
        )

        print(
            f"Therefore, B_i = {B_i}"
        )


        # =================================================
        # k <- 1
        # =================================================

        k = 1


        # Temporary winning executors for this task
        W_j_f = []


        print("\nk <- 1")
        print(f"Current k = {k}")


        # =================================================
        # CHECK EXECUTORS IN INCREASING BID ORDER
        # =================================================

        print("\nWINNER SELECTION")
        print("-" * 80)


        for executor_position, executor in enumerate(
            sorted_executors,
            start=1
        ):


            # ---------------------------------------------
            # c_f IS THE BID COST OF THIS EXECUTOR
            # ---------------------------------------------

            c_f = executor_cost[executor]


            print("\n" + "." * 70)

            print(
                f"Checking Executor {executor}"
            )

            print(
                f"Executor bid cost c_f = {c_f}"
            )

            print(
                f"Task cost B_i = {B_i}"
            )

            print(
                f"Current k = {k}"
            )


            # ---------------------------------------------
            # Calculate floor(B_i / k)
            # ---------------------------------------------

            budget_limit = B_i // k


            print("\nWinner condition:")

            print(
                "c_f <= floor(B_i / k)"
            )

            print(
                f"{c_f} <= floor({B_i} / {k})"
            )

            print(
                f"{c_f} <= {budget_limit}"
            )


            # =================================================
            # WINNER CONDITION
            # =================================================

            if c_f <= budget_limit:


                print(
                    "\nTRUE"
                )

                print(
                    f"{c_f} <= {budget_limit}"
                )

                print(
                    f"Executor {executor} "
                    f"is a WINNER."
                )


                # ---------------------------------------------
                # W_j^f <- W_j^f U {e_f}
                # ---------------------------------------------

                W_j_f.append(
                    executor
                )


                print(
                    "\nW_j^f = "
                    f"{W_j_f}"
                )


                # ---------------------------------------------
                # k <- k + 1
                # ---------------------------------------------

                k = k + 1


                print(
                    "\nk <- k + 1"
                )

                print(
                    f"New k = {k}"
                )


            else:


                print(
                    "\nFALSE"
                )

                print(
                    f"{c_f} > {budget_limit}"
                )

                print(
                    f"Executor {executor} "
                    f"is REJECTED."
                )


                print(
                    "\nBecause executors are sorted "
                    "in increasing order of bid cost,"
                )

                print(
                    "all remaining executors have "
                    "equal or higher bid costs."
                )

                print(
                    "Therefore, STOP checking executors "
                    "for this task."
                )


                break


        # =================================================
        # DISPLAY WINNERS
        # =================================================

        print("\n" + "-" * 80)
        print(
            f"WINNERS FOR TASK {task}"
        )
        print("-" * 80)


        if W_j_f:

            for executor in W_j_f:

                print(
                    f"Executor {executor} | "
                    f"Bid Cost = "
                    f"{executor_cost[executor]}"
                )

        else:

            print(
                "No winner for this task."
            )


        # =================================================
        # ADD WINNERS TO W
        # =================================================

        for executor in W_j_f:

            W.append(
                (
                    slot_number,
                    task,
                    executor
                )
            )


        # =========================================================
        # PAYMENT RULE
        #
        # p_i <- min{
        #          floor(B_i / k),
        #          c_(k+1)
        #        }
        # =========================================================

        if W_j_f:

            print("\n" + "=" * 80)
            print(f"PAYMENT CALCULATION FOR TASK {task}")
            print("=" * 80)

            # B_i = cost of the particular task
            B_i = task_costs[task]

            # k = number of selected/winning executors
            k = len(W_j_f)

            print(
                f"B_i = Task {task} cost = {B_i}"
            )

            print(
                f"Number of winning executors k = {k}"
            )


            # -----------------------------------------------------
            # First part:
            # floor(B_i / k)
            # -----------------------------------------------------

            budget_part = B_i // k

            print("\nFirst part of payment formula:")

            print(
                f"floor(B_i / k)"
            )

            print(
                f"= floor({B_i} / {k})"
            )

            print(
                f"= {budget_part}"
            )


            # -----------------------------------------------------
            # Second part:
            # c_(k+1)
            #
            # This is the BID COST of the (k+1)-th executor
            # in the sorted executor list.
            # -----------------------------------------------------

            if k < len(sorted_executors):

                next_executor = sorted_executors[k]

                c_k_plus_1 = executor_cost[next_executor]

                print(
                    "\nSecond part of payment formula:"
                )

                print(
                    f"c_(k+1) = bid cost of "
                    f"the ({k}+1)-th executor"
                )

                print(
                    f"({k}+1)-th executor = "
                    f"Executor {next_executor}"
                )

                print(
                    f"c_(k+1) = {c_k_plus_1}"
                )

            else:

                # No next executor exists
                c_k_plus_1 = budget_part

                print(
                    "\nThere is no (k+1)-th executor."
                )

                print(
                    f"c_(k+1) = {c_k_plus_1}"
                )

            # =================================================
            # PAYMENT FORMULA
            # =================================================

            print("\nPAYMENT FORMULA:")

            print(
                "p_i = min{"
                "floor(B_i / k), "
                "c_(k+1)"
                "}"
            )


            print(
                f"p_i = min{{"
                f"{budget_part}, "
                f"{c_k_plus_1}"
                "}"
            )


            # ---------------------------------------------
            # Calculate payment
            # ---------------------------------------------

            payment = min(
                budget_part,
                c_k_plus_1
            )


            print(
                f"\np_i = {payment}"
            )


            # =================================================
            # GIVE PAYMENT TO EVERY WINNING EXECUTOR
            # =================================================

            print(
                "\nPAYMENT TO WINNING EXECUTORS:"
            )


            for executor in W_j_f:


                if executor not in p:

                    p[executor] = []


                p[executor].append(
                    (
                        task,
                        payment
                    )
                )


                print(
                    f"Executor {executor} | "
                    f"Bid Cost = "
                    f"{executor_cost[executor]} | "
                    f"Payment = {payment}"
                )


        else:


            print(
                f"\nNo payment for Task {task} "
                f"because there is no winner."
            )


# =========================================================
# FINAL W AND P
# =========================================================

print("\n\n" + "=" * 80)
print("FINAL ALLOCATION W")
print("=" * 80)


if W:

    for (
        slot_number,
        task,
        executor
    ) in W:

        print(
            f"Slot {slot_number} | "
            f"Task {task} | "
            f"Executor {executor} | "
            f"Bid Cost = "
            f"{executor_cost[executor]}"
        )

else:

    print(
        "W = empty set"
    )


print("\n" + "=" * 80)
print("FINAL PAYMENT p")
print("=" * 80)


if p:

    for executor, payment_list in p.items():

        for task, payment in payment_list:

            print(
                f"Executor {executor} | "
                f"Task {task} | "
                f"Payment = {payment}"
            )

else:

    print(
        "p = empty set"
    )


