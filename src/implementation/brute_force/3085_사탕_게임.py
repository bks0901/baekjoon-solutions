"""
## [3085] 사탕 게임
🔗 https://www.acmicpc.net/problem/3085
"""

# 💡 Idea. 2차원 배열의 순회

def search_candy(board: list):
    n = len(board)
    max_length = 1

    # 행 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_length = max(max_length, count)

    # 열 검사
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_length = max(max_length, count)
    
    return max_length
            

def solution(total_row: int, input_list: list):

    answer = 0

    # 가로를 변경하면 세로를 체크하고, 세로를 변경하면 가로를 체크해야 한다
    # 그리고 오른쪽과 아래쪽으로 가면서 바꾸면 바꾸는건 모두 바뀌고,
    # 실제 내용물을 세는건 전체를 다 세봐야 한다


    for i in range(0, total_row):
        for j in range(0, total_row):

            # 오른쪽
            if j + 1 < total_row:
                # 바꾸기
                input_list[i][j], input_list[i][j+1] = input_list[i][j+1], input_list[i][j]
                answer = max(answer, search_candy(input_list))
                # 되돌려놓기
                input_list[i][j+1], input_list[i][j] = input_list[i][j], input_list[i][j+1]
            
            # 아래쪽
            if i + 1 < total_row:
                # 바꾸기
                input_list[i][j], input_list[i+1][j] = input_list[i+1][j], input_list[i][j]
                answer = max(answer, search_candy(input_list))
                # 되돌려놓기
                input_list[i+1][j], input_list[i][j] = input_list[i][j], input_list[i+1][j]

    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())
    input_list = []
    for _ in range(T):
        layer = list(input().strip())
        # input_list = input_list + layer
        input_list.append(layer)
    
    print(solution(T, input_list))

# 📘 Learnings.
# 순회구조를 작성하는 데 꼼꼼함이 필요하다. 그리고 바꾸고 나면 바꾼 전체를 검색해야지 부분만 들여다보면 틀리게 된다.
# 꼼꼼하지 못한 브루트포스 풀이는 시간만 잡아먹게 되므로 선명하게 풀이를 머릿속으로 정리하자.