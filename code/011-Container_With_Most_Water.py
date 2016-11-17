#  Description: 
#  ---------------

#  Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#  Note: You may not slant the container.



class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        if N < 2:
            return 0
        p1, p2 = 0, N - 1
        vol = []
        for i in range(N):
            h1, h2 = height[p1], height[p2]
            vol.append(min(h1, h2) * (p2 - p1))
            if h1 < h2:
                p1 += 1
            else:
                p2 -= 1
        return max(vol)
        