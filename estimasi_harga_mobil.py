import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('estimasi_harga_mobil.sav', 'rb'))

# Dataset mobil bekas
df = pd.read_csv('toyota.csv')  # Ganti dengan URL jika dataset berada di online

st.title('Estimasi Harga Mobil Toyota Bekas')

# Fungsi untuk halaman Deskripsi
def show_deskripsi():
    st.write("Selamat datang di aplikasi prediksi harga mobil bekas berbasis web.")
    st.write("<div style='text-align: justify;'>Aplikasi ini menggunakan teknologi <i>Machine Learning</i> untuk memberikan estimasi harga mobil bekas berdasarkan data historis. Dengan memasukkan data seperti tahun produksi, kilometer pemakaian, pajak, konsumsi bahan bakar, dan ukuran mesin, pengguna dapat dengan mudah mendapatkan estimasi harga mobil Toyota bekas. Model <i>Machine Learning</i> telah dilatih menggunakan data historis yang luas, memungkinkan hasil prediksi yang akurat dan andal. Aplikasi ini dirancang untuk membantu pengguna dalam pengambilan keputusan yang lebih baik terkait pembelian atau penjualan mobil bekas.</div>", unsafe_allow_html=True)
    st.write("Dataset: Toyota.csv")

# Fungsi untuk halaman Dataset
def show_dataset():
    st.header("Dataset")
    st.dataframe(df)
    st.markdown("""
( 1 ) **Tahun**
    - Tahun produksi mobil.
( 2 ) **Kilometer Pemakaian**
    - Jarak yang telah ditempuh mobil dalam satuan kilometer.
( 3 ) **Pajak**
    - Besaran pajak kendaraan.
( 4 ) **Konsumsi BBM**
    - Efisiensi bahan bakar mobil dalam satuan MPG (Miles Per Gallon).
( 5 ) **Ukuran Mesin**
    - Kapasitas mesin mobil dalam liter.
( 6 ) **Harga Mobil**
    - Harga aktual mobil bekas dalam dataset.
    """)

# Fungsi untuk halaman Prediksi
def show_prediksi():
    st.header("Halaman Prediksi")
    # Input fitur
    year = st.number_input('Input Tahun Mobil')
    mileage = st.number_input('Input Kilometer Pemakaian')
    tax = st.number_input('Input Pajak Mobil')
    mpg = st.number_input('Input Konsumsi BBM Mobil')
    engineSize = st.number_input('Input Ukuran Mesin')

    predict = ''

    if st.button('Estimasi Harga'):
        predict = model.predict([[year, mileage, tax, mpg, engineSize]])
        st.write('Estimasi harga mobil bekas dalam satuan Pound = ', predict[0])
        st.write('Estimasi harga mobil bekas dalam satuan Rupiah = ', predict[0] * 18559)

# Pilih menu di sidebar
add_selectbox = st.sidebar.selectbox(
    "PILIH MENU",
    ("Deskripsi", "Dataset", "Prediksi")
)

if add_selectbox == "Deskripsi":
    show_deskripsi()
elif add_selectbox == "Dataset":
    show_dataset()
elif add_selectbox == "Prediksi":
    show_prediksi()
