import sys
import pandas as pd
import numpy as np


in_file=sys.argv[1]
df=pd.read_csv(in_file,delimiter='\t')



nonzero_count = np.count_nonzero(df,axis=1)-1
#print(nonzero_count)


df1=df.sum(axis=1)
#print(df1)

list_x=[]
list_y=[]
for i in range(len(nonzero_count)):
	list_x.append(round(df1[i]/nonzero_count[i],3))
	list_y.append(nonzero_count[i])		
	#print([round(df1[i]/nonzero_count[i],3),nonzero_count[i]])
#print(list_x)
#print(list_y)

	
import matplotlib.pyplot as plt

plt.hexbin(list_x, list_y, gridsize=20, cmap=plt.cm.Blues)
#plt.show()
plt.savefig('scatter.png')
