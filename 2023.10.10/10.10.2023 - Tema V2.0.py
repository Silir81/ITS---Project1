# Defineste un dictionar pentru valorile de la 1 la 10
word_to_int = {
    'unu': 1,
    'doi': 2,
    'trei': 3,
    'patru': 4,
    'cinci': 5,
    'sase': 6,
    'sapte': 7,
    'opt': 8,
    'noua': 9,
    'zece': 10
}

# Introduceti numarul
input_word = input("Introduceti un numar de la 'unu' to 'zece': ").lower()  # Converteste stringul in lowercase

# Converteste numarul in integer folosind datele din dictionar(word_to_init)
if input_word in word_to_int:
    integer_equivalent = word_to_int[input_word]
    print(f"Integer equivalent: {integer_equivalent}")
else:
    print('Cuvantun introdus ne se afla in range-ul "unu" la "zece".')
