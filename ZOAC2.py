dictionary=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
starting_alphabet="A"
destination_alphabet=0

def minimum_distance(dictionary,starting_alphabet,destination_alphabet):
    for k in range(0,len(dictionary)):
        if dictionary[k]==starting_alphabet:
            start=k
        if dictionary[k]==destination_alphabet:
            destination=k
    if start-destination>0 or start==destination:
        absolute=start-destination
    if start-destination<0:
        absolute=destination-start
    if absolute<13 or absolute==13:
        return absolute
    if absolute>13:
        return 26-absolute



string_word=input()
word=[]
time=0
for k in range(0,len(string_word)):
    word.append(string_word[k])
for k in range(0,len(word)):
    destination_alphabet=word[k]
    time=time+minimum_distance(dictionary,starting_alphabet,destination_alphabet)
    starting_alphabet=destination_alphabet
print(time)
