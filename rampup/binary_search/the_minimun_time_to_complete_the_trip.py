class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, totalTrips * min(time)
        while l <= r:
            mid = l + (r-l)//2
            count_trips = 0
            for t in time:
                count_trips += mid // t
            if count_trips >= totalTrips:
                r = mid -1
            else:
                l = mid + 1
        return l
        