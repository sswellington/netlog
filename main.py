from ListenNet import ListenNet

if __name__ == '__main__':
    print("begin") # development variable
    try:
        t = ListenNet()
        print(t.info())
    except Error:
        print("Error 935: ListenNet")
print("end") # development variable