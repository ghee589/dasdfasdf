#!/home/jaesoon/miniconda2/bin/python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter

file = sys.argv[1]


with open(file) as nonzero_list:
	nonzero_list=nonzero_list.read().splitlines()

for i in range(len(nonzero_list)):
	nonzero_list[i] = float(nonzero_list[i])

plt.hist(nonzero_list,bins=100)


plt.savefig('non_zero_vaf.png')
#plt.show()
