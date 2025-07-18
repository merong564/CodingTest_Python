n = int(input())
num_list = list(map(int, input().split()))
add_cnt, sub_cnt, mul_cnt, div_cnt = map(int, input().split())
max_ans, min_ans = -int(1e9), int(1e9)

def dfs(idx, add_cnt, sub_cnt, mul_cnt, div_cnt, result):
    global max_ans, min_ans

    if idx == n:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return

    if add_cnt:
        dfs(idx + 1, add_cnt - 1, sub_cnt, mul_cnt, div_cnt, result + num_list[idx])
    if sub_cnt:
        dfs(idx + 1, add_cnt, sub_cnt - 1, mul_cnt, div_cnt, result - num_list[idx])
    if mul_cnt:
        dfs(idx + 1, add_cnt, sub_cnt, mul_cnt - 1, div_cnt, result * num_list[idx])
    if div_cnt:
        dfs(idx + 1, add_cnt, sub_cnt, mul_cnt, div_cnt - 1, int(result / num_list[idx]))

dfs(1, add_cnt, sub_cnt, mul_cnt, div_cnt, num_list[0])

print(max_ans)
print(min_ans)