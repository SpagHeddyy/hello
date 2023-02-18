# my_name = "giorgi"
# my_surname = "bijamovi"
# my_age = 24
# my_homework = "chemi saxeli {1} chemi gvari {2} chemi asaki {0}" .format (my_age,my_name,my_surname)
# print(my_homework)
# if "e" in my_name:
#     print("sheicavs e-s")
# else:
#     print("ar shecavs e-s")
# my_name = input("enter your name: ")
# print("chemi saxelia " + my_name )    

# my_name = "giorgi"
# my_surname = "bijamovi"
# my_age = 24 

# my_name = input("enter your name: ")
# my_surname = input("enter your surname: ")
# my_age = input("enter your age: ")
# my_age2 = int(my_age) + 3
 
# print("chemi saxelia {} chem gvari {} chemi asaki {} sami wlis shemdeg me gavxebi {} ".format(my_name,my_surname,my_age,my_age2))


first = int(input("enter first: "))
second = int(input("enter second: "))
third = int(input("enter third: "))
number = 0
if first % 2 == 1:  #39 
    number += first
if second % 2 == 1:   #40
    number += second        #1
if third % 2 == 1:
    number += third 
print("the total sum of the number is {}".format(number) )          