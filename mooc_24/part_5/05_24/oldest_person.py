def oldest_person(people: list):
    max = 10000
    person_max = ""

    for person in people:
        if person[1] < max:
            max = person[1]
            person_max = person[0]

    return person_max

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    people_list = [
        ('Emily', 2014), 
        ('Arthur', 1977)]

    print(oldest_person(people_list))