#!/home/jaesoon/miniconda3/bin/python

import sys

bam_file_list = sys.argv[1]
save_directory = sys.argv[2]
M_list = sys.argv[3]

with open(bam_file_list) as ba:
	ba=ba.read().splitlines()

with open(M_list) as f:
	f=f.read().splitlines()
list1=[]
for i in range(len(f)):
			list1.append(f[i].split("\t"))
for k in range(len(f)):
	f[k] = str(list1[k][0]) + ":" +str(int(list1[k][1])-75)+"-"+str(int(list1[k][1])+75)



	
a="new\ngenome b37\n"
c="goto hi\n"                                                        #hi is chr:pos-1~pos

d="sort\ncollapse\nsnapshotDirectory bye\nsnapshot HEY.CAT.png\n"                  #bye is directory for savefile, HEY is bamfile name, CAT is chrpos
d=d.replace('bye',save_directory)

b="load /data/jaesoon/DB/gunhee/new_singlecell/human_singlecell/02_BAM/bam/WOW\n"                            #WOW is bamfile name



for j in range(len(f)):
	for i in range(len(ba)):
		print(a+b.replace('WOW',ba[i])+c.replace('hi',f[j])+d.replace('HEY',ba[i]).replace('CAT',f[j]))
