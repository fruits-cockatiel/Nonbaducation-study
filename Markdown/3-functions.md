# 실습
## 함수와 import 문
- 함수는 특정한 기능을 수행하는 코드의 묶음이다.
- import 문은 다른 사람이 만든 유용한 기능들을 가져다 쓰는 방법이다.
- 함수와 import를 활용하면 코드 중복을 줄이고 재사용성을 높일 수 있다.

### 함수 (Function)
#### 왜 함수가 필요한가?
- 같은 코드를 여러 번 작성하는 것은 비효율적이다.
- 코드를 수정할 때 여러 곳을 바꿔야 하는 문제가 생긴다.

```python
# 함수 없이 코드 작성할 때의 문제점
print("김철수님 안녕하세요!")
print("오늘 날씨가 좋네요.")
print("좋은 하루 되세요!")

print("박영희님 안녕하세요!")
print("오늘 날씨가 좋네요.")
print("좋은 하루 되세요!")

print("이민수님 안녕하세요!")
print("오늘 날씨가 좋네요.")
print("좋은 하루 되세요!")
```

```python
# 함수를 사용하여 개선
def greet(name):
    print(f"{name}님 안녕하세요!")
    print("오늘 날씨가 좋네요.")
    print("좋은 하루 되세요!")

greet("김철수")
greet("박영희")
greet("이민수")
```

#### 기본 함수 정의와 호출
- 함수는 `def` 키워드로 정의한다.
- 함수명 뒤에 괄호 `()`를 붙이고, 콜론 `:`을 붙인다.
- 함수 내부 코드는 들여쓰기를 해야 한다.
- 함수를 사용하려면 함수명과 괄호를 써서 "호출"한다.

```python
def say_hello():
    print("안녕하세요!")
    print("함수를 배우고 있어요!")

# 함수 호출
say_hello()
```

#### 매개변수 (Parameter)
- 함수에 값을 전달할 수 있다.
- 함수 정의할 때 괄호 안에 적는 변수를 **매개변수**라고 한다.
- 함수를 호출할 때 전달하는 실제 값을 **인수(argument)**라고 한다.

```python
def introduce(name, age):  # name 과 age 가 매개변수
    print(f"제 이름은 {name}이고, {age}살입니다.")

introduce("홍길동", 25)  # "홍길동"과 25가 인수
introduce("김영희", 30)
```

#### 매개변수의 기본값
- 매개변수에 기본값을 설정할 수 있다.
- 기본값이 있는 매개변수는 함수 호출 시 생략할 수 있다.

```python
def order_coffee(size="medium", sugar=True):
    sugar_text = "설탕 있음" if sugar else "설탕 없음"
    print(f"{size} 사이즈 커피, {sugar_text}")

order_coffee()  # 기본값 사용
order_coffee("large")  # size만 변경
order_coffee("small", False)  # 둘 다 변경
order_coffee(sugar=False)  # 매개변수 이름으로 지정
```

#### 반환값 (return)
- 함수는 결과값을 돌려줄 수 있다.
- `return` 키워드를 사용한다.
- return 문을 만나면 함수가 종료된다.

```python
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    return a - b  # 계산 결과를 바로 반환

# 함수의 반환값을 변수에 저장
sum_result = add(10, 5)
diff_result = subtract(10, 5)

print(f"더하기 결과: {sum_result}")
print(f"빼기 결과: {diff_result}")
```

- 리턴값 없이 `return`만 써도 함수가 종료된다.

```python
def print_greeting(name):
    if not name:  # 이름이 빈 문자열이거나 None이면
        print("이름을 입력해주세요.")
        return  # 여기서 함수 종료 (리턴값 없음)
    
    # 위 조건을 통과했을 때만 실행됨
    print(f"{name}님, 안녕하세요!")
    print("좋은 하루 되세요!")

# 함수 테스트
print_greeting("")        # "이름을 입력해주세요." 출력 후 종료
print_greeting("홍길동")   # 인사말 모두 출력
```

#### 여러 값 반환하기
- 함수는 여러 개의 값을 동시에 반환할 수 있다.
- 콤마로 구분하여 반환하면 튜플 형태로 돌려준다.

```python
def get_name_and_age():
    name = input("이름을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    return name, age

def calculate_tip(bill, tip_rate=0.15):
    tip = bill * tip_rate
    total = bill + tip
    return tip, total

# 여러 값을 각각의 변수에 저장
user_name, user_age = get_name_and_age()
tip_amount, total_bill = calculate_tip(50000, 0.1)

print(f"사용자: {user_name}, 나이: {user_age}")
print(f"팁: {tip_amount}원, 총액: {total_bill}원")
```

