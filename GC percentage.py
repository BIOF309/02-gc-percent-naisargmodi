print("hello friends! How are you doing today?")
input()

Friend1 = input("Hey, I'm doing great! How about yourself? ")

Friend1 = input("Let's learn how to calculate GC percentage in a DNA template ")

Friend1 = print("In any DNA sequence,GC percentage= (Total no. of G&C bases/total no. of bases in DNA template)*100")

seq = input("Enter DNA sequence: ")

seq = seq.upper()

totalGbases= seq.count('G')

print("totalGbases=", totalGbases)

totalCbases= seq.count('C')

print("totalCbases=", totalCbases)

totalbases= len(seq)

print("totalbases=", totalbases)

GCpercent= ((totalGbases + totalCbases)/totalbases)*100

print("GCpercent=", GCpercent)

