class patricia():
    def __init__(self):
        self.data = {}

    def addWord(self, word):
        data = self.data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                if data:
                    data[word[i:i+1]] = [word[i+1:],{}]
                else:
                    if word[i:i+1] == '':
                        return
                    else:
                        if i != 0:
                            data[''] = ['',{}]
                        data[word[i:i+1]] = [word[i+1:],{}]
                return

            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                        except KeyError:
                            data = node[1]
                            data[''] = ['',{}]
                    return
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                ii = i
                j = 0
                while ii != len(word) and j != len(node[0]) and \
                      word[ii:ii+1] == node[0][j:j+1]:
                    ii += 1
                    j += 1
                tmpdata = {}
                tmpdata[node[0][j:j+1]] = [node[0][j+1:],node[1]]
                tmpdata[word[ii:ii+1]] = [word[ii+1:],{}]
                data[word[i-1:i]] = [node[0][:j],tmpdata]
                return

    def isWord(self,word):
        data = self.data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                        except KeyError:
                            return False
                    return True
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                return False

    def isPrefix(self,word):
        data = self.data
        i = 0
        wordlen = len(word)
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                return False
            i += 1
            if word.startswith(node[0][:wordlen-i],i):
                if wordlen - i > len(node[0]):
                    i += len(node[0])
                    data = node[1]
                else:
                    return True
            else:
                return False

    def removeWord(self,word):
        data = self.data
        i = 0
        while 1:
            try:
                node = data[word[i:i+1]]
            except KeyError:
                print("Word is not in trie.")
                return
            i += 1
            if word.startswith(node[0],i):
                if len(word[i:]) == len(node[0]):
                    if node[1]:
                        try:
                            node[1]['']
                            node[1].pop('')
                        except KeyError:
                            print("Word is not in trie.")
                        return
                    data.pop(word[i-1:i])
                    return
                else:
                    i += len(node[0])
                    data = node[1]
            else:
                print("Word is not in trie.")
                return

    __getitem__ = isWord

    def __str__(self, level=0, branch=""):
        img = "\t"*level + self.__repr__(branch) + "\n"
        for child in self.data:
            img += self.data[child].__str__(level+1, child)
        return img

    def __repr__(self, branch):
        return str(branch)


p = patricia()
words = ['foo','bar','baz', 'food']
for x in words:
    p.addWord(x)

print(p.data)
print(p)