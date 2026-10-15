class Publication: 
    """ This represents a publication that has a title and an author. This is the parent class for the Book and Magazine subclasses."""
    def __init__(self, title:str, author:str):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self): 
        print(f"Title: {self.__title}\nAuthor: {self.__author}")

class Book(Publication):
    """ This represents the Book subclass which inherits from Publication class, getting the data field: title and author, and adding a new datafield, number_of_pages. """
    def __init__(self, title:str, author:str, number_of_pages: int):
        super().__init__(title, author)
        if number_of_pages <= 0:
            print("Number of pages must be positive")
        else:
            self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_of_pages}"

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("Number of pages must be positive")
        else:
            self.__number_of_pages = number_of_pages

class Magazine(Publication):
    """ This represents the Magazine subclass which inherits from Publication class, getting the data field: title and author, and adding a new datafield, issue_number. """
    def __init__(self, title:str, author:str, issue_number:int):
        super().__init__(title, author)
        if issue_number <= 0:
            print("Issue number must be positive")
        else:
            self.__issue_number = issue_number

    def get_issue_number(self):
        return f"Issue number:{self.__issue_number}"

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("Issue number must be positive")
        else:
            self.__issue_number = issue_number

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# Printing the information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310) # setting invalid value on attribute
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())


