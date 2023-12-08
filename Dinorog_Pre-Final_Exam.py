def get_prime_number(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 1:
                return user_input

            elif user_input == 0:
                print("> [Program Terminated]")
                return None

            else:
                print("> [Invalid input. Please enter a \"Non-Negative Number\"]")

        except ValueError:
            print("> [Error 404. Please enter a \"Number\"]")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start_num, end_num):
    if endNum <= startNum:
        print(f"> [Enter a number greater than {start_num}]")
        return

    print(f"Prime numbers between {startNum} and {end_num}:")
    for num in range(startNum, endNum + 1):
        if is_prime(num):
            print(num, end=" ")
    print()


print("CS112: Computer Programming 1 - PRE-FINAL EXAM")
print("Created by: Artjohn Clark E. Dinorog")

print("\nProblem: Create a python program that displays all prime numbers within a range.")

print("\nRULES TO CONSIDER: "
      "\n[1] if number[start] is a negative number. The program will prompt a message: "
      "\"Enter a non-negative number\""
      "\n[2] if number[end] is less than number[start]. The program will prompt a message: "
      "\"Enter a number greater than number[start]\""
      "\n[3] if the user enter the number \"0\", the program will terminate. ")

while True:
    startNum = get_prime_number("\n> Enter a number [start]: ")

    if startNum is None:
        break

    endNum = get_prime_number("> Enter a number [end]: ")

    display_primes(startNum, endNum)
