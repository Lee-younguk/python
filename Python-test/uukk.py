# # 테스트
# # 하나만 출력됩니다.
# from ctypes.wintypes import PINT
# from doctest import REPORTING_FLAGS
# from lib2to3.pgen2.token import RPAR


# print("# 하나만 출력합니다.")
# print("hello python programming!")
# print()

# # 여러 개를 출력합니다.
# print("# 여러 개를 출력합니다.")
# print(53, 272, "hello")
# print(10, 20, 30, 40, 50)
# print("안녕하세요", "저의", "이름은", "이영욱입니다")
# print()

# # 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
# print("# 아무것도 출력하지 않습니다.")
# print("---확인 전용선---")
# print()
# print()
# print()
# print("---확인 전용선---")
# print()

# print("# class 는 문자열인 string 이다")
# print(type("안녕하세요"))
# print()

# print("# class 는 정수인 integer 이다")
# print(type(273))
# print()
# # print("# 내용") 중 ' print("# 내용") 을 입력 했을 때
# # 출력되는 것은 # 내용 이다.

# print("안녕하세요." + "저의" + "이름은" + "이영욱입니다.")
# # print() 식별자이며 문자열에 , 를 입력 후 출력 시 띄어쓰기 + 를 입력 후 출력 시 이어져서 나온다.

