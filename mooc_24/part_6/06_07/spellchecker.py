# write your solution here
words = []
final_sentance = ""

with open("wordlist.txt", "r") as wordlist:
    #contents = wordlist.read()
    for line in wordlist:
        words.append(line.strip())

    sentance = str(input("Write text: "))

    words_check = sentance.split()

    for w in words_check:
        if w.lower() not in words:
            final_sentance += f'*{w}*' + " "
        else:
            final_sentance += w + " "
    
    print(final_sentance)




