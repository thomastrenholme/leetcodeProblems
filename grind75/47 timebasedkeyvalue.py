from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = {}
        self.keyTimeDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key, timestamp)] = value
        self.keyTimeDict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if len(self.keyTimeDict[key])>0 and self.keyTimeDict[key][0]>=timestamp:
            time = self.searchTimes(self.keyTimeDict[key], timestamp)
            return self.store[(key, time)]
        return ""


    ##returns time or closest time less than time from list of times
    def searchTimes(self, arr, target):
        l = 0
        r = len(arr)-1


        while l<=r:
            middle = l + (r-l)//2
            print("l: " + str(l))
            print("R: " + str(r))
            print("m: " + str(middle))
            
            if target > arr[middle]:
                l = middle+1
            elif target < arr[middle]:
                r = middle-1
            else:
                return arr[middle]
        ##Return closest if not there
        return arr[l-1] if l>0 else arr[0]



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)