buah_yang_tersedia = ['jeruk', 'mangga', 'melon']
buah_yang_dicari = input('Masukkan nama buah dalam huruf kecil: ')

if (buah_yang_dicari in buah_yang_tersedia):
  if (buah_yang_dicari == 'jeruk'):
    print('Buah yang anda cari adalah jeruk!')
  else :
    print('Buah yang anda cari bukan jeruk!')
  print('Buah yang anda cari tersedia!')
else:
  print('Buah yang anda cari tidak tersedia!')