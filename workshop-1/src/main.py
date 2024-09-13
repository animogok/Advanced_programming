import datetime
import re
from classes import customer_functionalities as cf

MENU = """

Welcome to ElectronicDevices.inc system
\n
OPTIONS \n
\t1. Categories 
\t2. Shopping cart 
\t3. Delete Item from Cart
\t4. Shopping Receipt
\t5. Reviews
\t6. Exit

Select an option: 
------------------------
"""


def organize_list(iterable: [list | dict]) -> str:  # type: ignore
    """
    Organizes a list or dictionary into a readable format.

    Args:
        iterable (list | dict): The list or dictionary to be organized.

    Returns:
        str: A formatted string of the organized list or dictionary.
    """
    result = []
    if isinstance(iterable, list):
        for index, item in enumerate(iterable):
            result.append(f"{index+1}: {item}")
    else:
        for index, (category, subcategories) in enumerate(iterable.items()):
            result.append(f"{index+1}: {category}:")
            subcategories_str = "\n".join(
                [f"     {i+1}. {subcat}" for i, subcat in enumerate(subcategories)]
            )
            result.append(subcategories_str)

    return "\n".join(result)


def validate_email() -> str:
    """
    Solicita y valida el email del usuario usando expresiones regulares.

    Returns:
        str: Un email válido.
    """
    while True:
        email = input("Your email user: ")
        # Expresión regular para validar un email básico
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return email
        else:
            print("Invalid email. Please try again.")


def validate_user_id() -> int:
    """
    Solicita y valida el ID del usuario (debe ser un número entero positivo).

    Returns:
        int: Un ID de usuario válido.
    """
    while True:
        try:
            user_id = int(input("Your identification number: "))
            if user_id > 0:
                return user_id
            else:
                print("User ID must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# ============================= MAIN CODE ===========================


def main():
    """
    The main function that runs the ElectronicDevices.inc system.

    Returns:
        None

    Example:
        >>> main()
        Welcome to ElectronicDevices.inc system
        ...
    """
    option = int(input(MENU))
    cart = cf.ShoppCart()

    while option != 6:
        print("------------------------")
        if option == 1:
            categories_class = cf.ShowCategories()
            categories = categories_class.open_categories()
            sub_categories = categories_class.open_sub_categories

            print(organize_list(categories))

            option_2 = int(input("6 Exit\n\tSelect an option: "))

            while option_2 != 6:
                print("------------------------")
                if option_2 == 1:
                    print(organize_list(sub_categories(option_2 - 1)))
                elif option_2 == 2:
                    print(organize_list(sub_categories(option_2 - 1)))
                elif option_2 == 3:
                    print(organize_list(sub_categories(option_2 - 1)))
                elif option_2 == 4:
                    print(organize_list(sub_categories(option_2 - 1)))
                elif option_2 == 5:
                    print(organize_list(sub_categories(option_2 - 1)))
                else:
                    print("Invalid option. Please select a valid option.")

                option_2 = int(input("\n\tSelect an option: "))

        elif option == 2:
            categories = cf.SUB_CATEGORIES
            categories_class = cf.ShowCategories()
            catalog = categories_class.show_all()

            print(organize_list(catalog))

            shopp_options = input(
                "-1. Exit\n\tSelect an item (type like this index title, index item example : 1,1): "
            )
            while shopp_options != "-1":
                if not re.match(r"^\d+,\d+$", shopp_options):
                    print("\nInvalid input. Please use the correct format (1,1).")
                else:
                    try:
                        value = shopp_options.split(",")
                        item = categories.get(int(value[0]) - 1)[int(value[-1]) - 1]
                        cart.add_item(item=item)

                        print(f"Total: {sum(cart.user_total)}")
                    except (TypeError, IndexError):
                        print("\nChoose a valid literal for an item in the catalog.")
                shopp_options = input("\nSelect an item (use this form 1,1): ")

        elif option == 3:
            print(organize_list(cart.user_items))
            print(f"Total: {sum(cart.user_total)}")
            shopp_options = int(input("0. Exit\n\tSelect an item: "))
            while shopp_options != 0:
                cart.remove_item(shopp_options)
                print(organize_list(cart.user_items))
                print(f"Total: {sum(cart.user_total)}")
                shopp_options = int(input("\n\tSelect an item: "))

        elif option == 4:  # Shopping Receipt
            user_cart = cart.user_items

            # Validación de email y user ID
            user_name = input("Your name user: ")
            user_email = validate_email()  # Usamos la función para validar el email
            user_id = validate_user_id()  # Usamos la función para validar el ID

            payment_method = ["Debit card", "Credit card", "Cash"]
            date = datetime.datetime.now()

            print(organize_list(payment_method))

            payment_option = int(input("\n\tSelect a payment method option: "))

            print(
                f"""
            ElectronicDevices.inc
            --------------------------------------------------------------
            Date: {date}
            --------------------------------------------------------------
            User: {user_name}
            Email: {user_email}
            User Identification: {user_id}
            --------------------------------------------------------------
            ITEMS
                \t{organize_list(user_cart)}
            --------------------------------------------------------------
            SUB TOTAL: {sum(cart.user_total)} USD
            IVA (10%): {round(sum(cart.user_total) * 0.1, 3)} USD

            TOTAL: {sum(cart.user_total) + (sum(cart.user_total) * 0.1)} USD
            --------------------------------------------------------------
            PAYMENT METHOD: {payment_method.pop(payment_option)}
            """
            )

            break

        elif option == 5:
            review_submitter = cf.Reviews()
            categories = cf.SUB_CATEGORIES
            categories_class = cf.ShowCategories()
            catalog = categories_class.show_all()

            organize_list(catalog)

            shopp_options = input(
                """
                0. Exit
                1. Read reviews
                3. write a review (type index like this: 1,1)
                ---------------------------------------------------------------------
                Option: """
            )
            while shopp_options != "0":
                if shopp_options == "3":
                    try:
                        value = shopp_options.split(",")
                        desicion = int(
                            input("Would you like to write a review\n1. Yes\n2. No\n")
                        )
                        if desicion == 1:
                            review = input("Write your review: ")
                            review_submitter.submit_review(item=review, index=value)
                    except (TypeError, IndexError):
                        print("\nChoose a valid literal for an item in the catalog.")
                elif shopp_options == "1":
                    reviews = review_submitter.read_review()
                    print(reviews)

                elif not re.match(r"^\d+,\d+$", shopp_options):
                    print("\nInvalid input. Please use the correct format (1,1).")
                shopp_options = input(
                    """
                0. Exit
                1. Read reviews
                3. write a review (type index like this: 1,1)
                ---------------------------------------------------------------------
                Option: """
                )

        option = int(input(MENU))


if __name__ == "__main__":
    main()
