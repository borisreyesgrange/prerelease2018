p3, p5, p7 = 100, 120, 200
ram16, ram32 = 75, 150
sto1tb, sto2tb = 50, 100
sc19, sc23 = 65, 120
mini, midi = 40, 70
usb2, usb4 = 10, 20

userProcessor = userRam = userSto = userScreen = userCase = userUsb = estimateNumber = totalPrice = componentIndex = 0
estimateComponents = ""

print("PRE-RELEASE 2018 - TASK 1\n")
print("Choose your Components, enter the option number 1, 2 or 3: ")

while userProcessor not in ("1", "2", "3"):
    userProcessor = input("Processors: \n1)p3 = $100 \n2)p5 = $120 \n3)p7 = $200\n")
while userRam not in ("1", "2"):
    userRam = input("RAM Memories: \n1)16GB = $75 \n2)32GB = $150\n")
while userSto not in ("1", "2"):
    userSto = input("Storage: \n1)1TB = $50 \n2)2TB = $100\n")
while userScreen not in ("1", "2"):
    userScreen = input("Screen: \n1)19' = $65 \n2)23' = $120\n")
while userCase not in ("1", "2"):
    userCase = input("Case: \n1)Mini Tower = $40 \n2)Midi Tower = $70\n")
while userUsb not in ("1", "2"):
    userUsb = input("USB: \n1)2 ports = $10 \n2)4 ports = $20\n")

componentsChosen = [userProcessor, userRam, userSto, userCase, userScreen, userUsb]

for component in componentsChosen:
    if component == "1":
        if componentIndex == 0:
            totalPrice += p3
            estimateComponents += "PROCESSOR:\t p3  \t $100\n"
            componentsChosen[componentIndex] = "p3"
        if componentIndex == 1:
            totalPrice += ram16
            estimateComponents += "RAM MEMORY:\t 16 GB\t $75\n"
            componentsChosen[componentIndex] = "ram16"
        if componentIndex == 2:
            totalPrice += sto1tb
            estimateComponents += "STORAGE:\t 1 TB\t $50\n"
            componentsChosen[componentIndex] = "sto1tb"
        if componentIndex == 3:
            totalPrice += sc19
            estimateComponents += "SCREEN:  \t 19' \t $65\n"
            componentsChosen[componentIndex] = "sc19"
        if componentIndex == 4:
            totalPrice += mini
            estimateComponents += "CASE:   \t mini T\t $40\n"
            componentsChosen[componentIndex] = "mini"
        if componentIndex == 5:
            totalPrice += usb2
            estimateComponents += "USB:    \t 2ports\t $10\n"
            componentsChosen[componentIndex] = "usb2"
        componentIndex += 1
    elif component == "2":
        if componentIndex == 0:
            totalPrice += p5
            estimateComponents += "PROCESSOR:\t p5  \t $120\n"
            componentsChosen[componentIndex] = "p5"
        if componentIndex == 1:
            totalPrice += ram32
            estimateComponents += "RAM MEMORY:\t 32 GB\t $150\n"
            componentsChosen[componentIndex] = "ram32"
        if componentIndex == 2:
            totalPrice += sto2tb
            estimateComponents += "STORAGE:\t 2 TB\t $100\n"
            componentsChosen[componentIndex] = "sto2tb"
        if componentIndex == 3:
            totalPrice += sc23
            estimateComponents += "SCREEN:  \t 23' \t $120\n"
            componentsChosen[componentIndex] = "sc23"
        if componentIndex == 4:
            totalPrice += midi
            estimateComponents += "CASE:   \t midi T\t $70\n"
            componentsChosen[componentIndex] = "midi"
        if componentIndex == 5:
            totalPrice += usb4
            estimateComponents += "USB:    \t 4ports\t $20\n"
            componentsChosen[componentIndex] = "usb4"
        componentIndex += 1
    elif component == "3":
        totalPrice += p7
        estimateComponents += "PROCESSOR:\t p7  \t $200\n"
        componentsChosen[componentIndex] = "p7"
        componentIndex += 1
estimateNumber +=1
print("*** ESTIMATE NUMBER: "+str(estimateNumber)+" ***")
print("COMPONENT\t OPTION\t PRICE")
print(estimateComponents+"\nTOTAL COST: $"+str(totalPrice*1.2)+"\n**************************\n")

print("PRE-RELEASE 2018 - TASK 2\n")
p3Stock = p5Stock = p7Stock = ram16Stock = ram32Stock = sto1tbStock = sto2tbStock = sc19Stock = sc23Stock = miniStock = midiStock = usb2Stock = usb4Stock = 10
stockCheck = 0
ordersNumbers = list()
customerName = ""

print("*** STOCK CHECK ***")
for component in componentsChosen:
    if eval(component+"Stock") > 0:
        print(str(component)+" ..... OK")
        stockCheck += 1
    else:
        print(str(component) + " ..... NO STOCK")
if stockCheck == 6:
    print("\n*** STOCK UPDATE ***")
    for component in componentsChosen:
        exec(str(component+"Stock -= 1"))
        print(str(component)+" -> "+str(eval(component+"Stock")))
ordersNumbers.append(estimateNumber)
customerName = input("\nEnter your name and last name to produce your final estimated: ")
