import pandas as pd
import numpy as np

d = {'col1':[2,4,5,6],'col2':[8,8,6,1],'col3':[1,2,3,4],'col4':[4,4,4,4]}

df = pd.DataFrame(d,index=['Item1','Item2','Item1','Item2'])


pd.concat([y.assign(**{'diff_{0}'.format(x+1): y.iloc[:,0] - y.iloc[:,1]})for x , y in df.groupby(np.arange(df.shape[1])//2,axis=1)],axis=1)

print(df.shape[1]//2)