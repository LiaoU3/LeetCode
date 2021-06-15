import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        valid_ipv4 = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
        valid_ipv6 =r'(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])'
        if re.match(valid_ipv4, IP):
            return 'IPv4'
        elif re.match(valid_ipv6, IP, flags=re.IGNORECASE):
            return 'IPv6'
        else:
            return 'Neither'
# solution = Solution()
# # IP = "172.16.254.1"
# IP = "2001:0DB8:0000:0000:0000:0000:1428:57a"
# solution.validIPAddress(IP)