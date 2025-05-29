# 🧠 Python 알고리즘 최적화 & 코드 습관 패턴 모음

알고리즘 문제를 Python으로 풀 때 자주 마주치는 미세 최적화 팁과 코드 구조 패턴들을 정리합니다.  
시간/공간 효율뿐만 아니라, 가독성과 코드 스타일 측면에서도 큰 도움이 됩니다.

---

## ✅ 1. 슬라이싱은 반복하지 말고 변수에 저장

```python
# ❌ 매번 슬라이싱 (O(N))
for i in range(len(arr[1:])):
    ...

# ✅ 한 번만 슬라이싱
rest = arr[1:]
for i in range(len(rest)):
    ...
```

---

## ✅ 2. 문자열 누적은 리스트에 `append()` 후 `''.join()` 사용

```python
# ❌ 문자열 += 연산 반복 (비효율적)
result = ''
for c in chars:
    result += c

# ✅ 리스트에 누적 후 join
result = []
for c in chars:
    result.append(c)
result = ''.join(result)
```

---

## ✅ 3. `all()` / `any()`로 조건 판단 깔끔하게

```python
# ✅ 모두 같은지 확인
if all(x == nums[0] for x in nums[1:]):
    ...

# ✅ 하나라도 조건 만족하는지 확인
if any(c in special for c in password):
    ...
```

- `all()`과 `any()`는 **단락 평가**로 빠르게 종료됨
- 루프 + if문보다 짧고 명확

---

## ✅ 4. `range(len(...))` 대신 `enumerate(...)` 사용

```python
# ❌ 인덱스로 접근
for i in range(len(arr)):
    val = arr[i]

# ✅ 더 명확한 접근
for i, val in enumerate(arr):
    ...
```

---

## ✅ 5. 리스트 컴프리헨션은 간단할 때만

```python
# ✅ 적절한 컴프리헨션
squares = [x * x for x in range(10) if x % 2 == 0]

# ❌ 너무 복잡한 경우는 풀어서 쓰기
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x * x)
```

---

## ✅ 6. 빈 리스트/문자열/딕셔너리는 `if not`으로 판단

```python
# ❌ 길이로 확인
if len(arr) == 0:
    ...

# ✅ 더 Pythonic한 방법
if not arr:
    ...
```

---

## ✅ 7. 간단한 조건은 삼항 연산자로

```python
# ❌
if x > 0:
    sign = 1
else:
    sign = -1

# ✅
sign = 1 if x > 0 else -1
```

> 단, 조건이 복잡해지면 삼항 연산은 피하는 게 좋음

---

## ✅ 8. `set`을 이용한 빠른 탐색

```python
# ❌ 리스트에서 in → O(N)
if x in arr:
    ...

# ✅ 집합으로 변환 후 in → O(1)
s = set(arr)
if x in s:
    ...
```

---

## ✅ 9. `zip(*array)`로 세로 비교

```python
# 문자열 열 단위 비교
for col in zip(*strings):
    if all(c == col[0] for c in col):
        ...
```

---

## ✅ 10. 카운팅은 `collections.Counter`로 간단하게

```python
from collections import Counter

cnt = Counter(some_list)
cnt['a']  # → 'a'의 개수
```

---
