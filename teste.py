import pandas as pd
import numpy as np
def getio (year):
 path = "C:/Users/anton/Documents/Covinhas/bb22a10summarytables.xlsx"
 # Input output table
 df = pd.read_excel(path, 
 sheet_name = str(year), 
usecols = "C:L",

 header = None, 
skiprows = 52,
nrows = 10)
 z = np.array(df,dtype = float) # £ million
 
 # Output per sector 
 dfx = pd.read_excel(path,
 sheet_name = str(year),
 usecols = "C:L",
header = None,
skiprows = 75,
nrows = 1)
 x = np.array(dfx, dtype = float)[0] # £ million
 return [z, x]
# Example: Get input-output data for 2000
z, x = getio(2000)

def coefs(year):
    z, x = getio(year)
    
    return z
print (coefs(2000)[9, 9])
print(x[0])

import matplotlib.pyplot as plt
xaxis = range(1997, 2021)
yaxis = [coefs[year][1, 0] for year in range(2021-1997)]
plt.plot(xaxis, yaxis)