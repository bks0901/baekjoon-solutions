"""
## [17425] 약수의 합
🔗 https://www.acmicpc.net/problem/17425
"""

# 💡 Idea. 고전적 최적화 → 약수 기준이 아닌 배수 기준! 그리고 캐싱

def solution(input_list: list):

    largest_x = max(input_list)
    f_x = [0] * (largest_x + 1)
    g_x = [0] * (largest_x + 1)

    for i in range(1, largest_x+1):
        for j in range(i, largest_x+1, i):
            f_x[j] += i

    for i in range(1, largest_x+1):
        g_x[i] =g_x[i-1]+f_x[i]


    answer = [str(g_x[n]) for n in input_list]

    return '\n'.join(answer)
    
    # ❗ Note. 캐싱
    # 처음에는 아래와 같이 약수의 합을 구하는 고전적 최적화 방법을 직접 적용했다
    # for number in input_list:
    #     sum = 0
    #     for i in range(1, number+1):
    #         sum += (number // i) * i
    #     answer.append(str(sum))

    # 물론 이렇게 푸는 방법 자체에 문제는 없다
    # 그렇지만 연산한 내용을 재사용하지 않고 안쪽 for문에서 늘 다시 계산한다
    # 시간이 촉박하며, 연산한 내용을 재사용할 수 있게 로직을 수정해서 적용하면
    # 더욱 효율적인 코드가 된다

    # ❗ Note. pypy3 vs. python3(cpython)
    # pypy3는 python3와 같은 코드와 문법이지만, 실행방식을 다르게 최적화한 환경이다
    # pypy3는 JIT compiler를 이용해 실행하고, python3는 인터프리터를 이용해 한줄씩 코드를 적용한다
    # pypy3는 python3 대비 5~10배 정도 빠른 속도를 자랑하지만,
    # 안정성이 낮고, 라이브러리 지원이 제대로 되지 않아 일부 상황에서만 사용한다
    # 또한 JIT 방식의 특징으로 많은 메모리를 사용해, 메모리 제한이 작으면 사용하기 어렵다
    # 만약 알고리즘을 제대로 작성했지만 시간 문제로 통과가 어려운 경우에는
    # pypy3를 사용할 것을 권장한다(백준 공식 FAQ에서도 인정되는 방식)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    input_list = []
    for _ in range(N):
        temp = int(input())
        input_list.append(temp)

    print(solution(input_list))


# 📘 Learnings.
# 약수의 합 2를 리스트 형태로 더 많은 연산을 해보도록 한 문제
# 로직을 모른겠다면 17425_약수의_합_2.py 참고
# 로직과 별개로, 속도를 위해 캐싱이 필요하다
# 이 문제의 경우 python3(CPython)으로 실행시키면 약 4.8초,
# pypy3로 실행시키면 약 0.9초가 걸린다
# 메모리가 좀 더 넉넉하다면 이런 문제는 실행시간 초과 방지를 위해 반드시 pypy3로 제출