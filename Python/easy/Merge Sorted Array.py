def merge(nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1