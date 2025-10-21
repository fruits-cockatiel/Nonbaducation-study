# 실습
## 시각화 맛보기 (matplotlib & plotly 기초)

- 지금까지 숫자와 텍스트로만 결과를 확인했다면, 이제는 **그래프**로 데이터를 시각화해봅시다!
- **matplotlib**는 파이썬에서 가장 기본적인 그래프 라이브러리입니다.
- **plotly**는 인터랙티브(상호작용) 그래프를 만들 수 있는 현대적인 라이브러리입니다.
- 데이터를 그래프로 그리면 숫자만 봤을 때보다 **패턴과 경향**을 쉽게 파악할 수 있습니다.

### matplotlib vs plotly 비교

#### matplotlib 특징
- ✅ 기본적이고 안정적
- ✅ 정적 그래프 (이미지)
- ✅ 커스터마이징이 세밀하게 가능
- ❌ 상호작용 기능 제한적

#### plotly 특징
- ✅ 현대적이고 예쁨
- ✅ 인터랙티브 그래프 (확대, 호버 등)
- ✅ 웹에서 그대로 사용 가능
- ✅ 애니메이션 지원
- ❌ 조금 더 복잡할 수 있음

### matplotlib 시작하기

#### 한글 폰트 설정
```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
```

이후 꼭 런타임 > 세션 다시 시작을 한 뒤 아래 코드를 실행해주세요!

```python
import matplotlib.pyplot as plt

# 구글 코랩에서 한글 깨짐 방지
plt.rcParams['font.family'] = ['NanumBarunGothic']
plt.rcParams['axes.unicode_minus'] = False

print("matplotlib 준비 완료!")
```

#### 기본 그래프 그리기
```python
import matplotlib.pyplot as plt

# 간단한 데이터
days = ['월', '화', '수', '목', '금']
scores = [65, 70, 75, 80, 85]

# 선 그래프
plt.figure(figsize=(10, 6))
plt.plot(days, scores, marker='o', linewidth=2, markersize=8)
plt.title("일주일간 점수 변화 (matplotlib)", fontsize=16, pad=20)
plt.xlabel("요일")
plt.ylabel("점수")
plt.grid(True, alpha=0.3)
plt.show()
```

#### 막대 그래프
```python
import matplotlib.pyplot as plt

# 과목별 점수 데이터
subjects = ['수학', '영어', '과학', '국어']
scores = [85, 92, 78, 88]

plt.figure(figsize=(10, 6))
bars = plt.bar(subjects, scores, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.title("과목별 점수 (matplotlib)", fontsize=16, pad=20)
plt.xlabel("과목")
plt.ylabel("점수")
plt.ylim(0, 100)

# 막대 위에 점수 표시
for bar, score in zip(bars, scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(score), ha='center', fontweight='bold')

plt.show()
```

### matplotlib 기본 함수들 자세히 알아보기
#### 1. `plt.figure()` - 그래프 크기 설정
```python
import matplotlib.pyplot as plt

# 기본 크기 (작음)
plt.plot([1, 2, 3], [1, 4, 2])
plt.title("기본 크기")
plt.show()

# 큰 크기로 설정
plt.figure(figsize=(12, 8))  # 가로 12인치, 세로 8인치
plt.plot([1, 2, 3], [1, 4, 2])
plt.title("큰 크기")
plt.show()

# 정사각형으로 설정
plt.figure(figsize=(8, 8))
plt.plot([1, 2, 3], [1, 4, 2])
plt.title("정사각형")
plt.show()
```

#### 2. `plt.subplot()` - 여러 그래프를 한 번에 보기
```python
import matplotlib.pyplot as plt

# 샘플 데이터
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 2, 3, 5]
y2 = [2, 3, 1, 4, 2]
y3 = [3, 1, 4, 2, 3]
y4 = [5, 2, 3, 1, 4]

# 2x2 격자로 4개 그래프 배치
plt.figure(figsize=(12, 10))

# 첫 번째 그래프 (2행 2열 중 1번째 위치)
plt.subplot(2, 2, 1)  # (행, 열, 위치)
plt.plot(x, y1, 'ro-')
plt.title("첫 번째 그래프")
plt.grid(True)

# 두 번째 그래프 (2행 2열 중 2번째 위치)
plt.subplot(2, 2, 2)
plt.bar(x, y2, color='blue')
plt.title("두 번째 그래프")

# 세 번째 그래프 (2행 2열 중 3번째 위치)
plt.subplot(2, 2, 3)
plt.plot(x, y3, 'gs--')
plt.title("세 번째 그래프")
plt.xlabel("X축")

# 네 번째 그래프 (2행 2열 중 4번째 위치)
plt.subplot(2, 2, 4)
plt.scatter(x, y4, color='orange', s=100)
plt.title("네 번째 그래프")
plt.xlabel("X축")

plt.show()  # 이때 그래프들이 겹쳐서 보기 어려울 수 있음
```

