class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []

        # n =len(nums)

        # for i in range(n):

        #     product =1

        #     for j in range(n):

        #         if i == j:
        #             continue
        #         product *= nums[j]
            
        #     ans.append(product)

        # return ans

        n = len(nums)
        res =[0] * n

        res[0] = 1

        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]

        postfix = 1

        for i in range(n-1,-1,-1):
            res[i] = res[i] * postfix

            postfix = postfix * nums[i]

        return res
