class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sl = [i for i in s]
    
        pref = [shifts[-1]]

        for i in range(len(shifts) - 2, -1, -1):

            pref.append(pref[-1] + shifts[i])
        pref = pref[::-1]
        for i in range(len(sl)):
            curr = ord(sl[i]) - ord('a')
            
            sl[i] = chr((ord('a') + (curr + pref[i]) % 26))
         
        return "".join(sl)