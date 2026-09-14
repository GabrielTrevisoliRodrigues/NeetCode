class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for numero in nums:
            chave = numero
            if chave not in hashmap:
                hashmap[numero] = 0
            else:
                return True

        return False