import threading
import time

rekening_A = threading.Lock()
rekening_B = threading.Lock()

def transfer_dengan_ordering(dari, ke, jumlah):
    """Transfer dengan urutan lock konsisten"""
    # KUNCI: Semua thread HARUS ambil A dulu, baru B
    print(f"Transfer {dari}->{ke}: Kunci A dulu ...")
    with rekening_A:
        print(f"Transfer {dari}->{ke}: A terkunci!")
        time.sleep(0.3)

        print(f"Transfer {dari}->{ke}: Kunci B...")
        with rekening_B:
            print(f"Transfer {dari}->{ke}: Berhasil! Rp{jumlah}\n")

# Jalankan
t1 = threading.Thread(target=transfer_dengan_ordering, args=("A", "B", 100))
t2 = threading.Thread(target=transfer_dengan_ordering, args=("B", "A", 50))

t1.start()
t2.start()

t1.join()
t2.join()

print("SUKSES! Tidak ada deadlock karena urutan lock sama")
