


def Item(cost_item,):
    member=False
    date=(input("is day father day?(use yes or no):"))
    m=(input("Are you a member? (use Yes or No): "))
    
    print(m)
    if m=="yes"  :
        member=True 
    if member==True:
        cost=cost_item*10/100
        cost_item=cost_item-cost
        
    if date=="yes":
        cost=(cost_item*5)/100
        cost_item=cost_item-cost
        
    return cost_item






cost_item=100.0
print(Item(cost_item))
