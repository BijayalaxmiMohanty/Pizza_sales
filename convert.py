# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 01:40:26 2024

@author: Hp
"""

import pandas as pd
read_file=pd.read_excel(r"C:\Users\Hp\OneDrive\Desktop\CreditcardFraud\Pizza_sales\PizzaSales.xlsx")
#pip install openpyxl --upgrade
read_file.to_csv(r"C:\Users\Hp\OneDrive\Desktop\CreditcardFraud\Pizza_sales\Pizza_Sales.csv",index =False,header=True)
df=pd.DataFrame(pd.read_csv("Pizza_Sales.csv"))
df
