print("="*10,"Pattern Printer","="*10)

while True:
    print("""Pattern 1:
            1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5""")
    print("""Pattern 2:
            1
            2 2
            3 3 3
            4 4 4 4
            5 5 5 5 5""")
    print("""Pattern 3:
            5 4 3 2 1
            4 3 2 1
            3 2 1
            2 1
            1""")
    print("""Pattern 4:
                1
               121
              12321
             1234321
            123454321""")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Thank You! Exiting...")
        break

    if choice in ['1','2','3','4']:
        height = int(input("Enter the height of the pattern: "))

        if choice == '1':
            for i in range(height):
                for j in range(i+1):
                    print(j+1,end = " ")
                print()

        elif choice == '2':
            for i in range(height):
                for j in range(i+1):
                    print(i+1,end = " ")
                print()

        elif choice == '3':
            for i in range(height,0,-1):
                for j in range(i,0,-1):
                    print(j,end = " ")
                print()

        elif choice == '4':
            for i in range(1, height + 1):

                # print spaces
                for s in range(height - i):
                    print(" ", end="")

                # print increasing numbers
                for j in range(1, i + 1):
                    print(j, end="")

                # print decreasing numbers
                for j in range(i - 1, 0, -1):
                    print(j, end="")

                print()
    
    else:
        print("Invalid Choice! Please enter again.")

