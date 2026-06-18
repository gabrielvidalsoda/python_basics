import logging
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

check_errors(numbers)

# Execution

input_receiver = input("Enter a sequence of numbers, separated by commas: ")

numbers = input_receiver.split(",")

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








