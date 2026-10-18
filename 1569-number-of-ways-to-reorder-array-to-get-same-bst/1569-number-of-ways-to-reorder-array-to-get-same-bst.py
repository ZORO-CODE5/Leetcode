class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9 + 7

        def solve(a):
            if len(a) <= 2:
                return 1
            
            root = a[0]
            left = []
            right = []
            
            for x in a[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)
            
            mix = comb(len(left) + len(right), len(left))
            
            return mix * solve(left) * solve(right)

        return (solve(nums) - 1) % mod