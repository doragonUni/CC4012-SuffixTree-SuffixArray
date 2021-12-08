
class TrieNode():
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False
        self.full_string = ''
        self.most_freq = None
        self.counter = 1

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.char)+self.print_leaf()+"\n"
        for child in self.children.keys():
            ret += self.children[child].__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

    def print_leaf(self):
        if self.is_end:
            return '$'
        else: return ''


class Trie():
    def __init__(self):
        self.root = TrieNode("")

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.root.char)+self.print_leaf()+"\n"
        for child in self.root.children.keys():
            ret += self.root.children[child].__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

    def print_leaf(self):
        if self.root.is_end:
            return '$'
        else: return ''
    
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
        self.most_freq()

    def search(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        if node.is_end:
            node.counter += 1
            return node
        else: return None

    def most_freq(self):
        return 1  