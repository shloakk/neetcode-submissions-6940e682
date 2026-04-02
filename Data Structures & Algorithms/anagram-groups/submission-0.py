class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr_pos = ord(letter) - ord("a")
                arr[arr_pos] += 1

            str_arr = str(arr)
            if str_arr in buckets:
                buckets[str_arr].append(word)
            else:
                buckets[str_arr] = [word]
            
        return list(buckets.values())