import yfinance as yf
import streamlit as st

st.write("""
# Google Stock Price App


Shown are the stock **closing price** and **volume** of Google!
""")

#define the ticker symbol of Google
tickerSymbol = 'GOOGL'


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#getting the prices for this ticker between a period of time
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


# Displays info- Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write(""" 
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write(""" 
## Volume
""")
st.line_chart(tickerDf.Volume)