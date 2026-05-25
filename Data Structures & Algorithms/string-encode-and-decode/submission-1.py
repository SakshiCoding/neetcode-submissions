class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        for s in strs:
            sizes.append(len(s))
        result = ""
        for sz in sizes:
            result += str(sz)
            result += ","
        result += "#"
        for s in strs:
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        sizes = []
        result = []
        if not s:
            return []
        i = 0
        while s[i] != "#":
            current = ""
            while s[i] != ',':
                current += s[i]
                i += 1
            sizes.append(int(current))
            i += 1
        i += 1
        for sz in sizes:
            result.append(s[i: i+sz])
            i += sz
        return result
