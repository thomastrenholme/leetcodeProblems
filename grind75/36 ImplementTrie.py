class Trie:

    def __init__(self):
        self.stringDict = {}
        self.prefixDict = {}

    def insert(self, word: str) -> None:
        if word not in self.stringDict:
            self.stringDict[word] = True
        
        ctr = 1
        while ctr<= len(word):
            self.prefixDict[word[:ctr]] = True
            ctr+=1
        

    def search(self, word: str) -> bool:
        return True if word in self.stringDict else False
        

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.prefixDict else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)