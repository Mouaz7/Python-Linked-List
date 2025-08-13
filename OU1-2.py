"""
Reads floats from a file, sorts them using merge sort, and prints the result.
"""

from ListAsArray import List


def read_file(filename: str, lst: List) -> None:
    """
    Reads float values from a file and inserts them into the given list.

    Args:
        filename (str): Path to the file containing numbers.
        lst (List): Custom List object where numbers will be stored.
    """
    with open(filename) as f:
        for line in f:
            try:
                lst.insert(lst.end(), float(line))
            except ValueError:
                print("Skipping invalid value:", line.strip())


def print_list(lst: List) -> None:
    """
    Prints all values from the given list in order.

    Args:
        lst (List): Custom List object to print.
    """
    p = lst.first()
    while p != lst.end():
        print(lst.inspect(p))
        p = lst.next(p)


# Comparison functions
ascending = lambda a, b: a < b
descending = lambda a, b: a > b


def split_list(src: List) -> tuple[List, List]:
    """
    Splits the given list into two halves without using Python's built-in lists.

    Args:
        src (List): The source list.

    Returns:
        tuple[List, List]: Two lists containing the first and second half.
    """
    left, right = List(), List()
    slow = fast = src.first()

    while fast != src.end() and src.next(fast) != src.end():
        slow = src.next(slow)
        fast = src.next(src.next(fast))

    p = slow
    while p != src.end():
        right.insert(right.end(), src.inspect(p))
        p = src.next(p)

    p = src.first()
    while p != slow:
        left.insert(left.end(), src.inspect(p))
        p = src.next(p)

    return left, right


def merge_lists(a: List, b: List, cmp) -> List:
    """
    Merges two sorted lists into a new sorted list.

    Args:
        a (List): First sorted list.
        b (List): Second sorted list.
        cmp (callable): Comparison function.

    Returns:
        List: New sorted list.
    """
    result = List()
    pa, pb = a.first(), b.first()

    while pa != a.end() or pb != b.end():
        take_a = pb == b.end() or (pa != a.end() and cmp(a.inspect(pa), b.inspect(pb)))
        src, p = (a, pa) if take_a else (b, pb)
        result.insert(result.end(), src.inspect(p))

        if take_a:
            pa = a.next(pa)
        else:
            pb = b.next(pb)

    return result


def merge_sort_list(lst: List, cmp) -> List:
    """
    Sorts the list using merge sort.

    Args:
        lst (List): The list to sort.
        cmp (callable): Comparison function.

    Returns:
        List: New sorted list.
    """
    if lst.first() == lst.end() or lst.next(lst.first()) == lst.end():
        return lst
    left, right = split_list(lst)
    return merge_lists(merge_sort_list(left, cmp), merge_sort_list(right, cmp), cmp)


def menu() -> None:
    """Displays the menu and processes user input."""
    lst = List()
    read_file(input("Enter file name: "), lst)

    while True:
        print("\nMenu")
        print("1) Sort Ascending")
        print("2) Sort Descending")
        print("3) Exit")
        choice = input("Choice: ")

        if choice == "1":
            lst = merge_sort_list(lst, ascending)
            print_list(lst)
        elif choice == "2":
            lst = merge_sort_list(lst, descending)
            print_list(lst)
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
