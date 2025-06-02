"""
## [1476] 날짜 계산
🔗 https://www.acmicpc.net/problem/1476
"""

# 💡 Idea. 브루트 포스 with 모듈러

def solution(e: int, s: int, m: int):
    # 지구 e, 태양 s, 달 m -> 1~15 / 1~28 / 1~19

    count = 1
    brute_e = 1
    brute_s = 1
    brute_m = 1

    while True:

        if e == brute_e and s == brute_s and m == brute_m:
            break

        count += 1

        brute_e = (brute_e % 15) + 1
        brute_s = (brute_s % 28) + 1
        brute_m = (brute_m % 19) + 1

        # ❗ Note. 그냥 비교하기
        # 아래 코드와 같이 그냥 비교해도 답을 맞추는데는 무리가 없다

        # brute_e += 1
        # brute_s += 1
        # brute_m += 1

        # if brute_e > 15:
        #     brute_e = 1
        # if brute_s > 28:
        #     brute_s = 1
        # if brute_m > 19:
        #     brute_m = 1

        # 다만 코드를 좀 더 읽기 쉽게하고, 범위에 대한 혼동을 없애고 싶다면 mod를 사용하자



    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    e, s, m = map(int, input().split())

    print(solution(e, s, m))

