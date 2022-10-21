#list []===> array in other programming language
#tuple ()
#dictionary {} json
#set

#list မှာဆိုရင် data တွေအကုန်ထည့်လို့ရ
#List methods
#List ထဲကို data ထည့်ချင်ရင်
#1.append
#2.extend
#3.insert

my_list = [12,4,5,6]
# my_list.append(9)
# my_list.extend([6,7,8,89,9])
my_list.append([8,9,10])
print(my_list[4][1])

name_list = []
name_list.append("NCC")
print(name_list)

#ဖြတ်ထည့်ချင်ရင် insert ကိုသုံးတယ်
numbers_list = [11,222,333,444]
numbers_list.insert(1,"NCC")
print(numbers_list)
