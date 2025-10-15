# 실습
## 파일 입출력과 클래스 (구글 코랩 환경)

- 지금까지 만든 프로그램들은 실행이 끝나면 모든 데이터가 사라졌습니다.
- 파일에 데이터를 저장하면 다음에 프로그램을 실행할 때도 데이터를 불러올 수 있습니다.
- 클래스를 배우면 관련된 함수와 데이터를 하나로 묶어서 더 체계적으로 프로그램을 만들 수 있습니다.

**구글 코랩 주의사항:**
- 세션이 끊어지면 저장한 파일들이 사라집니다!
- 중요한 파일은 구글 드라이브에 연결하거나 다운로드 받아야 합니다.

### 구글 코랩에서 파일 다루기

#### 현재 위치 확인하기
```python
import os
print("현재 작업 디렉토리:", os.getcwd())
print("현재 폴더의 파일들:", os.listdir('.'))
```

구글 코랩에서는 보통 `/content/` 폴더에서 작업하게 됩니다.

#### 파일에 쓰기
```python
# 텍스트 파일에 내용 저장하기
with open("my_memo.txt", "w") as file:
    file.write("오늘은 파이썬을 공부했다.\n")
    file.write("구글 코랩에서 파일 저장을 배웠다.\n")
    file.write("내일은 클래스를 배울 예정이다.")

print("메모가 저장되었습니다!")

# 파일이 잘 만들어졌는지 확인
import os
if os.path.exists("my_memo.txt"):
    print("파일이 성공적으로 생성되었습니다!")
else:
    print("파일 생성에 실패했습니다.")
```

#### 파일에서 읽기
```python
# 파일 내용 읽어오기
import os

if os.path.exists("my_memo.txt"):
    with open("my_memo.txt", "r") as file:
        content = file.read()
        print("=== 저장된 메모 ===")
        print(content)
else:
    print("파일이 없습니다!")
```

- 파일 모드 설명:
    - "w" (write): 쓰기 모드 - 새로 쓰기 (기존 내용이 모두 지워짐)
    - "a" (append): 추가 모드 - 기존 내용 뒤에 추가하기
    - "r" (read): 읽기 모드 - 파일 내용 읽어오기

#### 구글 코랩에서 파일 다운로드하기
```python
# 만든 파일을 컴퓨터로 다운로드
from google.colab import files

# 파일 다운로드 (세션이 끊어져도 파일을 보관할 수 있음)
files.download("my_memo.txt")
```

#### 구글 코랩에서 파일 업로드하기
```python
# 컴퓨터에서 파일 업로드
from google.colab import files

uploaded = files.upload()
# 업로드 완료 후 파일명 확인
for filename in uploaded.keys():
    print(f"업로드된 파일: {filename}")
```

### 실습: 구글 코랩용 일기장

```python
from google.colab import files
import datetime
import os

def write_diary():
    """일기 쓰기"""
    diary_entry = input("오늘의 일기를 써주세요: ")
    
    with open("diary.txt", "a") as file:
        today = datetime.date.today()
        file.write(f"\n[{today}] {diary_entry}\n")
    
    print("일기가 저장되었습니다!")

def read_diary():
    """일기 읽기"""
    try:
        with open("diary.txt", "r") as file:
            diary_content = file.read()
            if diary_content.strip():
                print("=== 내 일기장 ===")
                print(diary_content)
            else:
                print("아직 작성된 일기가 없습니다.")
    except FileNotFoundError:
        print("일기 파일이 없습니다. 먼저 일기를 써주세요!")

def backup_diary():
    """일기 백업 (다운로드)"""
    if os.path.exists("diary.txt"):
        print("일기를 다운로드합니다...")
        files.download("diary.txt")
    else:
        print("다운로드할 일기 파일이 없습니다.")

def diary_app():
    """구글 코랩용 일기장 프로그램"""
    print("팁: 작성한 일기는 '백업하기'로 다운로드해서 보관하세요!")
    
    while True:
        print("\n=== 일기장 ===")
        print("1. 일기 쓰기")
        print("2. 일기 읽기")
        print("3. 일기 백업하기 (다운로드)")
        print("4. 종료")
        
        choice = input("선택하세요 (1-4): ")
        
        if choice == "1":
            write_diary()
        elif choice == "2":
            read_diary()
        elif choice == "3":
            backup_diary()
            break
        elif choice == "4":
            print("일기장을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

# 실행해보기
diary_app()
```

### 구글 드라이브 연동

구글 드라이브에 연결하면 파일이 영구적으로 보관됩니다:

```python
# 구글 드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')

# 이제 /content/drive/MyDrive/ 경로에 파일을 저장하면 
# 구글 드라이브에 영구 보관됩니다!

# 드라이브에 파일 저장 예시
with open("/content/drive/MyDrive/my_permanent_memo.txt", "w") as file:
    file.write("이 파일은 구글 드라이브에 저장되어 영구 보관됩니다!")

print("구글 드라이브에 파일이 저장되었습니다!")
```

