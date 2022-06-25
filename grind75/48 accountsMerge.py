from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        ##The first name in 
        accountToName = {}

        ##If 
        duplicateToOrig = {}