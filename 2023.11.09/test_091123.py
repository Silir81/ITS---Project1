# 1. Se da codul de mai jos.
# Folositi metoda corecta pentru:
# - a sterge elementul ce se afla la indexul 5
# - printati lista

# code start
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
print(type(my_list))
print('Initial list \n',my_list)
my_list.pop(5)
print('Modified list \n',my_list,"\n")

# code end


# 2. Se da codul de mai jos.
# Folositi metoda corecta pentru:
# - a adauga elementul "C++" la sfarsitul listei
# - printati lista

# code start
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
print(type(my_list))
print('Initial list \n',my_list)
my_list.append("C++")
print('Modified list \n',my_list,'\n')

# code end


# 3. Creaza o functie care verifica daca parametru pasat ei este o vocala:
#  - returneaza "True" daca este, "False" daca nu este
# 4. Documenteaza functia
# code start
def verify_if_vowel(param_string):
    """

    :param param_string:
    :return:
    """
    # insert code here
    # hint: vowel(vocale) sunt a, e, i, o, u
    #Ne asiguram ca litera introdusa este o litera mica
    litera_mica_string = param_string.lower()
    # Verificam daca sirul are o singura litera. Daca da, si este o vocala, va returna valoarea True.
    # Altfel va returna valoarea False
    if len(litera_mica_string) == 1 and litera_mica_string in "aeiou":
        return True
    else:
        return False

# code end
#
# # 5. Se da codul de mai jos.
# # Folosind metoda de list comprehension, generati o noua lista ce sa contina:
# # - doar vocalele din stringul din cod
#
# # code start
the_string_1 = "The rain in Spain stays mainly on the plain"
my_new_list = [voc for voc in the_string_1 if voc.lower() in 'aeiou']

print(my_new_list)
print(type(my_new_list))
#
# # code end
#
# # 6. Se da codul de mai jos.
# # Folosind metoda de set comprehension, generati o noua lista ce sa contina:
# # - doar vocalele din stringul din cod
#
# # code start
# the_string_2 = "The rain in Spain stays mainly on the plain"
# my_new_list = {}
#
# print(my_new_list)
# print(type(my_new_list))
#
# # code end
#
# # 7. Cate tipuri de date de tip "colectie" cunoastesti? Insirati-le
# # Raspuns:
#-list, tuple, set si dictionaries
#
# # 8. Enumerati cel putin 2 metode de control flow.
# # Raspuns: Conditional, loops
#
# # 9. Explicati, folosind cuvintele voastre, functionalitate cuvantului cheie "pass".
# # Raspuns:
#
# # 10. Care este sintaxa corecta pentru a defini o functie in python?
# # Raspuns: def #function_name(Parameter: data type) => Return Expresion