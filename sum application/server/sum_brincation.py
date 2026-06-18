import logging
logger = logging.getLogger(__name__)

# This is a sum of scores from a student. If the student scores more than 10, they pass. 
# If they score between 7 and 9 they receive another chance.
# If they score below 7 they fail.

# Functions

def check_errors(numbers):
    for number in numbers:
        if not number.isdigit():
            print("Burro do caralho, coloca um número")
            exit() 

def pass_or_fail (score):
    if score >= 10:
        return "Congratulations, you passed! 🚀"
    if score < 7:
        return "You suck 🤡"
    else:
        return "You'll get another chance"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Execution

input_receiver = input("Enter a sequence of numbers, separated by commas: ")

numbers = input_receiver.split(",")

check_errors(numbers)

numbers = [int(number) for number in numbers]

# total = sum(numbers)

for number in numbers:
    print(type(number))

sum_numbers = 0
for number in numbers:
    sum_numbers += number

score = sum_numbers

logger.debug(number)

logger.debug(numbers)

logger.debug(type(numbers))

print(pass_or_fail(score))








