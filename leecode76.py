# 最小覆盖子串
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def is_ok(cnt):
            t_count = Counter(t)
            if len(t_count) < len(cnt):
                return False
            for char, count in t_count.items():
                if cnt[char] < count:
                    return False
            return True

        ans = float('inf')
        ans_str = ""
        left = 0

        cnt = Counter()
        for right, ss in enumerate(s):

            cnt[ss] += 1
            while is_ok(cnt):
                # ans = min(ans, right-left+1)
                l = right - left + 1
                if l < ans:
                    ans = l
                    ans_str = s[left:right + 1]
                temp = s[left]
                cnt[temp] -= 1
                if cnt[temp] == 0:
                    cnt.pop(temp)
                left += 1
        # print(ans_str)
        return ans_str

class Solution_:
    def minWindow(self, s, t):
        need = Counter(t)
        len_need = len(t)
        ans = float('inf')
        ans_str = ""
        left = 0
        for right, ss in enumerate(s):
            if ss in t:
                need[ss] -= 1
                len_need -= 1
            if len_need == 0:
                while True:
                    c = s[left]
                    if c in need:
                        if need[c] == 0:
                            break
                    need[c] += 1
                    left += 1
                if right - left < ans:
                    ans = right - left
                    ans_str = s[left:right+1]
                need[s[left]] += 1
                len_need += 1
                left += 1

        return ans_str



if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    Sol = Solution_()
    print(Sol.minWindow(s, t))