#### 가변 인수 (*args, **kwargs)
- 함수에 전달되는 인수의 개수가 정해지지 않을 때 사용한다.
- `*args`: 여러 개의 일반 인수를 튜플로 받는다.
- `**kwargs`: 여러 개의 키워드 인수를 딕셔너리로 받는다.

```python
def print_numbers(*args):
    """여러 개의 숫자를 받아서 출력하는 함수"""
    print("받은 숫자들:", args)
    for num in args:
        print(f"숫자: {num}")

print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40, 50)
```

```python
def introduce_person(**kwargs):
    """키워드 인수로 사람 정보를 받아서 출력하는 함수"""
    print("사람 정보:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce_person(이름="홍길동", 나이=25, 직업="개발자")
introduce_person(이름="김영희", 나이=30, 도시="서울", 취미="독서")
```

```python
def flexible_function(*args, **kwargs):
    """일반 인수와 키워드 인수를 모두 받는 함수"""
    print("일반 인수들:", args)
    print("키워드 인수들:", kwargs)

flexible_function(1, 2, 3, name="철수", age=20)
```

#### 함수 설명 문서 (Docstring)
- 함수가 무엇을 하는지 설명하는 문서이다.
- 함수 정의 바로 아래 삼중 따옴표로 작성한다.
- 다른 사람이 함수를 사용할 때 도움이 된다.

```python
def calculate_bmi(weight, height):
    """
    BMI(체질량지수)를 계산하는 함수
    
    Args:
        weight (float): 체중 (kg)
        height (float): 키 (m)
    
    Returns:
        float: BMI 수치
    """
    return weight / (height ** 2)

def greet_customer(name, vip=False):
    """
    고객에게 인사하는 함수
    
    Args:
        name (str): 고객 이름
        vip (bool): VIP 고객 여부 (기본값: False)
    
    Returns:
        str: 인사 메시지
    """
    if vip:
        return f"{name} VIP 고객님, 환영합니다!"
    else:
        return f"{name}님, 안녕하세요!"

# 함수 사용 예시
my_bmi = calculate_bmi(70, 1.75)
print(f"BMI: {my_bmi:.1f}")
print(calculate_bmi.__doc__)

message = greet_customer("홍길동", True)
print(message)
print(greet_customer.__doc__)
```

#### 실생활 예시 - 음식점 주문 시스템
```python
def calculate_order_total(item, quantity, is_member=False):
    """주문 총액을 계산하는 함수"""
    menu_prices = {
        "라면": 5000,
        "김밥": 3500,
        "떡볶이": 4000,
        "순대": 4000
    }
    
    if item not in menu_prices:
        return 0, f"{item}는 메뉴에 없습니다."
    
    subtotal = menu_prices[item] * quantity
    
    # 회원이면 10% 할인
    if is_member:
        discount = subtotal * 0.1
        total = subtotal - discount
        return total, f"{item} {quantity}개 주문 (회원 할인 적용: -{discount}원)"
    else:
        return subtotal, f"{item} {quantity}개 주문"

# 함수 사용 예시
total, message = calculate_order_total("라면", 2, True)
print(f"{message}, 총액: {total}원")
```

#### 실생활 예시 - 은행 계좌 관리
```python
def process_transaction(current_balance, transaction_type, amount):
    """은행 거래를 처리하는 함수"""
    if transaction_type == "입금":
        new_balance = current_balance + amount
        return new_balance, f"{amount}원이 입금되었습니다."
    elif transaction_type == "출금":
        if current_balance >= amount:
            new_balance = current_balance - amount
            return new_balance, f"{amount}원이 출금되었습니다."
        else:
            return current_balance, "잔액이 부족합니다."
    else:
        return current_balance, "잘못된 거래 유형입니다."

# 함수 사용 예시
balance = 100000
balance, message = process_transaction(balance, "출금", 30000)
print(f"{message} 현재 잔액: {balance}원")
```

### 변수의 범위 (Scope)
#### 지역 변수와 전역 변수
- **지역 변수**: 함수 내부에서만 사용할 수 있는 변수
- **전역 변수**: 프로그램 전체에서 사용할 수 있는 변수

