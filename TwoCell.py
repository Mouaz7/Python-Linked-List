class TwoCell:
    """
    A simple node with a value and two links: prev and next.
    Useful for doubly linked list implementations.
    """

    def __init__(self):
        """
        Create a new cell with undefined value and links.
        """
        self._data = None
        self._prev = None
        self._next = None

    def setValue(self, data):
        """
        Set the cell's value.
        """
        self._data = data

    def setPrev(self, link):
        """
        Set the previous link.
        """
        self._prev = link

    def setNext(self, link):
        """
        Set the next link.
        """
        self._next = link

    def inspectValue(self):
        """
        Return the cell's value.
        """
        return self._data

    def inspectPrev(self):
        """
        Return the previous link.
        """
        return self._prev

    def inspectNext(self):
        """
        Return the next link.
        """
        return self._next
