"""
## [2309] 일곱 난쟁이
🔗 https://www.acmicpc.net/problem/2309
"""

# 💡 Idea. 빠른 거듭제곱 → O(log b), 모듈러 연산 활용 등

def solution(input_list: list):

    answer = []
    total = sum(input_list)

    for i in range(0, 9):
        for j in range(i + 1, 9):
            if total - input_list[i] - input_list[j] == 100:
                answer = [input_list[x] for x in range(0, 9) if x != i and x != j]
                break

    # ❗ Note. 내장조합(combinations)의 사용
    # 파이썬에서는 위 코드 대신 9개 중에서 7개를 직접 뽑는 방법을 쉽게 구현할 수도 있다
    # 바로, itertools.combinations를 사용하는 것이다

    # from itertools import combinations
    # 
    # for comb in combinations(arr, 7):  # 9개 중 7개 조합
    #     if sum(comb) == 100:
    #         for h in sorted(comb):
    #             print(h)
    #         break

    # 이렇게 표현하면 가독성도 높고 깔끔한 구현이 가능하다
    # 실제로 itertools의 도구들은 코딩 테스트에서도 사용 가능하므로,
    # 조합(combinations), 순열(permutations) 데카르트 곱(product) 등은 기억해두면 유용하다

    answer.sort()

    return '\n'.join(map(str, answer))

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    input_list = []
    for _ in range(0, 9):
        temp = int(input())
        input_list.append(temp)

    print(solution(input_list))



# 📘 Learnings.
# 브루트포스를 쓰는 건 필요하다. 그런데 그 안에서도 효율적인 방법을 고민하는 것이 중요하다.