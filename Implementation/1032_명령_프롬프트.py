"""
## [1032] 명령 프롬프트
🔗 https://www.acmicpc.net/problem/1032
"""

# 💡 Idea. 문자열을 세로로 비교하기

def solution(input_list: list):
    word_length = len(input_list[0])
    input_rest = input_list[1:]
    answer = []

    for i in range(word_length):
        char = input_list[0][i]
        if all(word[i] == char for word in input_rest):
            answer.append(char)
        else:
            answer.append('?')

    return ''.join(answer)

# ❗ Note. 불변 객체인 문자열
# 아래 코드는 처음 문제를 풀이하면서 작성해본 코드이다
# 전체적인 로직은 위와 동일하지만, answer = answer[:j]+'?'+answer[j+1:] 이라는 부분에서
# 불변 객체인 문자열을 수정하기 위해 새로운 문자열을 계속 만들어내고 있어 비효율적이다

# def solution(input_list: list, N: int):
#     word_length = len(input_list[0])
#     answer = input_list[0]
#   
#     for i in range(1, N):
#         for j in range(0, word_length):
#             if answer[j] != input_list[i][j]:
#                 answer = answer[:j]+'?'+answer[j+1:]
# 
#     return answer

# 추가로 새로운 코드 쪽이 이전 코드에 비해 보다 직관적이다
# 예를들어 all() 내부의 동작은 동일하지만, all이라는 함수 이름이 직관적인 이해를 도우며
# in 이하 input_rest 부분 역시 첫번째 문자열을 불필요하게 비교하지 않도록 하여 미세하지만 최적화했다

# ❗ Note. Zip의 활용
# 2차원 배열의 열 단위 순회에 가장 좋은 접근 방식은 zip이다
# 그렇기 때문에 같은 문제에 대해 아래와 같은 코드의 작성 역시 가능하다

# def solution(array):
#     return ''.join(
#         c[0] if all(x == c[0] for x in c) else '?' 
#         for c in zip(*array)
#     )

# 그렇지만 코드의 가독성 면에서 현재 남겨놓은 코드가 더 직관적이므로 위 코드를 사용한다



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    input_list = []
    for _ in range(N):
        temp = str(input())
        input_list.append(temp)

    print(solution(input_list))

# 📘 Learnings.
# 데이터 수가 많은 경우 TLE가 우려되어 고민을 해보게 되었다.
# 또한, 답을 맞추는 데서 더 나아가 코드의 가독성과 최적화, 유지보수에 대해 고민해봤다.