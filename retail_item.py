# Loveness Gumede & Thabang Mahapa

def main():
    """
    This main function gets input from the user and calculates the subtotal, tax, and total amount.
    Then displays the results.
    """
    # Input from the user
    description = get_retail_item_description()
    quantity_sold = get_number_of_purchased_items()
    price_per_unit = get_price_usd_per_unit()
    tax_rate = get_tax_rate()

    # Calculate the subtotal, tax_amount and total
    subtotal = calculate_subtotal_usd(price_per_unit, quantity_sold)
    tax_amount = calculate_tax_usd(subtotal, tax_rate)
    total = calculate_total_usd(subtotal, tax_amount)

    # Print the results
    print("\nSales Receipt:")
    print(f"Item Description: {description}")
    print(f"Number of Purchased items: {quantity_sold}")
    print(f"Unit Price (usd): {price_per_unit:.2f}")
    print(f"Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Subtotal: {subtotal:.2f} (usd)")
    print(f"Tax: {tax_amount:.4f} (usd)")
    print(f"Total: {total:.4f} (usd)")


def get_retail_item_description():
    """
    Prompts the user to enter the retail item description and returns it.

    Returns:
        str: The description of the retail item.
    """
    return input("Enter retail item description: ")


def get_number_of_purchased_items():
    """
    Prompts the user to enter the quantity sold and returns it.

    Returns:
        int: The quantity of items sold.
    """
    return int(input("Enter quantity purchased: "))


def get_price_usd_per_unit():
    """
    Prompts the user to enter the price in American dollars(USD) per unit and returns it.

    Returns:
        float: The price per unit in USD.
    """
    return float(input("Enter price per unit (usd): "))


def get_tax_rate():
    """
    Prompts the user to enter the tax rate as a floating point value and returns it.
    For example, if the tax rate was 6% the user should enter the value 0.6

    Returns:
        float: The tax rate.
    """
    return float(input("Enter tax rate: "))


def calculate_subtotal_usd(price_per_unit, quantity_sold):
    """
    Calculates the subtotal amount in American dollars(USD).

    parameters:
        price_per_unit (float): The price per unit in USD.
        quantity_sold (int): The quantity of items sold.

    Returns:
        float: The subtotal amount in USD.
    """
    return price_per_unit * quantity_sold


def calculate_tax_usd(subtotal, tax_rate):
    """
    Calculates the tax amount of the given subtotal in American dollars(USD).

    parameters:
        subtotal (float): The subtotal amount in USD.
        tax_rate (float): The tax rate.

    Returns:
        float: The tax amount in USD.
    """
    return subtotal * tax_rate


def calculate_total_usd(subtotal, tax_amount):
    """
    Calculates the total amount including tax in American dollars(USD).

    parameters:
        subtotal (float): The subtotal amount in USD.
        tax_amount (float): The tax amount in USD.

    Returns:
        float: The total amount in USD.
    """
    return subtotal + tax_amount


if __name__ == "__main__":
    main()
