def printTransactions(m, k, d, name, owned, prices):
    transactions = []
    
    for i in range(k):
        stock_name = name[i]
        num_owned = owned[i]
        price_history = prices[i]
        current_price = price_history[-1]
        
        if current_price > price_history[-2]:
            # Current price is higher than yesterday's price, consider selling
            if num_owned > 0:
                transactions.append(f"{stock_name} SELL {num_owned}")
        else:
            # Current price is not higher than yesterday's price, consider buying
            if m >= current_price:
                max_buyable = int(m // current_price)
                if max_buyable > 0:
                    transactions.append(f"{stock_name} BUY {max_buyable}")
                    m -= max_buyable * current_price
    
    # Output the transactions for the current day
    print(len(transactions))
    for transaction in transactions:
        print(transaction)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read initial parameters m, k, d
    m, k, d = map(float, data[0].split())
    m = int(m)  # Convert m to integer because the problem assumes m is integer
    k = int(k)  # Convert k to integer
    
    # Read stock details
    name = []
    owned = []
    prices = []
    for i in range(1, k + 1):
        stock_info = data[i].split()
        name.append(stock_info[0])
        owned.append(int(stock_info[1]))
        price_history = list(map(float, stock_info[2:]))
        prices.append(price_history)
    
    # Call the function
    printTransactions(m, k, int(d), name, owned, prices)

if __name__ == "__main__":
    main()
