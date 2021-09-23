#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd


in_file=sys.argv[1]


df=pd.read_csv(in_file,delimiter='\t')
print(df)

a='bamsnap -ref /data/jaesoon/DB/Mouse_Raw/GRCm38.fa -bam sample_m_296_271_s_tl_0110_1.s.md.ir.bam sample_m_296_271_s_tl_0110_2.s.md.ir.bam sample_m_296_271_s_tl_0110_3.s.md.ir.bam sample_m_296_271_s_tl_0110_4.s.md.ir.bam sample_m_296_271_s_tl_0110_5.s.md.ir.bam sample_m_296_271_s_tl_0501_1.s.md.ir.bam sample_m_296_271_s_tl_0501_2.s.md.ir.bam sample_m_296_271_s_tl_0501_3.s.md.ir.bam sample_m_296_271_s_tl_0501_4.s.md.ir.bam sample_m_296_271_s_tl_0501_5.s.md.ir.bam sample_M_296_Male_M_TL.s.md.ir.bam sample_m_271_female_f_tl.s.md.ir.bam -pos hi -show_soft_clipped -out /data/jaesoon/DB/SG/MutStr/iseced/296_271_isec/intersection_mutstr/intersection_mutstr_vaf/merged/result/bamsnap/296_271.merged.isec.hi.png'

list1=[]
for i in df:
	list1.append(a.replace('hi',i))

#for j in list1:
#	print(j)
