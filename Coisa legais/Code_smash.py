# import pandas as pd

# df = pd.DataFrame({'fruit':['apple','banana','orange'],'america_inv':[0,2,0],'asia_inv':[1,0,0],'aurope_inv':[2,1,3]})

# out = (df.melt('fruit', var_name='continent', ignore_index=False)
#          .query('value > 0')[['fruit', 'continent']].sort_index())
# #print(df.set_index('fruit'))
# print(out)

from os import remove
from subprocess import list2cmdline


def remove_nulos(x):
    if x:    
        return 'batata'
    else:
        return 'pickles'



lip = [0 ,0,'batata']

print(list(map(remove_nulos,lip)))