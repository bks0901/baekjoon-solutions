# baekjoon-solutions

<br />

백준 문제 풀이 정리 레포입니다.  
**시작일**: 2025.05 ~

- 문제 풀이 후 리뷰/실수/개선 포인트를 간단히 기록합니다.

<br />

## 프로젝트 세팅

- 이 프로젝트는 Poetry로 관리됩니다. 초기 세팅 시 다음을 따라주세요:

```bash
# (처음이라면) Poetry 설치
curl -sSL https://install.python-poetry.org | python3 -

# poetry 설치 경로가 PATH에 없다면 ~/.zshrc 등에 아래 추가
export PATH="$HOME/.local/bin:$PATH"
source ~/.zshrc

# 이 프로젝트는 별도의 패키징이 필요 없기 때문에 pyproject.toml에 다음 코드 추가
[tool.poetry.package-mode]
package-mode = false

# 가상환경 및 의존성 설치
poetry install

# 테스트를 위한 pytest 개발용 설치
poetry add --group dev pytest

# .vscode/settings.json를 만들고 vs code 세팅 추가
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.venvPath": ".",
  "python.analysis.autoSearchPaths": true,
  "python.analysis.extraPaths": ["."],
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["."],
  "python.testing.unittestEnabled": false
}

# extension 중 even better toml 설치

# 가상환경 경로 확인
poetry env info --path
```

<br />

## 테스트 수행

- pytest는 기본적으로 테스트 파일 이름이 test\_.py 또는 \*\_test.py 형식일 때만 자동으로 인식

```bash
# 테스트 수행
poetry run pytest

# 내용을 자세히 보고 싶다면
poetry run pytest -v
```

<br />

## 📚 알고리즘 정리 자료

- [Python 알고리즘 최적화 패턴](./docs/python_patterns.md)
- [알고리즘 풀이 접근 순서](./docs/algorithm_approach_structure.md)
- [알고리즘 주요 주제](./docs//algorithm_core_topics.md)
- 알고리즘 주요 주제별 생각노트
  1. [복잡도](./docs/topics/1.%20complexity.md)
  2. [수학과 구현](./docs//topics/2.%20mathmatics_and_implementation.md)

## 🔁 다시 풀어볼 문제

| 번호 | 문제명     | 유형       | 첫 풀이    | 1차 복습 | 2차 복습 | 링크                                                      |
| ---- | ---------- | ---------- | ---------- | -------- | -------- | --------------------------------------------------------- |
| 1    | 테트로미노 | 브루트포스 | 2025-06-08 |          |          | [14500 테트로미노](https://www.acmicpc.net/problem/14500) |
