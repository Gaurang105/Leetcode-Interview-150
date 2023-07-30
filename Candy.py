class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        new_arr = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                new_arr[i] = new_arr[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and new_arr[i] <= new_arr[i+1]:
                new_arr[i] = new_arr[i+1] + 1
        return sum(new_arr)