#you are given an array of integers, your task is to reverse the array without using any built-in functions.


class Solution:
    def reverseArray(self, arr):
        #return reverse_array(arr)
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
obj=Solution()
arr=[1,2,3,4,5]
result=obj.reverseArray(arr)
print("Reversed array:", result)