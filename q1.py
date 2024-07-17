def min_subsequences(source: str, target: str) -> int:
    # 首先检查是否所有的目标字符串都在源字符串中
    source_set = set(source)
    for char in target:
        if char not in source_set:
            return -1


    source_len = len(source)
    target_len = len(target)
    source_idx = 0
    target_idx = 0
    subsequences_count = 0
    # 贪心匹配
    while target_idx < target_len:
        subsequences_count += 1
        source_idx = 0
        while source_idx < source_len and target_idx < target_len:
            if source[source_idx] == target[target_idx]:
                target_idx += 1
            source_idx += 1

    return subsequences_count


# 测试用例
print(min_subsequences("abc", "abcbc"))  # Output: 2
print(min_subsequences("abc", "acdbc"))  # Output: -1
print(min_subsequences("xyz", "xzyxz"))  # Output: 3
