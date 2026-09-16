class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = dict.fromkeys(nums, 0)
        new_length = 0
        final_length = 0

        for number in nums:
            sequencia = True
            new_length = 0
            #Faz com que façamos as etapas a seguir apenas para numeros começo de sequencia
            if number-1 in hashmap:
                sequencia = False
            else:
                while sequencia == True:
                    if number in hashmap:
                        new_length = new_length + 1
                    else:
                        sequencia = False
                    number = number + 1
                if new_length > final_length:
                    final_length = new_length

        

        return final_length
