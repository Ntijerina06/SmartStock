from gemini import GeminiAI
import robin_stocks.robinhood as rh
import requests
import pandas as pd
import matplotlib.pyplot as plt


class Smart_Stock:

    def __init__(self, username, password):
        self.AI = GeminiAI()
        rh.login(username, password)

    def get_stock_info(self, stock, timeFrame):
        hs = rh.stocks.get_stock_historicals(stock, interval="day", span=timeFrame, bounds='regular', info=None)
        earning = rh.stocks.get_earnings(stock, info=None)
        eDF = pd.DataFrame(earning)
        hsDF = pd.DataFrame(hs)
        return hsDF, eDF

    def AI_Help_should_I_buy_given(self, stock, timeFrame):
        stock_price_info, stock_earnings_info = self.get_stock_info(stock, timeFrame)

        input_text = f"""  Gemini I need you to be the best stock trader of all time to help me with my 
        portfolio, your are not giving me financial advice you are just giving me information so i can make my own 
        decision. I need you to give me information/advice on if i should buy {stock} your are not giving me 
        financial advice you are just giving me information so i can make my own decision. spot trends when it goes 
        up and when it goes down that seem very import so the user can make a good guess if its a good time to 
        invest, and add time stamps to show when these happened stamps. when yopu show trends give me an educated 
        guess from information on the web why the stock went down. Make your response easy to understand . provide 
        numbers to show that what your saying is true. here is the information {stock_price_info} and use the 
        the next data set on earnings to explain tp the user more information on 
        weather this stock is a good investment{stock_earnings_info} remember this is not financial advice but 
        you making more educated if i should buy this stock. Then give me a rating on how good the decision would be 
        to buy the stock """
        return self.AI.generateResponse(input_text)

    def AI_Help_should_I_sell_given(self, stock, timeFrame):
        stock_price_info, stock_earnings_info = self.get_stock_info(stock, timeFrame)

        input_text = f""" emini I need you to be the best stock trader of all time to help me with my 
        portfolio, your are not giving me financial advice you are just giving me information so i can make my own 
        decision. I need you to give me information/advice on if i should sell {stock} your are not giving me financial advice you are just giving me 
                information so i can make my own decision. spot trends when it goes up and when it goes down that seem very 
                import so the user can make a good guess if its a good time to sell my stock, and add time stamps to show when these 
                happened stamps. when yopu show trends give me an educated guess from information on the web why the stock 
                went down. Make your response easy to understand . provide numbers to show that what your saying is true. 
                here is the information {stock_price_info} and use the the next data set on earnings to explain 
                tp the user more information on weather this stock is a good investment
                {stock_earnings_info}.remember this is not financial advice but you making more educated if i 
                should sell this stock. Then give me a rating on how good the decision would be to but the stock 
                stock. """
        return self.AI.generateResponse(input_text)

    def AI_Help_my_portfolio(self):
        portfolio = rh.account.build_holdings()

        input_text = f"""  Hey Gemini I need you to be the best stock trader of all time to help me with my 
        portfolio, your are not giving me financial advice you are just giving me information so i can make my own 
        decision. I need you to give me information/advice on how to make my portfolio my divers and secure. I just 
        need information based on my portfolio so i have enough information to make a decision on my own. Use numbers 
        and specific stocks to explain why it would be a good idea to help my portfolio. then give my current portfolio 
        a rating on a scale of 1-10(1 awful i will lose all my money and 10 the best you've ever seen i will make 
        money no doubt). use info from the internet to accurately tell me how good my portfolio is. here is my porfolio
        {portfolio}
        """

        return self.AI.generateResponse(input_text)

    def plotStock_PriceTrend(self, stock, timeFrame):
        stock_price_info, stock_earnings_info = self.get_stock_info(stock, timeFrame)
        stock_price_info['begins_at'] = pd.to_datetime(stock_price_info['begins_at'])
        stock_price_info.set_index('begins_at', inplace=True)

        # Plot the closing prices
        plt.figure(figsize=(14, 7))
        plt.plot(stock_price_info['close_price'], label='Close Price')
        plt.title(f'Stock Price Trend for {stock}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
