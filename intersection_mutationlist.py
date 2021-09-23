#!/home/jaesoon/miniconda2/bin/python

import sys
import cyvcf2

in_file_vcf = sys.argv[1]

vcf_object = cyvcf2.VCF(in_file_vcf)
variant_list = list(vcf_object)

chrompos=[]
for i in range(len(variant_list)):
	chrompos.append((variant_list[i].CHROM,variant_list[i].POS))
a=[]
for j in range(len(chrompos)):
	b=(str(chrompos[j][0]), int(chrompos[j][1]))
	a.append(b)
for l in range(len(a)):
	print(a[l])
