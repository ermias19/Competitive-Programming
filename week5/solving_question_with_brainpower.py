class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        score = [0]*n
        for i in range(n-1,-1,-1):
            pts,skip = questions[i]
            if i == n-1:
                score[i] = pts
                continue
            if skip < n-i-1:
                score[i] = max(pts + score[i+skip+1],score[i+1])
            else:
                score[i] = max(pts,score[i+1])
        return max(score)