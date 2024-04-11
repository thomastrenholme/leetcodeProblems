import sys


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        ##Higher timestamp = more recently used
        self.lruTimestamp = 1
        self.size = 0

        ## Initialize lfu and mfu dummy node.
        self.lfuNode = LFUCacheNode(-sys.maxsize, None, None)
        self.mfuNode = LFUCacheNode(sys.maxsize, None, None)
        self.lfuNode.useCount = -sys.maxsize
        self.mfuNode.useCount = sys.maxsize
        self.lfuNode.next = self.mfuNode
        self.mfuNode.prev = self.lfuNode

        ## Initialize list of nodes to

    def get(self, key: int) -> int:

        if key in self.cache:

            ##Add new usage timestamp
            self.lruTimestamp+=1

            ## Increment use count and timestamp
            node = self.cache.get(key)
            node.lruTimestamp=self.lruTimestamp
            node.useCount +=1

            ## Adjust LFU order
            while node.useCount > node.next.useCount or (node.useCount == node.next.useCount and node.lruTimestamp > node.next.lruTimestamp):
                ## Move node up:
                ##Adjust node behind
                node.prev.next = node.next

                ##Adjust node ahead back one, putting current node in front
                node.next.prev = node.prev
                node.next.next = node
                node.next = node.next.next

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:

        ##Add new usage timestamp
        self.lruTimestamp+=1

        newNode = LFUCacheNode(key, value, self.lruTimestamp)

        if key in self.cache:

            ## Increment use count and timestamp
            existingNode = self.cache.get(key)

            existingNode.lruTimestamp = newNode.lruTimestamp
            existingNode.useCount+=1

            ## Update value
            existingNode.value = value

            ## Adjust LFU order
            while existingNode.useCount > existingNode.next.useCount or (existingNode.useCount == existingNode.next.useCount and existingNode.lruTimestamp > existingNode.next.lruTimestamp):
                ## Move existingNode up:
                ##Adjust existingNode behind
                existingNode.prev.next = existingNode.next

                ##Adjust existingNode ahead back one, putting existingNode in front
                existingNode.next.prev = existingNode.prev
                existingNode.next.next = existingNode
                existingNode.next = existingNode.next.next

            return

        ## If not in cache, check for capacity and evict LFU (or tied for LFU -> LRU)
        if self.size == self.capacity:

            ## Remove the node from LFUNode's next and the hashtable.
            removedNode = self.lfuNode.next
            self.cache.pop(removedNode.key, None)
            self.size-=1

            self.lfuNode.next = removedNode.next
            self.lfuNode.next.prev = self.lfuNode

        ## Insert new node at back of LFU cache.
        self.cache[newNode.key] = newNode
        self.size+=1
        newNode.prev = self.lfuNode
        newNode.next = self.lfuNode.next
        self.lfuNode.next.prev = newNode
        self.lfuNode.next = newNode

        ## Adjust LFU order to move most recently used newNode with useCount 1 to the front of the 1's.
        while newNode.useCount > newNode.next.useCount or (newNode.useCount == newNode.next.useCount and newNode.lruTimestamp > newNode.next.lruTimestamp):
            ## Move newNode up:
            ##Adjust newNode behind
            newNode.prev.next = newNode.next

            ##Adjust newNode ahead back one, putting newNode in front
            newNode.next.prev = newNode.prev
            newNode.next.next = newNode
            newNode.next = newNode.next.next

class LFUCacheNode:

    def __init__(self, key: int, value: int, lruTimestamp: int):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
        self.useCount = 1
        self.lruTimestamp = lruTimestamp


# lfu = LFUCache(2)
# lfu.put(2, 2)
# lfu.put(1, 1)
# lfu.get(2)
# lfu.get(1)
# lfu.get(2)
# lfu.put(3, 3)
# lfu.put(4, 4)
# lfu.get(3)
# lfu.get(2)
# lfu.get(1)
# lfu.get(4)