

class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = True if n >= 0 else False
        ans,n=1,abs(n)
        b=bin(n)[2:]
        if int(b[-1]):
            ans*=x*int(b[-1])
        powers=[x for _ in range(len(b))]
        for i in range(2,len(b)+1):
            powers[-i]=powers[-i+1]*powers[-i+1]
            if int(b[-i]):
                ans*=powers[-i]*int(b[-i])
        return ans if sign else 1/ans


