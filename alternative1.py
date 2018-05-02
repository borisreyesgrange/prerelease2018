# CAMBRIDGE PRE-RELEASE 2018
# MODE: INDEPENDENT TASKS, step by step according the instructions

# GLOBAL CONDITIONS:
# Your program or programs must include appropriate prompts for the entry of data.
# Error messages and other output need to be set out clearly and understandably.
# All variables, constants and other identifiers must have meaningful names.

# TASK 1
# 1) The customer make a choice for each component...
# 2) ...and an estimate is produced.
# 3) The estimate must show a unique estimate number, the components chosen and the price of each component
# 4) The The estimate must also show the total cost of the computer, which is calculated as the sum
# of the cost of the components chosen plus 20%

# Declaring variables according to the choices in the table of components

# Processors
p3, p5, p7 = 100, 120, 200

# RAM Memories
ram16, ram32 = 75, 150

# Storage
sto1tb, sto2tb = 50, 100

#Screen
sc19, sc23 = 65, 120

# Case
mini, midi = 40, 70

# USB Ports
usb2, usb4 = 10, 20

# 1) The customer make a choice for each component...
# Declaring and initializing in cero, the 6 user input variables.
userProcessor = userRam = userSto = userScreen = userCase = userUsb = 0

print("Choose your Components, enter the number option 1, 2 or 3: ")

# Asking to the user for the components chosen, validating his options
while userProcessor not in ("1", "2", "3"):
    userProcessor= input("Processors: \n1)p3 = $100 \n2)p5 = $120 \n3)p7 = $200\n")
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

# You can take de value of each component from the variables, using "concatenate" (+) and string conversion:
# userProcessor = input("Processors: \n1)p3 = $"+str(p3)+" \n2)p5 = $"+str(p5)+" \n3)p7 = $"+str(p7)+"\n")