### 클래스 (Class)

#### 클래스가 왜 필요한가?
지금까지는 함수와 변수가 따로 놀았습니다:

```python
# 학생 정보를 관리하는 기존 방식
student_name = "김철수"
student_age = 20
student_grades = [85, 90, 78]

def show_student_info():
    print(f"이름: {student_name}")
    print(f"나이: {student_age}")
    print(f"성적: {student_grades}")

def add_grade(grade):
    student_grades.append(grade)

# 학생이 여러 명이면 변수가 너무 많아진다!
```

클래스를 사용하면 관련된 데이터와 함수를 하나로 묶을 수 있습니다!

#### 기본 클래스 만들기
```python
class Student:
    """학생 정보를 관리하는 클래스"""
    
    def __init__(self, name, age):
        """학생 객체를 만들 때 실행되는 함수"""
        self.name = name
        self.age = age
        self.grades = []
    
    def show_info(self):
        """학생 정보를 보여주는 함수"""
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"성적: {self.grades}")
    
    def add_grade(self, grade):
        """성적을 추가하는 함수"""
        self.grades.append(grade)
        print(f"{self.name}님의 성적 {grade}점이 추가되었습니다.")
    
    def get_average(self):
        """평균 성적을 계산하는 함수"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# 클래스 사용하기
student1 = Student("김철수", 20)
student2 = Student("박영희", 19)

# 각 학생의 성적 추가
student1.add_grade(85)
student1.add_grade(90)
student2.add_grade(92)
student2.add_grade(88)

# 정보 확인
student1.show_info()
print(f"평균: {student1.get_average():.1f}점")

student2.show_info()
print(f"평균: {student2.get_average():.1f}점")
```

#### 가계부 클래스

```python
from google.colab import files
import datetime
import os

class HouseholdBook:
    """가계부 클래스"""
    
    def __init__(self, filename="household_book.txt"):
        """가계부 초기화"""
        self.filename = filename
        self.load_data()
    
    def load_data(self):
        """파일에서 데이터 불러오기"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print(f"기존 가계부 데이터를 불러왔습니다: {self.filename}")
        else:
            print("새로운 가계부를 시작합니다.")
    
    def add_income(self, amount, description):
        """수입을 추가하는 함수"""
        if amount <= 0:
            return "금액은 0보다 커야 합니다."

        with open(self.filename, "a") as file:
            today = datetime.date.today()
            file.write(f"[{today}] 수입: +{amount:,}원 ({description})\n")
        print(f"수입이 기록되었습니다: {description} +{amount:,}원")
    
    def add_expense(self, amount, description):
        """지출을 추가하는 함수"""
        if amount <= 0:
            return "금액은 0보다 커야 합니다."

        with open(self.filename, "a") as file:
            today = datetime.date.today()
            file.write(f"[{today}] 지출: -{amount:,.0f}원 ({description})\n")
        print(f"지출이 기록되었습니다: {description} -{amount:,.0f}원")
    
    def show_summary(self):
        """수입/지출 요약을 보여주는 함수"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                records = file.read()
                if records.strip():
                    print("=== 가계부 요약 ===")
                    print(records)
                else:
                    print("아직 기록된 내역이 없습니다.")
        else:
            print("가계부 파일이 없습니다.")
    
    def show_balance(self):
        """현재 잔액을 보여주는 함수"""
        total_income = 0
        total_expense = 0
        
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    if "수입: +" in line:
                        amount_str = line.split("수입: +")[1].split("원")[0].replace(",", "")
                        total_income += int(amount_str)
                    elif "지출: -" in line:
                        amount_str = line.split("지출: -")[1].split("원")[0].replace(",", "")
                        total_expense += int(amount_str)
        else:
            print('가계부 파일이 없습니다.')
        
        balance = total_income - total_expense

        print("=== 잔액 현황 ===")
        print(f"총 수입: +{total_income:,.0f}원")
        print(f"총 지출: -{total_expense:,.0f}원")
        print(f"현재 잔액: {balance:,.0f}원")
        
        return balance
    
    def backup(self):
        """가계부 백업 (다운로드)"""
        if os.path.exists(self.filename):
            print("가계부를 다운로드합니다...")
            files.download(self.filename)
        else:
            print("다운로드할 가계부 파일이 없습니다.")

def household_book_manager():
    """가계부 관리 메인 함수"""
    book = HouseholdBook()
    
    print("=== 가계부 관리 프로그램 ===")
    print("* 주기적으로 '백업하기'를 눌러서 가계부를 다운로드하세요!")
    
    while True:
        print("\n" + "="*30)
        print("메뉴를 선택하세요:")
        print("1. 수입 추가")
        print("2. 지출 추가")
        print("3. 수입/지출 요약 보기")
        print("4. 현재 잔액 보기")
        print("5. 백업하기")
        print("6. 종료")
        print("="*30)
        
        choice = input("선택 (1-6): ").strip()
        
        if choice == '6':
            print("가계부 프로그램을 종료합니다.")
            break
        elif choice == '1':
            amount = int(input("수입 금액을 입력하세요: "))
            description = input("수입 내역을 입력하세요: ").strip()
            book.add_income(amount, description)
        elif choice == "2":
            amount = int(input("지출 금액을 입력하세요: "))
            description = input("지출 내역을 입력하세요: ").strip()
            book.add_expense(amount, description)
        elif choice == "3":
            book.show_summary()
        elif choice == "4":
            book.show_balance()
        elif choice == "5":
            book.backup()
            break
        else:
            print("올바른 메뉴를 선택해주세요.")

# 가계부 앱 실행
household_book_manager()
```

