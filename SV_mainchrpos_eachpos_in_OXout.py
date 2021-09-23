#!/home/jaesoon/miniconda2/bin/python

import sys

main_file = sys.argv[1]
sub_file = sys.argv[2]

with open(main_file) as mf:
	mf=mf.read().splitlines()

with open(sub_file) as sf:
	sf=sf.read().splitlines()

list1=[]
for i in range(len(mf)):
	list1.append(mf[i].split("\t")[1]) #make pos list of Main_file(mergeSV_chrpos_file)

	
list2=[]
for j in range(len(list1)):
	m=0
	for k in range(len(sf)):
		if list1[j] == sf[k]:     
			m=m+1
		else:
			m=m
	if m == 1:
	 	list2.append("O")
	else:
	 	list2.append("X")

			

for p in range(len(list2)):
	print(list2[p])
