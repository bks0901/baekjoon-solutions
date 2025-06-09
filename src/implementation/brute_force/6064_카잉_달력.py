"""
## [6064] 카잉 달력
🔗 https://www.acmicpc.net/problem/6064
"""

# 💡 Idea. 브루트 포스와 수학

# def solution(input_list: list):
    
#     from math import gcd

#     def lcm(a, b):
#         return a * b // gcd(a, b)

#     answer = [str(-1)] * len(input_list)

#     for index, [m, n, x, y] in enumerate(input_list):
#         count = 1
#         brute_x = 1
#         brute_y = 1
#         while count <= lcm(m, n):
#             if brute_x == x and brute_y == y:
#                 answer[index] = str(count)
#                 break

#             count += 1
#             brute_x = (brute_x % m) + 1
#             brute_y = (brute_y % n) + 1

#     return '\n'.join(answer)

def solution(input_list: list):
    from math import gcd

    def lcm(a, b):
        return a * b // gcd(a, b)

    answer = []

    for m, n, x, y in input_list:
        k = x
        max_k = lcm(m, n)
        found = False

        while k <= max_k:
            if (k - y) % n == 0:
                answer.append(str(k))
                found = True
                break
            k += m

        if not found:
            answer.append('-1')

    return '\n'.join(answer)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())
    input_list = []
    for _ in range(T):
        m, n, x, y = map(int, input().split())
        input_list.append([m, n, x, y])

    print(solution(input_list))

    # ❗ Note.

# 📘 Learnings.
# 기억에서 출발하되, 조건과 구조를 하나씩 확인하며 검증하자
# 전에 풀었던 [1476] 날짜 계산과 유사해서 바로 모듈러를 이용해서 풀었는데,
# 만약에 좀 더 고민했다면 더 나은 코드를 더 빨리 찾을 수 있었을 것이다