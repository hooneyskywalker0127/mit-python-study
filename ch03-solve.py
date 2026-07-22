#교재문제

# 1. Figure 3-2의 코드를, smallest divisor 대신 largest divisor를 반환하도록 고쳐라.
#    (힌트: y*z = x이고 y가 x의 smallest divisor이면 z가 largest divisor다.)
#    참고 - Figure 3-2 원본:
#    x = int(input('Enter an integer greater than 2: '))
#    smallest_divisor = None
#    for guess in range(2, x):
#        if x%guess == 0:
#            smallest_divisor = guess
#            break
#    if smallest_divisor != None:
#        print('Smallest divisor of', x, 'is', smallest_divisor)
        y = x // smallest_divisor
#    else:
#        print(x, 'is a prime number')




# 2. 사용자에게 정수를 입력받아, 1 < pwr < 6 이고 root**pwr 이 입력한 정수와 같은
#    두 정수 root와 pwr을 출력하는 프로그램을 작성하라.
#    그런 정수 쌍이 없으면 그 취지의 message를 출력한다.

num = int(input('type int'))
couple = {}
found = False
for pwr in range(2,6):
    for root in range(2,num+1):
        if root**pwr == num :
            print(root, pwr)
            found = True



# 3. 2보다 크고 1000보다 작은 prime들의 합을 출력하는 프로그램을 작성하라.
#    (힌트: 3부터 999까지 홀수를 도는 for loop 안에 primality test를 하는 for loop를 중첩하라.)




# 4. binary number 10011의 decimal 등가는 무엇인가?
#    (계산 과정을 주석이나 코드로 남겨 봐라.)




# 5. Figure 3-5의 코드는 x = -25이면 어떻게 동작하는가?
#    참고 - Figure 3-5 원본:
#    x = 25
#    epsilon = 0.01
#    num_guesses = 0
#    low = 0.0
#    high = max(1.0, x)
#    ans = (high + low)/2.0
#    while abs(ans**2 - x) >= epsilon:
#        num_guesses += 1
#        if ans**2 < x:
#            low = ans
#        else:
#            high = ans
#        ans = (high + low)/2.0
#    print('numGuesses =', num_guesses)
#    print(ans, 'is close to square root of', x)




# 6. Figure 3-5의 코드가 음수와 양수 모두의 cube root 근사를 구하도록 하려면 무엇을 바꿔야 하는가?
#    (힌트: 답이 탐색 구간 안에 들어오도록 low를 바꾸는 걸 생각하라.)




# 7. Empire State Building은 102층이다. 달걀이 깨지지 않고 떨어뜨릴 수 있는 가장 높은 층을 찾되,
#    맨 위층부터 한 층씩 내려가며 시험하는 방법은 최악의 경우 달걀 102개가 든다.
#    최악의 경우 달걀 7개만 쓰는 방법을 구현하라.




# 8. Newton-Raphson 구현에 root를 찾는 데 쓴 iteration 수를 세는 코드를 추가하고,
#    그 코드로 Newton-Raphson과 bisection search의 효율을 비교하는 프로그램을 작성하라.
#    참고 - Figure 3-7 원본:
#    epsilon = 0.01
#    k = 24.0
#    guess = k/2.0
#    while abs(guess*guess - k) >= epsilon:
#        guess = guess - (((guess**2) - k)/(2*guess))
#    print('Square root of', k, 'is about', guess)




#이해도 점검 문제

# 챕터를 제대로 이해했는지 스스로 확인하려고 낸 3문제다.

# 1. Figure 3-1의 cube root 코드에서 decrementing function은 abs(x) - ans**3 이다.
#    decrementing function이 갖춰야 할 네 가지 성질을 쓰고, 이 함수가 왜 그 네 성질을
#    만족하는지 설명해 이 loop가 어떤 정수 x에 대해서도 종료함을 논증해 봐라.




# 2. 같은 sqrt 문제를 exhaustive enumeration(Figure 3-4)으로 풀면 x=25에서 guess가 49990번,
#    bisection search(Figure 3-5)로 풀면 13번이다. 왜 이렇게 차이가 나는지를
#    "매 iteration마다 탐색 공간이 어떻게 변하는가"로 설명하고,
#    x가 123456처럼 커질 때 두 방식의 guess 수가 각각 어떻게 변할지 말해 봐라.




# 3. x = 0.0 에서 x = x + 0.1 을 열 번 반복한 뒤 x == 1.0 이 False가 된다.
#    왜 그런지를 float가 0.1을 어떻게 저장하는지(binary, significant digits, precision)로 설명하고,
#    float 두 값이 같은지 판정할 때 == 대신 어떻게 써야 하는지 코드로 써 봐라.
