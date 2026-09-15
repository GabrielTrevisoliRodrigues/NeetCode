class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        
        #calculo da multiplicação de todos os valores
        i = 0
        zero = False
        ocorrencia = 0
        multiplicacao = 1
        for numero in nums:
            if numero != 0:
                multiplicacao = multiplicacao * numero
            else:
                zero = True
                posicao = i
                ocorrencia = ocorrencia + 1
    
            i = i + 1
                

        #calculo de cada elemento do output
        if ocorrencia > 1:
            for numero in nums:
                output.append(int(0))

        elif ocorrencia == 1:
            i = 0
            for numero in nums:
                if i != posicao:
                    output.append(int(0))
                else:
                    output.append(int(multiplicacao))
                i = i + 1
        
        else:
            for numero in nums:
                output.append(int(multiplicacao/numero))

        return output