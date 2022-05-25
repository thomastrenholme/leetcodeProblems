

import copy


nums = [2, 4, 5, 7, 2]

tmpNums = copy.copy(nums)

tmpNums.remove(4)


print("nums: " + str(nums))

print("tmpNums: " + str(tmpNums))



p = ["232"]

print(p.pop())


g = [2, 4, 6, 8, 2, 1, 5, 7, 9, 122, 21]

print(tuple(g))