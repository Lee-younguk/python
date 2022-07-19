
# for i in range(1, 100+1) :
#     output = "{:b}".format(i)
#     if output.count("0") == 1 :
#         print(i, output)

# from audioop import avg


# output = [ i for i in range(1, 100+1) if "{:b}".format(i).count("0") == 1]
# print(output)
# # for i in output :
# #     print("{} : {}".format(i, "{:b}".format(i)))
# # print(sum(output))
# for i in output :
#     print(i, "{:b}".format(i))
# print(output)
# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sword" : "불꽃의 검",
#         "armor" : "풀플레이트"
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
#     }
# for keys in character :
#     if type(character[keys]) is dict :
#         for k in character[keys] :
#             print("{} : {}".format(k, character[keys][k]))
#     elif type(character[keys]) is list :
#         for k in character[keys] :
#             print("{} : {}".format(keys, k))
#     else :
#         print("{} : {}".format(keys, character[keys]))
#
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}
# for i in range(len(key_list)) :
#     character[key_list[i]] = value_list[i]
#     # print("{} : {}".format(key_list[i], value_list[i]))
# print(character)
#
# limit = 10000
# i = 1
# sum_value = 0
# while sum_value < limit :
#     sum_value += i
#     i += 1
    
#     if sum_value > limit :
#         break
# print("{} 더할 때 {} 을 넘으며 그때의 값은 {} 이다.".format(i-1, limit, sum_value))
#
max_value = 0
a = 0
b = 0
for i in range(1, 99+1) :
    j = 100 - i
    
    max_value = i * j
    print(i, j, max_value)
    a = i
    b = j
print("최대가 되는 경우 : {} * {} = {}".format(a, b, max_value))