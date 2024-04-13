Cruella = int(input("Jane always gets at least twice as many birthday cards as her older sister Cruella. How many cards did Cruella receive for her last birthday?"))
if Cruella < 0:
    print("You can't recieve negative cards! Rerun the code with a positive integer.")
    exit()
Jane = Cruella * 2
print("Jane recieves at least", Jane, "cards.")