import math
first_name="mastewal"
last_name="degu"
full_name="mastewal degu"
country="Ethiopia"
city="addis ababa"
age=23
year=2023
is_married=False
is_true=True
is_light_on= True
hobby,favorite_movie,is_admin="movie","good will hunting",False

print(type(first_name),type(last_name),type(full_name),type(country),type(city),type(age),type(year),type(is_married),type(is_true),type(is_light_on),type(hobby),type(favorite_movie),type(is_admin))


print(len(first_name))
print(len(first_name) > len(last_name))


num_one=5
num_two=4
total= num_one +num_two
diff=num_one - num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_variable=num_one//num_two
print(total,diff,product,division,remainder,exp,floor_variable)



radius=30
area_of_circle=math.pi * (radius **2) 
circum_of_circle=2*math.pi*radius
print(area_of_circle)
print (circum_of_circle)






radius1=input("ensert the radius")
area1=math.pi * (int(radius1) ** 2)
print(area1)

First_name=input("Enter the first name")
Last_name=input("Enter the last name")
Country=input("Enter your country")
Age=input("Ente your age")
print(First_name,Last_name,Country,Age)


print(help())