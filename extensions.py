d = input("File name: ")
#match d:
	#case "hello.jpg":
		#print("image/jpeg")
	#case "document.pdf":
		#print("application/pdf")

if d.endswith(".gif"):
	print("image/gif")
elif d.endswith(".jpg"):
	print("image/jpeg")
elif d.endswith(".jpeg"):
	print("image/jpeg")
elif d.endswith(".png"):
	print("image/png")
elif d.endswith(".pdf"):
	print("application/pdf")
elif d.endswith(".txt"):
    print("text/plain")
elif d.endswith(".zip"):
	print("application/zip")
else:
	print("application/octet-stream")