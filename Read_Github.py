# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:31:32 2019

@author: Chaitra
"""
#import matplotlib.pyplot as plt
import pandas as pd
#from matplotlib import pyplot as plt1
from matplotlib import style
style.use('ggplot')

f=open("C:\\Users\\Chaitra\\Desktop\\Vikram Solar\\Module_Temperature_trial.csv",'rb')

readfile=pd.read_csv("Module_Temperature_trial.csv")

#readfile.plot(readfile.TIME,readfile.moduletemperature_forecast)
#readfile.loc['moduletemperature_forecast'].plot()
#plt.show()

readfile.hist('moduletemperature_forecast')

