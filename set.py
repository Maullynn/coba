#Contoh Set Kosong
s = set()
print("Type of s is ",type(s))
# Deklarasi List
lis1 = [ 3, 4, 1, 4, 5 ]
# Cetak ITerasi sebelum Konversi
print("The list before conversion is : " + str(lis1))
# Iterables setelah konversi
print("The list after conversion is : " +
str(set(lis1)))
#set() pada tuple
# deklarasi tuple
tup1 = (3, 4, 1, 4, 5)
# cetak iterasi sebelum konversi
print("The tuple before conversion is : " + str(tup1))
# Iterables after conversion are
# notice distinct and elements
print("The tuple after conversion is : " +
str(set(tup1)))
# fungsi set() poda range
# deklarasi range
r = range(5)
r=set(r)
str(r)
