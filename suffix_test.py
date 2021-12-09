class suffix:
    def __init__(self):
        self.index = 0
        self.suffix = ''

    def get_suffix(self):
        return self.suffix

    def get_index(self):
        return self.index

def suffix_array(text):
    text_len = len(text)

    suffixes = [suffix() for _ in range(text_len)]

    for i in range(text_len):
        suffixes[i].index = i
        suffixes[i].suffix = text[i:]
    
    suffixes.sort(key=lambda x: x.suffix)
    return suffixes
    

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
        if fulltext[sa[mid].get_index():] < phrase:
            l = mid+1
        else:
            r = mid

    def match_at(i):
        return fulltext[i: i + len(phrase)] == phrase

    first = l
    while first > 0 and match_at(sa[first - 1].get_index()):
        first -= 1

    last = r
    while match_at(sa[last].get_index()):
        last += 1

    return sa[first:last]

