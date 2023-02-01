# Let's Go Shopping
## **Video Demo:**
https://youtu.be/sd0ZlxQFKKo

## **Description:**
This application was designed to simulate a shopping cart.
We can add funds to the account, see account balance, add products to the cart, view shopping cart, and checkout shopping cart using this application.

Let's Go Shopping allows users to interact with the application by navigating the main menu and selecting what they want to do. In the following we will go over each function to explain their role in the application.

### **add_balance(n)**
This function is used to add balance to the account. There is a global variable called balance, set up to start at 0. Using the add_balance function users will be able to add n amount to the global balance variable.

### **checkout(n)**
checkout function is used to subtract n amount to the global balance. This function is used inside another function called checkout_cart which we will see later on.


### **add_to_cart()**
This function starts off by printing out the so-called menu of all the products that the store sells in the form of a dictionary, with the key as the product name and the value as the product's price per unit. In addtion to instructions such as type 0 to go back to the main menu and/or press Ctrl+d to exit the whole application.

Then it moves on to a while loop that will keep prompting the user to add products to the cart. If the user types in a product that exists in the menu, the product will be added to the cart dictionary with product as key and value of one if it is a new element in the dictionary. Conversely, if the product typed in is already a key in cart, the value will increase by one. A message saying the product's name was added to the cart will appear to tell users it was added successfully.

On the other hand, if the user types in a product that is not on the menu a message stating "Product not available in store" will appear, nothing will be added to cart and user will be prompted to type a product to add into cart again. This prompt will appear over and over until the user types in 0 which will take him/her back to the main menu, or Ctrl+d which will exit the application.

### **total_price(cart)**
This function takes in the cart argument which will iterate through the cart dictionary and determine the price per unit of the product comparing it to the key in the products menu. Then it will multiply the price by the amount of the product inside the cart and add them all up to give out the total price to be paid for all products in the cart. This function will be used later on inside two other functions


### **delete_product(cart, product_to_delete)**
This function takes in two arguments, cart coming in with the product name as key and the quantity of product as value. And product_to_delete, if the product_to_delete name matches with a key inside cart and such product has a quantity greater than one, the quantity will decrease by one. Else if the product_to_delete name matches with a key in cart and such product has a quantity of one, such key-value pair will be deleted from the cart dictionary. Nevertheless, if product_to_delete name does not match any key in the cart, nothing will happen and a view of the cart will be shown.

### **view_cart()**
This function showcases all the products added to the cart by the user and the total price of the cart. There are several actions that the user can choose when in the cart. The user could choose 0 to go back to the main menu, 5 to delete a product from the cart using the delete_product function, or 6 to checkout the whole cart.

If the user does not select 0, 5, or 6 then "Unsupported action, try Again!" message will appear and the user will be prompted again for a selection until one supported action occurs.

### **checkout_cart(account_balance, cart)**
This function implements the total_price function and checkout function explained above to subtract the total cart price from the account balance if the balance is greater than the total. Otherwise, nothing will happen and a message stating "Not enough funds! please add to funds" will appear.

### **exit_app()**
This function simply exits the application with a message saying "See You Later!". This function is used mainly when the user quits the application by pressing Ctrl+d.

### **main_menu()**
In this function everything comes together. This is the function that will show the user the main menu with actions to select. If the user selects #1 then they will be able to view their account balance. If #2 is selected, they will be able to add balance to their account. #3 will allow the user to add products to the cart. And, #4 will allow users to view cart and do any other action that view_cart has to offer.

### **main()**
In main, a while loop is used so that the program keeps running forever keeping all changes made by the user until the user uses Ctrl+d to quit it and a "See You Later!" message appears. Ctrl+d can be used any time during the program to quit.

### **Design Choices**
The main menu was made into its own function rather than having it all inside main() so that the main menu can be called in any step or choice of the application by simply typing 0 whenever it was possible. Same way with view_cart, every time a product is deleted from the cart the view of the cart will appear again to showcase the actions that occurred and did not occur. Furthermore, a lot of while loops were implemented in the program so that the program keeps functioning, saving information from the user, such as the account balance, all the way until the program exits.

Pytest was used to test some of the functions in this application but not all. Some functions were able to be tested using Pytest mainly because they return another function making the program keep looping around a lot of the functions in the application. For example, the delete_product function was not able to be tested with pytest because it returns view_cart after some actions occurred and view_cart returns either main_menu, or back to delete_product and so on.

Future changes that can be made to improve the program is to create a file to keep users' information saved so that they can come back to it in the future. But we can leave this for the future.