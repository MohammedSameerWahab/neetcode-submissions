class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_res = []
        for s in strs:
            encoded_res.append(f"{len(s)}#{s}")
        return ''.join(encoded_res)

    def decode(self, s: str) -> List[str]:
        decoded_res = []

        i=0
        while i<len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            word_start = j+1
            word_end = word_start + length
            decoded_res.append(s[word_start:word_end])

            i = word_end
        return decoded_res
