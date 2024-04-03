import sys

## https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.size = 0

        ## Initialize lru and mru dummy node.
        self.lruNode = LRUCacheNode(-sys.maxsize, 1)
        self.mruNode = LRUCacheNode(sys.maxsize, 1)
        self.lruNode.next = self.mruNode
        self.mruNode.prev = self.lruNode

    def get(self, key: int) -> int:
        if key in self.cache:

            ## Remove from list
            node = self.cache.get(key)

            node.prev.next = node.next
            node.next.prev = node.prev

            ## Update mruNode
            node.prev = self.mruNode.prev
            self.mruNode.prev.next = node
            self.mruNode.prev = node
            node.next = self.mruNode

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:

        newNode = LRUCacheNode(key, value)
        if key in self.cache:
            ##Update dict witth new value
            self.cache[key] = newNode

            ## Remove from list
            node = self.cache.get(key)

            node.prev.next = node.next
            node.next.prev = node.prev

            ## Update mruNode
            node.prev = self.mruNode.prev
            self.mruNode.prev.next = node
            self.mruNode.prev = node
            node.next = self.mruNode

            return

        ## If not in cache, check for capacity and evict LRU
        if self.size == self.capacity:

            ## Remove the node from LRUNode's next and the hashtable.
            removedNode = self.lruNode.next
            self.cache.pop(removedNode.key, None)
            self.size-=1

            self.lruNode.next = removedNode.next

        ## Insert new node at front of LRU cache. Update mruNode
        self.cache[newNode.key] = newNode
        self.size+=1
        newNode.prev = self.mruNode.prev
        self.mruNode.prev.next = newNode
        self.mruNode.prev = newNode
        newNode.next = self.mruNode


class LRUCacheNode:

    def __init__(self, key: int, value: int):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

lRUCache = LRUCache(2)
lRUCache.put(1, 1) ##// cache is {1=1}
lRUCache.put(2, 2) ##// cache is {1=1, 2=2}
lRUCache.get(1)   ##// return 1
lRUCache.put(3, 3) ##// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    ##// returns -1 (not found)
lRUCache.put(4, 4) ##// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    ##// return -1 (not found)
lRUCache.get(3)    ##// return 3
lRUCache.get(4)   ##// return 4