class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "/" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            slash = s.index("/", i)
            size = int(s[i:slash])
            decoded.append(s[slash + 1:slash + 1 + size])
            i = slash + 1 + size
        return decoded
