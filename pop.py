s1 = {1, 2, 3, 4}
print("Before popping: ",s1)
s1.pop()
s1.pop()
s1.pop()
print("After 3 elements popped, s1:", s1)
#Setel Metode pop() dengan Python
#Python Set pop() adalah metode dalam Python yang
#digunakan untuk menghapus dan mengembalikan elemen acak
#apa pun dari set. Seperti kita ketahui, Set adalah
#kumpulan elemen unik yang tidak berurutan, jadi tidak
#ada jaminan elemen mana yang akan dihapus dan
#dikembalikan oleh metode pop(). Jika set kosong,
#memanggil pop() akan memunculkan KeyError.
s1 = {9, 1, 0}
s1.pop()
print(s1)
#Bagaimana Python mengatur issubset() Bekerja
#Dalam kode ini, ia memeriksa apakah himpunan A adalah
#himpunan bagian dari himpunan B dan kemudian apakah
#himpunan B adalah himpunan bagian dari himpunan A.
#Pernyataan cetak pertama mengembalikan True karena
#semua elemen himpunan A juga ada di himpunan B.
#Pernyataan cetak kedua mengembalikan Salah karena
#himpunan B berisi unsur-unsur yang tidak ada dalam
#himpunan A.
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print(A.issubset(B))
print(B.issubset(A))
#Contoh Metode set issubset() Python
#Kode ini memeriksa apakah set s2 adalah subset dari sets1 dan mencetak True jika itu adalah.
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1))