```python
# 전역 변수
bank_balance = 100000

def check_balance():
    # 지역 변수
    balance_message = "잔액 조회"
    print(f"{message}: {bank_balance}원")

def withdraw_money(amount):
    global bank_balance  # 전역 변수를 수정하려면 global 키워드 필요
    if bank_balance >= amount:
        bank_balance -= amount
        return f"{amount}원이 출금되었습니다. 잔액: {bank_balance}원"
    else:
        return "잔액이 부족합니다."

check_balance()
print(withdraw_money(20000))
```

- 여기서 만약 check_balance 안의 balance_message 변수를 접근하려고 하면 에러가 남
```python
print(balance_message)
```

#### global 키워드 주의사항
- global을 남용하면 코드가 복잡해진다.
- 가능하면 함수의 매개변수와 반환값을 활용하는 것이 좋다.

```python
# 권장하지 않는 방식 (global 남용)
score = 0

def bad_add_score(points):
    global score
    score += points

# 권장하는 방식 (매개변수와 반환값 활용)
def good_add_score(current_score, points):
    return current_score + points

# 사용 예시
score = 0
score = good_add_score(score, 100)
```

### 람다 함수 (Lambda Function)
- 간단한 함수를 한 줄로 만들 수 있다.
- `lambda 매개변수: 표현식` 형태로 사용한다.
- 주로 간단한 계산이나 정렬에 사용된다.

```python
# 일반 함수
def square(x):
    return x ** 2

# 람다 함수
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

# 리스트와 함께 사용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# 정렬에 활용
students = [("홍길동", 85), ("김영희", 92), ("이철수", 78)]
students.sort(key=lambda student: student[1])  # 점수 기준으로 정렬
print(students)
```

### import 문
#### 모듈이란?
- 모듈은 함수들을 파일로 정리해둔 것이다.
- 파이썬에는 유용한 기능들이 미리 만들어져 있다.
- 다른 사람이 만든 모듈도 가져다 쓸 수 있다.

#### 기본 import 방법들
```python
# 1. 전체 모듈 가져오기
import math
print(f"원주율: {math.pi}")
print(f"16의 제곱근: {math.sqrt(16)}")

# 2. 특정 함수만 가져오기
from math import pi, sqrt, ceil
print(f"원주율: {pi}")
print(f"16의 제곱근: {sqrt(16)}")
print(f"3.2를 올림: {ceil(3.2)}")

# 3. 별칭(alias) 사용하기
import random as rd
dice = rd.randint(1, 6)
print(f"주사위 결과: {dice}")

# 4. 모든 함수 가져오기 (권장하지 않음)
# from math import *  # 이렇게 쓰면 어떤 함수가 어디서 온 건지 헷갈릴 수 있음
```

#### 자주 사용하는 내장 모듈들
##### random 모듈 (이미 2장에서 사용해봤음)
```python
import random

# 정수 범위에서 무작위 선택
dice = random.randint(1, 6)
print(f"주사위: {dice}")

# 리스트에서 무작위 선택
choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)
print(f"컴퓨터의 선택: {computer_choice}")

# 리스트 섞기
cards = ['♠A', '♠K', '♠Q', '♠J']
random.shuffle(cards)
print(f"섞인 카드: {cards}")

# 범위에서 중복 없이 여러 개 선택
lottery_numbers = random.sample(range(1, 46), 6)
print(f"로또 번호: {lottery_numbers}")
```

##### datetime 모듈 - 날짜와 시간
```python
import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()
print(f"현재 시간: {now}")
print(f"현재 연도: {now.year}")
print(f"현재 월: {now.month}")
print(f"현재 일: {now.day}")

# 특정 날짜 만들기
my_birthday = datetime.date(1995, 5, 15)
print(f"내 생일: {my_birthday}")

# 날짜 계산
today = datetime.date.today()
days_since_birthday = today - my_birthday
print(f"태어난 지 {days_since_birthday.days}일이 지났습니다.")
```

##### os 모듈 - 운영체제와 상호작용
```python
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print(f"현재 디렉토리: {current_dir}")

# 파일 목록 확인
files = os.listdir('.')
print(f"현재 디렉토리의 파일들: {files}")

# 환경 변수 확인 (사용자 이름 등)
username = os.getenv('USER') or os.getenv('USERNAME')
print(f"사용자 이름: {username}")
```

