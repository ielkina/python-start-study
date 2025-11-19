num_1 = 100
num_2 = 10

num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)

num_1 = 7
num_2 = 2
# / - ділення 
# // - скільки цілих разів входить одне число в інше
num_3 = num_1 / num_2
num_4 = num_1 // num_2
print(num_3, num_4)

num_1 = 5
num_2 = 2

# ** - піднесення до степеня например  2*2=4, 4*2=8, 8*2=16, 16*2=32 2 в 5 степени 2 біла умнодена сама на себя 5 раз 
num_3 = num_2 ** num_1
print(num_3)

num_1 = 7
num_2 = 2
# % - залишок від відення  7 / 2 равно 3 и 1 в остатке 
num_3 = num_1 % num_2
print(num_3)

num_1 = 10
num_2 = 3

num_3 = num_1 % num_2
print(num_3)

# булевое значение true или false 
num_1 = 10
num_2 = 5

num_3 = num_1 == num_2
print(num_3)

num_3 = num_1 != num_2
print(num_3)

num_3 = num_1 < num_2
print(num_3)

num_3 = num_1 > num_2
print(num_3)



num = 10
name = "Tom"
# and = два операнта дорівнюють друг другу тому true
result = num > 5 and name == "Tom"
print(result) # true 

# or - один з оперантів дорівнює ture тому true 
result = num < 5 or name == "Tom"
print(result)

result = num < 5 and name == "Tom"
print(result)

# перемення name in есть в переменной message 
# перемення name not in нет в переменной message 
message = "Tom get some money"
print(name in message)
print(name not in message)

name = "John"
message = "You won!"
print(name in message)
print(name not in message)

age = 50
name = "Ira"
animal = "Cat"

print(age == 50 and "Ira" in name and animal != "dog")
print(age == 50 and "I" in name or animal == "dog")
print(age == 50 and "F" in name and animal != "dog")
