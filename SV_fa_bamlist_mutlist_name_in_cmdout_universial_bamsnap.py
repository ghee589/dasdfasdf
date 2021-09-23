#!/home/jaesoon/miniconda3/bin/python

import pandas as pd
import numpy as np
import sys

M_list=sys.argv[3]

with open(M_list) as f:
	f=f.read().splitlines()

bam_list = sys.argv[2]

with open(bam_list) as g:
	g=g.read().splitlines()

bam_string = str(g[0])

list1=[]
for i in range(len(f)):
		list1.append(f[i].split("\t"))

for k in range(len(f)):
		f[k] = str(list1[k][0]) + ":" +str(list1[k][1]) 



a= f'bamsnap -ref {sys.argv[1]} -bam {bam_string} -save_image_only -width 2500 -read_color_by interchrom -silence -pos hi -out /data/jaesoon/DB/SG/delly/DB15/vcf/allmutdel/pass/gunzip/filtered/chrpos/pos/OX/bamsnap/{sys.argv[4]}.merged.hi.png' #variable can be in formatting, not only in sys argv
list1=[]

for i in range(len(f)):
	list1.append(a.replace('hi',f[i]))

for j in range(len(list1)):
	print(list1[j])
	

