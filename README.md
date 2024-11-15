
# Instagram Follow Check

Script Python untuk memeriksa daftar orang yang Anda ikuti di Instagram tetapi tidak mengikuti Anda kembali. Program ini membandingkan dua file JSON (`followers_1.json` dan `following.json`) untuk mendapatkan hasil tersebut.

## 🛠️ Fitur
- Membaca data followers dan following dari file JSON.
- Membandingkan daftar following dengan followers.
- Menampilkan username dan URL profil Instagram dari pengguna yang Anda ikuti tetapi tidak mengikuti Anda balik.

## 📁 Struktur File
- `followers_1.json`: Berisi daftar orang yang mengikuti Anda.
- `following.json`: Berisi daftar orang yang Anda ikuti.

### Contoh Data
#### **followers_1.json**
```json
[
  {
    "title": "",
    "media_list_data": [],
    "string_list_data": [
      {
        "href": "https://www.instagram.com/revinasrr_",
        "value": "revinasrr_",
        "timestamp": 1731225097
      }
    ]
  }
]
```

#### **following.json**
```json
{
  "relationships_following": [
    {
      "title": "",
      "media_list_data": [],
      "string_list_data": [
        {
          "href": "https://www.instagram.com/parttime.jakarta",
          "value": "parttime.jakarta",
          "timestamp": 1731648584
        }
      ]
    }
  ]
}
```

## 🚀 Cara Menggunakan
1. Download Data Followers dan Following dari Instagram:
- Masuk ke akun Instagram Anda.
- Pilih Settings > Account Center > Your information and permissions.
- Pilih Download your information > Download or transfer information.
- Pilih Some of your information, pilih Followers and Following.
- Pilih Date Range sebagai All Time dan formatnya JSON.
- Klik Create File dan tunggu 5-10 menit hingga file tersedia untuk diunduh.
- Setelah file siap, unduh dan ekstrak file tersebut.
2. Simpan file JSON (`followers_1.json` dan `following.json`) di direktori yang sama dengan script Python.
3. Jalankan script dengan perintah:
   ```bash
   python main.py
   ```

4. Hasil akan ditampilkan di terminal dalam format berikut:
   ```
   Orang yang Anda ikuti tetapi tidak mengikuti Anda kembali:
   parttime.jakarta: https://www.instagram.com/parttime.jakarta
   ```

## 🧩 Kode Utama
Berikut adalah script utama untuk menjalankan program:
```python
import json

# Fungsi untuk mendapatkan daftar followers dari file JSON
def get_user_data_from_followers(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        followers = set()
        for entry in data:
            for item in entry['string_list_data']:
                followers.add((item['value'], item['href']))
        return followers

# Fungsi untuk mendapatkan daftar following dari file JSON
def get_user_data_from_following(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        following = set()
        for entry in data['relationships_following']:
            for item in entry['string_list_data']:
                following.add((item['value'], item['href']))
        return following

def find_non_followers(following, followers):
    return following - followers

# Path ke file JSON
followers_file = 'followers_1.json'
following_file = 'following.json'

# Ambil data dari file
followers = get_user_data_from_followers(followers_file)
following = get_user_data_from_following(following_file)

# Temukan siapa yang Anda ikuti tetapi tidak mengikuti Anda balik
non_followers = find_non_followers(following, followers)

# Tampilkan hasil
print("Orang yang Anda ikuti tetapi tidak mengikuti Anda kembali:")
for username, url in non_followers:
    print(f"{username}: {url}")
```

