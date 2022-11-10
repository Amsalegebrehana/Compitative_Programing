class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        size = len(s)
        letters = [i for i in s]
        result = []
        def backtrack(start, path):
            if len(path) == size:
                result.append("".join(path))
                return
            if letters[start].isalpha() and letters[start].isupper():
                backtrack(start +1, path + [letters[start].lower()])
            elif letters[start].isalpha() and letters[start].islower():
                backtrack(start +1, path + [letters[start].upper()])
            
            backtrack(start + 1, path + [letters[start]])
        backtrack(0,[])
        return result
                
        