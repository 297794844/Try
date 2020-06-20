class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)

        if size % 2 == 1:
            return nums[size//2]

        if size % 2 == 0:
            return (nums[size//2] + nums[size//2 - 1])/2
A=[1, 2]
B=[3]
t=Solution()
print(t.findMedianSortedArrays(A, B))