
#1-The single responsibility principle
# Class responsible for generating invoices
class Invoice:
    def generate_invoice(self):
        print("Generating invoice...")

# Class responsible for saving invoices
class InvoiceSaver:
    def save_to_file(self):
        print("Saving invoice to file...")




#2-The open/closed principle
from abc import ABC, abstractmethod

# Abstract class defining the tax calculation strategy
class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass

# Class for calculating USA tax
class USATax(TaxStrategy):
    def calculate_tax(self):
        return 0.1

# Class for calculating UK tax
class UKTax(TaxStrategy):
    def calculate_tax(self):
        return 0.2

# Tax calculator that uses a specific strategy
class TaxCalculator:
    def calculate_tax(self, strategy: TaxStrategy):
        return strategy.calculate_tax()

# Usage example
usa_tax = USATax()
calculator = TaxCalculator()
print(calculator.calculate_tax(usa_tax))  # Output: 0.1




#3-Liskov Substitution Principle 

from abc import ABC, abstractmethod

# Abstract class for shapes
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

# Using the classes
rect = Rectangle(10, 5)
square = Square(4)

print(rect.get_area())  # Output: 50
print(square.get_area())  # Output: 16


#4- Interface Segregation Principle
from abc import ABC, abstractmethod

# Interface for coding tasks
class Coder(ABC):
    @abstractmethod
    def code(self):
        pass

# Interface for testing tasks
class Tester(ABC):
    @abstractmethod
    def test(self):
        pass

# Programmer class implements only the coding interface
class Programmer(Coder):
    def code(self):
        print("Coding...")

# Quality Assurance class implements only the testing interface
class QualityAssurance(Tester):
    def test(self):
        print("Testing...")



#5-Dependency Inversion Principle
from abc import ABC, abstractmethod

# Abstract database interface
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

# MySQL database implementation
class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")

# MongoDB database implementation
class MongoDBDatabase(Database):
    def connect(self):
        print("Connecting to MongoDB database...")

# Application depends on the abstract database interface
class App:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()

# Using different database implementations
mysql_db = MySQLDatabase()
app = App(mysql_db)
app.start()  # Output: Connecting to MySQL database...

mongo_db = MongoDBDatabase()
app = App(mongo_db)
app.start()  # Output: Connecting to MongoDB database...
        