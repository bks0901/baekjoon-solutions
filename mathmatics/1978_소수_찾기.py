"""
## [1978] 소수 찾기
🔗 https://www.acmicpc.net/problem/1978
"""

# 💡 Idea. 에라토스테네스의 체 → O(n loglog n)

def solution(input_list: list):
    MAX = 1000
    is_prime = [False, False] + [True] * (MAX - 1)

    for i in range(2, int(MAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

    # ❗ Note. 에라토스테네스의 체 구현
    # 기본 개념은 굉장히 익숙하지만 에라토스테네스의 체를 구현하려면 연습이 필요하다
    # 코드에서 중요한 두 부분인 for문의 수학적 원리에 대해서 생각해보자
    # 먼저 range(2, int(MAX ** 0.5) + 1)을 살펴보자
    # 2는 소수 체크를 2부터 하기 때문이고
    # int(MAX ** 0.5) + 1은 MAX 까지의 수를 판별하는데 MAX ** 0.5까지만 체크해도 충분하기 때문이다
    # 예를 들어, 30이 소수인지 판별한다고 하자
    # 30이 소수가 아니라면 두 수의 곱으로 표현될 수 있는데, 두 수 중 적어도 하나는 30 ** 0.5 이하여야 한다
    # 즉, MAX ** 0.5까지만 검사해도 모든 합성수가 걸러진다
    # 다음으로 range(i * i, MAX + 1, i)를 살펴보자
    # i * i로 시작하는 이유는 i의 배수를 체크하는 과정에서 가장 먼저 확인해야할 수가 i * i여서이다
    # 예를 들어, i = 5이면, 5의 배수중 5는 남겨야하고, 2~24까지는 소수가 아닌 이상 이미 이전 단계에서 지워졌다
    # 그래서 i * i부터 시작하는 것이고, i씩 늘어나야 한다(참고로 pow(i, 2)로 코딩할 수도 있지만, 성능이 더 떨어져 곱으로 표기한다)


    answer = 0

    for num in input_list:
        if is_prime[num]:
            answer += 1

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    input_list = list(map(int, input().split()))

    print(solution(input_list))


# 📘 Learnings.
# 주어진 적은 범위에서 소수를 구한다면 에라토스테네스의 체!