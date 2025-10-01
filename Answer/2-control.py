import random

# 1. 3자리 숫자(서로 다른 숫자)를 생성하여 answer라는 변수에 대입
answer = random.sample(range(0, 10), 3)

# 2. while 문으로 사용자의 입력을 받을 수 있다. 무한루프를 돌면서 3 스트라이크일때만 while 문을 종료하게 만들 것이다.
while True:
    user = input("세 자리 숫자를 입력하세요:")

    # TODO: input으로 받은 값은 기본적으로 문자열이다. 이것이 숫자인지, 길이가 3인지 if 문으로 검사한다.
    # 만약 조건이 맞지 않을 경우 while 문의 처음으로 돌아간다.
    if not (user.isdigit() and len(user) == 3):
        print("잘못된 입력입니다. 세 자리 숫자를 입력하세요.")
        continue

    # TODO: 문자열을 정수 리스트로 변환한다.
    # 리스트 컴프리헨션을 사용할 수 있다.
    user = [int(n) for n in user]

    strike = 0
    ball = 0

    # TODO: for 문과 if 문을 이용하여 정답과 사용자의 입력을 자리별로 비교한다.
    # strike 수와 ball 수를 세어 계산한다.
    for i in range(3):
        if user[i] == answer[i]:
            strike += 1
        elif user[i] in answer:
            ball += 1

    # TODO: strike 와 ball 수를 출력한다.
    # strike 나 ball 이 0 인 경우 이를 출력하지 않는다.
    # 모두 틀렸을 경우에는 아웃이라고 출력해야 한다.
    # 다 맞은 경우에는 프로그램을 종료한다.
    if strike == 0 and ball == 0:
        print(f"{user}: 아웃")
    elif strike == 3:
        print(f"{user}: 정답입니다!")
        break
    else:
        if strike > 0:
            print(f"{user}: {strike} 스트라이크")
        if ball > 0:
            print(f"{user}: {ball} 볼")