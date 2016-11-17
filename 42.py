class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        left = 0
        right = len(height) - 1
        vol = 0
        while left < right - 1:
            if height[left] <= height[right]:
                i = left + 1
                while height[i] < height[left] and i < right:
                    vol += height[left] - height[i]
                    i += 1
                left = i
            else:
                i = right - 1
                while height[i] < height[right] and i > left:
                    vol += height[right] - height[i]
                    i -= 1
                right = i
        return vol
