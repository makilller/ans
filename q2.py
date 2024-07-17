
def check_parentheses(strings):
    #经典题目，使用栈进行匹配即可
    results = []
    for s in strings:
        stack = []
        markers = [' ' for _ in s]
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    markers[i] = '?'
        while stack:
            idx = stack.pop()
            markers[idx] = 'x'
        results.append(s)
        results.append(''.join(markers))
    return results


# 测试输入
input_strings = [
    "bge))))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]
output_results = check_parentheses(input_strings)
for result in output_results:
    print(result)
