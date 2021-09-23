#!/home/jaesoon/miniconda3/bin/python

import sys

M_list = sys.argv[1]


with open(M_list) as f:
	f=f.read().splitlines()
list1=[]
for i in range(len(f)):
	list1.append(f[i].split("\t"))
for k in range(len(f)):
	f[k] = str(list1[k][0]) + ":" +str(int(list1[k][1])-75)+"-"+str(int(list1[k][1])+75)
							

for j in range(len(f)):
	print(f[j])
