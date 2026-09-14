class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grupos = {}

        for palavra in strs:
            # descubro a chave do dicionario
            chave = "".join(sorted(palavra))

            if chave not in grupos:
                grupos[chave] = []

            grupos[chave].append(palavra)

        return list(grupos.values())