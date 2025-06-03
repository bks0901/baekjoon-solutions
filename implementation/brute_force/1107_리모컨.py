"""
## [1107] 리모컨
🔗 https://www.acmicpc.net/problem/1107
"""

# 💡 Idea. 완전탐색 브루트 포스 vs. 그리디

def solution(n: int, m: int, broken_buttons: list):
    broken = set(broken_buttons)
    min_presses = abs(n - 100)  # 100에서 + 또는 -만 누르는 경우

    for num in range(1000000):
        num_str = str(num)
        if all(int(d) not in broken for d in num_str):
            presses = len(num_str) + abs(num - n)
            min_presses = min(min_presses, presses)

    return min_presses

# ❗ Note. 그리디(부분) 풀이

# 가장 먼저는 아래처럼 직접적으로 주어진 수와 가까운 수를 찾아서
# 해당 숫자와 가깝게 만들어서 접근하려고 생각했다
#     for number in split_number:
#         digit = int(number)
#         if digit in usable_numbers:
#             if digit != 0:
#                 brute_number += digit * pow(10, rate)      
#             elif digit == 0 and 0 in usable_numbers:
#                 brute_number += max(usable_numbers) * pow(10, rate)  
#         else:
#             if digit != 0:
#                 temp = 10
#                 cache = 0
#                 for i in usable_numbers:
#                     if 0 < digit - i and digit - i < temp:
#                         temp = digit - i
#                         cache = i
#                 brute_number += cache * pow(10, rate)
#             elif digit == 0 and 0 not in usable_numbers:
#                 brute_number += min(usable_numbers) * pow(10, rate)
                
#         count += 1
#         rate -= 1

# 그러나 이 접근 자체의 근본적인 한계는 가장 비슷한 수를 만들면 최적해를 구하리란 가정에 기댔다는 점이다
# 즉 그냥 +-로 올라가는게 빠르다던가, 다른 조합의 가능성을 고려하지 않았다
# 결국 시간을 한참 들여놓고 완전탐색 브루트포스로 풀아하게 됐다

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    broken = list(map(int, input().split()))

    print(solution(n, m, broken))

# 📘 Learnings.
# 전체를 찾기보다 그리디로 풀이하려고 시도했는데, 결과적으로 경우의 수를 놓치게 됐다
# (예를 들어, 높은 쪽에서 오거나 단순하게 +-로 계산하는 경우 등)
# 그만큼 확실하게 상황을 판단하거나, 경우에 따라서는 브루트 포스로 푸는 접근이 낫다