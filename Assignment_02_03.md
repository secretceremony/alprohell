# Assignment 02

Group members
- Muhammad Kevin Wardhana (11231057) (Problem 2)
- Revalina Putria Hidayat (16231049) (Problem 3)
- Riska Fadlun Kahiriyah P (10231083) (Problem 4)
- Damasus Hardiven Waruwu (16231014) (Problem 5)
- Ansellma Tita Pakartiwuri Putri (10231017) (Problem 1 & 6)


## Problem 1: Automated symbol printing 1
Menggunakan _method_ pada _String_: `.rjust()`, `.ljust()` dan `.center()`,
susunlah logo ITK berikut.

```
IIIIIIIII   TTTTTTTTT   KKK   KKK
   III         TTT      KKK KKK
   III         TTT      KKKKKK
   III         TTT      KKK KKK
IIIIIIIII      TTT      KKK   KKK
```
Logo di atas memliki lebar `n = 3`. Perhatikan untuk `n = 3`
lebar huruf `3n` dan tinggi huruf `2n - 1` dan jarak antar antar
huruf adalah `n`.

Uji untuk ukuran logo `n = 5`, `n = 7`, dan `n = 9`

### Answer
Code:
```
def generate_logo(n):
    width = 3 * n
    height = 2 * n - 1

    # Membuat string untuk setiap baris
    lines = [
        "IIIIIIIII" + " " * n + "TTTTTTTTT" + " " * n + "KKK   KKK",
        "   III   " + " " * n + "   TTT   " + " " * n + "KKK KKK  ",
        "   III   " + " " * n + "   TTT   " + " " * n + "KKKKKK   ",
        "   III   " + " " * n + "   TTT   " + " " * n + "KKK KKK  ",
        "IIIIIIIII" + " " * n + "   TTT   " + " " * n + "KKK   KKK",
    ]

    # Cetak logo
    for line in lines:
        print(line.center(width))

# Uji untuk ukuran logo n = 5, n = 7, dan n = 9
sizes = [5, 7, 9]

for size in sizes:
    print(f"Logo untuk n = {size}:")
    generate_logo(size)
    print("\n")

```
Output:
![image](2.png)


## Problem 2: Automated symbol printing 2
Melanjutkan Problem 1. Tambahkan fitur berikut:
1. Masukan oleh _user_ logo yang ingin dicetak
   `logo_name: `
2. Masukan oleh _user_ ukuran logo `n: `

Contoh program
```
logo_name: KMITK
        n: 3

Hasil cetak logo

KKK   KKK   MMM         MMM   IIIIIIIII   TTTTTTTTT   KKK   KKK
KKK KKK     MMMM       MMMM      III         TTT      KKK KKK
KKKKKK      MMMMMM   MMMMMM      III         TTT      KKKKKK
KKK KKK     MMM   MMM   MMM      III         TTT      KKK KKK
KKK   KKK   MMM         MMM   IIIIIIIII      TTT      KKK   KKK
```
Lihat acuan semua karakter _alphanumeric_ di tautan berikut
[alphanumeric specs](./letter_spesification.md)

[Opsional (boleh dikerjakan atau tidak)] Untuk `n = 5`, `n = 7`, dan `n = 9`, silahkan 
dibuat terlebih dahulu spesifikasinya.

### Answer
```

```

## Problem 3
Buatlah suatu program _String Validator_ untuk _password_ 
menggunakan _methods_ berikut:
`isalpha()`, `isalnum()`, `isdigit()`, `islower()`, `isupper()`
dengan spesifikasi sebagai berikut:
- Jumlah karakter minimum 8 maksimum 16
- Hanya terdiri dari bilangan, abjad, dan _special characters_: `_`, `+`, `?`
- Minimum karakter bilangan 1, minimum karakter abjad 1, minimum
  _special characters_ 1

[Opsional (boleh dikerjakan atau tidak)]: Susunlah kode program Python hanya dalam satu baris kode

### Answer

