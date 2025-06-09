import os
import re
import importlib.util
import pytest

# 사용자 정의 경로
SOLUTION_FILE = "./src/implementation/brute_force/6064_카잉_달력.py"
TESTCASE_FILE = "./tests/cases/6064_카잉_달력_case.txt"

# solution 함수 불러오기
def load_solution(path):
    spec = importlib.util.spec_from_file_location("solution_module", path)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    return solution_module.solution


# 테스트 케이스 불러오기
def load_cases(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        raw = f.read().strip()

    # @@ 블럭 분리
    labeled_blocks = re.split(r'^@@', raw, flags=re.MULTILINE)
    cases = []

    for block in labeled_blocks:
        block = block.strip()
        if not block:
            continue

        # 블럭 내 케이스 분리: \n\n 으로
        sub_blocks = re.split(r'(?:\r?\n){2,}', block)
        current_label = ""

        for sub_block in sub_blocks:
            lines = [line.strip() for line in sub_block.strip().splitlines() if line.strip()]
            if not lines:
                continue

            # 첫 줄이 라벨일 수 있음
            if not lines[0].startswith("=") and not re.match(r"^[\d\s]+$", lines[0]):
                current_label = lines.pop(0).strip()

            # 블럭 내에서 =이 있는 줄 찾기
            expected_line = next((line for line in lines if line.startswith("=")), None)
            if not expected_line:
                raise ValueError(f"No expected result (= ...) in block:\n{sub_block}")

            expected = int(expected_line[1:].strip())
            input_lines = [line for line in lines if not line.startswith("=")]

            if not input_lines:
                raise ValueError(f"No input data in block:\n{sub_block}")

            # 매트릭스 타입인지 확인 (첫 줄이 2개 숫자)
            try:
                first = list(map(int, input_lines[0].split()))
            except ValueError:
                raise ValueError(f"Invalid input line: {input_lines[0]}")

            if len(input_lines) > 1 and len(first) == 2:
                n, m = first
                tile = [list(map(int, line.split())) for line in input_lines[1:]]
                cases.append((tile, n, m, expected, current_label))
            else:
                # 단순 입력형: 한 줄 입력
                simple_input = list(map(int, input_lines[0].split()))
                cases.append((simple_input, expected, current_label))

    return cases

# def load_cases(filepath):
#     with open(filepath, encoding="utf-8") as f:
#         raw = f.read()

#     if '@@' in raw:
#         # @@ 기준으로 구분 (label 포함)
#         case_blocks = re.split(r'^@@.*$', raw, flags=re.MULTILINE)[1:]
#         labels = re.findall(r'^@@.*$', raw, flags=re.MULTILINE)
#     else:
#         # 빈 줄 기준으로 구분 (label 없음)
#         case_blocks = re.split(r'(?:\r?\n){2,}', raw)
#         labels = [''] * len(case_blocks)

#     cases = []

#     for block, label in zip(case_blocks, labels):
#         # 한 block에 여러 케이스가 들어있는 경우 나눔
#         subcases = re.split(r'(?:\r?\n){2,}', block.strip())

#         for sub in subcases:
#             lines = sub.strip().splitlines()
#             data = []
#             expected = None

#             for line in lines:
#                 line = line.strip()

#                 if not line or line.startswith('#') or line.startswith('//'):
#                     continue
#                 if line.startswith('='):
#                     expected = int(line.split('=')[1].strip())
#                     continue

#                 data.append(list(map(int, line.split())))

#             if expected is not None and data:
#                 n, m = data[0]
#                 tile = data[1:]
#                 cases.append((tile, n, m, expected, label.strip()))

#     return cases

# solution 함수 및 테스트 파라미터 로딩
solution = load_solution(SOLUTION_FILE)
test_cases = load_cases(TESTCASE_FILE)
test_ids = [f"case_{i}" for i in range(len(test_cases))]

# 테스트 실행
@pytest.mark.parametrize("case", test_cases, ids=test_ids)
def test_solution(case):
    if len(case) == 5:
        tile, n, m, expected, label = case
        result = solution(tile, n, m)
        assert result == expected, f"{label}: expected {expected}, got {result}"
    elif len(case) == 3:
        simple_input, expected, label = case
        result = solution([simple_input])
        # result = solution(*simple_input)  # simple_input이 리스트 형태라면 언팩
        assert int(result) == expected, f"{label}: expected {expected}, got {result}"
    else:
        raise ValueError(f"Unexpected test case format: {case}")

# @pytest.mark.parametrize("tile, n, m, expected, label", test_cases, ids=test_ids)
# def test_solution(tile, n, m, expected, label):
#     result = solution(tile, n, m)
#     assert result == expected, f"\n❌ 틀린 케이스: {label}\nExpected {expected}, but got {result}"
