import numpy as np
import pandas as pd
import math
df=pd.read_csv("/Users/thrivenkumar/Desktop/turbloc.csv",sep=',')
turb_coords = df.to_numpy(dtype = np.float32)
for i in range(4):
    value1=(turb_coords[i,0]-turb_coords[i+1,0])**2
    value2=(turb_coords[i,1]-turb_coords[i+1,1])**2
    value3=math.sqrt(value1+value2)
    print(value3)
