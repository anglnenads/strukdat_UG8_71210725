class NodePelanggan:
    def __init__(self, namaPelanggan,n):
        self._namaPelanggan = namaPelanggan
        self._next = n
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        self._head=None
        self._tail=None
        self._size = 0 
        # self._data = []
       #tulis kode anda di sini
       
    def __len__(self): #mengembalikan ukuran Queue
        return self._size
        # tulis kode anda di sini

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self._size == 0
        # tulis kode anda di sini

    def dequeue(self): #menghapus data paling depan (front)
        if self.is_empty() == False:
            value = self._head._next
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                hapus = self._head
                self._head = self._head._next
                print("### Pelanggan {} selesai membayar ###".format(hapus.getNamaPelanggan()))
                del hapus
            self._size -= 1
            # return value
        else:
            return None
        
        # print("### Pelanggan {} selesai membayar ###".format(value))
        # n = NodePelanggan.getNamaPelanggan(self._size[0])
        # self._size = self._size[:1]
        # print("### Pelanggan {} selesai membayar ###".format(n))
        # tulis kode anda di sini

    def enqueue(self, namaPelanggan): #menambah data ke list
        baru = NodePelanggan(namaPelanggan, None)
        if self.is_empty()==True:
            self._head = baru
            self._tail = baru
        else:
            self._tail._next = baru
            self._tail = baru
        self._size += 1
        # tulis kode anda di sini

    def resize(self, cap): #mengubah ukuran queue pada list
        cap = self.DEFAULT_CAPACITIY
        self.DEFAUT_CAPACITY = cap*2
        print("Melakukan Resize")
        print()
        # tulis kode anda di sini
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        print("=== Kasir ===")
        # for i in range(self.DEFAULT_CAPACITY):
        #     if i >= self._size:
        #         print("{}.{}".format(i+1,self._namaPelanggan))
        # bantu = self._head
        # while bantu != None:
        #     print(bantu._namaPelanggan)
        #     bantu = bantu._next
        # if bantu._next == None:
        #     print("Kosong")

        bantu = self._head
        for i in range(self.DEFAULT_CAPACITY):
            if i >= self._size:
                print("{}.Kosong".format(i+1))
                bantu = bantu._next
            else:
                # print("{}.{}".format(i+1,NodePelanggan.getNamaPelanggan(self._size[i])))
                print("{}.{}".format(i+1,bantu._namaPelanggan))
                bantu = bantu._next
        
        print()
        # tulis kode anda di sini
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

