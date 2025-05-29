"""
## [1075] 나누기
🔗 https://www.acmicpc.net/problem/1075
"""

# 💡 Idea. 몫 기반 정규화

def solution(n: int, f: int):
    
    base = (n // 100) * 100  # 뒤 두 자리 00으로

    # ❗ Note. 받아오는 input을 문자열로 다뤄서 해결하면 안될까?
    # base = int(str(n)[:-2] + '00')와 같이 문자열 슬라이싱을 해도 되지 않을까 생각했는데
    # 사실 이 문제는 n >= 100 조건이 있어서 답을 맞추는데 문제가 없겠지만
    # 숫자가 100 미만인 범위에서는 99를 0으로 만들어 버리는 오류가 있고
    # 성능도 현재의 방식만 못하다

    for i in range(100):
        candidate = base + i
        if candidate % f == 0:
            return f"{i:02d}"

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    F = int(input())

    print(solution(N,F))



# 📘 Learnings.
# base = (n // 100) * 100처럼 10진수 체계에서 '자릿수 분리'를 훈련하는 과정이 필요하다
# 상위 바이트를 위지하고, 하위 바이트만 마스킹하는 방식으로 사고한다