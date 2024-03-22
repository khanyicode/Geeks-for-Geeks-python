
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



    

    
    
    