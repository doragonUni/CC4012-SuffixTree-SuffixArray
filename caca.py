class PatriciaNode():
    def __init__(self):
        #self.data = ["", 0]
        self.word = ""
        self.children = {}

class patricia():
    def __init__(self):
        self.root = PatriciaNode()

    def insert(self, word):
        children = self.root.children
        i = 0
        char= word[i:i+1]
        while 1:
            try:
                node = children[char] 
            except KeyError:
                if children: 
                    new_node = PatriciaNode()
                    new_node.word = word[i+1:]
                    children[char] = new_node
                else:
                    if char == '':
                        return
                    else:
                        new_node = PatriciaNode()
                        new_node.word=word[i+1:]
                        children[char] = new_node
                return
            print("caso donde existe la llave")
            #si existe la llave

            '''
            i += 1
            if word.startswith(node.word,i):
                if len(word[i:]) == len(node.word):
                    if node.children:
                        try:
                            node.children['']
                        except KeyError:
                            children = node.children
                            new_node = PatriciaNode()
                            children[''] = new_node
                    return
                else:
                    i += len(node.word)
                    data.children = node.children
            else:
                ii = i
                j = 0
                while ii != len(word) and j != len(node.word) and \
                      word[ii:ii+1] == node.word[j:j+1]:
                    ii += 1
                    j += 1
                tmpdata = {}
                tmpdata[node.word[j:j+1]] = [node[0][j+1:],node[1]]
                tmpdata[word[ii:ii+1]] = [word[ii+1:],{}]
                data[word[i-1:i]] = [node[0][:j],tmpdata]
                return
            '''

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.char)+self.print_leaf()+"\n"
        for child in self.children.keys():
            ret += self.children[child].__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'



#p = patricia()
#words = ['foo','bar','baz', 'food']
#for x in words:
#    p.insert(x)

#print(p.data)
#print(p)

trie = patricia()
trie.insert("banana")
trie.insert("anana")
trie.insert("nana")
#trie.insert("ana")
#print(trie)
print(trie.root.children['a'].children)
