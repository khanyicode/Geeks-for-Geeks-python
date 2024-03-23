
def even_number():
    numbers = [2,3,4,5,6,7,8]
    new_number = []
    for i in numbers:
        if i %2 == 0:
            new_number.append(i)
    print(new_number)
            
even_number()


def odd_number(numbers):
  
    new_num = []
    
    for i in numbers:
        if i % 3 ==0:
            new_num.append(i)
            
    return new_num

numbers = [1,2,3,4,5,6,7,8,9]
odd_list = odd_number(numbers)
print(odd_list)


def leap_year():
    year = int("2024")
    
    if year%4==0:
        print("it is a leap year")
        
    else:
        print(" it is not a leap year ")
        
leap_year()


def voting():
    age = int(18)
    
    if age >= 18:
        print( "you are eligible to vote")
        
    elif age<=18:
        print(" you are not eligible to vote")
        
    else:
        print("check if you are eligible")
        
voting()

def traffic_light():
    colour=input("enter colour of light:")
    if(colour=="green"):
        print("GO")
    elif(colour=="yellow"):
        print("GET READY")
    else:
        print("STOP")
    

traffic_light()


def  total():
    numbers = [1,2,3,4,5]
    tot = sum(numbers)
    print(tot)
    
total()
    
    
def addition(x,y):
    
    tot= (x+y)
    return(tot)

print(addition(3,3))

        
        
        