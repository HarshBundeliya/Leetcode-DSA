class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Merge Sort
        """
        Time Complexity (best,avg, worst) = O(nlogn(n))
        Space Complexity = O(n), - including temporary merging arrays; recursion stack is O(log n)

        Remember: Merge Sort has two essential operations: divide the array recursively, 
        then merge the sorted halves back into the original array.
        """
        def merge(arr, low, mid, high):
            temp_arr = []
            left = low
            right = mid + 1

            while left<=mid and right<=high:
                if arr[left] <= arr[right]:
                    temp_arr.append(arr[left])
                    left+=1
                else:
                    temp_arr.append(arr[right])
                    right+=1
            
            while left<=mid:
                temp_arr.append(arr[left])
                left+=1
            while right<=high:
                temp_arr.append(arr[right])
                right+=1
            arr[low:high+1] = temp_arr

        def merge_sort(arr, low, high):
            if low >= high:
                return
            mid = (low + high)//2
            merge_sort(arr, low, mid)
            merge_sort(arr, mid+1, high)
            merge(arr, low, mid, high)
            
        merge_sort(nums, 0, n-1)
        return nums