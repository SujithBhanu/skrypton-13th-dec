list1 = ["", "", ""]
list2 = ["", "", ""]
list3 = ["", "", ""]
index_list = ["a", "b", "c"]
final_list = [list1, list2, list3]

user_input = input("where to? ")
word = input("string: ")
final_list[int(user_input[-1])-1][index_list.index(user_input[0])]=word
print(f"{list1}\n{list2}\n{list3}")



# if user_input[-1] == '1':
#     if user_input[0] == 'a':
#         final_list[0][0] = word
#     elif user_input[0] == 'b':
#         final_list[0][1] = word
#     elif user_input[0] == 'c':
#         final_list[0][2] = word
# if user_input[-1] == '2':
#     if user_input[0] == 'a':
#         final_list[1][0] = word
#     elif user_input[0] == 'b':
#         final_list[1][1] = word
#     elif user_input[0] == 'c':
#         final_list[1][2] = word
# if user_input[-1] == '3':
#     if user_input[0] == 'a':
#         final_list[2][0] = word
#     elif user_input[0] == 'b':
#         final_list[2][1] = word
#     elif user_input[0] == 'c':
#         final_list[2][2] = word
