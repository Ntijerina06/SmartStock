from smartStock import Smart_Stock
import robin_stocks.robinhood as rh
import pandas as pd

if __name__ == "__main__":
    ss = Smart_Stock("noahtijerina06@gmail.com", "March3106$")
    print(ss.AI_Help_my_portfolio())
