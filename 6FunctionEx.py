#function exercise
#return day
#"Sunday"
#find largest element

# def return_day(num):
#     if num == 1:
#         return "Sunday"
#     elif num == 2:
#         return "Monday"
#     else:
#         return "Invalid Number"

# print(return_day(1))

def return_day(num):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday"
    ,"Friday","Saturday"]
    if num>0 and num<8:
        return days[num-1]
    else:
        return "Invalid Number"


print(return_day(7))
