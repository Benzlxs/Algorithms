
## recursive and monotonic stack

class Solution:
    def largestRectangleArea(self, heights) :
        ans, stk, heights = 0, [(0, 0)], heights + [0]
        for i, h in enumerate(heights):
            ti, th, left = *stk[-1], i
            while th > h:
                ans = max(ans, th * (i - ti)) #expands to the right
                left, _ = stk.pop() #records the left most
                ti, th = stk[-1]
            stk.append((left, h)) #expands to the left
        return ans



if __name__=="__main__":
    input_list = [2,1,5,6,2,3]
    test = Solution()
    res = test.largestRectangleArea(input_list)
    print(res)
