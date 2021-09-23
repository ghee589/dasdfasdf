#!/home/jaesoon/miniconda2/bin/python

import sys
import pysam
import cyvcf2


fa='/data/jaesoon/DB/gunhee/pig/before/Sscrefa11.1_rename/Sscrofa11.1_genomic.rename.fna'
ba=sys.argv[1]
file_1=sys.argv[2]

with open(file_1) as f:
	f=f.read().splitlines()

CHR=[]
POS=[]

for k in range(len(f)):
	CHR.append(eval(f[k])[0])
	print (CHR)
	print('hi')
	POS.append(eval(f[k])[1])


fasta=pysam.FastaFile(fa)


bam = pysam.AlignmentFile(ba)	



def VAFcal(bam, tup):
	global base
	base = []
	ref =fasta.fetch(tup[0],int(tup[1])-1,int(tup[1]))
	for pcol in bam.pileup(tup[0],int(tup[1])-1,int(tup[1]), truncate = True):
		for pileupread in pcol.pileups:
			base.append(pcol.get_query_sequences())
			print(base)
	list1 = [ref, ref.lower()]
	list2 = []
	for i in range(len(base)):
		if base[i] not in list1:
			 list2.append(base[i])
	return round(len(list2)/len(base), 3)

for j in range(len(POS)):	
	print(VAFcal(bam,(CHR[j], POS[j])))


