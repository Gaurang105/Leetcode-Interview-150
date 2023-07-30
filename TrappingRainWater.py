class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 
        
        n = len(height)
        l, r = 0, n-1

        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
