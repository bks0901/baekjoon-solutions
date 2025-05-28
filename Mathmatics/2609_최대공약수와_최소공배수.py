"""
## [2609] 최대공약수와 최소공배수
🔗 https://www.acmicpc.net/problem/2609
"""

# 💡 Idea. 유클리드 호제법 → 최대공약수와 최소공배수 찾기(O(log n))

def get_gcd(a: int, b: int):
    while True:
        a, b = b, a%b
        if b == 0:
            break
    return a

    # ❗ Note. 유클리드 호제법
    # 정규 교육과정에서는 다루지 않지만, 최대공약수를 구하는 알고리즘
    # 호제란 서로 나눈다라는 뜻이며, 이 알고리즘은 인류 최초의 알고리즘이라 한다
    # 두 양의 정수 a, b(단, a > b)에 대하여 a = b*q + r이라 할 때, 
    #  a, b의 최대공약수는 b, a%b의 최대공약수와 같다
    # 이 성질을 이용한 것이 위의 풀이이며, 이 알고리즘은 재귀 형태로 입력 숫자를 절반 이하로 줄이기 때문에 O(log n)이다

    # 이해를 돕기위해 예를 들어 생각해보자
    # 24와 15의 최대공약수를 구한다고 해보면 다음과 같다
    # 24 = 15 * 1 + 9
    # 15 = 9 * 1 + 6
    # 9 = 6 * 1 + 3
    # 6 = 3 * 2 + 0
    # a = b * q + (a % b) -> b = (a % b) * p + 0 꼴로 진행함을 확인할 수 있다
    # 이는 a, b의 공약수가 b, a%b와 공약수 집합을 공유하는 수학적 원리 때문이다

    # 증명
    # a = d * k1, b = d * k2라고 할 때,
    # a = b * q + r 를 정리한 r = a - bq에 대해
    # a - bq = d * k1 - (d * k2) * q가 성립하므로, a - bq는 d의 배수이다
    # 따라서 a, b의 공약수는 a - bq(= r)와 b의 공약수이기도 하며,
    # 이는 공약수 집합이 b, r에도 공유된다는 뜻이다 → 즉, gcd(a, b) = gcd(b, r)



def solution(a: int, b: int):

    gcd = 0
    lcm = 0

    gcd = get_gcd(a, b)
    lcm = a * b // gcd

    # ❗ Note. 소인수분해 + 브루트포스 풀이
    # 떠올리기 가장 쉬운 방법으로는 소인수분해를 브루트포스로 구현하는 방법이 있다
    # 이 방법도 수가 작다면 괜찮은 풀이일 수 있다

    # large_one = max(a, b)
    # temp = []
    # for i in range(1, large_one+1):
    #     if a % i == 0 and b % i == 0:
    #         temp.append(i)
            
    # gcd = max(temp)
    # lcm = a * b // gcd

    # 둘 중에 더 큰 수를 이용해 공약수들을 찾고, 그중 가장 큰 것에 접근하는 방식이며
    # O(n) 수준의 알고리즘이다
    # 다만 컴퓨터에서는 늘 유클리드 호제법이 더 빠르기 때문에 해당 방법을 익혀서 사용하는 것이 좋다




    return f"{gcd}\n{lcm}"

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    a, b = map(int, input().split())

    print(solution(a, b))



# 📘 Learnings.
# 최대공약수와 최소공배수가 보이면 바로 유클리드 호제법을 떠올리자.
# 컴퓨터에서는 그게 맞다! 그리고 일상 생활에서도 풀이가 여러개라면 더 좋지 않을까?