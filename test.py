choice="\'생활비지원'"
choice1="\'%대학생%'"
# print(choice)
# choice1 = '생활비지원'
# print(choice1)
# if(choice ==choice1):
#     print('1')
# choice2 = "\'생활비지원'"
# print(choice2)
# choice='생활비지원'
#     result= engine.execute("SELECT name FROM dreamspon WHERE advantage LIKE '{}' ".format(choice))

print("SELECT name FROM dreamspon WHERE advantage LIKE {0} ADN who LIKE {1}".format(choice,choice1))
print("select name from dreamspon where advantage like '%학비지원%'")

hello = "hello7"
hell1 ="\'"+ hello + "\'"
print(hell1)