class PatriciaNode():
    def __init__(self):
        self.word = ""
        self.children = {}
        self.count_sons=0
        self.most_popular = None

    def pre_count_sons(self):
        if self.children=={}:
            self.count_sons=0
            return 1
        count=0
        for k in self.children.keys():
            sum = self.children[k].pre_count_sons()
            if sum == None:
                sum = 0
            count+=sum
        self.count_sons=count
        return count

    def pre_most_popular(self):
        if self.children=={}:
            self.most_popular=self
            return self
        most = None
        for k in self.children.keys():
            popular = self.children[k].pre_most_popular()
            if most==None:
                most=popular
            elif popular.count_sons>most.count_sons:
                most=popular
        self.most_popular=most
        return most




        


class patricia():
    def __init__(self):
        self.root = PatriciaNode()

    def insert(self, word):
        children = self.root.children
        i = 0
        
        while 1:
            try:
                char= word[i:i+1]
                node = children[char] 
            except KeyError:
                if char == '':
                        return
                else: 
                    new_node = PatriciaNode()
                    new_node.word = word[i+1:]
                    children[char] = new_node
                return

            i += 1
            if word.startswith(node.word,i):
                if len(word[i:]) == len(node.word):
                    return
                else:
                    i += len(node.word)
                    children = node.children
            else:
                ii = i
                j = 0
                while ii != len(word) and j != len(node.word) and \
                      word[ii:ii+1] == node.word[j:j+1]:
                    ii += 1
                    j += 1

                tmpdata = {}
                new_node = PatriciaNode()
                new_node.word=node.word[j+1:]
                new_node.children=node.children
                tmpdata[node.word[j:j+1]] = new_node

                if word[ii:ii+1]!="":
                    new_node = PatriciaNode()
                    new_node.word=word[ii+1:]
                    tmpdata[word[ii:ii+1]] = new_node

                new_node = PatriciaNode()
                new_node.word = node.word[:j]
                new_node.children = tmpdata
                children[word[i-1:i]] = new_node
                return
            

    def pre_count_sons(self):
        self.root.pre_count_sons()
    def pre_most_popular(self):
        self.root.pre_most_popular()





p = patricia()
words = ['foo','bar','baz', 'food']
for x in words:
    p.insert(x)

p.pre_count_sons()
p.pre_most_popular()
print(p.root.most_popular.word)
#print(p.root.children['b'].count_sons)

