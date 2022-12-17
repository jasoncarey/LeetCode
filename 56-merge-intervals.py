# 57. Insert Interval
# ----------
# Medium
# Array

# This uses the same solution as 57. Insert Interval
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals)
        currinterval = intervals[0]

        for i in range(1, len(intervals)):

            # currinterval less than next interval
            if currinterval[1] < intervals[i][0]:
                res.append(currinterval)
                currinterval = intervals[i]
            
            # overlap, so merge interval
            # note: we can ignore the case where currinterval is > next interval because currinterval is an interval in intervals
            else:
                currinterval = [
                    min(currinterval[0], intervals[i][0]),
                    max(currinterval[1], intervals[i][1])
                ]
        
        # append our merged interval if it wasn't already picked up in if statement
        res.append(currinterval)
        return res
            