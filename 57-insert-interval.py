# 57. Insert Interval
# ----------
# Medium
# Array

# This uses the same solution as 56. Merge Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            
            # new interval less than current interval (no overlap)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # curr interval is less than new interval (no overlap)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # overlap, so let's merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
            
        res.append(newInterval)
        return res
