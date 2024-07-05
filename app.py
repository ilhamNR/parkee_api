import requests
import pandas as pd

def fetch_universities_data(country):
    # Format URL dengan negara yang spesifik
    url = f'http://universities.hipolabs.com/search?country={country}'
    response = requests.get(url)
    
    # Mengembalikan data JSON jika permintaan berhasil
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Menampilkan pesan jika gagal mengambil data dari API
        print("Gagal mengambil data dari API.")
        return []

def create_dataframe(data):
    # Mendefinisikan kolom-kolom yang diminati
    columns = ['name', 'web_pages', 'country', 'domains', 'state-province']
    df = pd.DataFrame(data, columns=columns)
    return df

def filter_by_state_province(df):
    # Memfilter baris yang 'state-province'-nya kosong atau None
    df_filtered = df[df['state-province'].notna()]
    return df_filtered

def main():
    # Ambil data dari API
    country = 'United States'
    data = fetch_universities_data(country)
    
    if not data:
        return
    
    # Buat DataFrame
    df = create_dataframe(data)
    
    # Filter data berdasarkan 'state-province'
    df_filtered = filter_by_state_province(df)
    
    # Tampilkan DataFrame yang sudah difilter
    print(df_filtered)

    # Simpan ke CSV
    csv_filename = f'universities_{country.replace(" ", "_").lower()}_filtered.csv'
    df_filtered.to_csv(csv_filename, index=False)
    print(f"\nData yang sudah difilter disimpan ke {csv_filename}")

if __name__ == "__main__":
    main()
