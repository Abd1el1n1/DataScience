import yfinance as yf
##import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#print("1. analisis normalizado")
#print("2. analisis sin normalizar")
#opt = int(input())

print("Numero de acciones a analizar")
num_accion = int(input())
f = open("analisis.py",'w')
f.write("import yfinance as yf")
f.write("\n")
f.write("import pandas as pd")
f.write("\n")
f.write("import matplotlib.pyplot as plt")
f.write("\n")
f.write("from datetime import datetime")
f.write("\n")

for i in range(num_accion):
    print("Nombre Accion")
    accion = input()
    #get data on this ticker
    f.write("\n")
    f.write(accion+"Data = yf.Ticker('"+accion+"')")
    f.write("\n")
    #get the historical prices for this ticker
    ##print("Fecha de Inicio(AAAA-MM-DD)")
    f.write("f_inicio = '2019-1-1'")
    f.write("\n")
    ##print("Ultima Fecha(AAAA-MM-DD)")
    ##f_final = input()
    f.write("hoy = datetime.today().strftime('%Y-%m-%d')")
    f.write("\n")
    f.write(accion+"Df = "+accion+"Data.history(period='1d', start=f_inicio, end=hoy)")
    f.write("\n")
    #see your data
    #f.write(accion+"Df.to_csv(str("+accion+")+'.csv', index=False)")
    f.write("\n")
    f.write(accion+"norma = "+accion+"Df['High'].max()")
    f.write("\n")
    f.write(accion+"Df['High'].div("+accion+"norma).plot(xlim=['2020-1-1',datetime.today().strftime('%Y-%m-%d')],figsize=(20, 15),label='"+accion+"')")
    f.write("\n")

f.write("plt.legend()")
f.write("\n")
f.write("plt.show()")
