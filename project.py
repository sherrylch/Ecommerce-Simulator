import sys
import re

balance = 0

products = {
        "foundation" : "$48",
        "blush" : "$35",
        "bronzer" : "$35",
        "eyeliner" : "$25",
        "lipstick" : "$20",
        "mascara" : "$25",
        "setting spray" : "$28",
        "primer" : "$30",
        "eyeshadow" : "$45",
        "finishing powder" : "$28"
    }

cart = {}


def main():
    global balance
    while True:
        try:
            main_menu()
        except EOFError:
            exit_app()


def main_menu():
    global balance
    print("")
    action = input("Select one of the following\n1. Account Balance\n2. Add Balance\n3. Add Product to Cart\n4. View Cart\nCtrl + d Exit Application\n\nSelection: #")

    if matches := re.search(r"^[1-4]$", action):
        # check balance
        if action == "1":
            print(f"Account Balance: ${balance}")
        elif action == "2":
            while True:
                try:
                    amount = int(input("Amount: $"))
                except ValueError:
                    pass
                else:
                    print(f"Account Balance: ${add_balance(amount)}")
                    break
        elif action == "3":
            add_to_cart()
        elif action == "4":
            view_cart()

    # if none of the given options
    else:
            print("Unsupported action, try again!")


def add_balance(n):
    ''' adds balance to the account and returns balance '''
    global balance
    balance += n
    return balance


def checkout(n):
    ''' substract n to balance, takes n as argument and returns balance '''
    global balance
    balance -= n
    return balance


def add_to_cart():
    print("")
    # shows users the list of products to choose from
    for product, price in products.items():
        print(product.title(), price)
    print("\nType 0 to go back to main menu \nCtrl+d to exit the application")

    # ask user for product to add
    while True:
        try:
            product_to_buy = input("\nAdd to Cart: ").strip().lower()

            # make sure store sells the product being asked
            if product_to_buy in products:

                # if product already in the cart update count
                if product_to_buy in cart:
                    cart[product_to_buy] = cart[product_to_buy]+1
                    print(f"{product_to_buy.title()} was added to the cart!")

                # if product not in the cart add it, and add price of each product
                else:
                    cart[product_to_buy] = 1
                    print(f"{product_to_buy.title()} was added to the cart!")

            elif product_to_buy == "0":
                return main_menu()

            else:
                print("Product not available in store")

        except EOFError:
            exit_app()


def view_cart():
    ''' returns the cart, with amount of each product and product name '''
    global balance
    while True:
        print("\nProducts in Cart:")
        for each in cart:
            print(f"{cart[each]} {each}")
        print(f"\nTotal: ${total_price(cart)}")

        action = input("\nSelect 0 to Go Back to Main Menu\nSelect 5 to Delete Product from Cart\nSelect 6 to Checkout Cart\nSelection: #")

        if match := re.search(r"^[0,5,6]$", action):
            if action == "0":
                return main_menu()
            elif action == "5":
                delete = input("Remove: ").strip().lower()
                delete_product(cart, delete)
            elif action == "6":
                checkout_cart(balance, cart)

        else:
            print("Unsupported action, try Again!")


def total_price(cart):
    ''' returns the total price of the cart
    argument cart is a dict with product:quantity '''
    total = 0
    for each in cart:
        price = int(products[each].replace("$",""))
        amount = cart[each]
        total += (price * amount)
    return total


def delete_product(cart, product_to_delete):
    ''' decreases product quantity or deletes product from the cart '''
    if product_to_delete in cart:
        if cart[product_to_delete] > 1:
            cart[product_to_delete] -= 1
            return view_cart()

        else:
            del cart[product_to_delete]
            return view_cart()
    else:
        return ("Product not Found in Cart")


def checkout_cart(account_balance, cart):
    ''' check out cart total, substracting amount from balance, shows balance and returns back to main menu '''
    total = total_price(cart)

    if account_balance < total:
        print(f"\nNot enough funds! please add to funds")
    else:
        account_balance = checkout(total)
        print(f"\nYour order has been processed!")
        print(f"Account Balance: ${account_balance}")
        return main_menu()


def exit_app():
    print("")
    sys.exit("See You Later!")


if __name__ == "__main__":
    main()