# print()
# print("# ' 와 , '를 구분하고 싶을때'")
# print()
# print("'이영욱이라는' '사람이' '말했습니다'", '"안녕하세요"')
# print()
# # print() 문자열에 ' 를 쓰고 싶다면 외부에 " 를 입력
# print("'이영욱'", "이라는 사람이", '"안녕하세요"', "라고 말했습니다")
# print()
# # print() 문자열에 " 를 쓰고 싶다면 외부에 ' 를 입력
# print()
# print("# 이스케이프 문자 \" 사용법")
# print()
# print("\"안녕하세요\" 라고 말했습니다.")
# # print 문자열에 역슬래시 ' , " 를 붙이게 되면 문자열을 만드는 기호가 아닌 단순한 따옴표로 생각
# print()
# print("# 이스케이프 문자 \' 사용법")
# print('\'이영욱이라는 사람이\'')
# # 그래서 동일한 따옴표를 쓸 수가 있다 (역슬래스) = 이스케이프 문자
# print()
# print("'이영욱' 이라는 사람이 \"안녕하세요\" 라고 말했습니다.")
# # 위와 같은 " 안에 " 내용을 사용하고 싶을 때 이스케이프 문자를 이용할 수 있다.
# print()
# print("# 이스케이프 \n 과 \t 사용법")
# print("\'이영욱\'\t이라는\t사람이\n\"안녕하세요\"\t라고\t말했습니다.")
# # 위와 같이 \t 는 탭을 치는 것과 같은 역할
# # 위와 같이 \n 은 줄바꿈과 같이 같은 역할
# print()
# print("# 이스케이프 문자 \\ 는 \ 를 의미한다.")
# print("\\ \n\\\n\\")
# # 위와 같이 \\ 는 \ 하나의 역슬래시 역할
# print()
# print("# \ n 은 끊어지지않고 길게 쳐야하기 때문에 다른 문자열 사용법")
# print()
# print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산 대한사람\n대한으로 길이 보전하세")
# print("""\n동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산 대한사람
# 대한으로 길이 보전하세
# """)
# # 위와 같이 \n 으로 줄바꿈도 가능하지만 """ 이나 ''' 로도 가능하다.
# print("안녕하세요"[0])
# print("안녕하세요"[1])
# print("안녕하세요"[2])
# print("안녕하세요"[3])
# print("안녕하세요"[4])
# # 위와 같이 0부터 숫자상태로 나열한 것이 제로 인덱스
# print()
# print("안녕하세요"[-5])
# print("안녕하세요"[-4])
# print("안녕하세요"[-3])
# print("안녕하세요"[-2])
# print("안녕하세요"[-1])
# # 위와 같이 - 도 가능한데 -5 -4 -3 -2 -1 / 0 1 2 3 4 이런꼴이다 -0 은 없다.
# print()
# print("안녕하세요"[0:1])
# print("안녕하세요"[0:2])
# print("안녕하세요"[0:3])
# print("안녕하세요"[0:4])
# print("안녕하세요"[0:5])
# # 위와 같이 범위를 지정할 수 있으나 뒤에 숫자는 포함하지 않는다 뒷 숫자가 n 이라면 n-1 이다.
# print()
# print("안녕하세요"[2:1])
# # 범위를 지정하는 것이기에 큰 숫자 : 작은 숫자는 될 수 없다.
# print()
# print("안녕하세요"[:1])
# print("안녕하세요"[:2])
# print("안녕하세요"[:3])
# print("안녕하세요"[:4])
# print("안녕하세요"[:5])
# # 뒷 숫자는 포함하지 않는다 ' : ' 앞 숫자는 0부터 시작한다는 의미이다.\
# print()
# print("안녕하세요"[0:])
# print("안녕하세요"[1:])
# print("안녕하세요"[2:])
# print("안녕하세요"[3:])
# print("안녕하세요"[4:])
# # 위와 같이 뒷 숫자가 없는 건 끝 자리까지 나열한다는 의미이다.
# # 앞 숫자는 ' 0 안 1 녕 2 하 3 세 4 요 ' 이다.
# print()
# # 인덱스 에러는 리스트/문자열 수를 넘는 요소/글자를 선택할 때 발생한다.
# print(len("안녕하세요"))
# print(len("이영욱"))
# print()
# print("8 + 27 = ", 8 + 27 )
# # print("8 + 27 = ",) 까지는 8 + 27 = 이라는 것을 출력하고
# # 괄호 안에 있는 8 + 27은 사직 연산해서 출력이 된다 즉 35 가 출력된다.
# # - , * , / 다 가능하다
# print()
# print("8 / 27 =", 8 / 27)
# # 소수점이 제한없이 나오는데 이것을 정수로 하고 싶다면 // 즉 슬래시를 하나 더 해준다.
# print("8 // 27 = ", 8 // 27)
# # 소수점 없이 정수만 0 이라는 숫자가 출력이 된다.
# print()
# print("8 % 27 =", 8 % 27)
# # 나머지 값만 구하는 나머지 연산자는 % 퍼센트 기호를 이용한다
# print()
# print("8 ** 27 =", 8 ** 27)
# # **의 수로 제곱근을 구하는 연산자이다
# print("3 ** 2 =", 3 ** 2 )
# print("3 ** 3 =", 3 ** 3 )
# # ** 제곱근을 구한다는 연산자 기호이며, 뒷 숫자는 지수를 의미한다.
# # 위에껀 3 의 2 제곱, 밑에껀 3 의 3 제곱을 의미한다.
# print()
# print(2 + 2 - 2 * 2 / 2 * 2)
# print()
# print("안녕" + "하세요" * 3 )
# print()
# # 정수 integer
# # 소수 floating point
# # 덧셈 +
# # 뺄셈 -
# # 곱셈 *
# # 나눗셈 /
# # 정수 나누기 //
# # 나머지 %
# # 제곱 **
# print("3462 // 17 =", 3462 // 17)
# print("3462 % 17 =", 3462 % 17)
# print()
# # 
# #a = input("문자열 입력>")
# #b = input("문자열 입력>")
# #print()
# #print(a,b)
# #a = b
# #b = b
# #print(a,b)
# format_a = "{}억 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}억 원 만들기".format(5000)
# format_c = "{} {} {}".format(5000, 10000, 15000)
# format_d = "{} {} {}".format(1, "문자열", True)
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)
# print()
# output_a = "{:d}".format(52)
# output_b = "{:5d}".format(-52)
# output_c = "{:10d}".format(52)
# output_d = "{:05d}".format(52)
# output_e = "{:010d}".format(-52)
# print()
# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)
# print(output_e)
# print()
# #a = input("입력>")
# #b = input("입력>")
# #print(a,b)
# #b = a
# #a = b
# #b = a
# #print(a,b)
# print()
# output_f = "{:+d}".format(52)
# output_g = "{:+d}".format(-52)
# output_h = "{:-d}".format(52)
# output_i = "{:-d}".format(-52)
# output_j = "{: d}".format(52)
# output_k = "{: d}".format(-52)
# print()
# print(output_f)
# print(output_g)
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print()
# output_a = "{:f}".format(52.273)
# output_b = "{:15.3f}".format(52.273)
# output_c = "{:+15.2f}".format(52.273)
# output_d = "{:015.1f}".format(52.273)
# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)
# print()
# a = "Hello World"
# a.upper()
# print(a.upper())
# print()
# input_a = """
#   안녕하세요
#         문자열의 함수를     
#                    알아보자
# """
# print(input_a.strip())
# print(input_a.replace(" ",""))
# print()
# a = "10 20 30 40 50".split(" ")
# print(a)
# print()
# format_a = "{} {}".format(52, type(273))
# print(format_a)
# print()
# a = input("> 1 숫자: ")
# b = input("> 2 숫자: ")
# print()
# print("{} + {} = {}".format(a,b,int(a)+int(b)))
# print()
# number = input("정수 입력>")
# number = int(number)
# print()
# if number > 0:
#     print("양수입니다")
# if number < 0:
#     print("음수입니다")
# if number == 0:
#     print("0입니다")
# print()
# from calendar import day_abbr
# import datetime
# print()
# now = datetime.datetime.now()
# print()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second
# ))
# print()
# print(now.year, "년")

