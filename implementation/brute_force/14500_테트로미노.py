"""
## [14500] 테트로미노
🔗 https://www.acmicpc.net/problem/테트로미노
"""

# 💡 Idea. 그리디 vs. 브루트포스

def solution(board, n, m):
    tetromino = [
        # ㅡ
        [(0,0),(0,1),(0,2),(0,3)],
        # ㅣ
        [(0,0),(1,0),(2,0),(3,0)],
        # ㅁ
        [(0,0),(0,1),(1,0),(1,1)],

        # ㄴ 4종
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],

        # ㄱ 반대 4종
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(0,1),(0,2),(1,0)],

        # ㅗ, ㅜ, ㅏ, ㅓ
        [(0,0),(0,1),(0,2),(1,1)],
        [(1,0),(1,1),(1,2),(0,1)],
        [(0,0),(1,0),(2,0),(1,1)],
        [(0,1),(1,1),(2,1),(1,0)],

        # ㄹ형 4종
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(0,2),(1,0),(1,1)],
    ]
    
    answer = 0

    for i in range(n):
        for j in range(m):
            for shape in tetromino:
                try:
                    temp = 0
                    for dx, dy in shape:
                        nx = i + dx
                        ny = j + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            raise IndexError
                        temp += board[nx][ny]
                    answer = max(answer, temp)
                except IndexError:
                    continue
    return answer

    # ❗ Note. 그리디 풀이
    # 이 문제에서 가장 간단한 풀이는 n*m을 전체 순회하면서 사전에 세팅한 테트리미노 도형이 맞는지 확인해 계산하는 것이다

    # 맨 처음 브루트포스를 먼저 떠올렸지만, max를 이용해 3*3 영역 안을 잘 커버하기만 하면 되지 않을까 하는
    # 그리디 풀이로 문제를 풀어봤다. 예시는 아래와 같다.

    # # 4 * 0
    # if i + 3 < n:
    #     temp = tile[i][j] + tile[i+1][j] + tile[i+2][j] + tile[i+3][j]
    #     answer = max(answer, temp)
    
    # # 0 * 4
    # if j + 3 < m:
    #     temp = tile[i][j] + tile[i][j+1] + tile[i][j+2] + tile[i][j+3]
    #     answer = max(answer, temp)
    
    # # 3 * 1
    # if i + 2 < n:
    #     if j + 1 < m:
    #         temp = tile[i][j] + tile[i+1][j] + tile[i+2][j] + max(tile[i][j+1], tile[i+1][j+1], tile[i+2][j+1])
    #         answer = max(answer, temp)
    #     elif j - 1 >= 0:
    #         temp = tile[i][j] + tile[i+1][j] + tile[i+2][j] + max(tile[i][j-1], tile[i+1][j-1], tile[i+2][j-1])
    #         answer = max(answer, temp)
    
    # # 1 * 3
    # if j + 2 < m:
    #     if i + 1 < n:
    #         temp = tile[i][j] + tile[i][j+1] + tile[i][j+2] + max(tile[i+1][j], tile[i+1][j+1], tile[i+1][j+2])
    #         answer = max(answer, temp)
    #     elif i - 1 >= 0:
    #         temp = tile[i][j] + tile[i][j+1] + tile[i][j+2] + max(tile[i-1][j], tile[i-1][j+1], tile[i-1][j+2])
    #         answer = max(answer, temp) 


    # # 2 * 2
    # if i + 1 < n and j + 1 < m:
    #     # 1. 정사각형 (ㅁ)
    #     temp = tile[i][j] + tile[i][j+1] + tile[i+1][j] + tile[i+1][j+1]
    #     answer = max(answer, temp)

    #     # 2. S자 (왼쪽 위 → 오른쪽 아래)
    #     temp = tile[i][j+1] + tile[i+1][j+1] + tile[i+1][j] + tile[i][j+2] if j + 2 < m else 0
    #     if temp:  # 유효할 때만 갱신
    #         answer = max(answer, temp)

    #     # 3. S자 좌우 반전 (오른쪽 위 → 왼쪽 아래)
    #     temp = tile[i][j] + tile[i+1][j] + tile[i+1][j+1] + tile[i][j-1] if j - 1 >= 0 else 0
    #     if temp:
    #         answer = max(answer, temp)

    #     # 4. Z자 (수직형) - 위에서 아래로 좌우 교차
    #     if i + 2 < n:
    #         temp = tile[i][j] + tile[i+1][j] + tile[i+1][j+1] + tile[i+2][j+1]
    #         answer = max(answer, temp)

    #     # 5. Z자 반대형 (수직형 좌우 반전)
    #     if i + 2 < n and j + 1 < m:
    #         temp = tile[i][j+1] + tile[i+1][j+1] + tile[i+1][j] + tile[i+2][j]
    #         answer = max(answer, temp)

    # 테스트 케이스를 대체적으로 통과하지만 반례를 맞이하게 되는데, 이는 max가 정교하게 3*1, 1*3, 2*2 유형을 통과하지 못하기 때문이다
    # 기하학적인 형태로서 형태를 잘 캐치하기도 하지만, 오히려 max에 의해 더 큰 값들이 덮어쓰기하는 경우가 발생할 수 있어 좋지 aa않은 풀이다

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    [n, m] = map(int, input().strip('\n').split())
    tile = []
    for i in range(0, n):
        tile.append(list(map(int, input().split())))

    print(solution(tile, n, m))


# 📘 Learnings.
# 때때로 의욕이 앞서 경우의 수를 나눈 그리디로 문제풀이를 할 수 있다. 그리고 그런 접근이 오히려 합리적일 수도 있다.
# 그럼에도 꼼꼼한 테스트를 통해 해당 로직에 대한 반례는 없을지 고민해야 한다.