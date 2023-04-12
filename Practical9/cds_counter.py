import re

seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
A = re.findall('TGA|TAA', seq)  # use re to find out all the coding	sequences
print(len(A))  # calculate the number
