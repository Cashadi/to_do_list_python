next_id = 1

def get_next_id():
    global next_id
    result = next_id
    next_id += 1
    return result


def menu():
    print("\n=== Aplikasi To-Do List ===")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Edit Tugas")
    print("6. Keluar")


def lihat_tugas(tasks):
    if not tasks:
        print("Belum ada tugas.")
    else:
        print("\n=== Daftar Semua Tugas ===")
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Judul: {task['title']}")
            print(f"Deskripsi: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Estimasi Waktu: {task['estimasi_waktu_pengerjaan']} menit")
            print("-" * 40)


def tambah_tugas(tasks):
    global next_id
    title = input("Masukkan judul tugas: ")
    description = input("Masukkan deskripsi tugas: ")

    task_id = get_next_id()
    status = "Belum Selesai"

    estimasi = 45 if task_id % 2 == 0 else 30

    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": status,
        "estimasi_waktu_pengerjaan": estimasi
    }

    tasks.append(task)
    print(f"Tugas '{title}' berhasil ditambahkan dengan ID {task_id}!\n")


def tandai_selesai(tasks):
    if not tasks:
        print("Belum ada tugas untuk ditandai.")
        return

    lihat_tugas(tasks)

    while True:
        try:
            task_id = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
            for task in tasks:
                if task["id"] == task_id:
                    if task["status"] == "Selesai":
                        print("Tugas ini sudah selesai sebelumnya.")
                    else:
                        task["status"] = "Selesai"
                        print(f"Tugas '{task['title']}' berhasil ditandai selesai.")
                    return
            print("ID tugas tidak ditemukan. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def hapus_tugas(tasks):
    if not tasks:
        print("Tidak ada tugas untuk dihapus.\n")
        return

    lihat_tugas(tasks)

    while True:
        try:
            task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
            for task in tasks:
                if task["id"] == task_id:
                    if task["status"] == "Selesai":
                        tasks.remove(task)
                        print(f"Tugas dengan ID {task_id} berhasil dihapus.\n")
                    else:
                        print("Tugas belum selesai, tidak bisa dihapus!\n")
                    return
            print("Tugas dengan ID tersebut tidak ditemukan. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Harus berupa angka. Coba lagi.\n")


def edit_tugas(tasks):
    if not tasks:
        print("Tidak ada tugas untuk diedit.\n")
        return

    lihat_tugas(tasks)

    while True:
        try:
            task_id = int(input("Masukkan ID tugas yang ingin diedit (atau 0 untuk batal): "))
            if task_id == 0:
                print("Edit dibatalkan.\n")
                return

            for task in tasks:
                if task["id"] == task_id:
                    if task["status"] == "Selesai":
                        print("Tugas sudah selesai, tidak bisa diedit.\n")
                        return
                    else:
                        print(f"\nMengedit tugas: {task['title']}")
                        new_title = input("Masukkan judul baru (kosongkan jika tidak diubah): ")
                        new_description = input("Masukkan deskripsi baru (kosongkan jika tidak diubah): ")

                        if new_title.strip():
                            task["title"] = new_title
                        if new_description.strip():
                            task["description"] = new_description

                        print("Tugas berhasil diperbarui!\n")
                        return
            print("ID tugas tidak ditemukan. Coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def main():
    tasks = []

    while True:
        menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            lihat_tugas(tasks)
        elif choice == '2':
            tambah_tugas(tasks)
        elif choice == '3':
            tandai_selesai(tasks)
        elif choice == '4':
            hapus_tugas(tasks)
        elif choice == '5':
            edit_tugas(tasks)
        elif choice == '6':
            print("Terima kasih, aplikasi ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
