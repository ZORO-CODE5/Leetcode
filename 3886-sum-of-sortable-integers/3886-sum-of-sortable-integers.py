class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)

        total = 0
        for k in divisors:
            possible = True
            for i in range(0, n, k):
                block = nums[i:i + k]
                target = sorted_nums[i:i + k]

                drop_idx = -1
                for j in range(k - 1):
                    if block[j] > block[j + 1]:
                        if drop_idx != -1:
                            possible = False
                            break
                        drop_idx = j

                if not possible:
                    break

                shift = 0 if drop_idx == -1 else drop_idx + 1
                if block[shift:] + block[:shift] != target:
                    possible = False
                    break

            if possible:
                total += k

        return total
        