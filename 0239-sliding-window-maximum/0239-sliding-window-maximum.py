class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # if not nums:
        #     return []
            
        # max_in_window = max(nums[0:k])
        # max_list = [max_in_window]
        # l = 1
        
        # while l <= len(nums) - k:
            
        #     old_out = nums[l - 1]
        #     new_in = nums[l + k - 1]
            
        #     if new_in >= max_in_window:
        #         max_in_window = new_in
                
        #     elif old_out == max_in_window:
        #         max_in_window = max(nums[l : l+k])
                
            
        #     max_list.append(max_in_window)
            
        #     l += 1

        # return max_list

        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output