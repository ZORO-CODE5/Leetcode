class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aliceDays = arriveAlice.split("-") + leaveAlice.split("-")
        bobDays = arriveBob.split("-") + leaveBob.split("-")
        bobstart = self.numberOfdays(int(bobDays[0]) , int(bobDays[1]))
        bobend = self.numberOfdays(int(bobDays[2]) , int(bobDays[3]))
        alicestart = self.numberOfdays(int(aliceDays[0]) , int(aliceDays[1]))
        aliceend = self.numberOfdays(int(aliceDays[2]) , int(aliceDays[3]))
        start = max(alicestart , bobstart)
        end = min(aliceend , bobend)
        if start > end:
            return 0
        count = 0
        return end - start + 1
    
    def numberOfdays(self , month , day):
        d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        print(month , day)
        for i in range(month-1):
            days += d[i]

        return days + day