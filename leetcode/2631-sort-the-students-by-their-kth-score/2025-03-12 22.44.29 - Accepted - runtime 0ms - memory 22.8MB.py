class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        kth_score = []
        for i in range (len(score)):
            kth_score.append([i,score[i][k]])
        kth_score.sort(key=lambda x: x[1],reverse=True)
        ans = []
        for i in range (len(score)):
            ans.append(score[kth_score[i][0]])
        return ans
