import itertools
import statistics
#没有想出来n^2的算法，不过我认为可以从中位数和平均数的关系入手，然后做动态规划
#写了一个2^n的baseline
def calculate_val(subset):
    if not subset:
        return float('-inf')
    mean_val = statistics.mean(subset)
    median_val = statistics.median(subset)
    return mean_val - median_val

def find_max_val_subsequence(n, a):
    max_val = float('-inf')
    for r in range(1, n + 1):
        for subset in itertools.combinations(a, r):
            val = calculate_val(subset)
            if val > max_val:
                max_val = val
    return max_val

# 测试用例
n = 4
a = [1, 3, 5, 9]
result = find_max_val_subsequence(n, a)
print(result)