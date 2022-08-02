import string
import random

##User
user_name = str(input("What is your name?: \n"))

## Number of Instance
num_of_instance = int(input("How many EC2 instance do you want names for?: "))
print("The number of instance I want is " + str(num_of_instance))


##Department
department = str(input("What Department do you work for, " + user_name + "?\n"))

dept_list = ["Accounting", "Marketing", "FinOps"]

if department in dept_list:
    print("The name of the department is " + department + ",")
else:
    print("Error!!! Department not supported")



k = 3 
for _ in range(num_of_instance):
    instance_name = str(''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for num_of_instance in range(7)]))
    print('{}-{}'.format(department[0 : k], instance_name))



