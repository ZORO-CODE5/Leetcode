class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        m = len(arr2)
        
        for x in arr1:
            low = 0
            high = m - 1
            valid = True
            
            while low <= high:
                mid = (low + high) // 2
                if abs(x - arr2[mid]) <= d:
                    valid = False
                    break
                elif arr2[mid] < x - d:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            if valid:
                count += 1
                
        return count