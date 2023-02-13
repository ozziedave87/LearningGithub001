# function that computes the average of a list of numbers

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

#implement functuon using split list from input of user
def main():
    numbers = input("Enter a list of numbers separated by commas: ").split(",")
    numbers = [int(number) for number in numbers]
    print("The average is", average(numbers))

#call main function
if __name__ == "__main__":
    main()
