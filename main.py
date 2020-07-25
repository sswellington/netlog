from ListenNet import ListenNet

if __name__ == '__main__':
    print("begin") # development variable
    try:
        t = ListenNet([22754])
        print(t.info)
        # t.report()
        print("ping:", t.ping)
        print("upload:", t.upload)
        print("download:", t.download)
    except ListenNet():
        raise SystemExit("Error 935: ListenNet")
print("end") # development variable