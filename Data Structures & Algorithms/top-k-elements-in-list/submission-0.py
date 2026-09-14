class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resultado = []
        #criamos o hashmap e o preenchemos, com os valores sendo as frequencias dos elementos
        hashmap = {}
        for numero in nums:
            if numero not in hashmap:
                hashmap[numero] = 1
            else:
                hashmap[numero] = hashmap[numero]+1 

        hashmap_ordenado= dict(sorted(hashmap.items(), key=lambda item:item[1], reverse=True))

        for valor, frequencia in hashmap_ordenado.items():
            if k != 0:
                resultado.append(valor)
                k = k-1
            else:
                break

        return resultado