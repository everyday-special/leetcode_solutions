class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_idx = 0
        for i, val in enumerate(arr):
            # Determine index of max(arr)
            if val > arr[max_idx]:
                max_idx = i
        if max_idx == 0 or max_idx == len(arr) - 1:
            # if index of max(arr) is 0 or -1, return False
            return False
        for i in range(max_idx):
            # Determine if values are strictly increasing leading up to max(arr)
            if arr[i] >= arr[i+1]:
                return False
        for i in range(max_idx, len(arr) - 1):
            # Determine if values are strictly decreasing past max(arr)
            if arr[i] <= arr[i+1]:
                return False
        return True
