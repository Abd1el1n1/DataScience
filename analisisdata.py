import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

AMDData = yf.Ticker('AMD')
f_inicio = '2019-1-1'
hoy = datetime.today().strftime('%Y-%m-%d')
AMDDf = AMDData.history(period='1d', start=f_inicio, end=hoy)

AMDDf['High'].plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20, 15))

NVDAData = yf.Ticker('NVDA')
f_inicio = '2019-1-1'
hoy = datetime.today().strftime('%Y-%m-%d')
NVDADf = NVDAData.history(period='1d', start=f_inicio, end=hoy)

NVDADf['High'].plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20, 15))
plt.show()