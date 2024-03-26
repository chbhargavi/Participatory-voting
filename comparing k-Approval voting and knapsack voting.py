import numpy as np
import random
def a1(n, t, budget):
   
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
    print("\nPreferences of each Agent:")
    for agent, preferences in agent_votes.items():
        print(f"Agent {agent}: {preferences}")
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
def a2(n, t, budget):
   
    for agent in range(1, n + 1):
        preferences = random.sample(range(1, t + 1), t)
        selected_tasks = []
        remaining_budget = budget
        for preference in preferences:
            task_cost = task_costs[preference]
            if remaining_budget >= task_cost:
                selected_tasks.append(preference)
                remaining_budget -= task_cost
            else:    
                continue
        agent_votes[agent] = selected_tasks
    print("\nPreferences of each Agent:")
    for agent, preferences in agent_votes.items():
        print(f"Agent {agent}: {preferences}")
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
n = int(input("Enter no.of agents:"))
t = int(input("Enter no. of tasks:"))
budget = int(input("Enter Budget:"))
tasks = []
total_cost = 0
budget1 = budget
task_costs = {i:float(input(f"Enter the cost for Task {i}: ")) for i in range(1, t + 1)}
agent_votes = {} 
print("***************Algorithm 1************")
a1(n,t,budget)
print("***************Algorithm 2************")
a2(n,t,budget)       