## 종합 실습 프로젝트
### 프로젝트 1: 계산기 프로그램
```python
import math

def add(a, b):
    """두 수를 더하는 함수"""
    return a + b

def subtract(a, b):
    """두 수를 빼는 함수"""
    return a - b

def multiply(a, b):
    """두 수를 곱하는 함수"""
    return a * b

def divide(a, b):
    """두 수를 나누는 함수"""
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다!"

def power(a, b):
    """a의 b제곱을 계산하는 함수"""
    return a ** b

def square_root(a):
    """제곱근을 계산하는 함수"""
    if a >= 0:
        return math.sqrt(a)
    else:
        return "음수의 제곱근은 계산할 수 없습니다!"

def get_numbers():
    """사용자로부터 두 개의 숫자를 입력받는 함수"""
    try:
        a = float(input("첫 번째 숫자를 입력하세요: "))
        b = float(input("두 번째 숫자를 입력하세요: "))
        return a, b
    except ValueError:
        return None, None

def get_single_number():
    """사용자로부터 하나의 숫자를 입력받는 함수"""
    try:
        a = float(input("숫자를 입력하세요: "))
        return a
    except ValueError:
        return None

def calculator():
    """계산기 메인 함수"""
    print("=== 파이썬 계산기 ===")
    
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 거듭제곱")
        print("6. 제곱근")
        print("7. 종료")
        
        choice = input("선택 (1-7): ")
        
        if choice == '7':
            print("계산기를 종료합니다.")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            a, b = get_numbers()
            if a is None or b is None:
                print("올바른 숫자를 입력해주세요.")
                continue
                
            if choice == '1':
                result = add(a, b)
                print(f"{a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"{a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"{a} × {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                if isinstance(result, str):  # 에러 메시지인 경우
                    print(result)
                else:
                    print(f"{a} ÷ {b} = {result}")
            elif choice == '5':
                result = power(a, b)
                print(f"{a}^{b} = {result}")
                
        elif choice == '6':
            a = get_single_number()
            if a is None:
                print("올바른 숫자를 입력해주세요.")
                continue
            result = square_root(a)
            if isinstance(result, str):  # 에러 메시지인 경우
                print(result)
            else:
                print(f"√{a} = {result}")
        else:
            print("올바른 메뉴를 선택해주세요.")

# 계산기 실행
# calculator()  # 주석을 해제하고 실행해보세요
```

### 프로젝트 2: 개인 일정 관리 프로그램
```python
import datetime

# 전역 변수로 일정 저장
schedule = []

def add_schedule(date_str, event):
    """일정을 추가하는 함수"""
    try:
        # 문자열을 날짜로 변환 (YYYY-MM-DD 형식)
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        schedule.append({"date": date_obj, "event": event})
        return f"일정이 추가되었습니다: {date_str} - {event}"
    except ValueError:
        return "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요."

def show_all_schedule():
    """전체 일정을 보여주는 함수"""
    if not schedule:
        return "등록된 일정이 없습니다."
    
    # 날짜 순으로 정렬
    sorted_schedule = sorted(schedule, key=lambda x: x["date"])
    
    result = "=== 전체 일정 ===\n"
    for item in sorted_schedule:
        result += f"{item['date']} - {item['event']}\n"
    return result

def find_schedule(date_str):
    """특정 날짜의 일정을 찾는 함수"""
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        found_events = [item["event"] for item in schedule if item["date"] == target_date]
        
        if found_events:
            result = f"=== {date_str} 일정 ===\n"
            for event in found_events:
                result += f"- {event}\n"
            return result
        else:
            return f"{date_str}에는 등록된 일정이 없습니다."
    except ValueError:
        return "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요."

def get_today_schedule():
    """오늘의 일정을 가져오는 함수"""
    today = datetime.date.today()
    today_events = [item["event"] for item in schedule if item["date"] == today]
    
    if today_events:
        result = f"=== 오늘({today}) 일정 ===\n"
        for event in today_events:
            result += f"- {event}\n"
        return result
    else:
        return f"오늘({today})에는 등록된 일정이 없습니다."

def schedule_manager():
    """일정 관리 메인 함수"""
    print("=== 개인 일정 관리 프로그램 ===")
    
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 일정 추가")
        print("2. 전체 일정 보기")
        print("3. 특정 날짜 일정 찾기")
        print("4. 오늘 일정 보기")
        print("5. 종료")
        
        choice = input("선택 (1-5): ")
        
        if choice == '5':
            print("일정 관리 프로그램을 종료합니다.")
            break
        elif choice == '1':
            date_str = input("날짜를 입력하세요 (YYYY-MM-DD): ")
            event = input("일정을 입력하세요: ")
            result = add_schedule(date_str, event)
            print(result)
        elif choice == '2':
            result = show_all_schedule()
            print(result)
        elif choice == '3':
            date_str = input("찾을 날짜를 입력하세요 (YYYY-MM-DD): ")
            result = find_schedule(date_str)
            print(result)
        elif choice == '4':
            result = get_today_schedule()
            print(result)
        else:
            print("올바른 메뉴를 선택해주세요.")

# 일정 관리 프로그램 실행
# schedule_manager()  # 주석을 해제하고 실행해보세요
```

