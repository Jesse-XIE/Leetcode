#  Description: 
#  ---------------

#  Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#  For example,
#  Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#  
#  The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        left = 0 
        right = len(height)-1
        vol = 0
        while left<right-1:
            if height[left]<=height[right]:
                i = left+1
                while height[i]<height[left] and i<right:
                    vol += height[left] - height[i]
                    i += 1
                left = i
            else:
                i = right-1
                while height[i]<height[right] and i>left:
                    vol += height[right] - height[i]
                    i -= 1
                right = i
        return vol