class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        for elemento in s:
            if elemento == '[' or elemento == '(' or elemento == '{':
                pilha.append(elemento)
            elif len(pilha) == 0:
                return False
            elif elemento == ']':
                if pilha.pop() != '[':
                    return False
            elif elemento == '}':
                if pilha.pop() != '{':
                    return False
            elif elemento == ')':
                if pilha.pop() != '(':
                    return False
        
        if len(pilha)==0: 
            return True
        else:
            return False
                