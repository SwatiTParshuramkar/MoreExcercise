# def Student_Budget(name1,budget):
#         if student_budget < 50000:
#             print(name1,"ka Budget ke hisaab se hai")
#         else :
#             print(name1,"ka Budget ke bahr hai")
    
# student_name=input("Enter the stuent name")
# student_budget= int(input("Enter the one student of budget"))

# Student_Budget(student_name,student_budget) 

def Student_Budget(num1):
        i=0
        count=0
        count1=0
        budget1=0
        while i < num:
            student_name = input("Enter the name")
            student_budget=int(input("Enter the Student_budget"))

            if student_budget < 50000:
                count+=1
                budget1+=student_budget
            else :
                count1+=1
                # print(count1,"Invalid Student")
            i+=1
        print(count, budget1,"total of student of navgurukul")
        print(count1)
        
num=int(input("Enter the Student of number"))


Student_Budget(num)