# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
The `Product` class could be created, where all data related to the product would be encapsulated; i.e., `name`, `price`, and `stock`. Encapsulation can be done using the methods such as `add_stock()` and `sell_product()`, where the stock would be managed instead of other parts of the application manipulating it.

### 2. Abstraction
The concept of abstraction can be realized in this instance by offering easy-to-use methods that will simplify the process of inventory operation. In this case, the inventory system can have a `sell_product()` method which will automatically determine the amount of the stock, deduct the sold quantity, and update the inventory. This will simplify the operation of the program without having to go through the complex procedures.

### 3. Inheritance
Inheritance can be applied in the scenario where there are several products which possess similar behaviors and characteristics. In this case, the parent class would be the Product with properties such as name, price, and stock. The other classes to be created would include FoodProduct and HouseholdProduct. These classes will then inherit the parent class attributes while at the same time possessing their own attributes.

### 4. Polymorphism
Polymorphism is useful when it comes to having different types of products use a single method name while doing the procedure in their own way. In this case, classes that define various kinds of products will have their own `calculate_price()` method if some products have certain special prices, discounts among others.

## Reflection
Of the four pillars of OOP, I believe that encapsulation would be the most beneficial in enhancing the efficiency of the sari-sari store inventory system. By encapsulation, I mean bundling up all the related information, which include the name of the product, the price, and the stock, and at the same time control access to that information. In doing so, mistakes such as setting a negative value for the stock of the product can be avoided.

## OOP Representation Through a Simple Diagram
'''
Product
│
├──Properties
│         ├──names
│         ├──price
│         ├──stock
│ 
├─Methods  
│      ├──calculate_price()
│      ├──sell_product()
│      ├──add_stock()
├──Encapsulation: Data is safe inside the object
├──Abstraction: Hides complex code to the user
├──Inheritance: Special products inherit Product
├──Polymorphism: Product that can implement different methods
'''