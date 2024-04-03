
## https://leetcode.com/problems/design-browser-history/
class BrowserHistory:

    def __init__(self, homepage: str):
        initial = BrowserHistoryNode(homepage, None)
        self.current = initial

    def visit(self, url: str) -> None:
        visitSite = BrowserHistoryNode(url, self.current)
        self.current = visitSite

    def back(self, steps: int) -> str:
        for i in range(0, steps):
            ## reached end of line
            if self.current.previous is None:
                return self.current.url

            previousSite = self.current.previous
            previousSite.next = self.current
            self.current = previousSite

        return self.current.url

    def forward(self, steps: int) -> str:
        for i in range(0, steps):
            ## reached end of line
            if self.current.next is None:
                return self.current.url

            nextSite = self.current.next
            nextSite.previous = self.current
            self.current = nextSite

        return self.current.url



class BrowserHistoryNode:
    def __init__(self, url:str, previous: 'BrowserHistoryNode'):
        self.previous = previous
        self.url = url
        self.next = None



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)