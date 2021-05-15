marks = {"maths": 80, "science": 76, "kiswahili": 60 , "social studies": 77, "english": 69}
print(marks)
key = marks.keys()
print(key)
value = marks.values()
print(value)
print("kiswahili" in marks)
marks["history"] = 80
print(marks)
games = ["football", "sandbox", "simulation", "shooters"]
games.append("puller")
print(games)
games_from_kenya = ["ruby", "sport", "action adventure"]
games.extend(games_from_kenya)
print(games)
games.pop()
print(games)
games.insert(2, "basketball")
print(games)

j = [19, 40, 30.8, 30, 100, 90, ]
for t in j:
    print(t)
    module = [p%7 for p in j]
    print(module)
    multiplication = [f%7 for f in j]
    print(module)

    p = (19, 40, 33, 70, 10)
    for y in p:
        print(y*y*y)


words = ["bat", "market", "caroline", "history"]
for m in words:
    print(m, len(m))

    k = range(0, 10)
    for t in k:
        print(t)

        def multiplication(* args):
            answer = 1
            for l in args:
                answer *= l
                print(answer)
                multiplication(10, 55, 33, 79, 20)

                p = range(30, 50)
                for y in p:
                    if y % 2 != 0:
                        print(y)











