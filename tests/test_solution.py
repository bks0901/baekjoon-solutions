import os
import re
import importlib.util
import pytest

# 사용자 정의 경로
SOLUTION_FILE = "./src/implementation/brute_force/14500_테트로미노.py"
TESTCASE_FILE = "./tests/cases/14500_테트로미노_case.txt"

# solution 함수 불러오기
def load_solution(path):
    spec = importlib.util.spec_from_file_location("solution_module", path)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    return solution_module.solution


# 테스트 케이스 불러오기
def load_cases(filepath):
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    if '@@' in raw:
        # @@ 기준으로 구분 (label 포함)
        case_blocks = re.split(r'^@@.*$', raw, flags=re.MULTILINE)[1:]
        labels = re.findall(r'^@@.*$', raw, flags=re.MULTILINE)
    else:
        # 빈 줄 기준으로 구분 (label 없음)
        case_blocks = re.split(r'(?:\r?\n){2,}', raw)
        labels = [''] * len(case_blocks)

    cases = []

    for block, label in zip(case_blocks, labels):
        # 한 block에 여러 케이스가 들어있는 경우 나눔
        subcases = re.split(r'(?:\r?\n){2,}', block.strip())

        for sub in subcases:
            lines = sub.strip().splitlines()
            data = []
            expected = None

            for line in lines:
                line = line.strip()

                if not line or line.startswith('#') or line.startswith('//'):
                    continue
                if line.startswith('='):
                    expected = int(line.split('=')[1].strip())
                    continue

                data.append(list(map(int, line.split())))

            if expected is not None and data:
                n, m = data[0]
                tile = data[1:]
                cases.append((tile, n, m, expected, label.strip()))

    return cases

# solution 함수 및 테스트 파라미터 로딩
solution = load_solution(SOLUTION_FILE)
test_cases = load_cases(TESTCASE_FILE)
test_ids = [f"case_{i}" for i in range(len(test_cases))]

# 테스트 실행
@pytest.mark.parametrize("tile, n, m, expected, label", test_cases, ids=test_ids)
def test_solution(tile, n, m, expected, label):
    result = solution(tile, n, m)
    assert result == expected, f"\n❌ 틀린 케이스: {label}\nExpected {expected}, but got {result}"

# # ids로 테스트 이름 지정
# @pytest.mark.parametrize("tile, n, m, expected, label", test_cases, ids=[c[-1] for c in test_cases])
# def test_solution(tile, n, m, expected, label):
#     result = solution(tile, n, m)
#     assert result == expected, f"\n❌ 틀린 케이스: {label}\nExpected {expected}, but got {result}"
