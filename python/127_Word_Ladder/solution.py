"""
Done with help from the discussion.
I knew the solution was 1) make a graph then 2) BFS
but I couldn't visualize how to make/traverse the graph without help
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Make adjacency graph
        wordSet, graph = set(wordList), {}
        for word in [beginWord] + wordList:
            graph[word] = []
            for i in range(26):
                for j in range(len(word)):
                    new_ch = chr(ord('a') + i)
                    if new_ch == word[j]:
                        continue
                    new_word = word[:j] + new_ch + word[j+1:]
                    if new_word in wordSet:
                        graph[word].append(new_word)

        # BFS
        queue = deque([(beginWord, 1)])
        while len(queue) > 0:
            curr_word, curr_dist = queue.popleft()
            for word in graph[curr_word]:
                if word == endWord:
                    return curr_dist + 1
                elif word in wordSet:
                    wordSet.remove(word)
                    queue.append((word, curr_dist + 1))
        return 0
