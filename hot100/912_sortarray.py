class Solution:
    def partition(self,nums,left,right):
        mid = nums[left]
        while left < right:
            while left < right and nums[right] >= mid:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        return left

    def quicksort(self,nums,start,end):
        if start < end:
            pviot = self.partition(nums,start,end)

            self.quicksort(nums,start,pviot-1)
            self.quicksort(nums,pviot+1,end)
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) < 2:
            return nums

        start = 0
        end = len(nums) - 1
        sort_nums = self.quicksort(nums,start,end)
        return sort_nums
