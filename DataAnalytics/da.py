import pandas as pd
import numpy as np

# creating a dataframe
data = pd.DataFrame({'PC': [12], 'Console': [24]})
print(data)

# reading csv files
gaming_link = "economy.csv"
gaming_data = pd.read_csv(gaming_link)

