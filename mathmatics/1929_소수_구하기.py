"""
## [1929] 소수 구하기
🔗 https://www.acmicpc.net/problem/1929
"""

# 💡 Idea. 에라토스테네스의 체

def solution(m: int, n: int):

    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # ❗ Note. 최적화 신경쓰기
    # 보통 MAX 지점까지 계산을 하지만, 이번 문제에서는 n까지의 소수만 구하면 되므로
    # MAX = n으로 처리해 반복문을 만든다

    answer = [str(i) for i in range(m, n+1) if is_prime[i]]

    return '\n'.join(answer)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split())
    print(solution(m, n))

# 📘 Learnings.
# 범위가 주어진 데서 소수를 구한다면 역시 에라토스테네스의 체
# 여유가 있다면 최적화 부분까지 조금 더 신경쓸 것