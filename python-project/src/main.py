def write_numbers_to_files():
    odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
    even_numbers = [num for num in range(1, 101) if num % 2 == 0]

    with open('odd.txt', 'w') as odd_file:
        for number in odd_numbers:
            odd_file.write(f"{number}\n")

    with open('even.txt', 'w') as even_file:
        for number in even_numbers:
            even_file.write(f"{number}\n")

if __name__ == "__main__":
    write_numbers_to_files()