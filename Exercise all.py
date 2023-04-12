#Exercise1

TVseries='Game of Thrones'
Seasons=8
ListChapters=['T1 10Chapters', 'T2 10Chapters', 'T3 10Chapters', 'T4 10Chapters', 'T5 10Chapters', 'T6 10Chapters', 'T7 7Chapters', 'T8 6Chapters']
SerieCompleted=True

print(TVseries)
print(Seasons)
print(ListChapters)
print(SerieCompleted)

#Exercise2

FirstWord= TVseries[0:3]
NewSentence=FirstWord

print(NewSentence)

#Exercise3

print(ListChapters[0])

#Exercise4

NewSeasons= Seasons + 10

print(NewSeasons)

#Exercise5

print(ListChapters[-1])

#Exercise6

names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')

print(list_of_names)

#Exercise7

FirstWord= TVseries[0:4]
NewSentence=FirstWord.upper()


print(NewSentence)

NewTVseries=TVseries.replace(FirstWord,NewSentence)

print(NewTVseries)

#Exercise8

sentence= f'la serie {TVseries} tiene {NewSeasons}'

print(sentence)

#Exercise9

print('hello world')