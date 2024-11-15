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
