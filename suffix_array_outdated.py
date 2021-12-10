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


# recordar cambiarlo
def suffixArray(s):
    '''
    Given a string, the function returns the suffix_array of the string
    '''
    suffixes = [(s[i:], i) for i in range(len(s))] # o(n)
    suffixes.sort(key=lambda x: x[0]) #nlog(n)
    return [s[1] for s in suffixes] #o(n)

class suffix:
     
    def __init__(self):
         
        self.index = 0
        self.rank = [0, 0]

def buildSuffixArray(txt):
    n = len(txt)
    # A structure to store suffixes
    # and their indexes
    suffixes = [suffix() for _ in range(n)]
 
    # Store suffixes and their indexes in
    # an array of structures. The structure
    # is needed to sort the suffixes alphabetically
    # and maintain their old indexes while sorting
    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = (ord(txt[i]) -
                               ord("a"))
        suffixes[i].rank[1] = (ord(txt[i + 1]) -
                        ord("a")) if ((i + 1) < n) else -1
 
    # Sort the suffixes according to the rank
    # and next rank
    suffixes = sorted(
        suffixes, key = lambda x: (
            x.rank[0], x.rank[1]))
 
    # At this point, all suffixes are sorted
    # according to first 2 characters.  Let
    # us sort suffixes according to first 4
    # characters, then first 8 and so on
    ind = [0] * n  # This array is needed to get the
                   # index in suffixes[] from original
                   # index.This mapping is needed to get
                   # next suffix.
    k = 4
    while (k < 2 * n):
         
        # Assigning rank and index
        # values to first suffix
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0
 
        # Assigning rank to suffixes
        for i in range(1, n):
             
            # If first rank and next ranks are
            # same as that of previous suffix in
            # array, assign the same new rank to
            # this suffix
            if (suffixes[i].rank[0] == prev_rank and
                suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
                 
            # Otherwise increment rank and assign   
            else: 
                prev_rank = suffixes[i].rank[0]
                rank += 1
                suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i
 
        # Assign next rank to every suffix
        for i in range(n):
            nextindex = suffixes[i].index + k // 2
            suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
                if (nextindex < n) else -1
 
        # Sort the suffixes according to
        # first k characters
        suffixes = sorted(
            suffixes, key = lambda x: (
                x.rank[0], x.rank[1]))
 
        k *= 2
 
    # Store indexes of all sorted
    # suffixes in the suffix array
    suffixArr = [0] * n
     
    for i in range(n):
        suffixArr[i] = suffixes[i].index
 
    # Return the suffix array
    return suffixArr

def search_in_array(sa, phrase, text):
    left = 0
    right = len(sa)
    while right > left:
        mid = (right+left)//2
        if text[sa[mid]:] < phrase:
            left = mid+1
        else: 
            right = mid
    if not text[sa[left]:].startswith(phrase): 
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        raise IndexError('not found')
    return sa[left]


def search_all(sa, phrase, fulltext):
    '''
    parameters: suffix array, phrase, full text
    Given a suffix array, a phrase and the full text
    The function uses binary search to find all the ocurrencies of the phrase in the text 
    returns an array of indexes of the phrase found in the text
    '''
    l = 0
    r = len(sa)
    while l < r:  #We do a binary search
        mid = (l+r)//2 
        if fulltext[sa[mid]:] < phrase:
            l = mid+1
        else:
            r = mid

    def match_at(i):
        return fulltext[i: i + len(phrase)] == phrase

    first = l
    while first > 0 and match_at(sa[first - 1]):
        first -= 1

    last = r
    while match_at(sa[last]):
        last += 1

    return sa[first:last]