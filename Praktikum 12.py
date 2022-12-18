# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:23:53 2022

@author: acer
"""

import pandas as pd

df = pd.read_csv("Negara.csv")
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Frame:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandardDeviation.csv')
print("Data Berhasil Dibuat.")