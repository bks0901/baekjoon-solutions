"""
## [1009] 분산처리
🔗 https://www.acmicpc.net/problem/1009
"""

# 💡 Idea. pow(a, b, mod)는 빠른 거듭제곱으로 O(log b), 모듈러 연산 활용

def solution(a: int, b: int):
    last = pow(a, b, 10)

    # ❗ Note. power(a, b, mod)
    # 계산 중간에 modular 연산을 하는 거듭제곱 알고리즘 사용 -> O(log b)
    # 제곱의 성질(결합법칙)을 이용해
    #   짝수일 때, a^b = (a^(b/2))^2
    #   홀수일 때, a^b = a * a^(b-1)
    # 처리하므로, 매 단계마다 b가 절반이 되어 빠르게 처리할 수 있다

    # 위 원리에 대한 실제 구현은 다음과 같다
    # def fast_pow(a, b, mod):
    #     result = 1
    #     a %= mod
    #     while b > 0:
    #         if b % 2 == 1:
    #             result = (result * a) % mod
    #         a = (a * a) % mod
    #         b //= 2
    #     return result

    # 추가로 이진법 환경이기 때문에 곱셈과 결합법칙은 '어떤 항을 포함할지 판단하는 기준'을 해준다
    # 예를 들어, a^13을 구한다면,
    #   13 = 8 + 4 + 0 + 1 = 1101(이진수)인데,
    # 제곱의 성질(덧셈법칙)에 따라 a^13 = a^(8+4+1)라고 쓸 수 있다
    # 따라서 a^13 = a^1 * a^4 * a^8이므로 '어떤 항을 포함하는지' 알 수 있게 되는 것이다

    # ❗ Note. a ** b % 10
    # a ** b % 10으로 연산해도 같은 계산을 할 수 있지만, b가 커지면 느려지고 메모리를 많이 사용
    # 연산 과정에서 a ** b의 결과를 메모리에 올려서 동작하기 때문에 시간과 공간이 매우 많이 듦 -> TLE/MLE 발생 가능

    return 10 if last == 0 else last


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())
        print(solution(a, b))

# 📘 Learnings
# 백준 풀이를 처음 하면서 눈에 들어온 부분은 생각보다 '입출력 흐름'에 더 집중한다는 점이다.
# 프로그래머스의 문제들은 '문제 풀이'에 집중하면 됐는데, 로직의 완벽 여부에 앞서 전체적인 흐름 구현도 생각해야한다.
# 모든 언어를 공통의 기준으로 평가할 수 있다는 점에서 이렇게 구현된건가 하는 생각을 해본다.