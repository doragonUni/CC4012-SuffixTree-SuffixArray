class PatriciaNode(): # Patricia node
    def __init__(self):
        self.word = "" # The word that contains the node
        self.children = {} # The sons of the node, it will be of the form {"a":PatriciaNode(),"b":PatriciaNode(),...}
        self.count_sons = 0 # The amount of sons that have the node
        self.most_popular = None # A reference to the most popular node

    def pre_count_sons(self): # Funtion that calcules the amount of sons of the node and his sons
        if self.children=={}: # If we dont have sons it means that is a leaf so we dont have sons but we are one
            self.count_sons=0
            return 1
        count=0
        for k in self.children.keys():
            sum = self.children[k].pre_count_sons() # we calcules de the amount of sosn for each son
            if sum == None:
                sum = 0
            count+=sum
        self.count_sons=count
        return count # returns the total count of sons

    def pre_most_popular(self): # Funtion that set the reference of the most popular son
        if self.children=={}: 
            self.most_popular = self # If we dont have sons it means that ourselft are the most_popular and we can be for other node
            return
        most = None
        for k in self.children.keys():
            self.children[k].pre_most_popular() # we set the reference of the most popular son for each node
            popular = self.children[k]
            if most == None or popular.count_sons > most.count_sons: # check if is beter than the one we have
                most = popular
        self.most_popular = most # set the most popular
        return

    def __str__(self, level=0, branch=""):
        ret = "\t"*level+ branch + self.word + "(" + str(self.count_sons) + ")" + "\n"
        for child in self.children.keys():
            ret += self.children[child].__str__(level+1, child)
        return ret

    def __repr__(self):
        return '<>'

class Patricia(): # Patricia tree
    def __init__(self):
        self.root = PatriciaNode() # The root is a node patricia empty

    def insert(self, word): # Function that insert a word in the tree
        children = self.root.children
        i = 0
        while 1:
            try: # We try to see if char exists as a key
                char= word[i:i+1]
                node = children[char] 
            except KeyError:
                # In the case that char not is a key, we need to create a node only in the case thar char !=""
                if char == '':
                        return
                else: 
                    new_node = PatriciaNode()
                    new_node.word = word[i+1:]
                    children[char] = new_node
                return

            #In the case that char is a key, we still need to found the place to insert it
            i += 1
            if word.startswith(node.word,i): # Example nana.startswith(an,1) == true and nana.startswith(ana,0)==false
                if len(word[i:]) == len(node.word): # If they have the same len it means that are the same word so i do nothing
                    return
                else:
                    i += len(node.word) # increased the variable i to skip the shared parts
                    children = node.children # change the childrens
            else: 
                ii = i
                j = 0
                # we get the indices from where they differ 
                while ii != len(word) and j != len(node.word) and \
                      word[ii:ii+1] == node.word[j:j+1]:
                    ii += 1
                    j += 1

                # Create a new node for the word in the node
                tmpChildren = {}
                new_node = PatriciaNode()
                new_node.word=node.word[j+1:]
                new_node.children=node.children
                tmpChildren[node.word[j:j+1]] = new_node

                # create a new node for word that wea want to insert only if we can make a key
                if word[ii:ii+1]!="":
                    new_node = PatriciaNode()
                    new_node.word=word[ii+1:]
                    tmpChildren[word[ii:ii+1]] = new_node

                # Create a new node that will have the tmpChildren like children
                new_node = PatriciaNode() 
                new_node.word = node.word[:j]
                new_node.children = tmpChildren
                children[word[i-1:i]] = new_node
                return
            
    def pre_count_sons(self): # pre calcules the count_sons for each node
        self.root.pre_count_sons()

    def pre_most_popular(self):
        self.root.pre_most_popular() # pre set the most_popular for each node
    
    def getThreeMost(self,children): # return a array with the three most popular sons

        hijos=[]
        values=[]
        for k in children.keys():
            if k != "$":
                values.append(children[k].count_sons)
                hijos.append(k)
        hijos.sort()
        if len(hijos)>3:
            return hijos[0:3]
        else:
            while len(hijos)<2:
                hijos.append("")
            return hijos


            

    def autocompletar(self,text): # return an array with options of autocomplete from a text
        children = self.root.children
        i = 0
        while 1:
            try:
                # We try to see if char exists as a key
                char= text[i:i+1] 
                node = children[char] 

            except KeyError:
                 # In the case that char not is a key we cant make a suggestion
                print(">No tengo sugerencia")
                return ["","",""]
            i += 1
            if text.startswith(node.word,i):# Example nana.startswith(an,1) == true and nana.startswith(ana,0)==false
                if len(text[i:]) == len(node.word): #If they have the same len it means that are the same word so i need to recomendate 3 my sons
                    print(">Tenemos las siguientes 3 sugerencias")
                    a=self.getThreeMost(node.children)
                    return a
                else:
                    #I have to continue searching
                    i += len(node.word)
                    children = node.children
            else:
                
                ii = i
                j = 0
                # we get the indices from where they differ 
                while ii != len(text) and j != len(node.word) and \
                      text[ii:ii+1] == node.word[j:j+1]:
                    ii += 1
                    j += 1
                # get the value that i will suggest
                value = node.word[j:j+1]
                if value == "$":
                    print(">No tengo sugerencia")
                    return ["","",""]
                print(">Te sugiero seguir con la siguiente letra")
                return [value,"",""]
                
    def __str__(self, level=0):
        ret = "\t"*level+ "_(" + str(self.root.count_sons) + ")" + "\n"
        for child in self.root.children.keys():
            ret += self.root.children[child].__str__(level+1, child)
        return ret

    def __repr__(self):
        return '<>'
