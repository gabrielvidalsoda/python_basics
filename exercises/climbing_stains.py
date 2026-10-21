class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        memory = [0] * (n + 1) # lista de tamanho n+1

        memory[1] = 1
        memory[2] = 2

        for i in range(3, n+1):
            memory[i] = memory[i-1] + memory[i-2]

        return memory[n]

