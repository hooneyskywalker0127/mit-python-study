#교재문제

# 1. Figure 4-3의 find_root 함수를 사용해서 25의 제곱근, -8의 세제곱근, 16의 네제곱근의 합을 출력하라.
#    epsilon=0.001 사용.




# 2. is_in 함수를 작성하라: 두 문자열을 인자로 받아, 한 문자열이 다른 문자열 어디든 나타나면 True를 반환하고,
#    아니면 False를 반환한다. (힌트: 내장 in 연산자 사용 가능)
#    함수는 `is_in(s1, s2)` 형태로, s1이 s2 어디든 나타나면 True.



# 3. 2번의 is_in 함수를 테스트하는 함수를 작성하라.



# 4. mult 함수를 작성하라: 1개 또는 2개의 정수를 인자로 받는다.
#    2개의 인자를 받으면 두 수의 곱을 출력하고, 1개의 인자만 받으면 그 인자를 출력한다.



# 5. Figure 3-6의 bisection search 알고리즘을 사용해서 log(x, base, epsilon) 함수를 작성하라.
#    """ Assumes x and epsilon int or float, base an int, epsilon > 0 & base > 1
#        Returns float y such that base**y is within epsilon of x.
#        If such a float does not exist, it returns None"""




#이해도 점검 문제

# 챕터를 제대로 이해했는지 스스로 확인하려고 낸 3문제다.

# 1. Scoping 규칙(lexical scoping)을 설명하고, Figure 4-5의 코드에서
#    print(x) 출력이 각 단계에서 어떤 값을 출력하는지 추적해 봐라.
#    (stack frame diagram을 그려가며 설명하면 더 좋음)




# 2. lambda abstraction(파라미터 추상화)이 무엇이고, 왜 필요한지 설명하고,
#    함수 정의에서 formal parameter를 사용할 때의 이점 3가지를 들어 봐라.
#    (예: 코드 재사용, 가독성, 범용성 등)




# 3. Function specification(함수 사양)이란 무엇이고, specification이 있을 때의 장점 2가지를
#    (클라이언트 입장과 구현자 입장으로 나눠서) 설명하고,
#    Figure 4-3의 find_root 함수 spec을 읽고 find_root(8, 3, 0)이 어떻게 동작할지 예측해 봐라.
