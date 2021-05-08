from database import Connection

def main():
    db1 = Connection()
    db2 = Connection()

    if db1 is db2:
        print("Same connection")
    else:
        print("Different connections")

if __name__ == "__main__":
    main()