# if 6 <= now.month <= 8:
#     print("여름인 {}월".format(now.month))

# print(now.day, "일")

# if now.hour < 12:
#     print("오전 {}시".format(now.hour))

# if now.hour > 12:
#     print("오후 {}시".format(now.hour))

# print("{}분 {}초 입니다.".format(now.minute,now.second))
# print()
# if 6 <= now.month <= 8: and
#     now.hour < 12  
# # if now.hour > 12 :
#     print("{}년".format(now.year),"여름 {}월".format(now.month),
#     "오전".format(now.hour),"오후".format(now.hour),
#     "{}분 {}시 입니다".format(now.minute,now.second))
# number = input("정수 입력>")
# last_character = number[-1]
# last_number = int(last_character)

# if  last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8 :
#     print("짝수입니다")

# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9 :
#     print("홀수입니다")
# number = input("정수")
# number = int(number)
# if number % 2 == 0:
#     print("짝수입니다")
# else : 
#     print("홀수입니다")
# number = input("정수>")
# number = int(number)
# if 1 <= number <= 3 :
#     print("현재는 봄입니다")
# elif 4 <= number <= 6 :
#     print("현재는 여름입니다")
# elif 7 <= number <= 9 :
#     print("현재는 가을입니다")
# elif 10 <= number <= 12 :
#     print("현재는 겨울입니다")
# from tkinter import scrolledtext


# score = float(input("학점 입력>"))
# if score == 4.5 :
#     print("신")
# elif score >= 4.2 :
#     print("사랑")
# elif score >= 3.5 :
#     print("수호자")
# elif score >= 2.8 :
#     print("일반인")
# elif score >= 2.3 :
#     print("소시민")
# elif score >= 1.75 :
#     print("선구자")
# elif score >= 1.0 :
#     print("천민")
# elif score >= 0.5 :
#     print("자벌레")
# elif score > 0:
#     print("플랑크톤")
# else:
#     print("혁명")
# print()
# x = 10 
# if 10 < x and x < 20 :
#     print("조건에 맞습니다.")
# print()
# str_input = input("태어난 해 입력>")
# birth_year = int(str_input) # int(str_input % 12) 로도 가능하다. 이렇게 하면 if 조건문 수정필요
# if birth_year % 12 == 0 :
#     print("원숭이")
# elif birth_year % 12 == 1 :
#     print("닭")
# elif birth_year % 12 == 2 :
#     print("개")
# elif birth_year % 12 == 3 :
#     print("돼지")
# elif birth_year % 12 == 4 :
#     print("쥐")
# elif birth_year % 12 == 5 :
#     print("소")
# elif birth_year % 12 == 6 :
#     print("범")
# elif birth_year % 12 == 7 :
#     print("토끼")
# elif birth_year % 12 == 8 :
#     print("용")
# elif birth_year % 12 == 9 :
#     print("뱀")
# elif birth_year % 12 == 10 :
#     print("말")
# else:
#     print("양")
# print()
# list_a = [[1,2,3],[4,5,6]]

