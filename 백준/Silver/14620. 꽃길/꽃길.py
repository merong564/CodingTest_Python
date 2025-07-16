N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]  # 방향벡터 (현재 위치와 상하좌우 4방향)
anw = 10001  # 꽃 하나당 최고 비용 (200 * 5군데 = 1000), G의 범위가 0~200이라서 / 최대 비용인 1000을 넘는 임의의 수


# 비용 계산
def func(case: list) -> int:
    anw = 0
    flower = []  # 꽃의 위치 좌표를 쌓을 것임

    # case는 꽃의 1차원 배열 좌표를 가져옴
    for i in case:
        # 1차원 배열 좌표를 2차원 배열 좌표로 변경 (화단 밖으로 나가는 경우를 제외시키기 위해)
        x = i // N
        y = i % N
        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return 10001  # 최대 비용 넘는 것으로 산정해서 min 함수에 걸리게 함
        # flower 리스트에 flower 위치 append / cost 계산
        for d in range(5):  # d = direction
            flower.append((x + dx[d], y + dy[d]))
            anw += G[x + dx[d]][y + dy[d]]

    # 꽃이 겹치는 경우 제외하기 위해 최대 비용 넘는 것으로 산정
    if len(set(flower)) != 15:
        return 10001

    return anw


# main
# 꽃의 위치를 2차원 배열에서 1차원 배열로 나타냄
for i in range(N ** 2):
    for j in range(i + 1, N ** 2):
        for k in range(j + 1, N ** 2):
            # 꽃의 위치가 1차원 배열로 나타나진 상태에서 func 함수로 비용을 구한 뒤에, min 함수로 최솟값을 구함
            anw = min(anw, func([i, j, k]))

print(anw)