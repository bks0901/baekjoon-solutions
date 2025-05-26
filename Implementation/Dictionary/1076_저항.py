"""
## [1076] 저항
🔗 https://www.acmicpc.net/problem/1076
"""

# 💡 Idea. 딕셔너리 → O(n)

def solution(first: str, second: str, thrid: str):
    
    resistance_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

    resistance = resistance_dict[first] * 10 + resistance_dict[second]
    return resistance * (10 ** resistance_dict[third])

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    first = str(input()).replace('\n','')
    second = str(input()).replace('\n','')
    third = str(input()).replace('\n','')

    print(solution(first, second, third))

# 📘 Learnings.
# 주어진 내용을 어떻게 매핑하고 안정적으로 동작하도록 구현할지 고민하자