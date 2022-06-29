from collections import defaultdict
from re import A
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        emailToAccountID = defaultdict(list)
        accountIDtoName = {}

        for i, arr in enumerate(accounts):
            accountIDtoName[i]=arr[0]

            for email in arr[1:]:
                emailToAccountID[email].append(i)

        ##DFS from all emails in an account to all accounts (indexes) they appear in in the accounts list[list]
        ##For all accounts in that list, DFS from them and add all emails together. Append all these values to a single array.

        def dfs(accountIdx, res =[]):

            if accountIdx not in visited:
                visited.add(accountIdx)
                for email in accounts[accountIdx][1:]:

                    if email not in emailChecked:
                        emailChecked.add(email)
                        res.append(email)
                        
                        for idx in emailToAccountID[email]:
                            moreAccounts = dfs(idx, [])
                            if moreAccounts:
                                res+=moreAccounts
                        
            return sorted(res)
        
        result = []
        visited = set()
        emailChecked=set()
        for account in accountIDtoName:
            dfsRes = dfs(account, [])
            if dfsRes:
                result.append([accountIDtoName[account]] + dfsRes)
        
        return result


g = Solution()

print("\n\n\n")
print(g.accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]))
            