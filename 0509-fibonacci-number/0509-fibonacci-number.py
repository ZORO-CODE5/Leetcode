class Solution:
    tab =[0,1,1]
    def fib(self, n: int) -> int:
        if n in Solution.tab:
            return Solution.tab[n]
        return self.fib(n-1) + self.fib(n-2)
        