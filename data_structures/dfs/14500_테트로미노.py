"""
## [14500] 테트로미노
🔗 https://www.acmicpc.net/problem/테트로미노
"""

# 💡 Idea. 변형 dfs로 풀어보기 → implementation/brute_force의 테트로미노와 비교

def solution(tile, n, m):
    import sys
    sys.setrecursionlimit(10000)

    visited = [[False] * m for _ in range(n)]
    max_val = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(x, y, depth, total):
        nonlocal max_val
        if depth == 4:
            max_val = max(max_val, total)
            return

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + tile[nx][ny])
                visited[nx][ny] = False

    # ❗ Note. depth
    # depth가 1로 순회구조가 시작되며 중점을 세팅하고
    # depth가 1씩 추가되면서 가로, 세로로 중점을 형성해 따라 들어간다

    def check_extra_shape(x, y):
        nonlocal max_val
        shapes = [
            [(0, 0), (0, -1), (0, 1), (-1, 0)],  # ㅗ
            [(0, 0), (0, -1), (0, 1), (1, 0)],   # ㅜ
            [(0, 0), (-1, 0), (1, 0), (0, -1)],  # ㅓ
            [(0, 0), (-1, 0), (1, 0), (0, 1)]    # ㅏ
        ]

        for shape in shapes:
            try:
                total = 0
                for dx_, dy_ in shape:
                    nx = x + dx_
                    ny = y + dy_
                    if nx < 0 or ny < 0:
                        raise IndexError
                    total += tile[nx][ny]
                max_val = max(max_val, total)
            except:
                continue

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, tile[i][j]) # 출발점 세팅
            visited[i][j] = False
            check_extra_shape(i, j)

    return max_val

    # ❗ Note. dfs로 다룰 수 없는 특수형
    # dfs는 한 노드(칸)에서 시작해서 갈 수 있는 한 방향으로 끝까지 깊게 들어갔다가, 더 이상 갈 수 없으면 다시 돌아와서 다른 방향으로 탐색한다
    # 결국 갈림길이 여러개 나오는 ㅗ, ㅏ, ㅓ, ㅜ 형태에 대해서는 갈 길을 모르므로 커버가 불가능하다
    # 저런 shape만 따로 넘겨서 체크하는 형태로 구현한다

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    [n, m] = map(int, input().strip('\n').split())
    tile = []
    for i in range(0, n):
        tile.append(list(map(int, input().split())))

    print(solution(tile, n, m))




# 📘 Learnings.
# 이미 브루트포스 풀이로 이 문제는 잘 맞출 수 있다. 그렇지만 dfs를 변형한 방식으로도 풀이가 가능해 검토한다