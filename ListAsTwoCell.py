class MethodNotDefinedForThisPositionError(Exception):
    pass

from TwoCell import TwoCell

class List:
    """
    Doubly linked list implementation using a TwoCell structure.
    """

    def __init__(self):
        """
        Creates an empty list with a head TwoCell.
        """
        self._head = TwoCell()
        self._head.setPrev(self._head)
        self._head.setNext(self._head)

    def insert(self, position, obj):
        """
        Inserts a new element with value `obj` before the given position.

        Args:
            position (TwoCell): The node before which the new element will be inserted.
            obj: The value to insert.

        Returns:
            TwoCell: The newly inserted node.
        """
        newCell = TwoCell()
        newCell.setValue(obj)

        if self.isempty():
            newCell.setPrev(self._head)
            newCell.setNext(self._head)
            self._head.setPrev(newCell)
            self._head.setNext(newCell)
        else:
            newCell.setPrev(position.inspectPrev())
            newCell.setNext(position)
            position.setPrev(newCell)
            newCell.inspectPrev().setNext(newCell)

        return newCell

    def isempty(self):
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return (self._head.inspectPrev() == self._head) and (self._head.inspectNext() == self._head)

    def inspect(self, position):
        """
        Returns the value at the given position.

        Args:
            position (TwoCell): The node to inspect.

        Returns:
            The value stored at the given position.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self.end():
            raise MethodNotDefinedForThisPositionError("Error in inspect")
        return position.inspectValue()

    def first(self):
        """
        Returns the first node in the list.
        """
        return self._head.inspectNext()

    def end(self):
        """
        Returns the end (head) node of the list.
        """
        return self._head

    def next(self, position):
        """
        Returns the node after the given position.

        Args:
            position (TwoCell): Current node.

        Returns:
            TwoCell: Next node.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self.end():
            raise MethodNotDefinedForThisPositionError("Error in next")
        return position.inspectNext()

    def previous(self, position):
        """
        Returns the node before the given position.

        Args:
            position (TwoCell): Current node.

        Returns:
            TwoCell: Previous node.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the first node.
        """
        if position == self.first():
            raise MethodNotDefinedForThisPositionError("Error in previous")
        return position.inspectPrev()

    def remove(self, position):
        """
        Removes the node at the given position.

        Args:
            position (TwoCell): The node to remove.

        Returns:
            TwoCell: The node after the removed node.

        Raises:
            MethodNotDefinedForThisPositionError: If position is the end position.
        """
        if position == self.end():
            raise MethodNotDefinedForThisPositionError("Error in remove")

        position.inspectPrev().setNext(position.inspectNext())
        position.inspectNext().setPrev(position.inspectPrev())

        return position.inspectNext()
