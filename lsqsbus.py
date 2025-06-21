class Solution:
    def longestSquareStreak(self, nums):
        def binary_search(arr, target, new_count):
            low = 0
            count = new_count
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target:
                    count+=1
                    
                    
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return count
        nums.sort()
        count = 0
        max_count = 0

        for i in nums:
            count = binary_search(nums, i**2, 0)
            if count>max_count:
                max_count = count
        
        if count > 1:
            return count
        else:
            return -1

sol = Solution()
print(sol.longestSquareStreak([4,3,6,16,8,2]))