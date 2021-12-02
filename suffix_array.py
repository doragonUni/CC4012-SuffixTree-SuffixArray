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