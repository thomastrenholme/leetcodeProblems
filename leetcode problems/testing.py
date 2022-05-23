

import copy


nums = [2, 4, 5, 7, 2]

tmpNums = copy.copy(nums)

tmpNums.remove(4)


print("nums: " + str(nums))

print("tmpNums: " + str(tmpNums))