# list_a.insert(([0],[1]),7)
# print(list_a)
# print()
# from cgi import print_arguments


# aaa = [1998, 1999, 2000]
# for bbb in aaa :
#     if bbb == 1998 :
#         print("{}년생은 호랑이띠".format(bbb))
#     elif bbb == 1998 :
#         print("{}년생은 토끼띠".format(bbb))
#     else:
#         print(bbb,"년생은 용띠")
# print()
# ddd = {
#     "name" : "망고",
#     "type" : "당",
#     "ingredient" : ["망고", "설탕", "나트륨", "색소"],
#     "origin" : "필리핀"
# }
# print()
# print("name:", ddd["name"])
# print("type:", ddd["type"])
# print("ingerdient:", ddd["ingredient"])
# print("origin:", ddd["origin"])
# print()

# ddd["name"] = "건조 망고"
# print("name:", ddd["name"])
# print(ddd["ingredient"][1])
# print(ddd)
# print()
# vvv = ddd.get("존재하지 않는 키")
# kkk = input("알고싶은 키>")
# if kkk in ddd :
#     print(ddd[kkk])
# elif vvv == None:
#     print("존재하지 않는 키에 접근")

# foods = {
#     "떡볶이" : "맥주",
#     "짜장면" : "고량주",
#     "라면" : "콜라",
#     "피자" : "소맥",
#     "치킨" : "폭탄주",
#     "삼겹살" : "소주"
#     }
# print()
# while (True) :
#     # whlie 은 무한 반복문 , True 참 일때까지
#     myfood = input(str(list(foods.keys())) + " 중 좋아하는 음식은 ? ")
#     # foods.keys (변수 foods 안에 있는 키들)(keys) 을 list (나열) str (문자열)
#     # myfood 에 대입한다.
#     if myfood in foods :
#         print("<%s> 궁합 술은 <%s> 입니다." % (myfood, foods.get(myfood)))
#         # <%s> 는 .format() 구문의 {} 와 같다. 
#     elif myfood == "끝" :
#         # while 무한 반복문을 끝내고 싶을 때 '끝' 이라고 입력하면 나가진다.
#         break # 끝낸다. = exit
#     else :
#         print("그런 음식은 없습니다. 다시 시도해보세요.")

# years = {
#     "0" : "원숭이",
#     "1" : "닭",
#     "2" : "개",
#     "3" : "돼지",
#     "4" : "쥐",
#     "5" : "소",
#     "6" : "범",
#     "7" : "토끼",
#     "8" : "용",
#     "9" : "뱀",
#     "10" : "말",
#     "11" : "양"
#     }

# while (True) :
#     myyear = input(str(list(years.keys())) + "중 태어난 년도는 ?")
#     if myyear in years :
#         print(" <%s> 년의 띠는 <%s> 입니다." % (myyear, years.get(myyear)))
#     elif myyear == "끝" :
#         break
#     else:
#         print("입력 실패입니다. 다시 시도하세요.")

# from __future__ import print_function


# for i in reversed(range(5)):
#     print("현재 반복 변수 : {}".format(i))

# i = 0
# while i < 10 :
#     print("{}번째 반복입니다.".format(i))
#     i += 1

