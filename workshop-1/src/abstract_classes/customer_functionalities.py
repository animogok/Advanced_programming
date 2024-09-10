"""
This module works to make the abstract classes of this program
"""

from abc import ABC, abstractmethod
from typing import List


class AShowCategories(ABC):
    """
    Abstract base class for showing categories.

    This class provides an interface for opening and closing categories.
    """

    @abstractmethod
    def open_categories(self) -> List:
        """
        Opens all categories.

        Returns:
            List: A list of categories.

        Example:
            >>> categories = AShow_categories()
            >>> categories.open_categories()
            ['Category 1', 'Category 2', 'Category 3']
        """
        return List

    @abstractmethod
    def close_categories(self) -> None:
        """
        Closes all categories.

        Example:
            >>> categories = AShow_categories()
            >>> categories.close_categories()
        """
        return None


class AShoppCart(ABC):
    """
    Abstract base class for a shopping cart.

    This class provides an interface for adding and removing items from the cart.
    """

    _items = list[str]
    _total = float

    @abstractmethod
    def add_item(self, index: int, items: list) -> None:
        """
        Adds an item to the cart by index.

        Args:
            index (int): The index of the item.
            items (list): The list of items in sub-categories.

        Example:
            >>> cart = AShopp_cart()
            >>> cart.add_item(0)
        """
        return None

    @abstractmethod
    def remove_item(self, index: int) -> None:
        """
        Removes an item from the cart by index.

        Args:
            index (int): The index of the item.

        Example:
            >>> cart = AShopp_cart()
            >>> cart.remove_item(0)
        """
        return None
