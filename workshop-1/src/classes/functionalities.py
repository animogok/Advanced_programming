"""
This module will make the actual user classes of the program
"""

from ..abstract_classes import customer_functionalities as cf

CATEGORIES = [
    "Mobile Devices",
    "Home Appliances",
    "Computers",
    "Audio & Accessories",
    "Entertainment & Gaming",
]

SUB_CATEGORIES = {
    0: ["Dataphones", "Phones", "Smartwatches"],
    1: [
        "Washing Machines",
        "Microwaves",
        "Clothes Irons",
        "Pressure Cookers",
        "Air Fryers",
        "Blenders",
    ],
    2: ["PCs", "Laptops"],
    3: ["Headphones"],
    4: ["TVs", "Xbox Series X", "PlayStation 5 (PS5)"],
}


class ShowCategories(cf.AShowCategories):
    """
    A class to handle category-related functionality.

    Attributes:
        None

    Methods:
        open_categories()
        close_categories()
        open_sub_categories(index)
    """

    def open_categories(self) -> cf.List:
        """
        Returns a list of all categories.

        Returns:
            cf.List: A list of categories.

        Example:
            >>> show_categories = ShowCategories()
            >>> categories = show_categories.open_categories()
            >>> print(categories)
            ['Mobile Devices', 'Home Appliances', 'Computers', 'Audio & Accessories', 'Entertainment & Gaming']
        """
        return cf.List(CATEGORIES)

    def close_categories(self) -> None:
        """
        Closes the categories.

        Returns:
            None
        """
        return super().close_categories()

    def open_sub_categories(self, index: int) -> list:
        """
        Returns a list of sub-categories for a given category index.

        Args:
            index (int): The index of the category.

        Returns:
            list: A list of sub-categories.

        Example:
            >>> show_categories = ShowCategories()
            >>> sub_categories = show_categories.open_sub_categories(0)
            >>> print(sub_categories)
            ['Dataphones', 'Phones', 'Smartwatches']
        """
        return SUB_CATEGORIES.get(index)


class ShoppCart(cf.AShoppCart):
    """
    A class to handle shopping cart-related functionality.

    Attributes:
        _total (int): The total cost of items in the cart.
        _items (list): A list of items in the cart.

    Methods:
        __init__()
        add_item(index, items)
        remove_item(index)
    """

    def __init__(self) -> None:
        """
        Initializes the shopping cart.

        Returns:
            None
        """
        self._total = 0
        self._items = []
        super().__init__()

    def add_item(self, index: int, items: list) -> None:
        """
        Adds an item to the shopping cart.

        Args:
            index (int): The index of the item to add.
            items (list): A list of items to choose from.

        Returns:
            None

        Example:
            >>> shopping_cart = ShoppCart()
            >>> items = ["Item 1", "Item 2", "Item 3"]
            >>> shopping_cart.add_item(0, items)
            >>> print(shopping_cart._items)
            ['Item 1']
        """
        self._items.append(items.pop(index))
        return super().add_item(index, items)

    def remove_item(self, index: int) -> None:
        """
        Removes an item from the shopping cart.

        Args:
            index (int): The index of the item to remove.

        Returns:
            None

        Example:
            >>> shopping_cart = ShoppCart()
            >>> shopping_cart._items = ["Item 1", "Item 2", "Item 3"]
            >>> shopping_cart.remove_item(0)
            >>> print(shopping_cart._items)
            ['Item 2', 'Item 3']
        """
        self._items.pop(index)
        return super().remove_item(index)
