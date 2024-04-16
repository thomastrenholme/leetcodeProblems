from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        beginWordPresent = False
        endWordPresent = False
        for word in wordList:
            if word == beginWord:
                beginWordPresent = True
            if word == endWord:
                endWordPresent = True
        if not endWordPresent:
            return 0

        patternToWordsPossible = defaultdict(list)

        if not beginWordPresent:
            wordList.append(beginWord)

        for i in range(len(wordList)):

            word = wordList[i]

            for j in range(len(word)):

                pattern = word[0:j]+"*"+word[j+1:]
                patternToWordsPossible[pattern].append(word)

        visit = set([beginWord])
        queue = deque([beginWord])
        steps = 1

        while queue:

            for i in range(len(queue)):
                word = queue.popleft()
                #print("Word, currSteps: " + str((word, steps)))
                #print("Queue: " + str(queue))

                if word == endWord:
                    return steps

                for j in range(len(word)):
                    pattern = word[0:j]+"*"+word[j+1:]

                    for possibleWord in patternToWordsPossible[pattern]:
                        if possibleWord not in visit:
                            visit.add(possibleWord)
                            queue.append(possibleWord)
                            #print("Adding to queue: " + str(word))

            steps += 1
        return 0

sol = Solution()
print(sol.ladderLength("a", "c", ["a","b","c"]))