
def palindrom():
    word = "racecar"
    if word == word[::-1]:
        print(word,"is palindrom")
        
    else:
        print(word," is not plaindrom")
    
palindrom()


def symmetrical():
    
    word="khokho"
    
    midpoint_of_word= int(len(word)/2)
    first_half=word[:midpoint_of_word]
    second_half=word[midpoint_of_word:]
    
    if first_half==second_half:
        print(word,"is symmetrical")
        
    else:
        print(word,"is not symmetrical")
        
symmetrical()

 
def vowel_count(str):
    
    vowels= " aeiou"
    
    count = 0
    
    for i in  str:
        if i in vowels:
            count = count +1
            
    print("vowels found are ", count)
    
            
str= "sindy"
vowel_count(str)


def find_number_of_even_numbers(numbers):
    """Find the number of even numbers in a list of numbers"""
    
    count = 0
    
    for num in numbers:
        if num % 2 == 0:
            count += 1
            
    print(count)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_number_of_even_numbers(number_list)


def remove_duplicates():
    word=["a","t","e","g","a","n","g"]
    new=set(word)
    print(new)
    
remove_duplicates()
    
    
def find_average(numbers):
   tot=sum(numbers)/len(numbers)
   print(tot)
   
numbers_list=[1,2,3,4,5,6]
find_average(numbers_list)


def find_even_numbers(numbers):
    even_numbers = []
    
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
            
    return even_numbers

number_list = [2, 3, 4, 5, 6]
even_numbers_list = find_even_numbers(number_list)
print(even_numbers_list)


def string_length():
 string = "midrand"
 print(len(string))
 
string_length()


def string_length(str):
    count =0
    
    for i in str:
        count +=1
    return count

str = "midrand"

new_string = string_length(str)
print(new_string)
    
    
def uppercase_half_string():
    string= "midrand"
    
    midpoint= int(len(string))//2
    
    result = string[:midpoint] + string[midpoint:].upper()
    print(result)
    
uppercase_half_string()
    
def reverse_string():
    string = "khanyisile"
    
    new_string = string[::-1]
    print(new_string)
    
reverse_string()

def checkString(str):
    flag_digit = False
    flag__letter = False
    
    for i in str:
        if i.isdigit():
            flag_digit = True
            
            
        if i.isalpha():
            flag__letter = True
            
    return flag__letter and flag_digit

something = "this2shallpass"
the_check= print(checkString(something))
