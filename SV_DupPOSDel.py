#!/home/jaesoon/miniconda2/bin/python

import sys

f=sys.argv[1]

with open(f) as mf:
	mf=mf.read().splitlines()

list1=[]
for i in range(len(mf)):
	list1.append(mf[i].split("\t")[1])

list2=[]
for j in range(len(list1)):
	list2.append(str(list1[j])[0:-3])


list3=[]	
for k in range(len(list2)-1):
	if list2[k] != list2[k+1]:
		list3.append(mf[k])

for p in range(len(list3)):
	print(list3[p])
