'''
IDEA OF SUFFIX ARRAY
given a string, let say: 'abracadabra$'

We do the following:

0 abracadabra
1 bracadabra
2 racadabra
3 acadabra
4 cadabra
5 adabra
6 dabra
7 abra
8 bra
9 ra
10 a
11 $

then we sort the elements
and the suffix array is completed as shown:
10-7-0-3-5-8-1-4-6-9-2
'''

#[10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]

import sys

#if len(sys.argv) != 2:
  #  print('Use: '+sys.argv[0]+' archivo.txt')
    #sys.exit(1)
s='banana'

#Momentanio, solucion sacada de google

txt = open(sys.argv[1])
fulltext = txt.read()

# recordar cambiarlo
def suffixArray(s):
    suffixes = [(s[i:], i) for i in range(len(s))] # o(n)
    suffixes.sort(key=lambda x: x[0]) #nlog(n)
    return [s[1] for s in suffixes] #o(n)

print(suffixArray(fulltext))
