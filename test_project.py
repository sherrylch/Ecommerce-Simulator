from project import delete_product, total_price, add_balance, checkout

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

balance = 0


def main():
    test_total_price()
    test_add_balance()
    test_checkout()


def test_add_balance():
    assert add_balance(200) == 200
    assert add_balance(0) == 200
    assert add_balance(100) == 300


def test_checkout():
    # given that now balance is 300 since we add_balance up to 300 previously
    assert checkout(100) == 200
    assert checkout(50) == 150
    assert checkout(0) == 150


def test_total_price():
    assert total_price({"mascara" : 1, "primer" : 3}) == 115
    assert total_price({"blush" : 2, "setting spray" : 4}) == 182
    assert total_price({}) == 0


def test_delete_product():
    assert delete_product({"mascara" : 1, "primer" : 3}, "cat") == "Product not Found in Cart"


if __name__ == "__main__":
    main()
