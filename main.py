import pandas as pd

data = pd.read_csv("Qualitative_Bankruptcy.data.txt")

data.columns = ["Industrial Risk","Industrial Risk"," Financial Flexibility","Credibility","Competitiveness","Operating Risk","Class"]

data.to_csv("data.csv",index=None,header=True)