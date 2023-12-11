things = []
for i in range(5):
    things.append(input("a thing? "))

#delete phase
index = int(input("number 0-4"))
things.pop(index)

index = int(input("number 0-3"))
things.pop(index)

print(things)