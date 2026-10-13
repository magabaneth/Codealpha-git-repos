"""
CodeAlpha Task 2: Stock Portfolio Tracker
Calculates total investment value from hardcoded stock prices and
user-entered quantities. Optionally saves the result to a .txt or .csv file.
"""

import csv


STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_available_stocks():
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict {symbol: qty}."""
    portfolio = {}

    print("Enter your stocks one at a time. Type 'done' when finished.")
    while True:
        symbol = input("Stock symbol (or 'done'): ").upper().strip()

        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Stock not found. Please choose from the available list.")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

       
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    """Return (rows, total) where rows is a list of (symbol, qty, price, value)."""
    rows = []
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        rows.append((symbol, qty, price, value))
        total += value
    return rows, total


def display_summary(rows, total):
    print("\n=== Portfolio Summary ===")
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}")
    print("-" * 36)
    for symbol, qty, price, value in rows:
        print(f"{symbol:<8}{qty:>6}{price:>10}{value:>12}")
    print("-" * 36)
    print(f"Total investment value: ${total}")


def save_to_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write("Portfolio Summary\n")
        f.write("-" * 36 + "\n")
        for symbol, qty, price, value in rows:
            f.write(f"{symbol}: {qty} shares x ${price} = ${value}\n")
        f.write("-" * 36 + "\n")
        f.write(f"Total investment value: ${total}\n")
    print(f"Saved to {filename}")


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Goodbye!")
        return

    rows, total = calculate_total(portfolio)
    display_summary(rows, total)

    choice = input("\nSave results to a file? (txt / csv / no): ").lower().strip()
    if choice == "txt":
        save_to_txt(rows, total)
    elif choice == "csv":
        save_to_csv(rows, total)
    else:
        print("Results not saved.")


if __name__ == "__main__":
    main()
