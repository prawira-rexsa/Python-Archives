import time
from datetime import datetime
from DrissionPage import ChromiumPage, ChromiumOptions
from bs4 import BeautifulSoup
import requests

options = ChromiumOptions()
options.incognito(True)
options.headless(False)
driver = ChromiumPage(options)

driver.get('https://classroom.itats.ac.id/login')
time.sleep(7)

email = "input email anda"
password = "input password anda"

time.sleep(2)
driver('xpath://input[@placeholder="NPM/NIP/Email"]').input(email)
driver('xpath://input[@placeholder="Password"]').input(password)
driver('xpath://button[@class="btn-common btn-active"]').click()
time.sleep(5)

if "mahasiswa/home" in driver.url:
    print(f"{datetime.now().strftime('%H:%M:%S')} : Login berhasil...")
    
    cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
    html_content = driver.html

    soup = BeautifulSoup(html_content, 'html.parser')
    meta_tag = soup.find('meta', attrs={'name': 'csrf-token'})
    csrf_token_content = meta_tag.get('content') if meta_tag else None

    if csrf_token_content:
        print(f"CSRF Token ditemukan: {csrf_token_content}")

        url = 'https://classroom.itats.ac.id/mahasiswa/list-tugas/getTugas'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRF-TOKEN': csrf_token_content,
            'User-Agent': 'Mozilla/5.0',
            'Cookie': '; '.join([f"{key}={value}" for key, value in cookies.items()])
        }
        payload = {'_token': csrf_token_content}

        response = requests.post(url, headers=headers, data=payload)
        
        if response.status_code == 200:
            try:
                tugas_data = response.json()

                if 'tugas' in tugas_data and isinstance(tugas_data['tugas'], list):
                    print("Data tugas berhasil diambil:\n")
                    
                    for index, tugas in enumerate(tugas_data['tugas'], start=1):
                        minggu = tugas.get('weekid', 'Tidak ada minggu')
                        judul = tugas.get('judul_tugas', 'Tidak ada judul')
                        batas = tugas.get('batas_pengumpulan', 'Tidak ada batas pengumpulan')
                        submission = tugas.get('submission', False)  
                        status_submission = "Sudah Dikumpulkan" if submission else "Belum Dikumpulkan"
                        
                        print(f"Tugas {index}:")
                        print(f"Minggu            : {minggu}")
                        print(f"Judul Tugas       : {judul}")
                        print(f"Batas Pengumpulan : {batas}")
                        print(f"Status            : {status_submission}")
                        print("-" * 40) 
                else:
                    print("Data 'tugas' tidak ditemukan atau bukan list.")
            except ValueError:
                print("Response bukan format JSON. Berikut adalah teks respons:")
                print(response.text)
        else:
            print(f"Gagal mendapatkan data. Status: {response.status_code}, Pesan: {response.text}")


    else:
        print("CSRF Token tidak ditemukan.")
else:
    print(f"{datetime.now().strftime('%H:%M:%S')} : Login gagal, periksa ulang email atau password.")
