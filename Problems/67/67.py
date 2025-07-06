class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = []
        carry = 0
        for i in range(max(len(a), len(b))):
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[i]) if i < len(b) else 0
            res.append(str((n1 + n2 + carry) % 2))
            carry = 1 if n1 + n2 + carry >= 2 else 0
        if carry == 1:
            res.append("1")
        return "".join(res[::-1])
