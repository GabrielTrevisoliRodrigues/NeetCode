class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        resultado = []
        i = 0
        for indice, valor in enumerate(nums):
            hashmap[valor] = indice    
        for numero in nums:
            interrese = target - numero
            if (interrese in hashmap) and (hashmap[interrese]!=i):
                resultado.append(i)
                resultado.append(hashmap[interrese])
                return resultado
            i=i+1