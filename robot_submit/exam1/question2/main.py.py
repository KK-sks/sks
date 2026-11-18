class Book:
    def __init__(self,title="",price=0.0,stock=0):
        self.__title=title
        seif.__price=price
        self.__stock=stock

    def input_data(self):
        self.__title=input("书名:")
        self.__price=float(input("价格:"))
        self.__stock=int(input("仓库:"))

    def display_data(self):
        print(f"书名:{self.__title}")
        print(f"价格:{self.__price}")
        print(f"库存:{self.__stock}")

if __name__=="__main__":
    book=Book()
    book.input_data()
    book.display_data()
