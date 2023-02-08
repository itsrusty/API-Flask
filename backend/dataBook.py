# super class
class Book:
    # attributes
    def __init__(self, title_book, description_book, price_book):
        # instance attributes  
        self.__title_book = title_book
        self.__description_book = description_book
        self.__price_book = price_book

    # methods for Book
    def book(self):
        return "Titulo: " + self.__title_book  + " Descripción: " + self.__description_book + " Precio:  " + self.__price_book

    # getters methods for class Book
    def get_title(self):
        return self.__title_book

    def get_description(self):
        return self.__description_book

    def get_price(self):
        return self.__price_book

    # setters
    def set_title(self, new_title):
        self.__title_book = new_title


# ? 
# clase que hereda de la super clase book
class personMe(Book):
    def __init__(self, title, description, price):
        super().__init__(title, description, price)

# ?
# clase persona normal hereda de la  super clase book
class personNormal(Book):
    def __init__(self, title, description, price):
        super().__init__(title, description, price)


# ?
# instance de la clase que hereda de la super clase book
personMe1 = personMe("manual de python", "un libro de python", 3200)
personMe2 = personMe("manual de c++", "un libro de c++", 4000)
personMe3 = personMe("manual de javascript", "un libro de javascript", 12000)
personMe4 = personMe("manual de reactjs", "un libro de reactjs", 12000)
personMe5 = personMe("manual de flask", "un libro de flask", 12000)
personMe6 = personMe("manual de mysql", "un libro de mysql", 12000)


# ? instancia de techs que sabe normalPerson
personNormal1 = personNormal("html5", "lenguaje de etiquetas", 1000)
personNormal2 = personNormal("css3", "lenguaje de estilos", 2000)
personNormal3 = personNormal("javascript ECM6", "lenguaje de programación", 10000)

# export function data my techs
def export_data_me():
    data = [
        {
            "name": personMe1.get_title(),
            "description": personMe1.get_description(),
            "price": personMe1.get_price()
        },
        {
            "name": personMe2.get_title(),
            "description": personMe2.get_description(),
            "price": personMe2.get_price()
        },
        {
            "name": personMe3.get_title(),
            "description": personMe3.get_description(),
            "price": personMe3.get_price()
        },
        {
            "name": personMe4.get_title(),
            "description": personMe4.get_description(),
            "price": personMe4.get_price()
        },
        {
            "name": personMe5.get_title(),
            "description": personMe5.get_description(),
            "price": personMe5.get_price()
        },
           {
            "name": personMe6.get_title(),
            "description": personMe6.get_description(),
            "price": personMe6.get_price()
        }
    ]

    # ! return data
    return data

def export_data_person_simple():
    data_person_simple_techs = [
          {
            "name": personNormal1.get_title(),
            "description": personNormal1.get_description(),
            "price": personNormal1.get_price()
        },
          {
            "name": personNormal2.get_title(),
            "description": personNormal2.get_description(),
            "price": personNormal2.get_price()
        },
          {
            "name": personNormal3.get_title(),
            "description": personNormal3.get_description(),
            "price": personNormal3.get_price()
        }
    ]
    return data_person_simple_techs