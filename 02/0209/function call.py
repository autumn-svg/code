def f1():
    print("f1 시작")
    f2():
    print("f1 종료")


def f2():
    print("f2 시작")
    f3():
    print("f2 종료")

def f3():
    print("f3 시작")

    print("f3 종료")

print("코드 실행")
a =10

f1()
print("코드 실행 종료")