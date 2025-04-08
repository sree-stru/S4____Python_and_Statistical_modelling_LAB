d = {}

while True:
    print("\n1. Add Stock")
    print("2. Update Stock")
    print("3. Delete Stock")
    print("4. Search Stock")
    print("5. Display Stocks")
    print("6. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if ch == 1:
        print("\nAdd Stock")
        bn = input("Enter Book Name: ")

        if bn in d:
            print(bn, "already exists.")
        else:
            try:
                d[bn] = int(input("Enter Stock Quantity: "))
            except ValueError:
                print("Please enter a valid quantity.")

    elif ch == 2:
        print("\nUpdate Stock")
        bn = input("Enter Book Name: ")

        if bn in d:
            try:
                addn = int(input("Enter number of stocks to be added: "))
                d[bn] += addn
            except ValueError:
                print("Please enter a valid number.")
        else:
            print(bn, "doesn't exist.")

    elif ch == 3:
        print("\nDelete Stock")
        bn = input("Enter Book Name to be deleted: ")

        if bn in d:
            del d[bn]
            print(bn, "deleted.")
        else:
            print(bn, "doesn't exist.")

    elif ch == 4:
        print("\nSearch Stock")
        bn = input("Enter Book Name to search: ")

        if bn in d:
            print("Book Name:", bn)
            print("Stocks:", d[bn])
        else:
            print(bn, "doesn't exist.")

    elif ch == 5:
        print("\nDisplay Stocks")
        print(f"{'Book Name':<20}{'Stock':<5}")
        for book, stock in d.items():
            print(f"{book:<20}{stock:<5}")

    elif ch == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose between 1 to 6.")
