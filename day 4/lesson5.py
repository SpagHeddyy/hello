# name = "giorgi"
# for gio in name:
#     print(gio)
# n = input("click to check: ")
# n2 = input("click to check2: ")
# ammount_of_vowels_in_n = 0
# ammount_of_vowels_in_n2 = 0
# #giorgi
# for char in n:
#     if char in "aeiou":
#         ammount_of_vowels_in_n += 1
# #aleksandre        
# for char in n2:
#     if char in "aeiou":
#         ammount_of_vowels_in_n2 += 1  
# if   ammount_of_vowels_in_n > ammount_of_vowels_in_n2:
#     print("the ammount of volwes in n is more and it contains {} vowels".format(ammount_of_vowels_in_n))
__name__ = input("enter _name_: ")
ammount_of_a = 0
for char in __name__:
    if char == "a":
        ammount_of_a += 1
print("there is {} 'a' in my text".format(ammount_of_a))        