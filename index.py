import streamlit as st

#Hitung Luas
def luas_segitiga(a, t):
    return (a * t) / 2

def luas_rectangle(p, l):
    return p * l

def luas_jajargenjang(a, t):
    return a * t


#Hitung Keliling
def keliling_segitiga(a, b, c):
    return a + b + c

def keliling_rectangle(p, l):
    return 2 * (p + l)

def keliling_jajargenjang(a, b):
    return 2 * (a + b)


hitungLuas = {
    "Luas segitiga": {
        "Fungsi": luas_segitiga,
        "Input": ['Alas', 'Tinggi']
    },
    "Luas Persegi Panjang": {
        "Fungsi": luas_rectangle,
        "Input": ['Panjang', 'Lebar']
    },
    "Luas Jajargenjang": {
        "Fungsi": luas_jajargenjang,
        "Input": ['Alas', 'Tinggi']
    }
}

hitungKeliling = {
    "Keliling segitiga": {
        "Fungsi": keliling_segitiga,
        "Input": ['Sisi A', 'Sisi B', 'Sisi C']
    },
    "Keliling Persegi Panjang": {
        "Fungsi": keliling_rectangle,
        "Input": ['Panjang', 'Lebar']
    },
    "Keliling Jajargenjang": {
        "Fungsi": keliling_jajargenjang,
        "Input": ['Sisi A', 'Sisi B']
    }
}




#TAMPILAN

st.title("Aplikasi Hitung Bangun Datar")

opt = st.selectbox(
    label = "Pilih Operasi Perhitungan",
    options = ['Hitung Luas', 'Hitung Keliling']
)

def pilih_rumus(option):
    allRumus = {}

    if (option == 'Hitung Luas'):
        allRumus = hitungLuas
    else:
        allRumus = hitungKeliling

    return allRumus

all_rumus = pilih_rumus(opt)

pilih_hitung = st.radio(
    label = 'Pilih Hitung',
    options = all_rumus.keys(),
    horizontal = True
)

inputs = [st.number_input(label, value = 0.0) for label in all_rumus[pilih_hitung]["Input"]]

if st.button('Hitung'):
    hasil = all_rumus[pilih_hitung]["Fungsi"](*inputs)
    st.markdown(f' <h2 style="color:green; text-align:center; ">Hasil: {hasil}</h2>', 
                unsafe_allow_html=True)
    

