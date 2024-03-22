# 最小覆盖子串
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        cnt = {}
        for c in t:
            cnt[c] = cnt.get(c, 0) + 1

        left = 0
        right = 0
        win_cnt = 0

        min_len = float('inf')
        res: str = str()

        while right < len(s):
            if s[right] in cnt.keys():
                cnt[s[right]] -= 1
                win_cnt += 1
            if win_cnt == len(t):
                while s[right] in cnt.keys() and cnt[s[right]] < 0:
                    if s[left] in cnt.keys():
                        cnt[s[left]] += 1
                        win_cnt -= 1
                    left += 1

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
            right += 1
        return res


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    Sol = Solution()
    print(Sol.minWindow(s, t))
