import math

highest = -math.inf
lowest = math.inf

while True:
        user_input = input("Enter a number (or 'exit' to stop): ")

        if user_input.lower() == 'exit':
            break
          
            number = float(user_input)
            if number > highest:
                highest = number
            if number < lowest:
                lowest = number

          

print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
