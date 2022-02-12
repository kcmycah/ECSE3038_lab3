FRUITS_DB = [
  {
    "name": "apple",
    "sugar content": 10,
    "color": "red",
    "calories": 52
 },

 {
   "name": "banana",
   "sugar content": 12,
   "color": "yellow",
   "calories": 89
 },

 {
   "name": "orange",
   "sugar content": 9,
   "color": "orange",
   "calories": 47
 }
]

#for i in range(0,2): #counts from 0 to 1
# print(FRUITS_DB[i]["name"])
#for i in range(0,len(FRUITS_DB)): #gets the length of our list
#we use the virtual envuronment when we're using librarries
i = "something else" #this doesnt affect the for loop
for i in range(0, len(FRUITS_DB), 2): #increments  by 2
 print(f"the current element in the loops is {FRUITS_DB[i]['name']}")

for i in[0,1,2]:
 print(f"the value of i is {i}")

for fruit in FRUITS_DB:
    print(f"the current element in the loop is {fruit['name']}")