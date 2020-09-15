from tkinter import *
import os,sys
import time
import sqlite3
from tkinter import messagebox
import random

# window=Tk()
# window.geometry('1500x780+100+100')
# msg = Tk()
# msg.eval('tk::PlaceWindow %s center' % msg.winfo_toplevel())
# msg.withdraw()


class Reg:
    # def __init__(self):
    #     self.acc_name = 'NONE'
    def signup(self):
        self.e1 = input('ENTER YOUR NAME : ')
        self.e2 = input('ENTER YOUR EMAIL : ')
        self.e3 = input('ENTER YOUR PASSWORD : ')

        conn = sqlite3.connect('arbii.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY,name text,email text, password text)")
        cur.execute("INSERT INTO records Values(Null,?,?,?)", (self.e1 , self.e2 , self.e3))
        print('ACCOUNT  CREATED ...')
        conn.commit()
        conn.close()

    # def login(self):
    #     self.a1 = input('ENTER EMAIL TO Login :')
    #     self.a2 = input("ENTER PASSWORD TO Login : ")
    #     conn = sqlite3.connect('arbii.db')
    #     cur = conn.cursor()
    #
    #     #cur.execute("SELECT * FROM records WHERE email=? AND password=?", (self.a1 , self.a2))
    #     cur.execute('SELECT * FROM records')
    #
    #     self.row = cur.fetchall()
    #
    #     print(self.row)
    #
    #
    #
    #     if self.row == []:
    #         print('INVALID ENTRIES')
    #
    #     elif self.row != []:
    #         for self.i in self.row:
    #             if self.i[2] == self.a1 and self.i[3]==self.a2:
    #                 print('ACCOUNT LOGIN SUCCESSFULLY')
    #
    #                 print('USER NAME FOUND WITH NAME :', self.i[1])
    #
    #                 self.acc_name = self.i[1]
    #                 print(self.acc_name)
    #
    #
    #     else:
    #         print('USER NOT FOUND')
    #
    #
    #     w = menu()
    #     w.option()
    #     conn.commit()
    #     conn.close()
    # def kk(self):
    #     self.mm = self.acc_name
    def del_records(self):
        conn = sqlite3.connect('arbii.db')
        obj = conn.cursor()
        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        print(c)
        id = int(input("ENTER INDEX NUMBER YOU WANT TO DELETE : "))
        quirry = 'DELETE FROM records WHERE id = ?;'
        # obj.execute('DELETE FROM test WHERE id = ?')
        conn.execute(quirry, (id,))


        obj.execute('SELECT * FROM records')
        c = obj.fetchall()
        print(c)
        print("ACCOUNT DELETED.....")
        conn.commit()
        conn.close()
class fileread:

    def read(self,a):
        l = open(a,"r+")
        print(l.read())
        self.localtime = time.asctime(time.localtime(time.time()))



class menu(fileread):
    # print("1. View the list of product\n2. Add products\n3. remove products from the cart\n4. View your cart\n5. CHeakOut our Items\n6. View shopping History")
    def __init__(self):
        self.TShirt = 50
        self.pent = 50
        self.kurta = 50
        self.pajama = 50
        self.shirt = 50
        self.jogger = 50
        self.tie = 50
        self.Trowser = 50
        self.watches = 50
        self.TShirtsprice = 500
        self.pentprice = 700
        self.kurtaprice = 400
        self.pajamasprice = 300
        self.shirtprice = 500
        self.joggersprice = 1500
        self.tieprice = 100
        self.trowserprice = 700
        self.watchesprice = 1000


    def addi(self):
        while True:
            print('--------------------------------------------------------------------------\nADDING ITEMS STOCK')
            print("1. SHIRT ")
            print("2. T-SHIRT")
            print("3. PENT")
            print("4. TIE")
            print("5. JOGGERS")
            print("6. TROWSER")
            print("7. WATCH  ")
            print("8. KURTA ")
            print("9. PAJAMAS ")
            print('---------------------------------------------------------------------------')
            try:
                l = int(input("CHOOSE YOUR OPTION : "))
                m = int(input("enter the quantity you want to add : "))
            except ValueError:
                print('please Enter DIGIT...')
            else:
                if l == 1:
                    self.shirt+=m
                    print(self.shirt)

                elif l == 2:
                    self.TShirt+=m
                    print(self.TShirt)
                elif l == 3:
                    self.pent+=m
                    print(self.pent)
                elif l ==4:
                    self.tie+=m
                    print(self.tie)
                elif l == 5:
                    self.jogger+=m
                    print(self.jogger)
                elif l == 6:
                    self.Trowser+=m
                    print(self.Trowser)
                elif l == 7:
                    self.watches+=m
                    print(self.watches)
                elif l == 8:
                    self.kurta+=m
                    print(self.kurta)
                elif l == 9:
                    self.pajama+=m
                    print(self.pajama)
                elif l == 10:
                    break

    def login(self):
        self.a1 = input('ENTER EMAIL TO Login :')
        self.a2 = input("ENTER PASSWORD TO Login : ")
        conn = sqlite3.connect('arbii.db')
        cur = conn.cursor()

        #cur.execute("SELECT * FROM records WHERE email=? AND password=?", (self.a1 , self.a2))
        cur.execute('SELECT * FROM records')

        self.row = cur.fetchall()

        print(self.row)



        if self.row == []:
            print('INVALID ENTRIES')

        elif self.row != []:
            for self.i in self.row:
                if self.i[2] == self.a1 and self.i[3]==self.a2:
                    print('=====================================================================')
                    print('ACCOUNT LOGIN SUCCESSFULLY')

                    print('ACCOUNT FOUND','USER NAME FOUND WITH NAME :'+str(self.i[1]))

                    self.acc_name = self.i[1]
                    print('Assalam O Alaikum !!\n WELCOME TO MY BOUTIQUE :',self.acc_name)
                    print('======================================================================')
                    self.option()

        else:
            print('USER NOT FOUND')


        conn.commit()
        conn.close()
    def category(self):

        print('---------------------------------------------------------------------------------\nCATEGORIES :\n')
        print("1. SHIRT PRICE " , self.shirtprice )
        print("2. T-SHIRT PRICE" , self.TShirtsprice)
        print("3. PENT PRICE", self.pentprice)
        print("4. TIE PRICE" , self.tieprice)
        print("5. JOGGERS PRICE" , self.joggersprice)
        print("6. TROWSER PRICE", self.trowserprice)
        print("7. WATCH PRICE ", self.watchesprice)
        print("8. KURTA PRICE" , self.kurtaprice)
        print("9. PAJAMAS PRICE" , self.pajamasprice)
        print('----------------------------------------------------------------------------------')

    def addToCart(self):
        self.a = []
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        c5 = 0
        c6 = 0
        c7 = 0
        c8 = 0
        c9 = 0
        while True :
            self.category()
            print("10. MAIN MENU : ")
            try:
                d = int(input("CHOOSE YOUR OPTION FROM 1-9 : "))
            except ValueError:
                print("ENTER YHE DIGIT VALUE ")
            else:
                if d == 1 :

                    self.c = int(input('enter the quantity : '))

                    while True:

                        if self.c > self.shirt:

                            print("Sorry we have only ",self.shirt," Shirts")
                            break
                        else:
                            if c1 == 0:
                                self.shirt -= self.c

                                self.a.append([self.c, "Shirt"])
                                print(self.a)
                                c1+=1


                                break
                            else:
                                c1 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Shirt":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break





                elif d == 2:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.TShirt:
                            print("Sorry we have only ", self.TShirt ,"TShirts")
                            break
                        else:
                            if c2 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "TShirts"])
                                print(self.a)
                                c2+=1

                                break
                            else:
                                c3 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "TShirts":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 3:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.pent:
                            print("Sorry we have only ", self.pent ," pent")
                            break
                        else:
                            if c3 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "pent"])
                                print(self.a)
                                c3+=1

                                break
                            else:
                                c3 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "pent":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 4:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.tie:
                            print("Sorry we have only ", self.tie ," Tie")
                            break
                        else:
                            if c4 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Tie"])
                                print(self.a)
                                c4+=1

                                break
                            else:
                                c4 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Tie":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break

                elif d == 5:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.jogger:
                            print("Sorry we have only ", self.jogger ," Jogger")
                            break
                        else:
                            if c5 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Jogger"])
                                print(self.a)
                                c5+=1

                                break
                            else:
                                c5 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Jogger":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 6:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.Trowser:
                            print("Sorry we have only ", self.Trowser ," Trowser")
                        else:
                            if c6 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Towser"])
                                print(self.a)
                                c6+=1

                                break
                            else:
                                c6 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Towser":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 7:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.watches:
                            print("Sorry we have only ", self.watches ," Watches")
                            break
                        else:
                            if c7 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Watches"])
                                print(self.a)
                                c7+=1

                                break
                            else:
                                c7 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Watches":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 8:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.kurta:
                            print("Sorry we have only ", self.kurta ," Kurta")
                            break
                        else:
                            if c8 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Kurta"])
                                print(self.a)
                                c8+=1

                                break
                            else:
                                c8 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Kurta":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break
                elif d == 9:
                    self.c = int(input('enter the quantity : '))

                    while True:
                        if self.c > self.pajama:
                            print("Sorry we have only ", self.pajama ," Pajamas")
                            break
                        else:
                            if c9 == 0:
                                self.shirt -= self.c
                                self.a.append([self.c, "Pajamas"])
                                print(self.a)
                                c9+=1

                                break
                            else:
                                c9 += 1
                                self.shirt -= self.c
                                for i in range(len(self.a)):
                                    if self.a[i][1] == "Pajamas":
                                        self.a[i][0] = self.a[i][0] + self.c

                                print(self.a)

                                break

                elif d == 10:
                    self.option()

    def remove(self):
        self.category()


        while True :

            print("10. MAIN MENU : ")
            try:
                d = int(input("CHOOSE YOUR OPTION FROM 1-9 FROM WHICH YOU WANT TO REMOVE : "))
            except ValueError:
                print('Enter the digit : ')
            else:
                if d == 1:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Shirt":
                            if self.a[i][0] >= self.n :
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else :
                                print('NOTT ENOUGH SHIRTS IN CART')
                elif d == 2:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "TShirts":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else:
                                print('NOTT ENOUGH TSHIRTS IN CART')

                elif d == 3:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "pent":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else:
                                print('NOTT ENOUGH PENT IN CART')
                elif d == 4:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Tie":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else :
                                print('NOTT ENOUGH TIE IN CART')
                elif d == 5:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Jogger":
                            if self.a[i][0] >= self.n:
                             self.a[i][0] = self.a[i][0]-self.n
                             print(self.a)
                            else:
                                print('NOTT ENOUGH SHIRTS IN CART')
                elif d == 6:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Towser":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else:
                                print('NOTT ENOUGH SHIRTS IN CART')


                elif d == 7:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Watches":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else:
                                print('NOTT ENOUGH SHIRTS IN CART')
                elif d == 8:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Kurta":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else :
                                print('NOTT ENOUGH TIE IN CART')
                elif d == 9:
                    self.n = int(input("ENTER QUANTITY YOU WANT TO REMOVE : "))
                    for i in range(len(self.a)):
                        if self.a[i][1] == "Pajamas":
                            if self.a[i][0] >= self.n:
                                self.a[i][0] = self.a[i][0]-self.n
                                print(self.a)
                            else:
                                print('NOTT ENOUGH TIE IN CART')
                elif d == 10:
                    self.option()
    # def caller(self):
    #     super().__init__()
    #     Reg.login(self)
    #     Reg.
    def bill(self):

        self.category()
        self.total = 0
        print("__________________________________________")
        print("\n   CUSTOMER BILL     \n")
        self.invoice = random.randint(00000000 , 99999999)
        print('Invoice No.', self.invoice, '\n')
        self.localtime = time.asctime(time.localtime(time.time()))
        print(self.localtime, "\n")
        # self.ff = self.acc_name+'.txt'
        #
        # print(self.ff)
        self.f = open(self.acc_name+'.txt',"a+")
        self.f.write(self.localtime+"\n")
        self.f.write('INVOICE NO : '+str(self.invoice) + "\n")
        print()
        for i in range(len(self.a)):


            if self.a[i][1] == "Shirt":
                self.total+=self.a[i][0]*self.shirtprice
                self.f.write("Shirts Quantity is "+str(self.a[i][0])+" total price of the Shirt is : "+str(self.a[i][0]*self.shirtprice)+"\n")
                print("Shirts Quantity is ",self.a[i][0]," total price of the Shirt is : ",self.a[i][0]*self.shirtprice)
            if self.a[i][1] == "TShirts":
                self.total += self.a[i][0] * self.TShirtsprice
                self.f.write("TShirts Quantity is "+ str(self.a[i][0])+ " total price of the TShirt is : "+
                      str(self.a[i][0] * self.TShirtsprice)+"\n")
                print("TShirts Quantity is ", self.a[i][0], " total price of the TShirt is : ",
                      self.a[i][0] * self.TShirtsprice)
            if self.a[i][1] == "pent":
                self.total += self.a[i][0] * self.pentprice
                self.f.write("Pents Quantity is "+ str(self.a[i][0])+ " total price of the Pent is : "+
                      str(self.a[i][0] * self.pentprice)+"\n")
                print("Pents Quantity is ", self.a[i][0], " total price of the Pent is : ",
                      self.a[i][0] * self.pentprice)
            if self.a[i][1] == "Tie":
                self.total += self.a[i][0] * self.tieprice
                self.f.write("Tie Quantity is "+ str(self.a[i][0])+ " total price of the tie is : "+
                      str(self.a[i][0] * self.tieprice)+"\n")
                print("Tie Quantity is ", self.a[i][0], " total price of the tie is : ",
                      self.a[i][0] * self.tieprice)
            if self.a[i][1] == "Jogger":
                self.total += self.a[i][0] * self.joggersprice
                self.f.write("Jogger Quantity is "+str(self.a[i][0])+" total price of the Joggers is : "+
                      str(self.a[i][0] * self.joggersprice)+"\n")
                print("Jogger Quantity is ", self.a[i][0], " total price of the Joggers is : ",
                      self.a[i][0] * self.joggersprice)
            if self.a[i][1] == "Towser":
                self.total += self.a[i][0] * self.trowserprice
                self.f.write("Trowser Quantity is "+ str(self.a[i][0])+" total price of the Trowser is : "+
                      str(self.a[i][0] * self.trowserprice)+"\n")
                print("Trowser Quantity is ", self.a[i][0], " total price of the Trowser is : ",
                      self.a[i][0] * self.trowserprice)
            if self.a[i][1] == "Watches":
                self.total += self.a[i][0] * self.watchesprice
                self.f.write("Watch Quantity is "+ self.a[i][0]+ " total price of the Watches is : "+
                     str(self.a[i][0] * self.watchesprice)+"\n")
                print("Watch Quantity is ", self.a[i][0], " total price of the Watches is : ",
                      self.a[i][0] * self.watchesprice)
            if self.a[i][1] == "Kurta":
                self.total += self.a[i][0] * self.kurtaprice
                self.f.write("Kurta Quantity is "+str(self.a[i][0])+ " total price of the Kurta is : "+
                      str(self.a[i][0] * self.kurtaprice)+"\n")
                print("Kurta Quantity is ", self.a[i][0], " total price of the Kurta is : ",
                      self.a[i][0] * self.kurtaprice)
            if self.a[i][1] == "Pajamas":
                self.total += self.a[i][0] * self.pajamasprice
                self.f.write("Pajama Quantity is "+ self.a[i][0]+ " total price of the Pajama is : "+
                      str(self.a[i][0] * self.pajamasprice)+"\n")
                print("Pajama Quantity is ", self.a[i][0], " total price of the Pajama is : ",
                      self.a[i][0] * self.pajamasprice)

        self.f.write("The total bill of the customer is : "+str(self.total)+"\n")
        print("The total bill of the customer is : ",self.total)

        self.f.close()
    def history(self):
        print("------------------------------------------------------------------------------------------")
        # super().read(self.acc_name+'.txt')
        c = fileread()
        c.read(self.acc_name+'.txt')

    def Cheakout(self):
        print("CHEAKOUT\nSHIPPING HERE\nENTER YOUR DETAILS HERE")
        self.name = input("ENTER YOUR NAME : ")
        self.city = input("ENTER YOUR CITY NAME : ")
        self.country = input("ENTER YOUR COUNTRY NAME :")
        self.phoneNo = input("ENTER YOUR PHONE NUMBER : ")
        self.zipCode = input("ENTER ZIP CODE HERE : ")
        print('\nHERE YOU GO\nYOUR NAME ; '+ self.name + '\nYOUR CITY NAME : ' + self.city  + '\nYOUR COUNTRY NAME : ' + self.country + '\nYOUR PHONE NUMBER : ' +  str(self.phoneNo) + '\nYOUR ZIP CODE : ' + str(self.zipCode) + '\nYOUR TOTAL BILL : ' + str(self.total) + 'IN pkr')

    def option(self):
        while True:
            print("******************************************************************\n                     MENU                  \n\n1. View the list of product\n2. Add products\n3. remove products from the cart\n4. CHEAK-OUT ITEMS\n5. View shopping History\n6. FOR LOGOUT\n************************************************************")
            k = int(input("enter the option : "))
            if k == 1:
                self.category()
            elif k == 2:
                self.addToCart()
            elif k == 3:
                self.remove()
            elif k == 4:
                self.bill()
            # elif k == 4:
            #     self.Cheakout()
            elif k == 5:
                self.history()
            elif k ==6:
                self.logout()
            else:
                break
    def logout(self):
        b = userinterface()

        # self.login()






