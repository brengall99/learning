# Write your solution here
def older_people(people: list, year: int):
    maximum = year
    people_list = []

    for person in people:
        if person[1] < maximum:
            people_list.append(person[0])

    return people_list

if __name__ == "__main__":
    people = [
        ("Adam", 1977), 
        ("Ellen", 1985), 
        ("Mary", 1953), 
        ("Ernest", 1997)]

    older = older_people(people, 1979)
    print(older)