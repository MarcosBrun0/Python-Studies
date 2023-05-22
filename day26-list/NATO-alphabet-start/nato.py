import pandas



df = pandas.read_csv("/home/mb/Documents/codes/PythonCourse/day26-list/NATO-alphabet-start/nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for(index, row) in df.iterrows()}
print(nato_dict)


word = input("write a word:")
word = word.upper()

nato_list = [ nato_dict[n] for n in word]
print(nato_list)