import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day.csv")

st.sidebar.header('Dashboard')
pilihan = st.sidebar.selectbox(
    label="Menu Tampilan",
    options=('Home', 'Musim (Season)', 'Holiday/Workingday', 'Suhu (Temperature)')
)


st.title('Final Project Analisis Data Bike Sharing Dataset')

if pilihan == 'Home':
    st.image('https://cdn0-production-images-kly.akamaized.net/baKr7P7mNt9DvGALEMda-RtlW7k=/1200x900/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/3169554/original/054235300_1593770750-20200703-Pemprov-DKI-Akan-Sediakan-Layanan-Bike-Sharing-angga-5.jpg', caption='Peminjaman Sepeda', use_column_width=True)
    st.write('Berikut Tabel Dataset')
    st.write(df)

elif pilihan == 'Musim (Season)':
    st.write('Analisis Peminjaman Sepeda Berdasarkan Musim (Season)')
    st.markdown("---")
    nama_musim = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season'] = df['season'].map(nama_musim)
    peminjaman_musim = df.groupby('season')['cnt'].sum().sort_values(ascending=False)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Fall", value=peminjaman_musim['Fall'].sum())
    with col2:
        st.metric("Summer", value=peminjaman_musim['Summer'].sum())
    with col3:
        st.metric("Winter", value=peminjaman_musim['Winter'].sum())
    with col4:
        st.metric("Springer", value=peminjaman_musim['Spring'].sum())
    st.bar_chart(peminjaman_musim)
    st.markdown('''
                Musim Fall (Gugur) memiliki jumlah peminjam sepeda terbanyak. Jumlah peminjaman sepeda tertinggi terjadi pada musim gugur, diikuti oleh musim panas, musim dingin, dan musim semi. Musim gugur memiliki jumlah peminjaman sepeda yang tinggi karena cuaca yang hangat dan nyaman untuk bersepeda.
                ''')

elif pilihan == 'Holiday/Workingday':
    st.write('Analisis Peminjaman Sepeda Berdasarkan Hari Libur/Hari Kerja')
    st.markdown("---")
    peminjaman_holiday = df.groupby('holiday')['cnt'].sum().sort_values(ascending=False)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Peminjaman pada Hari Kerja", value=peminjaman_holiday[0])
    with col2:
        st.metric("Total Peminjaman pada Hari Libur", value=peminjaman_holiday[1])
    st.bar_chart(peminjaman_holiday)
    st.markdown('''
                Keterangan: \n
                0 : Hari Kerja \n
                1 : Hari Libur
                ''')
    st.markdown('''
                Holiday / bukan Working Day (Hari libur/ bukan hari kerja) memiliki jumlah peminjam sepeda terbanyak. Jumlah peminjaman sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan hari libur mungkin karena orang-orang menggunakan sepeda sebagai sarana transportasi sehari-hari untuk pergi bekerja atau sekolah. Pada hari libur, aktivitas penggunaan sepeda mungkin lebih bergantung pada rekreasi atau kegiatan khusus, atau mungkin orang banyak menghabiskan waktu dirumah dan tidak beraktivitas keluar. 
                ''')

elif pilihan == 'Suhu (Temperature)':
    st.write('Analisis Peminjaman Sepeda Berdasarkan Suhu (Temperature)')
    st.markdown("---")

    temp_rendah = 0.4
    temp_tinggi = 0.7

    peminjam_temp_rendah = df[(df['temp'] < temp_rendah)]['cnt'].sum()
    peminjam_temp_sedang = df[(df['temp'] >= temp_rendah) & (df['temp'] <=temp_tinggi)]['cnt'].sum()
    peminjam_temp_tinggi = df[df['temp'] > 0.7]['cnt'].sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Peminjaman pada Suhu Rendah", value=peminjam_temp_rendah)
    with col2:
        st.metric("Peminjaman pada Suhu Sedang", value=peminjam_temp_sedang)
    with col3:
        st.metric("Peminjaman pada Suhu Tinggi", value=peminjam_temp_tinggi)

    fig, ax = plt.subplots()
    ax.hist(df['temp'], color='green', edgecolor='black')
    ax.set_title('Distribusi Jumlah Peminjaman Sepeda berdasarkan Rentang Suhu')
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.scatter(df['temp'], df['cnt'], color='green', alpha=0.5)
    ax.set_title('Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda')
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)
    st.pyplot(fig)

    st.markdown('''
                Suhu {} - {} merupakan range suhu yang memiliki peminjaman sepeda yang lebih banyak. Jumlah peminjaman sepeda cenderung meningkat pada suhu keadaan sedang (tidak terlalu dingin dan tidak terlalu panas) karena pengguna sepeda mengutamakan kenyamanan.
                '''.format(temp_rendah, temp_tinggi))

st.caption('Copyright (c), created by Johansen Sihombing')