#### 3. `plt.tight_layout()` - 그래프 간격 자동 조정
```python
import matplotlib.pyplot as plt

# 같은 데이터로 tight_layout 없이
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(x, y1, 'ro-')
plt.title("이 제목이 길어서 다른 그래프와 겹칠 수 있습니다")

plt.subplot(2, 2, 2)
plt.bar(x, y2, color='blue')
plt.title("이것도 긴 제목입니다")

plt.subplot(2, 2, 3)
plt.plot(x, y3, 'gs--')
plt.title("세 번째 그래프")
plt.xlabel("이것은 긴 X축 라벨입니다")

plt.subplot(2, 2, 4)
plt.scatter(x, y4, color='orange', s=100)
plt.title("네 번째 그래프")
plt.xlabel("X축")
plt.ylabel("이것은 긴 Y축 라벨입니다")

# tight_layout() 추가 - 간격을 자동으로 조정!
plt.tight_layout()
plt.show()
```

#### 4. 다양한 subplot 배치 방법
```python
import matplotlib.pyplot as plt

# 1행 3열로 배치
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)  # 1행 3열 중 1번째
plt.plot([1, 2, 3], [1, 4, 2], 'bo-')
plt.title("선 그래프")

plt.subplot(1, 3, 2)  # 1행 3열 중 2번째
plt.bar(['A', 'B', 'C'], [3, 7, 2])
plt.title("막대 그래프")

plt.subplot(1, 3, 3)  # 1행 3열 중 3번째
plt.pie([30, 40, 30], labels=['X', 'Y', 'Z'])
plt.title("원 그래프")

plt.tight_layout()
plt.show()
```

### plotly 시작하기
#### plotly 설치 및 기본 설정
```python
import plotly.io as pio

pio.renderers.default = "colab"

print("plotly 준비 완료!")
```

#### 같은 데이터를 plotly로 그리기
```python
import plotly.graph_objects as go

# 선 그래프 (인터랙티브)
days = ['월', '화', '수', '목', '금']
scores = [65, 70, 75, 80, 85]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=days,
    y=scores,
    mode='lines+markers',
    name='점수 변화',
    line=dict(width=3),
    marker=dict(size=10, color='blue')
))

fig.update_layout(
    title="일주일간 점수 변화 (plotly)",
    title_font_size=16,
    xaxis_title="요일",
    yaxis_title="점수",
    width=800,
    height=500
)

fig.show()
```

#### plotly 막대 그래프
```python
import plotly.graph_objects as go

subjects = ['수학', '영어', '과학', '국어']
scores = [85, 92, 78, 88]

fig = go.Figure(data=[
    go.Bar(
        x=subjects,
        y=scores,
        marker_color=['skyblue', 'lightcoral', 'lightgreen', 'gold'],
        text=scores,  # 막대 위에 숫자 표시
        textposition='outside'
    )
])

fig.update_layout(
    title="과목별 점수 (plotly)",
    title_font_size=16,
    xaxis_title="과목",
    yaxis_title="점수",
    yaxis_range=[0, 100],
    width=800,
    height=500
)

fig.show()
```

### plotly 기본 함수들 자세히 알아보기
#### matplotlib vs plotly 레이아웃 방식 비교
**matplotlib 방식:**
```python
import matplotlib.pyplot as plt

# matplotlib: subplot() 함수 사용
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)  # 2행 2열의 1번째
plt.plot([1, 2, 3], [1, 4, 2])
plt.title("첫 번째 그래프")

plt.subplot(2, 2, 2)  # 2행 2열의 2번째
plt.bar(['A', 'B', 'C'], [3, 7, 2])
plt.title("두 번째 그래프")

plt.tight_layout()  # 간격 자동 조정
plt.show()
```

**plotly 방식:**
```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# plotly: make_subplots() 함수 사용
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=["첫 번째 그래프", "두 번째 그래프", "세 번째", "네 번째"]
)

# add_trace()로 각 위치에 그래프 추가
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 2]), row=1, col=1)
fig.add_trace(go.Bar(x=['A', 'B', 'C'], y=[3, 7, 2]), row=1, col=2)

# 레이아웃은 자동으로 조정됨!
fig.show()
```

