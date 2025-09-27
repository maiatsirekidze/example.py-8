
print(" TCP თუ UDP ")

q1 = input("გჭირდება თუ არა სანდო კავშირი, სადაც ყველა პაკეტი მივა? (კი/არა): ")
q2 = input("გირჩევნია თუ არა სისწრაფე სანდოობაზე მეტად? (კი/არა): ")
result="არასწორი input"
if q1.lower() == "კი" and q2.lower() == "არა":
    result = "TCP"
elif q1.lower() == "არა" and q2.lower() == "კი":
    result = "UDP"
elif q1.lower()=="არა" and q2.lower()=="არა":
    result="შეგიძლია გამოიყენო ორივე,TCP გირჩევდი"
elif q1.lower()=="კი" and q2.lower()=="კი":
    result= "TCP"

print(f" თქვენ აირჩიეთ: {result}")

