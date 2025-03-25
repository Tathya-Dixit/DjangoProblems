
def minloss(price):
    mini = 0
    minj = 0
    minloss = 1000000 # initializing minimum loss with infinity
    for i in range(0,len(price)-1):
        for j in range(i+1, len(price)):
            if price[i] - price[j] < 0:
                continue
            if price[i] - price[j] < minloss:
                minloss = price[i] - price[j]
                mini = i
                minj = j
            elif price[i] - price[j] == minloss:# added this condition so that the cost is also minimum
                if price[i] < price[mini]:
                    mini = i
                    minj = j
    return minloss, mini, minj

price = list(map(int, input("Enter the prices: ").split()))
loss, buy, sell = minloss(price)
print(f"Minimum loss : {loss}\nYear to buy : {buy}\nYear to sell : {sell}")