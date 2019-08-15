#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if len(prices) < 2:
    return "Need two prices to compare"

  profit = prices[1] - prices[0]            #sets initial max profit
  buy_low = prices[0]                       #marker - starts lowest price at first price

  for i in range(1, len(prices)):           #skips index 0
    current_price = prices[i]
    current_gain = current_price - buy_low  #profit comparison at current marker
    profit = max(profit, current_gain)      #compares against current determined max profit
    buy_low = min(buy_low, current_price)   #compares and sets the lowest stock price
      
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))