#교재문제

# 1. 세 variable x, y, z를 살펴, 그중 가장 큰 홀수를 출력하는 프로그램을 작성하라. 셋 중 어느 것도 홀수가 아니면 셋 중 가장 작은 값을 출력한다.

# 사용자로부터 세 정수를 한 줄에 입력받음 (예: 7 12 3)
x, y, z = map(int, input("세 정수를 입력하세요 (공백으로 구분): ").split())

# 1. 셋 중 홀수만 추출
odds = [num for num in (x, y, z) if num % 2 != 0]

# 2. 조건에 따른 결과 계산
if odds:
    result = max(odds)
else:
    result = min(x, y, z)

print(f"결과: {result}")


# 2. 사용자에게 생일을 mm/dd/yyyy 형식으로 입력받아, `You were born in the year yyyy.` 형태의 string을 출력하는 코드를 작성하라.


birthday = input("Type your birthday (mm/dd/yyyy): ")

month, day, year = birthday.split('/')

print(f"You were born in the year {year}.")



# 3. 다음 코드의 comment를 while loop로 바꿔라.

# ```
# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# #concatenate X to to_print num_x times
# print(to_print)
# ```

num_x = int(input('How many times should I print the letter X? '))
to_print = ''

# while 루프를 이용해 num_x번만큼 'X'를 이어붙입니다.
i = 0
while i < num_x:
    to_print += 'X'
    i += 1

print(to_print)

# 4. 사용자에게 정수 10개를 입력받아, 그중 입력된 가장 큰 홀수를 출력하는 프로그램을 작성하라. 홀수가 하나도 입력되지 않았다면 그런 취지의 message를 출력한다.

odds = []

for i in range(10):
    num = int(input(f'{i+1}번째 정수를 입력하세요:'))
    if num%2 != 0:
        odds.append(num)
if odds:
    print(max(odds))

else:
    print("입력된 숫자 중 홀수가 없습니다.")



# 5. 2보다 크고 1000보다 작은 prime들의 합을 출력하는 프로그램을 작성하라. (힌트: 3부터 999까지 홀수를 도는 for loop 안에, primality test를 하는 for loop를 중첩하면 된다.)


prime_sum = 0

for num in range(3, 1000, 2):
    is_prime = True  
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  
            break           
            
    if is_prime:
        prime_sum += num

print(f"2보다 크고 1000보다 작은 소수들의 합: {prime_sum}")

print(sum(sum_num))

#이해도 점검 문제

# 챕터를 제대로 이해했는지 스스로 확인하려고 낸 3문제다.

# 1. 다음 코드를 실행한 뒤 `area`의 value는 무엇이며, `radius`의 value는 무엇인가? 두 value가 그렇게 되는 이유를 "variable은 그저 name"이라는 관점으로 설명해 봐라.

# ```
# pi = 3
# radius = 11
# area = pi * (radius**2)
# radius = 14
# ```
area는 363, radius는 14. pi가 3


# 2. `6/4`, `6//4`, `6%4`, `2**3`의 value와 type(int/float)을 각각 말하고, `/`와 `//`가 어떻게 다른지 한 문장으로 정리해 봐라.

float, int, int, int
1.5, 1, 2, 8
/ 나누기 
// 몫


# 3. `n = input('Enter an int: ')`를 실행하고 사용자가 `3`을 입력했다. 이때 `type(n)`은 무엇이고 `n*4`는 무엇을 출력하는가? 왜 12가 아닌지를 1장의 type·semantics 개념과 연결해 설명하고, 12를 얻으려면 코드를 어떻게 고쳐야 하는지 써 봐라.

n = int(input('Enter an int: '))
input만 하면 str
type(n)은 str이고, n*4는
  '3333'을 출력한다