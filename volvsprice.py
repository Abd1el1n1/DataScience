import yfinance as yf
##import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#print("1. analisis normalizado")
#print("2. analisis sin normalizar")
#opt = int(input())

accion = str(input("Accion Vol y Precio"))


accionData = yf.Ticker(accion)

accionDf = accionData.history(period='1d',start='2019-1-1',end=datetime.today().strftime('%Y-%m-%d'))

#accionDf.to_csv(str(accion)+'.csv',index=False)

norm_accion = accionDf['High'].max()
vol_accion = accionDf['Volume'].max()
#fig, ax = plt.subplots()

#ax.legend(label='This is My Legend Title')
plt.figure(1)
accionDf['High'].div(norm_accion).plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20,10),label="High",marker='o')
accionDf['Low'].div(norm_accion).plot(marker='o')
accionDf['Volume'].div(vol_accion).plot(marker='o')
plt.figure(2)
accionDf['High'].plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20,10),label="High",marker='o')
accionDf['Low'].plot(marker='o')
plt.figure(3)
accionDf['Volume'].plot(marker='o',figsize=(20,10))

#accionDf['High'].div(norm_accion).plot(xlim=['2020-1-1','2020-4-3'],label="se")
#accionDf['Volume'].div(vol_accion).plot()
plt.legend()
plt.show()
