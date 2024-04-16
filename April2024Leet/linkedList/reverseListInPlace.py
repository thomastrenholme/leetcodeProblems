from builtins import list
from typing import Union, Sequence


class Solution:
    def reverse_list_mutate(self, num_list: Union[None, Sequence[float]]) -> None:
        # 'Reverses a list of numbers, modifies the input list, returns None!
        if num_list is None:
            raise ValueError ('List is None')
        if num_list == []:
            return None

        i = 0
        j = len(num_list) -1
        while i < j:
            tmp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = tmp
            i+=1
            j-=1

        return None

sol = Solution()
grr = [1, 2, 3, 4, 5, -7, 9, 11]
sol.reverse_list_mutate(grr)
print(grr)