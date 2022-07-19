# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# for number in numbers :
#     if number >= 100 :
#         print("100이상 :", number)
# from curses import ACS_GEQUAL
# from multiprocessing.sharedctypes import Value
# from unicodedata import name


# from queue import PriorityQueue
# from xml.dom.minidom import Element


# print()
# for number in numbers : 
#     if number % 2 == 0 :
#         print("{}는 짝수".format(number))
#     else :
#         print("{}는 홀수".format(number))
# 
# game = ["짝수", "홀수"]
# for number in numbers :
#     print("{}는 {}입니다.".format(number, game[number % 2]))
# print()
# for number in numbers :
#     # len(number) == 1
#     print("{}는 {}자릿수".format(number,len(str(number)))) 
# list_o_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9, 10]
# ]
# for element in list_o_list :
#     # character = element 
#     for character in element :
#         print(character)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output =[[], [] ,[]]
# for number in numbers :
#     output[(number -1) % 3].append(number)
# print(output)
#
# exes = ["    *    ", "   ***   ", "  *****  ", " ******* ", "*********"]
# for exe in exes :
#     print(exe)
#
# for i in range(4) :
#     for j in range(4) :
#         print("*", end = " ")
#     print()
#
# number = int(input("피라미드 계단 수를 입력 :"))
# for i in range(0,number) :
#     for j in range(0,number-i-1) :
#         print(end = " ")
#     for j in range(0,i+1) :
#         print("*", end = " ")
#     print()
# print()
# pets = [
#     {"name" : "구름", "age" : "5"},
#     {"name" : "초코", "age" : "3"},
#     {"name" : "아지", "age" : "2"},
#     {"name" : "호랑이", "age" : "1"}
# ]
# print()
# for pet in pets :
#     print("{} {}살".format(pet["name"], pet["age"]))
# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}
# for number in numbers :
#     if number in counter :
#         counter[number] += 1
#     else :
#         counter[number] = 1
# print(counter)
# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sword" : "불꽃의 검",
#         "armor" : "풀플레이트",
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
# }
# for key in character :
#     pass
# def print_3_times(value, n) :
#     for i in range(n) :
#         print(value)
# print_3_times("안녕하세요", 3)
# def f_1(x) :
#     return (2 * x) + 1 
# print(f_1(10))
# def f_2(x) :
#     return (x ** 2) + (2 * x) + 1
# print(f_2(10))
def mul(*values) : 
    output = 1
    for i in values : 
        output *= i
    return output
print(mul(5, 7, 9, 10))

def mul(*values) : 
    output = 0
    for i in values : 
        output += i
    return output
print(mul(5, 7, 9, 10))
#
# def function(valueA, valueB, *values) :
#     print(valueA)
#     print(valueB)
#     print(*values)
# function(1, 2, 3, 4, 5)
#
# output = 1
# for i in range(1, 5) :
#     output *= i
# print(output)
#
# def factorial(n) :
#     if n == 0 :
#         return 1
#     else :
#         return n * factorial(n-1)
# print(factorial(4))
# 토끼
# counter = 0
# def fivonacci(n) :
#     global counter
#     counter += 1 
#     if n == 1 :
#         return 1
#     elif n == 2 :
#         return 1
#     else :
#         return fivonacci(n-1) + fivonacci(n-2)
# print(fivonacci(40),counter)
#
# number_a = int(input("숫자 입력 1 >"))
# number_b = int(input("숫자 입력 2 >"))
# output = 0
# for i in range(number_a, number_b) :
#     output += i
# print(output)


# def sum_number(number_a, number_b) :
#     output = 0
#     for i in range(number_a, number_b) :
#         output += i
#     return output
# print(sum_number(5, 10))