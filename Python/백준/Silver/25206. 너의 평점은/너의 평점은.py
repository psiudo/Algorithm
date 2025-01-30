import sys

grade = {
    "A+" : 4.5, "A0" : 4.0, "B+" : 3.5,
    "B0" : 3.0, "C+" : 2.5, "C0" : 2.0,
    "D+" : 1.5, "D0" : 1.0, "F" : 0.0, 
}

total_score = 0
total_credit = 0

for line in sys.stdin :
    line = line.strip()
    if not line :
        continue
    
    word = line.split()

    if word[2] == "P" :
        continue
    else :
        total_score += grade[word[2]] * float(word[1])
        total_credit += float(word[1])

if total_credit != 0:
    print(total_score / total_credit)
else:
    print(0.0)