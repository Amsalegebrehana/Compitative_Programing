class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        Dict={}
        l=[]
        changed[:]=sorted(changed)

        for i in range(0,len(changed)):
            if changed[i]  not in Dict:
                Dict[changed[i]] = 1
            else:
                 Dict[changed[i]] += 1
        if len(changed)%2!=0 or len(changed)==1:
            return []

        for i in range(0,len(changed)):
            # l=[Dict[changed[i]]]
        
            if Dict[changed[i]] !=0:
                if changed[i]*2 in Dict:
                    if Dict[changed[i]*2] != 0:
                        l.append(changed[i])
                        Dict[changed[i]] -=1
                        Dict[changed[i]*2] -=1
                    else:
                        return []

                else:
                        return []

        return l