import sys
from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.minSteps = sys.maxsize

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        present = False

        patternToWordsPossible = defaultdict(set)

        for i in range(len(wordList)):

            word = wordList[i]

            if endWord == word:
                present = True

            for j in range(len(word)):

                wordWithWildcard = word[0:j]+"*"+word[j+1:len(word)]
                patternToWordsPossible[wordWithWildcard].add(word)

        if not present:
            return 0

        print(patternToWordsPossible)

        for j in range(len(beginWord)):
            wordWithWildcard = beginWord[0:j]+"*"+beginWord[j+1:len(beginWord)]

            visited = set()

            self.bfs(beginWord, wordWithWildcard, visited.copy(), patternToWordsPossible, endWord, 1)

        if self.minSteps == sys.maxsize:
            return 0
        return self.minSteps


    def dfs(self, currWord, currPattern, visited, patternToWordsPossible, endWord, numSteps):

        #print("BFS, currWord: " + str(currWord) + ", currPattern: " + str(currPattern) + ", numSteps: " + str(numSteps))
        if numSteps > self.minSteps or currPattern in visited:
            return

        visited.add(currPattern)

        for word in patternToWordsPossible[currPattern]:

            if word == endWord:
                if self.minSteps > numSteps:
                    self.minSteps = numSteps+1
                return

            if word == currWord:
                continue

            for j in range(len(word)):
                wordWithWildcard = word[0:j]+"*"+word[j+1:len(word)]

                self.dfs(word, wordWithWildcard, visited.copy(), patternToWordsPossible, endWord, numSteps+1)

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))