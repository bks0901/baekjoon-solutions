"""
## [9095] 1, 2, 3 더하기
🔗 https://www.acmicpc.net/problem/9095
"""

# 💡 Idea. 동적 프로그래밍(DP)

def solution(input_list: list):

    # 0 -> 1
    # 1 -> 1
    # 2 -> 2
    # 3 -> 1 + 1 + 1 / 1 + 2 / 2 + 1 / 3 -> 4
    # 4 -> 1 + 1 + 1 + 1 / 1 + 3 / 3 + 1 / 2 + 1 + 1 / 1 + 2 + 1 / 1 + 1 + 2 / 2 + 2 -> 7

    answer = [0] * 12
    answer[1], answer[2], answer[3] = 1, 2, 4

    for i in range(4, 12):
        answer[i] = answer[i-1] + answer[i-2] + answer[i-3]

    # ❗ Note. 수학적 귀납에 기반한 점화식 유도
    # 이 방법을 보다보면 왜 이게 가능할까 궁금할 수 있다
    # 이 문제는 1, 2, 3의 합으로 정수 n을 나타내는 방법의 수를 구하는 '중복 순열' 계산 문제이다
    # 다음과 같은 귀납 구조를 따르는데,
    # 어떤 수 n을 만들기 위해 마지막으로 더한 수가 1이라면, 그 전에 n-1을 만들었어야 한다
    # 마지막이 2였다면, 그 이전에는 n-2를 만들었어야 한다
    # 이런 식으로 n을 만들기 위한 경우의 수는
    # f(n) = f(n-1) + f(n-2) + f(n-3)이 된다
    # 만약 어렵다면, 이 증명이 형식적 정당화에 가까운 방법이다보니 직관적으로 잘 와닿지 않을 수 있으므로 천천히 생각해보자

    return '\n'.join(str(answer[i]) for i in input_list)

    # ❗ Note. 브루트 포스 풀이
    # 이 문제는 n이 작은 편이기 때문에 브루트 포스로도 풀 수 있다. 그리고 백준의 분류는 브루트 포스로 되어 있다.
    # 아래처럼 코드를 작성해 접근 가능하다.
    # def count(n):
    #     if n < 0:
    #         return 0
    #     if n == 0:
    #         return 1
    #     return count(n-1) + count(n-2) + count(n-3)

    # 그렇지만 확장성을 생각했을 때 현재 풀이와 같은 DP로 풀이하는 것이 더 효율적이다


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())
    input_list = []
    for _ in range(T):
        temp = int(input())
        input_list.append(temp)

    
    print(solution(input_list))

    # ❗ Note.

# 📘 Learnings.
# 셋만 쓸 수 있다. 그것은 셋을 중심으로 다시 사고하라는 뜻으로 이해해야 한다.
# n을 1, 2, 3의 합으로 표현하는 모든 경우의 수는, 마지막 숫자가 1인 경우 + 2인 경우 + 3인 경우의 수의 총합이다.
# 만약 1, 3, 4만 가능하다면 f(n) = f(n-1) + f(n-3) + f(n-4)가 되어야 한다