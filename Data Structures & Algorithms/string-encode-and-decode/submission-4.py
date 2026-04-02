class Solution:

    def encode(self, strs: List[str]) -> str:
        each_str_len = [str(len(s)) for s in strs]
        encoded = ""
        for i in range(len(strs)):
            encoded = encoded + str(each_str_len[i]) + "≈" + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        output = []
        while len(s) > 0:
            str_len, s = s.split("≈", 1)
            output += [s[:int(str_len)]]
            s = s[int(str_len):]
        return output