# Iterables setelah konversi
print("The Range after conversion is :")
# fungsi set() pada kamus
# deklarasi list
dic1 = { 4 : 'geeks', 1 : 'for', 3 : 'geeks' }
# cetal librari
# iternal sorted
print("Dictionary before conversion is : " + str(dic1))
# kamus setelah konfersi
print("Dictionary after conversion is : " +
str(set(dic1)))
#Hapus Elemen dari Set menggunakan Metode pop()
def Remove(initial_set):
  initial_set.pop()
  print(initial_set)
initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)
