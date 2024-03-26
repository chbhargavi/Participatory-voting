import random
import time
def measure_running_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    running_time = end_time - start_time
    print("Running time:", running_time )
def a1(n, task, budget, bids):
    winning_set = []
    utility = []
    for k in range(1, n):
        if bids[k - 1] <= budget / k:
            winning_set.append(bids[k - 1])
    k1= len(winning_set)
    print("Value of k (largest index):", len(winning_set))
    payment = min(budget / len(winning_set), bids[len(winning_set)])
    for i in range(len(winning_set)):
     utility.append(payment - bids[i])
    print("Sorted bids in increasing order:", bids)
    print("Winning set:", winning_set)
    print("Payment for winning agent:", [payment] * len(winning_set))
    print("payment sum:", sum([payment] * len(winning_set)))
    print("Utility for winning agent:", utility)
    print("Utility sum:", sum(utility))    
def a2(n,task,budget,bids):
    winning_set = []
    remaining_budget = budget
    for k, bid in enumerate(bids):
        if bid <= remaining_budget:
            winning_set.append(bid)
            remaining_budget -= bid
        else:
            break
    payment=[]
    for a in range(len(winning_set)):
        payment.append(winning_set[a])
    print("Sorted Bids (in increasing order):", bids)
    print("Winning set:", winning_set)
    total_payment = sum(payment)
    print("total payment", total_payment)
    utility = [winning_set[i] - payment[i] for i in range(len(winning_set))]
    remaining_budget = budget - total_payment
    print("Payment for the winning agents:", payment)
    print("Utility for each winning agent:", utility)
    print("Remaining budget:", remaining_budget)
def a3(n,task,budget,bids):
    print("Sorted Bids (in increasing order):", bids)
    winning_set=[]
    total_payment=0
    utility=[]
    count=0
    selected_bids=[]
    selected_bids=int(n/2)
    random_selected_agents_indices = random.sample(range(len(bids)), selected_bids)
    random_selected_agents = [bids[i] for i in random_selected_agents_indices]
    random_selected_agents.sort()
    print(" random_selected_agents:", random_selected_agents)
    random_selected_agents_indices.sort()
    print("random_selected_agents_indices:", random_selected_agents_indices)
    newlist=[]
    newlistflags=[]
    for i in range(n):
        if i in random_selected_agents_indices:
         newlist.append(bids[i]+(bids[i]*0.3))      
    print("newlist:", newlist)
    dupnewlist=newlist
    total_bids = []
    for i, bid in enumerate(bids):
        if i in random_selected_agents_indices :
            total_bids.append(newlist[random_selected_agents_indices.index(i)])
        else:
            total_bids.append(bid)
    print("Total Bids:", total_bids)
    total_bids.sort()
    print("Total Bids sorted(increasing order):", total_bids)
    winning_set = []
    remaining_budget = budget
    for k, total_bids in enumerate(total_bids):
        if total_bids <= remaining_budget:
           winning_set.append(total_bids)
           remaining_budget -= total_bids 
        else:
             break
    payment=[]
    for a in range(len(winning_set)):
        payment.append(winning_set[a])
    utility=[]
    print("Winning set:", winning_set)
    for i in range(len(winning_set)):
        if winning_set[i] in dupnewlist:
            index=newlist.index(winning_set[i])
            dupnewlist[index]=0
            utility.append(payment[i]-bids[index])   
        else:
           utility.append(0)
    total_payment = sum(payment)
    print("total payment", total_payment)
    print("Payment for the winning agents:", payment)
    print("Utility for each winning agent:", utility)
    print("utility sum:",sum(utility))
n = int(input("Enter the number of agents: "))
task = input("Enter the task: ")
budget = int(input("Enter the budget: "))
bids = []
for i in range(n):
    bid = random.gauss(17, 5)
    bids.append(bid)
    bids.sort()
print("*************** Algorithm 1 ************")
measure_running_time(a1, n, task, budget, bids)
print("*************** Algorithm 2 ************")
measure_running_time(a2, n, task, budget, bids)
print("*************** Algorithm 3 ************")
measure_running_time(a3, n, task, budget, bids)








