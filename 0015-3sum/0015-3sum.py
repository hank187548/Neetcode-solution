class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Ans = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1

            while l < r :
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r  -= 1
                elif total < 0:
                    l += 1
                else:
                    Ans.append([nums[i],nums[l],nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # (其實 r 那邊也可以寫去重，但因為 l 跳過了(左邊到的指標會往右所以變得更大)，r 自然配對不到(sum一定會變得比原本大)，所以寫一邊就夠了)
        
        return Ans



        
            
            

 


        