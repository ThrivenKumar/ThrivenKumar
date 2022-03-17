import matplotlib.pyplot as plt
import pandas as pd
data=[['e001','M',34,123,'Normal',350],
      ['e002','F',34,123,'Overweight',450],
      ['e003','M',34,123,'Obesity',169],
      ['e004','F',34,123,'Underweight',350],
      ['e005','M',34,123,'Underweight',350],
      ['e006','M',34,123,'Normal',350],
      ['e007','F',34,123,'Obesity',350],
      ['e008','M',34,123,'Normal',350],
      ['e009','F',34,123,'Normal',350],
      ['e010','M',34,123,'Underweight',350]]

df=pd.DataFrame(data,columns=['EmPID','Gender','AGe','Sales',"BMI",'income'])
df.hist()
plt.show()
