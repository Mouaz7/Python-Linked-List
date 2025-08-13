class MethodNotDefinedForThisPositionError(Exception):
    pass


class List:
    """
    Array-based list implementation with a fixed maximum size.
    """

    def __init__(self):
        """
        Creates an empty list with a fixed maximum capacity.
        """
        self._MAX = 100
        self._values = [None for _ in range(self._MAX)]
        self._endpos = 0
        self._size = 0

    def insert(self, position, obj):
        """
        Inserts a new element with value `obj` before the given position.

        Args:
            position (int): Index where the new value should be inserted.
            obj: The value to insert.

        Returns:
            int: The position of the newly inserted element.
        """
        if (position < 0) or (position > self._endpos):
            raise MethodNotDefinedForThisPositionError("Error in insert")
        if not self.isempty():
            for i in range(self._endpos, position, -1):
                self._values[i] = self._values[i - 1]

        self._values[position] = obj
        self._endpos += 1
        self._size += 1
        return position

    def isempty(self):
        """
        Checks if the list is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self._endpos == 0

    def inspect(self, position):
        """
        Returns the value at the given position.

        Args:
            position (int): Index in the list.

        Returns:
            Value at the given position.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in inspect")
        return self._values[position]

    def first(self):
        """
        Returns the first position in the list.
        """
        return 0

    def end(self):
        """
        Returns the end position in the list.
        """
        return self._endpos

    def next(self, position):
        """
        Returns the position after the given position.

        Args:
            position (int): Current index.

        Returns:
            int: Next position.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in next")
        return position + 1

    def previous(self, position):
        """
        Returns the position before the given position.

        Args:
            position (int): Current index.

        Returns:
            int: Previous position.
        """
        return position - 1

    def remove(self, position):
        """
        Removes the element at the given position.

        Args:
            position (int): Index to remove.

        Returns:
            int: The position directly after the removed element.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self._endpos:
            raise MethodNotDefinedForThisPositionError("Error in remove")

        for i in range(position, self._endpos - 1):
            self._values[i] = self._values[i + 1]

        self._endpos -= 1
        self._size -= 1
        return position

    def length(self):
        """
        Returns the number of elements in the list.
        """
        return self._size
