counter = 0

while counter < 10:
    counter += 1
    print(counter)

counter = 0
line = "*****"
while counter < 5:
    print(line)
    counter += 1

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i, j)
        j += 1
    i += 1

i = 0
while i < 6:
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print("")
    i += 1

i = 0
while i < 5:
    i += 1
    print("*" * i)

email = "student@localhost.ru"
print(email[4])
print(email[0])
print(email[-1])
print(len(email))

contains = '@' in email
print(contains)

not_contains = '#' not in email
print(not_contains)

data = [8, 16, 20, 15, 4]
current = data[0]
for datum in data:
    if current < datum:
        current = datum

print(current)

max_value = max(data)
min_value = min(data)
print(max_value)
print(min_value)

data = [8, 16, 20, 15, 4]
total = 0
for datum in data:
    total += datum

#scores = [1, 200, -50, 10, -20]

def negativ_count(scores):


    count = 0
    for score in scores:
        if score < 0:
            count += 1
    return count

