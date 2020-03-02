class Book:
    
    def accept(self):
        self.name = str(input("Enter name of Book: "))
        self.author = str(input("Enter author of Book: "))
        self.price = float(input("Enter price of Book: "))
        self.n_copies = int(input("Enter number of copies to be purchased: "))
        
    def total_price(self):
        t = self.price*self.n_copies
        print("Total Price : ", t)
        
    def details(self):
        print("Purcashe Details".center(70, "-"))
        print("Name of Book : ", self.name)
        print("Author of Book : ", self.author)
        print("Price of Book : ", self.price)
        print("Number of copies : ", self.n_copies)
        

c = Book()
c.accept()
c.details()
c.total_price()
