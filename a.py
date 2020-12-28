# import numpy as np
# f = open('output.txt','r')
# total = f.readlines()
# tmp = []
# i = 0
# for line in total:
#     i = i + 1
#     tmp.append(line.rstrip("\n"))
# print(list(dict.fromkeys(tmp)))
# a = list(dict.fromkeys(tmp))
# print(len(list(dict.fromkeys(tmp))))
# print(len(a))
# print(i)
# output_duplicate = open('result.txt','w')
# for word in a:
#     output_duplicate.write(word+'\n')
# output_duplicate.close() 
# from colorama import Fore, Back, Style 
from termcolor import colored
# print(Style.DIM + 'and in dim text')
print(colored('hello', 'red'), colored('world', 'green'))
for i in range(19):
    print(i)
# listdata = ['boy','girl','test','girl','boy']
# print(np.unique(listdata))