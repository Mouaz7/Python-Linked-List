"""
Reads float values from a file, stores them in a list, and prints them.
"""

from ListAsArray import List
# from ListAsTwoCell import List

def read_file(file_path, lst):
    """
    Reads float values from the given file and stores them in the list.

    Args:
        file_path (str): Path to the file.
        lst (List): List object where the numbers will be stored.
    """
    with open(file_path, "r") as f:
        for line in f:
            num = float(line.strip())
            lst.insert(lst.end(), num)

def print_values(lst):
    """
    Prints all values from the list in order.

    Args:
        lst (List): List object containing the values.
    """
    p = lst.first()
    while p != lst.end():
        print(lst.inspect(p))
        p = lst.next(p)

def main():
    """
    Main function to read file and print its contents.
    """
    data = List()
    file_path = input("Enter file name: ")
    read_file(file_path, data)
    print("\nList contents:")
    print_values(data)

if __name__ == "__main__":
    main()