#### 1. plotly의 `make_subplots()` - matplotlib의 subplot()에 해당
```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 2x2 서브플롯 생성
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=["그래프 1", "그래프 2", "그래프 3", "그래프 4"],
    specs=[[{"type": "scatter"}, {"type": "bar"}], [{"type": "scatter"}, {"type": "pie"}]]
)

# 각 위치에 그래프 추가
fig.add_trace(
    go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], name="선 그래프"),
    row=1, col=1
)

fig.add_trace(
    go.Bar(x=['A', 'B', 'C'], y=[1, 3, 2], name="막대 그래프"),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(x=[1, 2, 3, 4], y=[2, 4, 3, 5], mode='markers', name="산점도"),
    row=2, col=1
)

fig.add_trace(
    go.Pie(labels=['X', 'Y', 'Z'], values=[30, 40, 30], name="원 그래프"),
    row=2, col=2
)

fig.update_layout(
    title_text="plotly 서브플롯 예제",
    width=1000,
    height=800
)

fig.show()
```

#### 2. plotly는 `tight_layout()` 없이도 자동 조정!

### 실전 비교: 같은 대시보드를 두 방식으로
**matplotlib 버전:**
```python
import matplotlib.pyplot as plt

# matplotlib으로 학습 대시보드
plt.figure(figsize=(15, 10))

# 1. 일별 점수
plt.subplot(2, 3, 1)
days = ['월', '화', '수', '목', '금']
scores = [75, 80, 85, 90, 88]
plt.plot(days, scores, 'bo-', linewidth=2)
plt.title("일별 점수 변화")
plt.grid(True, alpha=0.3)

# 2. 과목별 평균
plt.subplot(2, 3, 2)
subjects = ['수학', '영어', '과학']
averages = [85, 92, 78]
bars = plt.bar(subjects, averages, color=['gold', 'lightgreen', 'orange'])
plt.title("과목별 평균")
for bar, avg in zip(bars, averages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(avg), ha='center', fontweight='bold')

# 3. 시간 분배
plt.subplot(2, 3, 3)
activities = ['공부', '수면', '여가', '식사']
hours = [8, 8, 6, 2]
plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("하루 시간 분배")

# 4-6. 더 많은 그래프들...
plt.subplot(2, 3, 4)
# ... 계속

plt.tight_layout()  # 필수!
plt.show()
```

**plotly 버전:**
```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 같은 데이터를 plotly로
fig = make_subplots(
    rows=2, cols=3,
    specs=[
        [{"type": "scatter"}, {"type": "bar"}, {"type": "pie"}],
        [{"colspan": 2}, None, {"type": "scatter"}]
    ],
    subplot_titles=[
        "일별 점수 변화", "과목별 평균", "시간 분배",
        "주간 학습 패턴", "", "성과 분석"
    ]
)

# 1. 일별 점수 (인터랙티브!)
fig.add_trace(
    go.Scatter(
        x=days, y=scores,
        mode='lines+markers',
        hovertemplate='%{x}: %{y}점<extra></extra>'
    ),
    row=1, col=1
)

# 2. 과목별 평균 (호버 정보!)
fig.add_trace(
    go.Bar(
        x=subjects, y=averages,
        text=averages,
        textposition='outside',
        hovertemplate='%{x}: %{y}점<extra></extra>'
    ),
    row=1, col=2
)

# 3. 시간 분배 (인터랙티브 원그래프!)
fig.add_trace(
    go.Pie(
        labels=activities,
        values=hours,
        hovertemplate='%{label}: %{value}시간 (%{percent})<extra></extra>'
    ),
    row=1, col=3
)

fig.update_layout(
    title_text="학습 대시보드 - plotly 버전 (클릭하고 호버해보세요!)",
    width=1200,
    height=700
)
# tight_layout() 필요없음! 자동 조정!

fig.show()
```

### 언제 어떤 라이브러리를 사용할까?

#### matplotlib를 사용하는 경우
- **보고서용 그래프**: 인쇄물이나 PDF에 포함할 정적 그래프
- **세밀한 커스터마이징**: 디자인을 정확히 조절해야 할 때
- **통계 분석**: 학술적이거나 전문적인 분석 결과
- **파일 저장**: PNG, PDF 등으로 저장이 주목적일 때

#### plotly를 사용하는 경우
- **웹 대시보드**: 웹페이지에서 보여줄 때
- **사용자 상호작용**: 확대, 필터링 등이 필요할 때
- **프레젠테이션**: 발표나 시연할 때
- **애니메이션**: 시간에 따른 변화를 보여줄 때