```
import string

def is_valid_password(password):
    if 8 <= len(password) <= 16:
        if all(char in string.ascii_letters + string.digits + '_+?' for char in password):
            has_digit = any(char.isdigit() for char in password)
            has_alpha = any(char.isalpha() for char in password)
            has_special = any(char in '_+?' for char in password)

            if has_digit and has_alpha and has_special:
                return True

    return False

password = input("Masukkan password: ")

if is_valid_password(password):
    print("Password valid!")
else:
    print("Password tidak valid. Pastikan memenuhi semua kriteria.")
```

## Problem 4
Diberikan data _string_ di Python sebagai berikut:
```py
inventory = "apple emerald brick bone brick coal emerald bone apple brick brick coal bone emerald bone bone apple apple coal bone bone apple brick brick coal brick brick apple brick coal bone brick bone coal apple apple brick apple bone apple brick apple bone apple emerald coal emerald apple brick brick coal brick apple apple bone apple emerald bone bone brick bone bone apple emerald emerald bone brick emerald brick emerald apple bone coal coal coal bone brick bone bone emerald bone emerald coal coal emerald brick brick emerald emerald bone apple brick bone brick emerald brick apple bone apple brick"
```

Hitunglah frekuensi tiap kata dan simpanlah dalam bentuk _dict_ di Python
di variabel `inventory_dict`.

Contoh output program ketika mencetak `inventory_dict`:
```
  apple = 21
emerald = 16
  brick = 25
   bone = 25
   coal = 13
```

### Answer
```
inventory = "apple emerald brick bone brick coal emerald bone apple brick brick coal bone emerald bone bone apple bone apple coal bone bone apple brick brick coal brick brick apple brick coal bone brick bone coal apple apple brick apple bone apple brick apple bone apple emerald coal emerald apple brick brick coal brick apple apple bone apple emerald bone bone brick bone bone apple emerald emerald bone brick emerald brick emerald apple bone coal coal coal bone brick bone bone emerald bone emerald coal coal emerald brick brick emerald emerald bone apple brick bone brick emerald brick apple bone apple brick"
words = inventory.split()
inventory_dict = {}
for word in words:
    if word in inventory_dict:
        inventory_dict[word] += 1
    else:
        inventory_dict[word] = 1
for word, count in inventory_dict.items():
    print(f"{word.ljust(10)} = {count}")
```

## Problem 5: CLI histogram 1
Diberikan suatu data _inventory_ beberapa _materials_ di dalam _video game_
_Mineraft_ sebagai berikut, 
yang dinyatakan dalam bentk _dict_ Python
```py
inventory = {
  "Emerald": 2,
  "Diamond": 30,
  "Redstone": 11,
  "Brick": 28,
  "Coal": 17,
  "Snowball": 0
  "Leather": 10,
  "Paper": 9,
  "Flint": 4,
}
```

Buatlah program Python yang dapat mengubah data _dict_ tersebut ke dalam 
bentuk histogram sebagai berikut:
```
Tabel inventory:
 Emerald: **
 Diamond: ******************************
Redstone: ***********
   Brick: ****************************
    Coal: *****************
Snowball:
 Leather: **********
   Paper: *********
   Flint: ****
```

Jumlha tanda bintang `*` menyatakan banyaknya _materials_. Misal
`"Flint": 4` maka akan tercetak empat kali tanda bintang `****`.
Perhatikan juga nama _materials_ memiliki kesejajaran (_alignment_)
rata-rata kanan dan ada satu spasi setelah `:`.

### Answer

```
inventory = {
  "Emerald": 2,
  "Diamond": 30,
  "Redstone": 11,
  "Brick": 28,
  "Coal": 17,
  "Snowball": 0,
  "Leather": 10,
  "Paper": 9,
  "Flint": 4
}

max_length = max(len(material) for material in inventory.keys())

print("Tabel inventory:")
for material, count in inventory.items():
    stars = "*" * count

    print(f"{material:{max_length}s}: {stars}")
```

