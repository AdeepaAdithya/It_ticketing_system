import time
print("If you want to signup please enter y and if you don't please press enter")
b = input()
if b:
    q = input("Enter the new username: ")
    w = input("Enter the new password: ")
    e = (q+".txt")
    u = (w+".txt")
    with open(e, "w") as r:
        r.write(w)
    with open(u, "w") as r:
        r.write(w)
    print("Done")
    time.sleep(5)
else:
    x=input("what's your username? ")
    y=input("what's your password? ")
    v=(x+".txt")
    t=(y+".txt")
    with open(v) as p:
        lines = p.readlines()

    with open(t) as p:
        lines = p.readlines()


    print("#################################")
    print("dashboard")
    print("#################################")
    print("To create a ticket enter n and to view the tickets press enter.")
    a = input()
    if a:
     print("new ticket please enter the problem")
     b = input()
     k = input("Enter the name of the error: ")
     c = (k+".txt")

     with open(c, "w") as f:
            f.write(b)
            print("done")
            time.sleep(5)
    else:
          print("enter the name of the error ")
          l = input()
          z = (l+".txt")
          with open(z) as f:
              lines = f.readlines()
              print(lines)
          time.sleep(60)


exit()
