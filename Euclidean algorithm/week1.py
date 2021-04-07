# a = b*q + r
r = []
q = []

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
r.append(num1)
r.append(num2)

while True:
    # q[0]으로 두 정수 나눗셈의 몫이 들어감
    q.append(int(r[0] / r[1]))

    # r[2]로 두 정수 나눗셈의 나머지 값이 들어감
    r.append(r[0] % r[1])

    print(r[0], "=", r[1], "x", q[0], "+", r[2])

    if r[2] == 0:
        break

    # r[1]의 값이 r[0]이 된다.
    del r[0]
    del q[0]

print("GCD({0},{1}) = {2}".format(num1, num2, r[1]))

