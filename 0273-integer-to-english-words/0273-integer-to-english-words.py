class Solution:
    def numberToWords(self, num: int) -> str:
        l1 = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        l2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
   
        def rec(num):
            s = ""
            if num < 20:
                s = l1[num]
            elif num < 100:
                s = l2[num // 10] + " " + l1[num % 10]
            elif num < 1000:
                s = rec(num // 100) + " Hundred " + rec(num % 100)
            elif num < 1000000:
                s = rec(num // 1000) + " Thousand " + rec(num % 1000)
            elif num < 1000000000:
                s = rec(num // 1000000) + " Million " + rec(num % 1000000)
            else:
                
                s = rec(num // 1000000000) + " Billion " + rec(num % 1000000000)
           
            return  s.strip()
        if num == 0:
            return "Zero"
    
        return rec(num)