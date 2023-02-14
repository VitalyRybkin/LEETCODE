"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

n = 6

def climbStairs(n: int) -> int:
    res = 0
    step1 = 0
    step2 = 1
    for i in range(n):
        res = step1 + step2
        step1, step2 = step2, res


    return res

print(climbStairs(n))