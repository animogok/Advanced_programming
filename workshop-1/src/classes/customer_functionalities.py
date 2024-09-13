"""
This module works to make the abstract classes of this program

Simple ElectronicDevice Shopping System
Copyright (C) 13/09/2024  Sebastian Avendaño Rodriguez - sebastian.avenda43@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Source: http://opensource.org/licenses/GPL-3.0
"""

from abc import ABC, abstractmethod


class AShowCategories(ABC):
    """
    Abstract base class for showing categories.

    This class provides an interface for opening and closing categories.
    """

    @abstractmethod
    def open_categories(self) -> list:
        """
        Opens all categories.

        Returns:
            List: A list of categories.

        Example:
            >>> categories = AShowCategories()
            >>> categories.open_categories()
            ['Mobile Devices', 'Home Appliances', 'Computers', 'Audio & Accessories', 'Entertainment & Gaming']
        """
        return


class AShoppCart(ABC):
    """
    Abstract base class for a shopping cart.

    This class provides an interface for adding and removing items from the cart.
    """

    @abstractmethod
    def add_item(self, item: str) -> None:
        """
        Adds an item to the cart by index.

        Args:
            item (str): The item from the catalog

        Example:
            >>> cart = AShoppCart()
            >>> cart.add_item("item : price")
        """
        return None

    @abstractmethod
    def remove_item(self, index: int) -> None:
        """
        Removes an item from the cart by index.

        Args:
            index (int): The index of the item.

        Example:
            >>> cart = AShoppCart()
            >>> cart.remove_item(0)
        """
        return None


# =========================================== CONCRETE CLASSES =====================================

CATEGORIES = [
    "Mobile Devices",
    "Home Appliances",
    "Computers",
    "Audio & Accessories",
    "Entertainment & Gaming",
]

SUB_CATEGORIES = {
    0: ["Dataphones : 60", "Phones : 525.99"],
    1: [
        "Washing Machines : 247.74",
        "Microwaves : 75.67",
        "Clothes Irons : 25",
        "Pressure Cookers : 79.25",
        "Air Fryers : 90",
        "Blenders : 45",
    ],
    2: ["PCs : 500", "Laptops : 450"],
    3: ["Headphones : 100"],
    4: ["TVs : 1000", "Xbox Series X : 474", "PlayStation 5 (PS5) : 500"],
}


class ShowCategories(AShowCategories):
    """
    A class to handle category-related functionality.

    Attributes:
        categories =  CATEGORIES
        sub_categories = SUB_CATEGORIES

    Methods:
        open_categories()
        close_categories()
        open_sub_categories(index)
    """

    def __init__(self) -> None:
        """
        Initializes the ShowCategories class.
        """
        self.categories = CATEGORIES
        self.sub_categories = SUB_CATEGORIES
        super().__init__()

    def open_categories(self) -> list:
        """
        Returns a list of all categories.

        Returns:
            list: A list of categories.

        Example:
            >>> show_categories = ShowCategories()
            >>> categories = show_categories.open_categories()
            >>> print(categories)
            ['Mobile Devices', 'Home Appliances', 'Computers', 'Audio & Accessories', 'Entertainment & Gaming']
        """
        return self.categories

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
            ['Dataphones : 60', 'Phones : 525.99']
        """
        return SUB_CATEGORIES.get(index)

    def show_all(self) -> dict:
        """
        Returns all the catalog

        Returns:
            dict: A dictionary representating all the catalog

        Example:
            >>> show_categories = ShowCategories()
            >>> catalog = show_categories.show_all()
            >>> print(catalog)
            {"Mobile Devices": ["Dataphones : 60", "Phones : 525.99"],
             "Home Appliances": [...],
             ...}
        """
        new_sub_cat = {}
        for index, category in enumerate(CATEGORIES):
            new_sub_cat[category] = SUB_CATEGORIES[index]
        return new_sub_cat


class ShoppCart(AShoppCart):
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
        Initializes the ShoppCart class.
        """
        self.user_items = []
        self.user_total = []
        super().__init__()

    def add_item(self, item: str) -> None:
        """
        Adds an item to the shopping cart.

        Args:
            item (str): The item from the catalog

        Returns:
            None

        Example:
            >>> shopping_cart = ShoppCart()
            >>> shopping_cart.add_item("Dataphones : 60")
            >>> print(shopping_cart.user_items)
            ['Dataphones']
            >>> print(shopping_cart.user_total)
            [60.0]
        """
        item = item.split(" : ")
        self.user_items.append(item[0])
        self.user_total.append(float(item[-1]))

        return None

    def remove_item(self, index: int) -> None:
        """
        Removes an item from the shopping cart.

        Args:
            index (int): The index of the item to remove.

        Returns:
            None

        Example:
            >>> shopping_cart = ShoppCart()
            >>> shopping_cart.add_item("Dataphones : 60")
            >>> shopping_cart.remove_item(0)
            >>> print(shopping_cart.user_items)
            []
            >>> print(shopping_cart.user_total)
            []
        """
        self.user_items.pop((index - 1))
        self.user_total.pop((index - 1))
        return None


class Reviews:
    """
    A class that handles the submiting and reading of a review file

    Methods:
        submit_review() -> None
        read_review() -> str
    """

    def submit_review(self, item: str, index: list) -> None:
        """
        Submits a review for an item.

        Args:
            item (str): The item being reviewed.
            index (list): The index of the item.

        Returns:
            None

        Example:
            >>> reviews = Reviews()
            >>> reviews.submit_review("Great product!", ["Dataphones"])
        """
        review = {"item": index, "Review": f"{item}"}
        try:
            with open(
                r"Advanced_programming\workshop-1\docs\user_reviews.txt",
                "a",
                encoding="utf8",
            ) as file:
                file.write(f"{review['item']} : {review['Review']}\n")
                file.close()
        except (IOError, FileNotFoundError) as e:
            print(f"An error occurred: {e}")
            return None

    def read_review(self) -> str:
        """
        Reads all reviews from the file.

        Returns:
            str: all the reviews that were wrote into user_reviews.txt
        """
        try:
            with open(
                r"Advanced_programming\workshop-1\docs\user_reviews.txt",
                "r",
                encoding="utf8",
            ) as file:
                reviews = file.read()
                file.close()
                return reviews
        except FileNotFoundError as e:
            return f"An error occurred: {e}"
