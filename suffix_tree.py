
class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False
        self.counter = 1

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.char)+"\n"
        for child in self.children.keys():
            ret += self.children[child].__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.root.char)+"\n"
        for child in self.root.children.keys():
            ret += self.root.children[child].__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        node.counter += 1
        
root = Trie()
root.insert("caca")
print(root)
root.insert("camaleon")
print(root)
root.insert("dama")
print(root)