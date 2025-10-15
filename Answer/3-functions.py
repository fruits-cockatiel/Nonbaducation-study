# 전역 변수로 가계부 데이터 저장
income_list = []  # 수입 리스트
expense_list = []  # 지출 리스트

def add_income(amount, description):
    """
    수입을 추가하는 함수
    
    Args:
        amount (float): 수입 금액
        description (str): 수입 내역 설명
    
    Returns:
        str: 결과 메시지
    """
    if amount <= 0:
        return "금액은 0보다 커야 합니다."
    
    income_record = {
        "amount": amount,
        "description": description
    }
    income_list.append(income_record)
    return f"수입이 추가되었습니다: {description} (+{amount:,.0f}원)"

def add_expense(amount, description):
    """
    지출을 추가하는 함수
    
    Args:
        amount (float): 지출 금액
        description (str): 지출 내역 설명
    
    Returns:
        str: 결과 메시지
    """
    if amount <= 0:
        return "금액은 0보다 커야 합니다."
    
    expense_record = {
        "amount": amount,
        "description": description
    }
    expense_list.append(expense_record)
    return f"지출이 추가되었습니다: {description} (-{amount:,.0f}원)"

def show_summary():
    """
    수입/지출 요약을 보여주는 함수
    
    Returns:
        str: 요약 정보
    """
    if not income_list and not expense_list:
        return "등록된 내역이 없습니다."
    
    result = "=== 가계부 요약 ===\n\n"
    
    # 수입 내역
    if income_list:
        result += "수입 내역:\n"
        for i, record in enumerate(income_list, 1):
            result += f"  {i}. {record['description']} | +{record['amount']:,.0f}원\n"
    else:
        result += "수입 내역: 없음\n"
    
    result += "\n"
    
    # 지출 내역
    if expense_list:
        result += "지출 내역:\n"
        for i, record in enumerate(expense_list, 1):
            result += f"  {i}. {record['description']} | -{record['amount']:,.0f}원\n"
    else:
        result += "지출 내역: 없음\n"
    
    return result

def show_balance():
    """
    현재 잔액을 보여주는 함수
    
    Returns:
        str: 잔액 정보
    """
    total_income = sum(record['amount'] for record in income_list)
    total_expense = sum(record['amount'] for record in expense_list)
    balance = total_income - total_expense
    
    result = "=== 잔액 현황 ===\n"
    result += f"총 수입: +{total_income:,.0f}원\n"
    result += f"총 지출: -{total_expense:,.0f}원\n"
    result += f"현재 잔액: {balance:,.0f}원"

    return result

def household_book_manager():
    """가계부 관리 메인 함수"""
    print("=== 가계부 관리 프로그램 ===")
    
    while True:
        print("\n" + "="*30)
        print("메뉴를 선택하세요:")
        print("1. 수입 추가")
        print("2. 지출 추가")
        print("3. 수입/지출 요약 보기")
        print("4. 현재 잔액 보기")
        print("5. 종료")
        print("="*30)
        
        choice = input("선택 (1-5): ").strip()
        
        if choice == '5':
            print("가계부 프로그램을 종료합니다.")
            break
        elif choice == '1':
            amount = int(input("수입 금액을 입력하세요: "))
            description = input("수입 내역을 입력하세요: ").strip()
            result = add_income(amount, description)
            print(result)
        elif choice == '2':
            amount = int(input("지출 금액을 입력하세요: "))
            description = input("지출 내역을 입력하세요: ").strip()
            result = add_expense(amount, description)
            print(result)
        elif choice == '3':
            result = show_summary()
            print(result)
        elif choice == '4':
            result = show_balance()
            print(result)
        else:
            print("올바른 메뉴를 선택해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    # 메인 프로그램 실행
    household_book_manager()