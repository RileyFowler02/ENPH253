import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df0 = pd.read_csv('data/zero_slits.csv', names=['Voltage_0', 'Angle_0'], header=None, index_col=False, on_bad_lines='skip')
df1 = pd.read_csv('data/one_slit.csv', names=['Voltage_1', 'Angle_1'], header=None, index_col=False, on_bad_lines='skip')
df2 = pd.read_csv('data/two_slits.csv', names=['Voltage_2', 'Angle_2'], header=None, index_col=False, on_bad_lines='skip')
df4 = pd.read_csv('data/four_slits.csv', names=['Voltage_4', 'Angle_4'], header=None, index_col=False, on_bad_lines='skip')
df6 = pd.read_csv('data/six_slits.csv', names=['Voltage_6', 'Angle_6'], header=None, index_col=False, on_bad_lines='skip')

print(df0.head())
print('-------------------')
print(df1.head())
print('-------------------')
print(df2.head())
print('-------------------')
print(df4.head())
print('-------------------')
print(df6.head())