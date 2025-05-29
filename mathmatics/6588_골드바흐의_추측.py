"""
## [6588] 골드바흐의 추측
🔗 https://www.acmicpc.net/problem/6588
"""

# 💡 Idea. 에라토스테네스의 체

def solution(numbers: list[int]):

    largest = max(numbers)
    is_prime = [False, False] + [True] * (largest - 1)

    for i in range(2, int(largest ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, largest + 1, i):
                is_prime[j] = False

    answer = []

    for number in numbers:
        found = False
        for a in range(3, number // 2 + 1, 2):
            b = number - a
            if is_prime[a] and is_prime[b]:
                answer.append(f"{number} = {a} + {b}")
                found = True
                break 
        if not found:
            answer.append("Goldbach's conjecture is wrong.")

        # ❗ Note. 최적화 → for문의 범위 비교해보기
        # 처음 코드를 작성하면서는 다음과 같이 범위를 설정했었다
        # for a in range(1, number - 1, 2):
        # 그런데 홀수에서 시작할 때, 1로 시작하기보다 소수면서 가장 작은 홀수인 3부터 시작하는 게 효율적이고
        # a가 반 이상을 넘길 이유가 없으므로 number - 1까지 대신 number // 2까지 반복하는 것이 더 효율적이다

    return '\n'.join(answer)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    numbers = []

    while True:
        line = input()
        if not line:
            break
        num = int(line.strip())
        if num == 0:
            break
        numbers.append(num)

    print(solution(numbers))




# 📘 Learnings.
# 소수 관련 문제에서 '범위가 정해져 있다면' 에라토스테네스의 체를 먼저 고려하자
# 수가 아주 크다면 밀러-라빈을, 단일 숫자 한 개만 소수인지 확인한다면 n ** 0.5까지를 브루트포스로 풀이하고
# 기타 나머지 모든 경우는 에라토스테네스의 체로 푼다