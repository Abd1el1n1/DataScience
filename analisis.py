import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

NDAQData = yf.Ticker('NDAQ')
f_inicio = '2019-1-1'
hoy = datetime.today().strftime('%Y-%m-%d')
NDAQDf = NDAQData.history(period='1d', start=f_inicio, end=hoy)

NDAQnorma = NDAQDf['High'].max()
NDAQDf['High'].div(NDAQnorma).plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20, 15),label='NDAQ')

GSPCData = yf.Ticker('GSPC')
f_inicio = '2019-1-1'
hoy = datetime.today().strftime('%Y-%m-%d')
GSPCDf = GSPCData.history(period='1d', start=f_inicio, end=hoy)

GSPCnorma = GSPCDf['High'].max()
GSPCDf['High'].div(GSPCnorma).plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20, 15),label='GSPC')
plt.legend()
plt.show()