## Problem 6: CLI histogram 2
Melanjutkan Problem 5, tambahkan beberapa fitur berikut:
1. Masukan oleh _user_ `lebar_max` dengan type data `int` 
   untuk membatasi lebar histogram.   
 
   $`lebar_max` ini menyatakan berapa banyak tanda bintang `*`
   yang harus dicetak untuk _materials_ dengan jumlah terbanyak.   

   Misalkan _material_ terbanyak `"Diamond": 30` untuk `lebar_max = 50` 
   maka jumlah tanda bintang yang harus tercetak adalah 50 buah. 
   Sedangkan untuk _materials_ yang lain mengikut aturan normalisasi ini. 
   Contoh untuk `"Flint": 4`, maka tanda bintang yang tercetak sebanyak
   `(4/jumlah_material_terbanyak) * lebar_max = (4/30) * 50 = 6.7 = 7`
   (dibulatkan ke bilangan bulat terdekat). 
   
   Pembulatan dapat menggunakan 
   perintah `round()`.

2. Masukan oleh _user_ `is_sorted?` dengan jawaban `y` atau `n`
   untuk mengurutkan secara alfabet nama _materials_.
3. Tambahan angka penunjuk setelah nama _materials_ yang menyatakan
   banyaknya _materials_ tersebut dalam format digit yang sama.
   Misal nilai tertinggi 2 digit, yaitu 30, maka untuk digit-digit yang
   hanya terdiri dari satu digit perlu dilakukan _zero padding_ seperti
   yang ditampilkan contoh di bawah.

Contoh output program:
```
lebar_max: 30 
is_sorted? y

=================
 Tabel inventory 
=================
   Brick [28]: ****************************
    Coal [17]: *****************
 Diamond [30]: ******************************
 Emerald [02]: **
   Flint [04]: ****
 Leather [10]: **********
   Paper [09]: *********
Redstone [11]: ***********
Snowball [00]:
```

Lakukan pengujian untuk `lebar_max = 80` dan data _inventory_ berikut:

```py
inventory = {
  "Lead": 15,
  "Bread": 79,
  "Apple": 22,
  "Bone": 75,
  "Hoe": 1,
  "Pickaxe", 60,
  "Egg": 13,
  "Milk": 17,
  "Slimeball", 94,
  "Salmon": 29,
  "Potato": 45,
  "Gunpowder": 3,
  "Feather": 85,
  "Shears": 95,
  "Wheat": 70,
  "Bucket": 98,
  "Carrot": 26,
  "Crossbow": 23,
  "Arrow": 33,
  "Clay": 23
}
```


### Answer
Code:
```
def create_histogram(inventory, lebar_max, is_sorted=False):
    sorted_inventory = dict(sorted(inventory.items())) if is_sorted else inventory
    max_quantity = max(sorted_inventory.values())
    histogram = {}
    for item, quantity in sorted_inventory.items():
        normalized_quantity = round((quantity / max_quantity) * lebar_max)
        histogram[item] = '*' * normalized_quantity
    return histogram

def print_histogram(histogram):
    max_item_length = max(len(item) for item in histogram.keys())
    print("=" * (max_item_length + 9))
    print(f" Tabel inventory ")
    print("=" * (max_item_length + 9))
    for item, bars in histogram.items():
        print(f"{item} [{bars.count('*'):02d}]: {bars}")

lebar_max = int(input("lebar_max: "))
is_sorted = input("is_sorted? (y/n): ").lower() == 'y'

inventory = {
    "Lead": 15,
    "Bread": 79,
    "Apple": 22,
    "Bone": 75,
    "Hoe": 1,
    "Pickaxe": 60,
    "Egg": 13,
    "Milk": 17,
    "Slimeball": 94,
    "Salmon": 29,
    "Potato": 45,
    "Gunpowder": 3,
    "Feather": 85,
    "Shears": 95,
    "Wheat": 70,
    "Bucket": 98,
    "Carrot": 26,
    "Crossbow": 23,
    "Arrow": 33,
    "Clay": 23
}

histogram = create_histogram(inventory, lebar_max, is_sorted)
print_histogram(histogram)
```
Output:
![image](1.png)