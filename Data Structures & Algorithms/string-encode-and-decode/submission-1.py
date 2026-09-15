class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "EMPTY ARRAY"

        encode_text = ""
        for word in strs:
            for letter in word:
                encode_text = encode_text + str(ord(letter)) + "*"
            
            
            if word != "":
                encode_text = encode_text[:-1]

            encode_text = encode_text + "-"
            
        return encode_text[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY ARRAY":
            return [] 
            
        decode_list = []
        encode_words = s.split("-")
        
        for word in encode_words:
            decode_word = ""
            if word != "":
                letters = word.split("*")
                for letter in letters:
                    decode_word = decode_word + chr(int(letter))
                    
            
            decode_list.append(decode_word)
            
        return decode_list