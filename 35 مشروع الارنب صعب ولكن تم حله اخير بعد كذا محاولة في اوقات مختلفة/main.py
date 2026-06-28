‎#Saturday, ‎August ‎2, ‎2025, ‏‎12:33:40 AM

print("wellcom to place the rabbit")
print("""    [🌿, 🌿, 🌿 ]
    [🌿, 🌿, 🌿 ]
    [🌿, 🌿, 🌿 ]""")
num = []
meme= [["🌿", "🌿", "🌿" ], ["🌿", "🌿", "🌿" ],["🌿", "🌿", "🌿" ]]
print("where should the rabbit go 🐰 ? ")
in1= input("please enter the row and the column ")
num.append(int(in1[0]))
num.append(int(in1[1]))
num1 = num[0]
num2 = num[1]
print("success")
meme[num1-1].remove("🌿")
meme[num1-1].insert(num2-1,"🐰")         
print(meme[0])
print(meme[1])
print(meme[2])
----------------------------------------
#sec time in different time
#Saturday, ‎March ‎28, ‎2026, ‏‎11:46:26 AM
rabbit_house = [["🌿", "🌿", "🌿" ], ["🌿", "🌿", "🌿" ],["🌿", "🌿", "🌿" ]]
print("wellcom to place the rabbit")
print("""    [🌿, 🌿, 🌿 ]
    [🌿, 🌿, 🌿 ]
    [🌿, 🌿, 🌿 ]""")
print("where should the rabbit go 🐰 ? ")
qu = input("please enter a row and column ")
row = int(qu[0])
column = int(qu[1])
rabbit_house[row-1][column-1]="🐰"
print(rabbit_house[0])
print(rabbit_house[1])
print(rabbit_house[2])
