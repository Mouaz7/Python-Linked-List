# OU1 List Sorting Project

This project demonstrates two custom list implementations (`ListAsArray` and `ListAsTwoCell`) and how they can be used to store, print, and sort floating-point numbers read from a file.  
The sorting algorithm implemented is **Merge Sort**, adapted to work without Python's built-in list type.

## Project Structure

```
.
├── data.txt               # Example input data
├── ListAsArray.py         # Array-based list implementation
├── ListAsTwoCell.py       # Doubly linked list implementation
├── TwoCell.py             # Node structure for ListAsTwoCell
├── OU1-1.py               # Reads floats from file and prints them
├── OU1-2.py               # Reads floats, sorts them, and prints result
```

## Features

- **Two list implementations**
  - `ListAsArray`: Fixed-size array-based list.
  - `ListAsTwoCell`: Doubly linked list using a `TwoCell` node structure.
- **Merge Sort** implementation that works with both list types.
- **Menu-based interface** in `OU1-2.py` for sorting ascending or descending.
- File reading with error handling for invalid lines (in `OU1-2.py`).

## Requirements

- Python 3.x
- No external libraries are required.

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Prepare an input file**  
   The file should contain one floating-point number per line.  
   Example (`data.txt`):
   ```
   3.14
   2.71
   1.0
   4.2
   ```

3. **Run OU1-1.py (Print list contents)**
   ```bash
   python OU1-1.py
   ```
   - Enter the file name (e.g., `data.txt`).
   - The program will print the numbers in the order they appear in the file.

4. **Run OU1-2.py (Sort and print)**
   ```bash
   python OU1-2.py
   ```
   - Enter the file name (e.g., `data.txt`).
   - Choose:
     - `1` to sort ascending
     - `2` to sort descending
     - `3` to exit

## Switching List Implementations

By default, the programs use `ListAsArray`.  
To use `ListAsTwoCell` instead:
- In `OU1-1.py` and `OU1-2.py`, comment out:
  ```python
  from ListAsArray import List
  ```
  and uncomment:
  ```python
  from ListAsTwoCell import List
  ```

## Example Output

### Ascending sort
```
Menu
1) Sort Ascending
2) Sort Descending
3) Exit
Choice: 1
0.5
1.0
2.0
2.71
3.14
4.2
5.5
6.28
7.3
8.88
9.81
```

### Descending sort
```
Menu
1) Sort Ascending
2) Sort Descending
3) Exit
Choice: 2
9.81
8.88
7.3
6.28
5.5
4.2
3.14
2.71
2.0
1.0
0.5
```

## License

This project is provided for educational purposes and does not include any specific license terms.
