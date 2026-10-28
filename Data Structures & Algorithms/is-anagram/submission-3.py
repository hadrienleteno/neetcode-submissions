class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for c1, c2 in zip(s, t):
            d[c1] = d.get(c1, 0) + 1
            d[c2] = d.get(c2, 0) - 1
        return all(v == 0 for v in d.values())