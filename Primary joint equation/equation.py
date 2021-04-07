# sympy 모듈을 사용하여 일차연립방정식 구하기
from sympy import Symbol, solve
import numpy as np

# 변수명과 대수기호를 같은 것으로 하기 위해서 Symbol() 함수 사용
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# 모든 항을 좌변으로 이동시켜서 각각 변수에 대입
# numpy 모듈의 mod 라이브러리를 사용
equation1 = 3*x + 5*y + 7*z - np.mod(3, 16)
equation2 = x + 4*y + 13*z - np.mod(5, 16)
equation3 = 2*x + 7*y + 3*z - np.mod(4, 16)

# sympy의 solve() 함수 사용, 인수로 방정식이 들어있는 변수 넣어주기
# 기본적으로 튜플로 반환, 따라서 딕셔너리로 변환
result = solve((equation1, equation2, equation3), dic=True)

# 결과 출력
print("결과:", result)

# 검산
eval1 = equation1.subs({x:result[x], y:result[y], z:result[z]})
eval2 = equation2.subs({x:result[x], y:result[y], z:result[z]})
eval3 = equation3.subs({x:result[x], y:result[y], z:result[z]})

# 검산결과가 0이 나오면 올바른 것
print("검산결과:", eval1, eval2, eval3)