### 클래스로 가계부를 만든 이유

#### 기존 함수 방식의 문제점
```python
# 기존 방식 - 함수들이 따로 놀고 있음
income_list = []  # 전역 변수
expense_list = []  # 전역 변수
filename = "household_book.txt"  # 전역 변수

def add_income(amount, description):
    # 전역 변수를 사용해야 함
    global income_list, filename
    # ... 코드

def add_expense(amount, description):
    # 또 다시 전역 변수 사용
    global expense_list, filename
    # ... 코드

def show_balance():
    # 또 다시 전역 변수 사용
    global income_list, expense_list
    # ... 코드
```

**문제점:**
- 전역 변수가 많아져서 관리하기 어려움
- 함수들이 서로 연관되어 있는데 따로 떨어져 있음
- 가계부가 여러 개 필요하면 변수명이 복잡해짐

#### 클래스 방식의 장점

```python
class HouseholdBook:
    def __init__(self, filename="household_book.txt"):
        self.filename = filename  # 각 객체가 자신만의 파일명을 가짐
        self.load_data()
    
    def add_income(self, amount, description):
        # self.filename 사용 - 자신의 데이터에만 접근
        pass
    
    def add_expense(self, amount, description):
        # self.filename 사용 - 안전하게 관리
        pass
```

**장점 1: 데이터와 기능이 하나로 묶임**
```python
# 가계부 객체 하나에 모든 기능이 들어있음
my_book = HouseholdBook("my_money.txt")
my_book.add_income(50000, "용돈")
my_book.add_expense(15000, "점심값")
my_book.show_balance()
```

**장점 2: 여러 개의 가계부를 쉽게 관리**
```python
# 개인 가계부
personal_book = HouseholdBook("personal.txt")
personal_book.add_income(100000, "알바비")

# 동아리 가계부
club_book = HouseholdBook("club.txt")
club_book.add_income(50000, "회비")

# 각각 독립적으로 관리됨!
```

**장점 3: 코드 재사용이 쉬움**
```python
# 새로운 가계부를 만들 때마다 클래스만 생성하면 됨
family_book = HouseholdBook("family.txt")
travel_book = HouseholdBook("travel.txt")
study_book = HouseholdBook("study.txt")

# 모든 가계부가 같은 기능을 사용할 수 있음
```

**장점 4: 유지보수가 쉬움**
```python
class HouseholdBook:
    # 새로운 기능을 추가하면 모든 가계부 객체가 사용 가능
    def get_monthly_summary(self, month):
        # 새로운 기능 추가
        pass
    
    def export_to_excel(self):
        # 또 다른 새로운 기능
        pass
```

#### 클래스의 핵심 개념 정리

**1. `__init__` 메소드 (생성자)**
```python
def __init__(self, filename="household_book.txt"):
    self.filename = filename  # 객체의 속성 설정
    self.load_data()         # 초기화 작업
```
- 객체가 만들어질 때 자동으로 실행
- 객체의 초기 상태를 설정

**2. `self` 키워드**
```python
def add_income(self, amount, description):
    with open(self.filename, "a") as file:  # self.filename 사용
        # self는 "이 객체 자신"을 의미
        pass
```
- 객체 자신을 가리키는 키워드
- 객체의 데이터에 접근할 때 사용
- 클래스 안의 함수인 메소드는 항상 첫번째 인자를 self로 받는다

**3. 메소드 (객체의 함수)**
```python
# 클래스 안의 함수들을 메소드라고 부름
class HouseholdBook:
    def add_income(self):     # 메소드
        pass

    def add_expense(self):    # 메소드
        pass

    def show_balance(self):   # 메소드
        pass
```

#### 실제 사용 비교

