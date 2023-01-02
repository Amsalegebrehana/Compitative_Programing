class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
        news =  s.split(" ")
        print(pattern, news)
        if len(pattern) != len(news):
            return False
        ps = {}
      
        ss = {}

        for i in range(len(pattern)):
            if news[i] not in ss:
                ss[news[i]] = pattern[i]
            elif ss[news[i]] != pattern[i]:
                return False
            if pattern[i] not in ps:
                ps[pattern[i]] = news[i]
            elif ps[pattern[i]] != news[i]:
                return False
            
     
        return True

        