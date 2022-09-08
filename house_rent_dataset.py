# -*- coding: utf-8 -*-
"""House Rent_Dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ec1yRut5-pqvLuHABM5frsqHLg_E1ihF

# Load packages
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from IPython import get_ipython
import warnings
warnings.filterwarnings("ignore")

"""# Data preparation"""

from google.colab import drive
drive.mount('/content/drive')

# Read data 

import pandas as pd
from google.colab import drive
df = pd.read_csv('/content/sample_data/House_Rent_Dataset.csv')
print(df)

# Check data teratas

df.head(10)

# Check row and column

df.shape

df.tail()

df.columns

df.info()

df.describe()

df.isnull().sum()

df.nunique()

df_new = df.drop(['Posted On', 'BHK', 'Rent'], axis = 1)
df_new.head()

df_new['Area Type'].unique()

df_new['Area Type'].value_counts()

import plotly.express as px
fig1 = px.histogram(df_new, x = 'Area Type', color = 'Area Type')
fig1.show()

"""### Summary Area Locality"""

df_new = df.drop(['Area Locality', 'City', 'Furnishing Status'], axis = 1)
df_new.head()

df_new['Rent'].unique()

df_new['Rent'].value_counts()

fig2 = px.histogram(df_new, x = 'Rent', color = 'Rent')
fig2.show()

"""### Menentukan standar & varians"""

import pandas as pd
df = pd.read_csv('/content/sample_data/House_Rent_Dataset.csv')
print(df)
# Standar variasi kolom Rent
df.loc[:, "Rent"].std()
# Varians kolom BHK
df.loc[:, "BHK"].var()

"""### Menemukan nilai outliers"""

# Check outliers Rent

import pandas as pd
df = pd.read_csv('/content/sample_data/House_Rent_Dataset.csv')
# Hitung quartile 1
Q1 = df[["Rent"]].quantile(0.25)
# Hitung quartile 3
Q3 = df[["Rent"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1

# Check outliers Size

import pandas as pd
df = pd.read_csv('/content/sample_data/House_Rent_Dataset.csv')
# Hitung quartile 1
Q1 = df[["Size"]].quantile(0.25)
# Hitung quartile 3
Q3 = df[["Size"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1

"""### Rename kolom Dataframe"""

# Rename columns

import pandas as pd
df = pd.read_csv('/content/sample_data/House_Rent_Dataset.csv')
# Ganti nama kolom tenant_preferred menjadi customer_preferred
df.rename(columns={"Tenant Preferred": "Customer Preferred"}, inplace=True)
print(df)

"""### Groupby menggunakan pandas

Kegunaan .groupby adalah mencari summary dari data frame dengan menggunakan aggregate dari kolom tertentu.
"""

df["Bathroom"].groupby([df["BHK"]]).mean()

df["Bathroom"].groupby([df["BHK"], df["Rent"]]).sum()

"""### Sorting data

Sorting adalah sebuah metode mengurutkan data berdasarkan syarat kolom tertentu dan biasanya digunakan untuk melihat nilai maksimum dan minimum dari dataset. Library Pandas sendiri menyediakan fungsi sorting sebagai fundamental dari exploratory data analysis.
"""

# Sorting data column Rent

df.sort_values(by="Rent")

# Sorting data column BHK

df.sort_values(by="BHK")

# Sorting data column Bathroom

df.sort_values(by="Bathroom")