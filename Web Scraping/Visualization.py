import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("E:\Application\Python Project\Covid19\Scrapping\Housing\Housing_csv\housing_P3659o4itp2vujkis_Navi_Mumbai.csv")
print(data.shape)
print(data.describe())
price_range = data['Price_Range']
project_name = data['Project_Name']

plt.scatter(project_name, price_range, color='red')
plt.xticks(rotation=35)
plt.show()

'''
count  20.00000
mean   10.50000
std     5.91608
min     1.00000
25%     5.75000
50%    10.50000
75%    15.25000
max    20.00000
'''