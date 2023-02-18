def change_cases(word:str)->str:
    word_cases_swapped = ''
    for letter in word:
        word_cases_swapped += letter.swapcase()
    print(word_cases_swapped)
    
    
change_cases("aBcD")


def my_function(a:int, b:str)->int:
    return a + ord(b)


print(my_function(3, 'a'))
print(my_function(3, '5'))

def test(a:str, b:str)->str:
    print(type(a))
    
    print("hello world")
    print(a+b)
    return a + b 
    
test(5, 6)