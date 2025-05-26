"""
## [4375] 1
🔗 https://www.acmicpc.net/problem/4375
"""

# 💡 Idea. 모듈러 누적

def solution(n: int):

    remainder = 0
    count = 0
    while True:
        remainder = (remainder * 10 + 1) % n
        count += 1
        if remainder == 0:
            break
    
    return count
        

    # ❗ Note. 모듈러 누적
    # 아래와 같이 직접적으로 pow를 이용해 자릿수를 올려가며 나머지를 확인할 수 있다
    # def solution(n: int):

    #     rest = 0
    #     last_i = 0
    #     for i in range(0, 10000):
    #         rest = (rest + pow(10, i)) % n
    #         if rest == 0:
    #             last_i = i
    #             break

    #     return last_i+1

    # 하지만 이 방식은 자릿수가 커질수록 pow과 누적된 덧셈으로 시간과 메모리 면에서 비효율적이다

    # 같은 논리를 더 효율적으로 구현하는 방법이 모듈러 누적이다
    # 모듈러 연산은 합이나 곱에 대해 중간중간 모듈러 연산을 진행해도 전체 결과에 영향이 없다
    # 그래서 전체 수의 나머지를 직접 구하는 대신 이전 나머지에 자릿수를 늘려나가는 방식으로 나머지를 갱신한다
    # 즉, 원래 수를 늘려나가지 않고 나머지 쪽을 늘려나가는 것이다
    # remainder = (remainder * 10 + 1) % n


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    for line in sys.stdin:
        if not line.strip():
            continue
        n = int(line)
        print(solution(n))



# 📘 Learnings.
# 각 자리가 모두 1이라는건, 10^0 + 10^1 + 10^2 + ... + 10^n이라는 것이고
# 등비수열의 합에 대해 나누어 떨어지는 지 실제로 확인할 수 있겠지만 이는 비효율적이다
# 그 수가 n의 배수인지 여부만 확인하면 되기 때문에, 모듈러 누적을 활용한다