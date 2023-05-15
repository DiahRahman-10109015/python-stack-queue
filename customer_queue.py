class Customer:
    def __init__(self, name, transaction):
        self.name = name
        self.transaction = transaction

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def display_next_transaction(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada antrian yang dapat ditampilkan")
        else:
            customer = self.queue[0]
            print(f"Transaksi berikutnya: {customer.transaction} - {customer.name}")

    def remove_completed_transaction(self):
        if self.is_empty():
            print("Antrian kosong tidak ada antrian yang dapat ditampilkan")
        else:
            customer = self.queue.pop(0)
            print(f"Menghapus transaksi yang telah dilayani: {customer.transaction} - {customer.name}")

queue = Queue()

while True:
    print("\nProgram Antrian!") 
    print("1. Menambahkan Transaksi ke Dalam Antrian")
    print("2. Menampilkan Transaksi Berikutnya")
    print("3. Hapus Transaksi yang Sudah Dilayani")
    print("4. Keluar")

    pilih = input("Masukkan pilihan (1/2/3/4): ")

    if pilih == "1":
        name = input("Masukkan Nama Pelanggan: ")
        transaction = input("Masukkan Jenis Transaksi: ")
        customer = Customer(name, transaction)
        queue.enqueue(customer)
        print("Transaksi berhasil ditambahkan ke antrian.")
    elif pilih == "2":
        queue.display_next_transaction()
    elif pilih == "3":
        queue.remove_completed_transaction()
    elif pilih == "4":
        print("Terima kasih! Program berakhir.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
