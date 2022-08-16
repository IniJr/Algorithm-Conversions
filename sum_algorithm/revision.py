#task1

#list=[5,2,3,1,5,67,89,4,5,34,21,3,45,55,2,44,55,6]
#print(len(list))

#understandingloops
#get input from the user. prompt them to input a multiple of 7. if it's not a multiple of 7, they have to input again, until it is, then they get "yes"
#value = int(input("enter a multiple of 7: "))

#while value % 7 !=0:
#    value = int(input("enter a multiple of 7: "))
#else:
#   print ("correct , that is a multiple of 7")

nums=[1,2,3,4,5,6,7,8,9,10,11]

sum=0
for i in nums:
    sum=sum + i
    if i==nums[len(nums)-1]:
        print(sum)



#for num in nums:
#   for letter in 'abc':
#       print(num,letter)

