class patricia():
    def __init__(self):
        self.tuple = ["", 0]
        self.data = {}
        self.pre_count_leaf = 0

    def insert(self, word):
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
                        #if i != 0:
                            #data[''] = ['',{}]
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

    
    






p = patricia()
words = ['foo','bar','baz', 'food']
for x in words:
    p.insert(x)


def pre_count_leaf(data):
    print(data)
    if data == {}:
        print("llegue a una hoja")
        return 1

    count = 0
    for k in data.keys():
        count += pre_count_leaf(data[k][1])
    return count

print(p.data)
print(pre_count_leaf(p.data))

