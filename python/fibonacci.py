class Solution:
    def fib(self, N: int) -> int:
        list = []
        list.append(0)
        list.append(1)
        for i in range(2, N+1):
            list.append(list[i-1]+list[i-2])
        return list[N]
