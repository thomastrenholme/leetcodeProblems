import collections
from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        patternToPossibleWords = defaultdict(set)

        wordList.append(beginWord)

        endWordPresent = False

        for word in wordList:
            if endWord==word:
                endWordPresent = True

            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                patternToPossibleWords[pattern].add(word)

        if not endWordPresent:
            return 0

        transformations = 1

        q = collections.deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return transformations

                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    patternToPossibleWords[pattern].add(word)

                    for transformableWord in patternToPossibleWords[pattern]:
                        if transformableWord not in visited:
                            visited.add(transformableWord)
                            q.append(transformableWord)

            transformations+=1
        return 0


