''' file ini berisi data dari siswa,
    isi data :
        -> id kartu
        -> nama siswa
        -> masuk jam berapa
        -> pulang jam berapa

    karena hanya masih ada dua kartu maka siswanya ada dua dulu,
    nanti bisa ditambahkan sesuai keinginan.
    data beruap dictionay didalam list
 '''

siswa = [{'id': 932286074320, 'nama': 'Farid al hisni', 'nisn': '12345678', 'masuk': 0, 'keluar': 0}]

#cara menambahkan siswa
siswa.append({'id': 660981583203, 'nama': 'Ikhsan', 'nisn': '12345678', 'masuk': 0, 'keluar': 0})
siswa.append({'id': 932286074322, 'nama': 'Didik', 'nisn': '12345678', 'masuk': 0, 'keluar': 0})


# testing
# print(siswa[1])
