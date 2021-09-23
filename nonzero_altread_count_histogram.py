#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd
import numpy as np

file = sys.argv[1]

df=pd.read_csv(file,delimiter='\t') #tsv file call


list1=[]
for i in range(len(df)):
	a=df.loc[i][1:len(df.columns)]
	for j in range(len(a)):
		n=0
		while j<=len(a)-1:
			if int(a[j][1])!=0:
				n=n+1
			if j==len(a)-1:
				list1.append(n)
			j=j+1


import matplotlib.pyplot as plt
plt.hist(list1,bins=100)
plt.savefig('m_96.merged.hcvsunion.snvs.isec.allmutdel.readinfo.chrposaltcountdepth.dupdel.png')
#plt.show()


