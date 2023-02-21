class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        queryIP = queryIP.replace(":",".")
        spl = queryIP.split(".")
        hexa = {"a","b","c","d","e","f"}

        if len(spl) == 4:
            for ip in spl:
                if not ip.isdigit() or len(ip) >= 2 and ip[0] == "0" or int(ip) > 255 or int(ip) < 0:
                    
                    return "Neither"
            return "IPv4"
        elif len(spl) == 8:
            for ip in spl:
                # print(ip, ip.isdigit())
                if len(ip) < 1 or len(ip) > 4:
                    return "Neither"
                elif  not ip.isdigit() and 1<=len(ip)<=4 :
                    
                    for i in ip:
          
                        if not i.isdigit() and i.lower() not in hexa:
                    
                            return "Neither"
                   
            return "IPv6"
        else:
            return "Neither"