# -*- coding: utf-8 -*-
import math
def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]))
    file.close()
    
num_files = 10
n = 1
m = 20180712163300

IQ = open("a.txt", 'r')
num_lines = len(open("a.txt").readlines(  ))
num_slice = math.floor(num_lines / num_files)
if num_slice % 2 == 1:
    num_slice = num_slice - 1

line_output = ''
for line in IQ.readlines():
    if n == 1:
        line_output = line
    else:
        line_output = line_output + line
##        print(line_output)

    if n % num_slice == 0:
        name_file = str(m) + '_AOA_1M_250k_2012_Vanilla-09-39_330_60_F_-60 - lin(a-b).txt'
        text_save(line_output, name_file)
        m = m + 1
        n = 0

    n = n + 1

IQ.close()
