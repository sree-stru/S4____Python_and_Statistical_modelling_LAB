def read_numbers_file(file_name):
    numbers = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                numbers.extend(map(int, line.split()))
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
    except ValueError:
        print(f"File '{file_name}' contains non-numeric values.")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {e}")
    return numbers

def merge_and_sort_files(file_list, output_filename):
    all_numbers = []
    for file_name in file_list:
        numbers = read_numbers_file(file_name)
        all_numbers.extend(numbers)
    all_numbers.sort()
    try:
        with open(output_filename, 'w') as file:
            file.write('\n'.join(map(str, all_numbers)))
        print(f"Sorted numbers have been written to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to '{output_filename}': {e}")

file_list = ['file1.txt', 'file2.txt', 'file3.txt']
output_filename = 'sorted_numbers.txt'

merge_and_sort_files(file_list, output_filename)
