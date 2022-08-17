class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.time_winning = collections.defaultdict(lambda: -1)
        vote_count = collections.defaultdict(int)
        cur_max, cur_win = 0, -1
        for p, t in zip(persons, times):
            vote_count[p] += 1
            if vote_count[p] >= cur_max: cur_max, cur_win = vote_count[p], p
            self.time_winning[t] = cur_win
        self.times = times                

    def q(self, t: int) -> int:
        return self.time_winning[self.times[bisect.bisect_right(self.times, t)-1]]