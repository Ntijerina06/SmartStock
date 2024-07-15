from smartStock import Smart_Stock
import robin_stocks.robinhood as rh
import pandas as pd

if __name__ == "__main__":
    ss = Smart_Stock("UserName", "Password")
    print(ss.AI_Help_my_portfolio())
