class Solution:
    def reformatDate(self, date: str) -> str:
        ans = ''
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split()
        for i in date[0]:
            if i.isdigit():
                ans += i
        if len(ans) == 1:
            ans = '0' + ans
        ans = '-' + ans
       
        ans = '0' * (month.index(date[1])+1 < 10) + str(month.index(date[1])+1) + ans
        ans = '-' + ans
        ans = str(date[2]) + ans
        return ans
        