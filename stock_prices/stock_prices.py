#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = prices[1] - prices[0]
    prices.remove(prices[0])
    # temp_prices = prices.copy()
    for i in range(len(prices)):
        # print(i)
        for _ in range(len(prices)-1):
            # print(_)
            current_profit = prices[_+1] - prices[0]
            # print(current_profit)
            if current_profit > max_profit:
                max_profit = current_profit

        # print(prices)
        prices.remove(prices[0])
        # print(temp_prices)
    return max_profit


# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))