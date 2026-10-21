import logging
logger = logging.getLogger(__name__)

from sum_brincation import check_errors, pass_or_fail

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
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


if __name__ == "__main__":
    main()
