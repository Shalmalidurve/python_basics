
def Max_profit(list):
    max_profit=0
    for i in range (len(list)):
        for j in range (i,(len(list))):
            profit=list[j]-list[i]
            max_profit = max(profit,max_profit)

    for i in range (len(list)):
        for j in range (i,(len(list))):
            
            if max_profit==0:       
                return "no profit"
            else:
                if max_profit==list[j]-list[i]:
                    return f"Buy at {list[i]}; sellat {list[j]} ; maximum profit is {max_profit}"
list=[int(x) for x in input("Enter numbers: ").split()]
print(Max_profit(list))