**함수 방식:**
```python
# 매번 파일명을 전달해야 함
add_income("my_book.txt", 50000, "용돈")
add_expense("my_book.txt", 15000, "점심값")
show_balance("my_book.txt")
```

**클래스 방식:**
```python
# 한 번 객체를 만들면 계속 사용
my_book = HouseholdBook("my_book.txt")
my_book.add_income(50000, "용돈")
my_book.add_expense(15000, "점심값")
my_book.show_balance()
```

클래스를 사용하면 **관련된 데이터와 기능을 하나로 묶어서** 더 체계적이고 안전하게 프로그램을 만들 수 있습니다!

### 클래스 상속 (Inheritance)

클래스는 다른 클래스의 기능을 물려받을 수 있습니다. 마치 부모가 자식에게 특징을 물려주는 것과 같습니다!

#### 상속이 왜 필요한가?

```python
# 상속 없이 만들면 중복 코드가 많아짐
class Dog:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name}가 밥을 먹습니다.")
    
    def sleep(self):
        print(f"{self.name}가 잠을 잡니다.")
    
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다.")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def eat(self):  # Dog과 똑같은 코드
        print(f"{self.name}가 밥을 먹습니다.")
    
    def sleep(self):  # Dog과 똑같은 코드
        print(f"{self.name}가 잠을 잡니다.")
    
    def meow(self):
        print(f"{self.name}가 야옹 웁니다.")
```

#### 상속을 사용하면 중복을 줄일 수 있음

```python
# 부모 클래스 (기본 동물)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name}가 밥을 먹습니다.")
    
    def sleep(self):
        print(f"{self.name}가 잠을 잡니다.")

# 자식 클래스 (Animal을 상속받음)
class Dog(Animal):  # Animal의 기능을 모두 물려받음
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다.")

class Cat(Animal):  # Animal의 기능을 모두 물려받음
    def meow(self):
        print(f"{self.name}가 야옹 웁니다.")

# 사용하기
dog = Dog("강아지")
cat = Cat("고양이")

# 부모 클래스의 기능 사용 가능
dog.eat()    # Animal에서 물려받은 기능
dog.sleep()  # Animal에서 물려받은 기능
dog.bark()   # Dog만의 고유 기능

cat.eat()    # Animal에서 물려받은 기능
cat.sleep()  # Animal에서 물려받은 기능
cat.meow()   # Cat만의 고유 기능
```

#### 가계부에서 상속 활용하기

```python
# 기본 가계부 클래스
class BasicHouseholdBook:
    def __init__(self, filename):
        self.filename = filename
    
    def add_record(self, amount, description, record_type):
        with open(self.filename, "a") as file:
            import datetime
            today = datetime.date.today()
            file.write(f"[{today}] {record_type}: {amount:,}원 ({description})\n")
    
    def show_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print(file.read())

# 개인 가계부 (BasicHouseholdBook 상속)
class PersonalHouseholdBook(BasicHouseholdBook):
    def add_allowance(self, amount):
        self.add_record(amount, "용돈", "수입")
    
    def add_snack_expense(self, amount, snack_name):
        self.add_record(amount, f"간식-{snack_name}", "지출")

# 동아리 가계부 (BasicHouseholdBook 상속)
class ClubHouseholdBook(BasicHouseholdBook):
    def add_membership_fee(self, amount, member_name):
        self.add_record(amount, f"{member_name} 회비", "수입")
    
    def add_event_expense(self, amount, event_name):
        self.add_record(amount, f"{event_name} 행사비", "지출")

# 사용하기
my_book = PersonalHouseholdBook("personal.txt")
my_book.add_allowance(50000)  # PersonalHouseholdBook만의 기능
my_book.show_records()        # 부모 클래스에서 물려받은 기능

club_book = ClubHouseholdBook("club.txt")
club_book.add_membership_fee(10000, "김철수")  # ClubHouseholdBook만의 기능
club_book.show_records()                       # 부모 클래스에서 물려받은 기능
```

#### 상속의 장점

**1. 코드 재사용**
- 공통 기능을 부모 클래스에 한 번만 작성
- 자식 클래스들이 모두 사용 가능

**2. 유지보수 편리**
- 공통 기능을 수정할 때 부모 클래스만 수정하면 됨
- 모든 자식 클래스에 자동으로 적용

**3. 확장 가능**
- 기본 기능은 유지하면서 새로운 기능 추가 가능

#### 상속 관계 확인하기

```python
# 상속 관계 확인
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog은 Animal을 상속받음)
print(isinstance(cat, Dog))     # False
```

- 핵심 정리
    - `class 자식클래스(부모클래스):` 형태로 상속
    - 자식 클래스는 부모 클래스의 모든 기능을 사용할 수 있음
    - 자식 클래스에서 고유한 기능을 추가할 수 있음
    - 코드 중복을 줄이고 체계적인 프로그램 작성 가능