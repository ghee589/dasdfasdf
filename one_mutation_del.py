#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd
import numpy as np

in_file=sys.argv[1]

df=pd.read_csv(in_file,delimiter='\t')

df=df[(np.count_nonzero(df,axis=1)-1) != 1]
df=df.round(3)

df.to_csv('test.txt',sep='\t',index=False)
