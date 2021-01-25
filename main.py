import pandas as pd

#read the CSV
data = pd.read_csv("Qualitative_Bankruptcy.data.txt")

#Name columns
data.columns = ["Industrial Risk","Industrial Risk"," Financial Flexibility","Credibility","Competitiveness","Operating Risk","Class"]

#store file as data.csv
data.to_csv("data.csv",index=None,header=True)