class Admin(menu, Reg):
    # kk = int(input("enater the code for login as admin : "))
    # if kk==123:
    #     print('LOGIN SUCCCESSFULLY AS ADMIN')
        def addAccount(self):
            print('Adding Account...')
            super().signup()
        def removeAccount(self):
            print('Removing Account...')
            super().del_records()
        def manageStock(self):
            print('MANAGE STOCK')
            super().addi()

        def calling(self):
            while True :
                print("You're an Admin, what do you want to do ?\n1. FOR ADD ACCOUNT\n2. FOR DELETE ACCOUNT\n3. FOR MANAGE STOCK\n4 .FOR EXIT")
                t = int(input())
                if t==1:
                    # print('Adding Account...')
                    # super().signup()
                    self.addAccount()
                elif t==2:
                    self.removeAccount()
                elif t==3:
                    self.addi()
                elif t==4:
                    sys.exit()
                else:
                    break

class userinterface:
    def __init__(self):
        print('########################################## \nMY BOUTIQUE :)\n \n1. LOGIN AS ADMIN\n2. LOGIN AS USER\n##########################################')
        k = int(input("ënter the option : "))
        if k ==1:
            while True:
                n = input('ENTER PASSWORD TO LOGIN AS ADMIN : ')
                if n.lower() == 'arbii':
                    w = Admin()
                    w.calling()
                    break
                else:
                    print('WRONG KEY, INSERT PLEASE')

        elif k ==2:
            print("1)signup \n2)login")
            gg = int(input("ënter the option : "))
            if gg == 1:
                w = Reg()
                w.signup()
                        # self.signup()
            elif gg==2:
                w = menu()
                w.login()
                w.logout()
        elif k == 3:
            sys.exit()









r = userinterface()
#
# r.user()



