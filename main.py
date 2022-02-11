# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [1]*length
        factor = 1
        for i in range(1, length + 1):
            print(factor)
            result[i - 1] = factor
            factor *= nums[i - 1]
        factor = 1
        for i in range(length - 1, -1, -1):
            result[i] *= factor
            factor *= nums[i]
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.productExceptSelf([7, 3, 8, 2, 4, 6]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
