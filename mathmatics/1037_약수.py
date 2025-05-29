"""
## [1037] 약수
🔗 https://www.acmicpc.net/problem/1037
"""

# 💡 Idea. 진짜 약수의 최소값 * 최대값 = N

def solution(input_list: list):
    return min(input_list) * max(input_list)

    # ❗ Note. min/max vs. sort()
    # 원래 먼저 생각한 해답은 아래와 같다. 실제로 논리적으로는 완벽히 동일하며, 수학적 원리에 부합한다
    # def solution(input_list: list):
    #     input_list.sort()
    #     return input_list[0] * input_list[-1]

    # 다만, 이 문제에 맞춰 코드를 최적화한다면
    # min/max 함수는 O(n), sort()는 O(n log n)이기 때문에 min/max가 더 빠를 수 밖에 없어서 
    # min/max의 사용으로 최적화가 가능하다

    # 추가로 min/max는 전체 값을 순회하며 값을 찾아내는 방식으로 O(n)
    # sort()는 파이썬의 경우에는 timsort를 사용하는데, 거의 정렬된 경우에는 O(n)이지만, 평균적으로 O(n log n)이다
    # timsort는 리스트를 왼쪽부터 스캔하면서 원래부터 정렬되어 있는 구간(run)을 감지하고, 이것들을 merge sort하는 방식이다


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    input_list = list(map(int, input().split()))

    print(solution(input_list))


# 📘 Learnings.
# 진짜 약수는 1과 자기자신을 제외한 수이며, 정렬했을 때 첫번째와 마지막번째의 곱이 N이 된다