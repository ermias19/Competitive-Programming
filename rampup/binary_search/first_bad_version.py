class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=1
        end=n
        bad_version=n
        while start<=end:
            mid=(start+end)//2
            v=isBadVersion(mid)
            if v:
                bad_version=mid
                end=mid-1
            else:
                start=mid+1
        return bad_version
            