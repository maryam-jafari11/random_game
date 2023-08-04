import random

pc_num = random.randint(0, 20)
count = 1
for i in range(10):
    user_num = int(input("enter your number: "))
   
    if pc_num == user_num and count == 1:
        print("congratulation!! you have  new chance!! ")
        pc_num2 = random.randint(0, 20)
        user_num2 = int(input("enter new number: "))
    if pc_num == user_num and count != 1:
        print("congratulation!! ")
        print(count , "time attempt! ")
        break

    if pc_num > user_num :
        print("boro balatar!! ")
        count+=1
        
    if pc_num < user_num :
        print("boro paeentar!! ")
        count+=1
        
