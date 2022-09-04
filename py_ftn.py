# py_ftn.py
  
import pandas as pd

def py_read_iris(file):
  data = pd.read_csv(file)
  data = data[data['SP'] == "vc"]
  return data


from sklearn.linear_model import LinearRegression
py_reg = LinearRegression()


def  py_desc(data) :
     data = pd.DataFrame(data)
     desc = data.describe()
     return desc




 