# list_a = [1,2,3,4,1,2,3,4]
# value = 2
# while value in list_a:
#     list_a.remove(value)
# print(list_a)

# list_a = [1,2,3,4,1,2,3,4]
# list_a.remove(2)
# print(list_a)

# import time # 유닉스타임 가져오는 기능

# nnn = 0 # 시작은 0 부터 한다

# target = time.time() + 5 # 기본 유닉스 타임에 + 5 초

# while time.time() < target: # 기본 유닉스 타임이 < + 5 초 보다 작을 때 ( 5초 뒤라는 소리 )
#     nnn += 1 # 나갈때는 1 을 + 해서 나간다.

# print("5초 동안 {}번 반복했습니다.".format(nnn)) # 즉 결과는 5 초 동안 0부터 1을 몇번 더했는지

# i = 0

# while True : 
#     print("{}번째 반복입니다. 다시 시도하세요.".format(i))
#     i += 1 

#     input_t = input("종료 (Y/y) : >")
#     if input_t in ["Y", "y"] :
#         print("종료합니다.")
#         break
#     if i == 5 : # i > 4
#         break

# num = [5, 15, 20, 1, 2, 7, 25, 30]

# for nnn in num :
#     if nnn >= 10:
#         print(nnn) # 10 보다 크거나 같은 숫자들을 출력

# for nnn in num :
#     if nnn <= 10 :
#         continue
#     print(nnn)     # 10 보다 작거나 같은 숫자들은 continue 로 나가고 아닌 숫자들은 출력
# print()
# print(nnn)         # 맨 마지막 꺼가 나온다
# print()
# for nnn in num :
#     if nnn <= 10:
#         print(nnn) # 10 보다 작거나 같은 숫자들을 출력

# for nnn in num :
#     if nnn >= 10 :
#         continue
#     print(nnn)     # 10 보다 크거나 같은 숫자들은 continue 로 나가고 아닌 숫자들은 출력
# print()
# key = ["name", "hp", "mp", "level"]
# value = ["기사", 200, 30, 5]
# ccc = {}

# for i in range(len(key)) :
#     ccc[key[i]] = value[i]

# print(ccc)
# print()
# from ipaddress import summarize_address_range

# limit = 10000
# i = 1

# sum_v = 0
# while sum_v < limit :
#     sum_v = sum_v + i
#     i = i + 1
#     if sum_v > limit :
#         break

# print("{}를 더할 때 , {} 넘으며 그때 값은 {}이다.".format(i-1, limit, sum_v))

# limit = 10000
# i = 1
# sum_v = 0
# for i in range(143) :
#     if sum_v < limit :
#         sum_v += i
#         i + 1
#     else :
#         print("{}를 더할 때 , {} 넘으며 그때 값은 {}이다.".format(i-1, limit, sum_v))

# print("{}를 더할 때 , {} 넘으며 그때 값은 {}이다.".format(i-1, limit, sum_v))

# list_a = [1, 2, 3, 4, 5]
# print(list(reversed(list_a)))
# print(reversed(list_a))
# print(list(list_a))
# print(list_a)
# print(next(reversed(list_a)))
# print(next(list(list_a)))

# max_v = 0
# a = 0
# b = 0

# for i in range(1, 99 +1):
#     j = 100 - i
#     if max_v < i * j :
#         a = i
#         b = j
#         max_v = i * j

# print("최대가 되는 경우: {} * {} = {} ".format(a, b, max_v))

# print("Hello Python")
# print("Hello Python" * 3)
# print()
# sss = input("반지름 입력>")
# nuu = float(sss)
# print()
# print(2 * 3.14 * nuu)

# if True:
#     print("True입니다")
#     print("정말 True입니다")

# if False :
#     print("False입니다")

# print()
# list = [[1,2,3],[4,5,6],[7,8,9]]
# print(list[1][1])

from inspect import FrameInfo


nums = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for num in nums :
    if num >= 100 :
        print("100이상:",nums)