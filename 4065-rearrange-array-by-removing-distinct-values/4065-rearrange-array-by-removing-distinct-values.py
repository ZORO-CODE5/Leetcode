class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while len(nums)>0:
            diff=[]
            for num in nums:
                if num not in diff:
                    diff.append(num)

            diff.sort()
            for value in diff:
                nums.remove(value)
                ans.append(value)
        return ans
        