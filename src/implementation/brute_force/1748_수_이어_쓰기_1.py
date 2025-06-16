"""
## [1748] 수 이어 쓰기 1
🔗 https://www.acmicpc.net/problem/1748
"""

# 💡 Idea. 자릿수 범위를 구간별로 나누기

def solution(n: int):

    answer = 0
    length = len(str(n))

    for i in range(0, length - 1):
        answer += 9 * pow(10, i) * (i + 1)

    # ❗ Note. 몇 개나 되나?
    # 1 ~ 9 -> 10^0 ~ 10^1 - 1 = 9
    # 10 ~ 99 -> 10^1 ~ 10^2 - 1 = 90
    # 100 ~ 999 -> 10^2 ~ 10^3 -1 = 900

    answer += ((n - pow(10, length - 1) + 1) * length)

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    print(solution(n))



# 📘 Learnings.
# 간단한 문제라고 생각될수록 빠르게 규칙을 찾아 접근한다