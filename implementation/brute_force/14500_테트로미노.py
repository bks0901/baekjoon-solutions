"""
## [14500] 테트로미노
🔗 https://www.acmicpc.net/problem/테트로미노
"""

# 💡 Idea. 빠른 거듭제곱 → O(log b), 모듈러 연산 활용 등

def solution(tile: list, n: int, m: int):

    total = n * m

    # 4 * 0
    # 3 * 1
    # 2 * 2
    
    




    answer = 0
    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    [n, m] = map(int, input().strip('\n').split())
    tile = []
    for i in range(0, n):
        tile.append(list(map(int, input().split())))

    print(solution(tile, n, m))


    # ❗ Note.

# 📘 Learnings.
# 