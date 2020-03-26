import requests
from bs4 import BeautifulSoup

def iterate(fishIter):
  return fishIter.find_next_sibling()

# fish data
result = requests.get("https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)")
src = result.content
soup = BeautifulSoup(src, 'lxml')
fishTable = soup.table.table

fish = fishTable.tr.find_next_sibling()
critterMap = {}

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

while fish != None:
  
  fishMonthsBool = [False]*12

  fishIter = fish.td
  fishName = fishIter.get_text().strip()
  fishIter = iterate(iterate(fishIter))
  fishData = [fishName]
  for i in range(0, 4):
    fishData.append(fishIter.get_text().strip())
    fishIter = iterate(fishIter)

  for i in range(0, 12):
    if fishIter.get_text().strip() != "-":
      fishMonthsBool[i] = True
    fishIter = iterate(fishIter)

  fishMonths = []
  allYearFlag = True
  for i in range(0, 12):
    if fishMonthsBool[i]:
      fishMonths.append(months[i])
    else:
      allYearFlag = False

  if allYearFlag:
    fishData.append("All Year")

  else:
    fishData.append(fishMonths)

  #is this a fish?
  fishData.append(True)

  critterMap[fishName.lower()] = fishData

  fish = iterate(fish)

# bug data
result = requests.get("https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)")
src = result.content
soup = BeautifulSoup(src, 'lxml')
bugTable = soup.table.find_next_sibling().find_next_sibling().table.table

bug = bugTable.tr.find_next_sibling()


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

while bug != None:
  
  bugMonthsBool = [False]*12

  bugIter = bug.td
  bugName = bugIter.get_text().strip()
  bugIter = iterate(iterate(bugIter))
  bugData = [bugName]
  for i in range(0, 3):
    bugData.append(bugIter.get_text().strip())
    bugIter = iterate(bugIter)

  for i in range(0, 12):
    if bugIter.get_text().strip() != "-":
      bugMonthsBool[i] = True
    bugIter = iterate(bugIter)

  bugMonths = []
  allYearFlag = True
  for i in range(0, 12):
    if bugMonthsBool[i]:
      bugMonths.append(months[i])
    else:
      allYearFlag = False

  if allYearFlag:
    bugData.append("All Year")

  else:
    bugData.append(bugMonths)

  #is this a fish?
  bugData.append(False)

  critterMap[bugName.lower()] = bugData

  bug = iterate(bug)


print("\nHowdy, welcome to my fish and bug info tool for Animal Crossing New Horizons\n")

print("With this tool, you can see the price of any fish or bug in the game, as well as where and when they can be caught.\n")

print("The size of a fish's shadow is on a scale of 1 to 6; 1 being the smallest and 6 being the biggest. If (fin) is listed, the shadow has a fin sticking out of the water, and narrow means it will have an eel shaped shadow.\n")

print("The current version of this tool only checks northern hemisphere availability. Support for southern hemisphere may come soon (but probably not)\n")

print("To use this tool, type the name of the fish or bug below, being sure to spell the name correctly. If at any point you wish to exit the tool, type 'exit' or press ctrl+C\n")

print("Lastly, this information is taken from https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons) and https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons). This tool is only as accurate as these sites (a disclaimer on the bug page claims the month info may be incorrect)\n")
print("Enjoy :)\n")

while True:
  critterToCheck = input("Please enter the name of a fish or bug:\n\n")
  print("")

  if critterToCheck.lower() == "exit":
    break

  if critterToCheck.lower() in critterMap:
    if critterMap[critterToCheck.lower()][-1]:
      print("********************************************************************************")
      print("Name:", critterMap[critterToCheck.lower()][0])
      print("Cost:", critterMap[critterToCheck.lower()][1])
      print("Location:", critterMap[critterToCheck.lower()][2])
      print("Size of Shadow:", critterMap[critterToCheck.lower()][3])
      print("Time of Day:", critterMap[critterToCheck.lower()][4])
      print("Available Months:", critterMap[critterToCheck.lower()][5])
      print("********************************************************************************\n")

    else:
      print("********************************************************************************")
      print("Name:", critterMap[critterToCheck.lower()][0])
      print("Cost:", critterMap[critterToCheck.lower()][1])
      print("Location:", critterMap[critterToCheck.lower()][2])
      print("Time of Day:", critterMap[critterToCheck.lower()][3])
      print("Available Months:", critterMap[critterToCheck.lower()][4])
      print("********************************************************************************\n")

  else:
    print("Given name is not the name of a fish or bug\n")
    

 

# fishName = fish.td.get_text().strip()

# print(fishName)

# fishPrice = fish.td.find_next_sibling().find_next_sibling().get_text().strip()

# print(fishPrice)



# fishName = fishIter.get_text().strip()

# fishIter = iterate(iterate(fishIter))

# fishPrice = fishIter.get_text().strip()

# fishIter = iterate(fishIter)

# fishLocation = fishIter.get_text().strip()

# fishIter = iterate(fishIter)

# fishSize = fishIter.get_text().strip()

# print(fishName)
# print(fishPrice)
# print(fishLocation)
# print(fishSize)
# while fishIter != None:
#   print(fishIter.get_text().strip())
#   fishIter = fishIter.find_next_sibling()


