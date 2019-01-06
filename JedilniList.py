# -*- encoding: utf-8 -*-

print "Hello user! Let's start with making your menu."

menu_list = {}

while True:
    name = raw_input("Insert name of the dish:")
    price = raw_input("Insert price of the dish:")

    menu_list[name] = price

    new = raw_input("Would you like to continue? yes/no")

    if new.lower() == "no":
        break

print "All items: %s" % menu_list


menu_file = open("menu.txt", "w+")
menu_file.write("Koncan menu:  \n")

for name, price in menu_list.iteritems():
     if new == "no":
         menu_file.write("- " + name  + ":"  + price + "€" + "\n")

menu_file.close()

print "END"
