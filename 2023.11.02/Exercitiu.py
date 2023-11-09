
# 1. Se da codul de mai jos.
# Folositi metoda corecta pentru ca:
# - inainte de a asigna la o noua variabila, convertiti, pe rand, variabila "my_var" in tipul de date (specificat
# in comment)

# code start
my_var = "10"

# convert to integer
my_int = int(my_var)
print(type(my_int))

# convert to float
my_float = float(my_var)
print(type(my_float))

# # convert to list
my_list = [my_var]
print(type(my_list))

# # convert to set
my_set = {my_var}
print(type(my_set))
# # code end


# 2. Se da codul de mai jos.
# Folosind metoda de list comprehension, generati o noua lista ce sa contina:
# - toate carcaterele corespunzand doar indexurilor impari
#
# # code start
x = "The days of Python 2 are almost over. Python 3 is the king now."

my_new_list = [x[i] for i in range(len(x)) if i % 2 != 0]

print(my_new_list)
print(type(my_new_list))
# code end


# 3. Se da codul de mai jos.
# Folosind metoda de list comprehension, generati o noua lista ce sa contina:
# - doar numerele impare din lista de mai jos
#
# code start
numbers = [3,5,45,97,32,22,10,19,39,43]

my_new_list = [x for x in numbers if x % 2 != 0]

print(my_new_list)
print(type(my_new_list))

# code end


# 4. Se da codul de mai jos.
# Folosind metoda de list comprehension, generati o noua lista ce sa contina:
# - toate numerele de la 0 la 1000 care au cifra 3 in componenta lor (de ex. 33, 83, 233)
#
# code start
my_new_list2 = [n for n in numbers if "3" in str(n)]

print(my_new_list2)
print(type(my_new_list2))

# code end

# 5. Se da codul de mai jos.
# Folosind metoda de list comprehension, generati o noua lista ce sa contina:
# - doar vocalele din stringul din cod
#
# code start
the_string = "The rain in Spain stays mainly on the plain"
my_new_list = [voc for voc in the_string if voc.lower() in 'aeiou']

print(my_new_list)
print(type(my_new_list))

# code end

# 6.5 Se da codul de mai jos.
# Folosind metoda de set comprehension, generati o noua lista ce sa contina:
# - doar vocalele din stringul din cod

# code start
the_string  = "The rain in Spain stays mainly on the plain"
# Nu putem folosi set comprehension pentru a genera o listă, deoarece set comprehension creează un set, nu o listă.
# Putem totusi crea un set care conține doar vocalele din șirul the_string folosind set comprehension
# și apoi putem converti set-ul într-o listă. Nu vo avea valori duplicate. https://www.w3schools.com/python/python_sets.asp
my_set = {voc1 for voc1 in the_string if voc1.lower() in 'aeiou'}
my_new_list = list(my_set)

print(my_new_list)
print(type(my_new_list))

# tema 10.txt
# Displaying tema 10.txt.