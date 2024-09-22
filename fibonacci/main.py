def fibonacci_iterative(number:int) -> None:
    prev = 0
    pos = 1
    for _ in range(2,number):
       f = pos + prev 
       prev = pos 
       pos = f 
       print(f)

def fibonacci_recursive(number:int) -> int: 
    if number < 2: return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)
    



if __name__ == "__main__":
   fibonacci_recursive(8)
   print("*****************************")
   fibonacci_iterative(8)
    