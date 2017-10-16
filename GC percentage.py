print("hello friends! How are you doing today?")
input()

Friend1 = input("Hey, I'm doing great! How about yourself?")

Friend1 = input("Let's learn how to calculate GC percentage in a DNA template")

Friend2 = input("Sure, That sounds so damn cool! Could you teach me how to calculate GC percentage in DNA Template?")

Friend1 = input("Sure! In any Template DNA, you can calculate gc percentage using following formula")

Friend2 = input("thanks friend! let me try and calculate gc percentage for my DNA Template1")

template1 = input("Enter DNA Template")

totalGbases= template1.count('G')

print(totalGbases)

totalCbases= template1.count('C')

print(totalCbases)

totalbases= len(template1)

print(totalbases)

GCpercentage = ((totalGbases + totalCbases)/totalbases)*100

print(GCpercentage)

