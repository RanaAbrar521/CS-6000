# -*- coding: utf-8 -*-
"""spam _email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqRmzB9Iklf8WoNP2xQBo5WMOfTo52Gq
"""

import pandas as pd
import matplotlib.pyplot as plt

# Import the dataset
data = pd.read_csv("/content/emails.csv")

# Display the first 5 rows
print(data.head())

# Display some basic statistics or visualize the data
data.describe()