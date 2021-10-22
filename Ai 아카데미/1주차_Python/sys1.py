import sys

# print(sys.argv)

# for a in range(int(sys.argv[1])):
#     print("Hello world",a)

with open ("new1.txt", "r") as new1:
    new2 = open("new2.txt","w")
    
    for line in new1.readlines():
        new2.write(line)
    
    new2.close()