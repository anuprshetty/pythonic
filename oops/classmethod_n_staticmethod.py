# Methods:
# - Method is a function associated to an object of the class or to the class itself.
# - The methods defined in a class determine the behaviour of the objects created from the class and how they can interact with their state.

# 3 types of methods:
# a. Instance method:
#    - Methods that belong to a specific object.
#    - They have access to the state of the object that calls them by having reference to the calling object itself. i.e., self parameter - python convention.
#    - NOTE: Instances don't have their own copies of the methods. They reference the methods defined in the class.
# b. Class method:
# c. Static method:

class ClassTest:
    # Bound Method:
    # - If a function is an attribute of class and it is accessed via the instances, they are called bound methods.
    # - A bound method is one that has ‘self‘ as its first argument.
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    # static methods are used to place functions inside a class.
    # Binding a function to a class or object.
    @staticmethod
    def static_method():
        print(f"Called static method")

    # Unbound Method:
    # - Methods that do not have an instance of the class as the first argument are known as unbound methods.
    # - It does not accept any instance as an argument.
    # - As of Python 3.0, the unbound methods have been removed from the language.
    # - They are not bounded with any specific object of the class.
    # - To make the below method unbound_method() work, it should be made into a static method.
    # - Static methods are similar to class methods but are bound completely to class instead of particular objects. They are accessed using class names.
    # - Not all the methods need to alter the instances of a class. They might serve any common purpose. A method may be a utility function also.
    def unbound_method():
        print(f"Called unbound method")

    
classtest = ClassTest()
# instance_method
classtest.instance_method()
# class_method
ClassTest.class_method()
# static_method
classtest.static_method()
ClassTest.static_method()
# unbound_method
# classtest.unbound_method()  # TypeError: unbound_method() takes 0 positional arguments but 1 was given
ClassTest.unbound_method()  # Called unbound method

# Method Chaining:
# - In Object-Oriented Programming, Method Chaining is a very common syntax that lets us call several methods one after the other on the same instance.
# - We can do this by returning self from a method.

class Pizza:
 
    def __init__(self):
        self.toppings = []
 
    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self
 
    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())


pizza = Pizza()
# To make the code more readable, you can write the method calls in several lines using \ to indicate that the next line is a continuation of the current line.
pizza.add_topping("mushrooms") \
    .add_topping("olives") \
    .add_topping("chicken") \
    .display_toppings()

# Use Cases and Advantages of Method Chaining:
# Method chaining can be used to improve the readability of your code. 
# It makes the code more concise and avoids creating variables to store intermediate results.
