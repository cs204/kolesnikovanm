d = input("Приветствие: ")
if d.startswith("здравствуйте"):
	print("$0")
elif (d.startswith("з")) and (not d.startswith("здравствуйте")):
    print("$20")
else:
	print("$100")