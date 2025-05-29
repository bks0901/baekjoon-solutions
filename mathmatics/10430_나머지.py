"""
## [10430] 나머지
🔗 https://www.acmicpc.net/problem/10430
"""

# 💡 Idea. 모듈러 연산

def solution(a: int, b: int, c: int):

    first = (a + b) % c
    second = ((a % c) + (b % c)) % c
    third = (a * b) % c
    fourth = ((a % c) * (b % c)) % c

    # ❗ Note. 모듈러 연산의 분배법칙
    # 덧셈: 성립 -> (a + b) % c = ((a % c) + (b % c)) % c 
    # 뺄셈: 성립(단, 음수 보정 필요) -> (a - b) % c = ((a % c) - (b % c) + c) % c
    #      (파이썬에서는 자동 보정해주지만, 대부분의 경우에서는 음수 보정을 위한 + c가 요구된다)
    # 곱셈: 성립 -> (a * b) % c = ((a % c) * (b % c)) % c
    # 나눗셈: 일반적으로 불성립

    return f"{first}\n{second}\n{third}\n{fourth}"


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    
    print(solution(a, b, c))

# 📘 Learnings.
# 모듈러 연산의 분배법칙에 대해 학습