### 프로젝트 3: 숫자 야구 게임 (함수로 리팩토링)
```python
import random

def generate_answer():
    """정답을 생성하는 함수"""
    return random.sample(range(0, 10), 3)

def validate_input(user_input):
    """사용자 입력을 검증하는 함수"""
    # 길이 확인
    if len(user_input) != 3:
        return False, "3자리 숫자를 입력해주세요."
    
    # 숫자인지 확인
    if not user_input.isdigit():
        return False, "숫자만 입력해주세요."
    
    # 중복 숫자 확인
    if len(set(user_input)) != 3:
        return False, "서로 다른 숫자를 입력해주세요."
    
    return True, "올바른 입력입니다."

def convert_to_list(user_input):
    """문자열을 정수 리스트로 변환하는 함수"""
    return [int(digit) for digit in user_input]

def calculate_result(answer, user_guess):
    """스트라이크와 볼을 계산하는 함수"""
    strike = 0
    ball = 0
    
    for i in range(3):
        if user_guess[i] == answer[i]:
            strike += 1
        elif user_guess[i] in answer:
            ball += 1
    
    return strike, ball

def format_result(strike, ball):
    """결과를 문자열로 포맷팅하는 함수"""
    if strike == 3:
        return "3 스트라이크! 정답입니다!"
    elif strike == 0 and ball == 0:
        return "아웃!"
    else:
        result_parts = []
        if strike > 0:
            result_parts.append(f"{strike} 스트라이크")
        if ball > 0:
            result_parts.append(f"{ball} 볼")
        return " ".join(result_parts)

def play_baseball_game():
    """숫자 야구 게임 메인 함수"""
    print("=== 숫자 야구 게임 ===")
    print("0-9 사이의 서로 다른 숫자 3개를 맞춰보세요!")
    
    answer = generate_answer()
    attempts = 0
    
    while True:
        attempts += 1
        user_input = input(f"\n{attempts}번째 시도 - 3자리 숫자를 입력하세요: ")
        
        # 입력 검증
        is_valid, message = validate_input(user_input)
        if not is_valid:
            print(message)
            attempts -= 1  # 잘못된 입력은 시도 횟수에 포함하지 않음
            continue
        
        # 문자열을 리스트로 변환
        user_guess = convert_to_list(user_input)
        
        # 결과 계산
        strike, ball = calculate_result(answer, user_guess)
        
        # 결과 출력
        result = format_result(strike, ball)
        print(result)
        
        # 게임 종료 조건
        if strike == 3:
            print(f"\n축하합니다! {attempts}번 만에 정답을 맞췄습니다!")
            print(f"정답: {answer}")
            break

# 게임 실행
# play_baseball_game()  # 주석을 해제하고 실행해보세요
```

## 추가 학습 자료
### 함수 작성 시 좋은 습관
1. **함수명은 동사로 시작**하여 무엇을 하는지 명확하게 표현
   - 좋은 예: `calculate_total()`, `validate_input()`, `generate_password()`
   - 나쁜 예: `data()`, `stuff()`, `thing()`

2. **한 가지 기능만** 수행하도록 작성
   - 함수가 너무 길어지면 여러 개의 작은 함수로 나누기

3. **docstring 작성**하여 함수의 목적을 설명

### 모듈 사용 시 좋은 습관
1. **필요한 것만 import**하기
2. **import 문은 파일 상단**에 모아두기
3. **별칭은 의미있게** 작성하기

```python
# 좋은 예
import datetime as dt
from math import sqrt, pi

# 나쁜 예
from math import *  # 모든 것을 가져오면 충돌 위험
import datetime as d  # 의미를 알기 어려운 별칭
```

## 과제
### 가계부 프로그램
- 수입/지출을 기록하고 관리하는 프로그램을 함수를 활용하여 작성해보세요.
- 필요한 함수들:
  - `add_income(amount, description)`: 수입 추가
  - `add_expense(amount, description)`: 지출 추가
  - `show_summary()`: 수입/지출 요약 보기
  - `show_balance()`: 현재 잔액 보기
