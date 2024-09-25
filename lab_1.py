import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

df = pd.read_csv(path)
print(df.head())
print(df['peak-rpm'].dtypes)