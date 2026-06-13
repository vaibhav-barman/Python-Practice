# F - Strings

first_name = 'vaibhav'
last_name = 'barman'
sentence = f'My name is {first_name.capitalize()} {last_name.upper()}'
print(sentence)


person = {'name': 'Jenn', 'age': 23}
sentence = f'My name is {person['name'].upper()} and I am {person['age']} years old.'
print(sentence)


calculation = f'4 times 11 is equal to {4*11}'
print(calculation)


for n in range(1,11):
    sentence = f'The value is {n:04}' # 0 pad by 4 digits
    print(sentence)


pi = 3.14159265
sentence = f'Pi is equal to {pi:.5f}' # Precision of 5 digits after decimal
print(sentence)


from datetime import datetime
birthday = datetime(1990,1,1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}' 
print(sentence) # Output: Jenn has a birthday on January 01, 1990
# Before Formatting Output: Jenn has a birthday on 1990-01-01 00:00:00