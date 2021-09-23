#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd
import numpy as np

low_file=sys.argv[1] #274,295
high_file=sys.argv[2]

###1###
df1=pd.read_csv(low_file,delimiter='\t') #df1 = low vaf
df1_sum=df1.sum(axis=1)

low_list=[]	
for i in range(len(df1)):
	a=round(df1_sum[i]/len(df1.columns),3) #average with zero
	if a<0.1 :
		low_list.append(df1.loc[i][0])
#print(low_list)

###2###
df2=pd.read_csv(high_file,delimiter='\t') #df2 = high vaf
df2_sum=df2.sum(axis=1)
nonzero_df2=np.count_nonzero(df2,axis=1)-1 #df2 nonzero count

#print(df2)
high_list=[]
for j in range(len(df2)):
	b=round(df2_sum[j]/nonzero_df2[j],3) #average without zero
	if b>0.2 and b<0.8:
		high_list.append(df2.loc[j][0])

###3###
final_list=[]	
for k in range(len(high_list)):
	if high_list[k] in low_list:        #if high_list elements in low_list 
		final_list.append(high_list[k])
for p in final_list:
	print(p)



