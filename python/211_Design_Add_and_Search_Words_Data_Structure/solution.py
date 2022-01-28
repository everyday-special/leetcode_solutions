class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['$'] = word

    def search(self, word: str) -> bool:
        def dfs(curr, word):
            if word == '':
                return '$' in curr
            elif word[0] == '.':
                for ch in curr:
                    if ch != '$' and dfs(curr[ch], word[1:]):
                        return True
                return False
            elif word[0] in curr:
                return dfs(curr[word[0]], word[1:])
            else:
                return False
        
        return dfs(self.trie, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
