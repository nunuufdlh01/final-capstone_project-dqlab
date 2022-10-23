import streamlit as st
import pandas as pd
import scipy.stats
import openpyxl
import plotly
import plotly_express as px

st.set_page_config(layout = "wide")

st.title("Apakah Kecenderungan Membaca Berhubungan pada Penggunaan Media Sosial?")

st.text("Oleh: Nurul Fadilah Syahrul")

st.header("Pendahuluan")

st.write("Menurut data dari Digital 2022, "
        "penggunaan media sosial telah mencapai lebih dari 50 persen jumlah penduduk dari 26 negara. "
         "Tercatat bahwa dari 5,06 miliar penduduk terdapat 3,15 miliar penduduk yang merupakan pengguna aktif media sosial. "
         "Angka tersebut terbilang mencengangkan untuk saat ini. "
         "Sementara durasi rata-rata penggunaan media sosial per orang selama 1 pekan tercatat paling tinggi di Filipina, "
         "yaitu 1785 menit dan terendah di Jepang, yaitu 357 menit. "
         "Apabila dibandingkan dengan durasi rata-rata membaca buku per orang selama 1 pekan hal ini akan berbeda jauh. "
         "Menurut data dari Books of Brilliance 2022, "
         "durasi tertinggi tercatat sebesar 642 menit (India) dan terendah tercatat sebesar 186 menit (Korea Selatan). "
         "Hal ini menjadi pertanyaan bukan? Apakah durasi membaca buku itu mempunyai hubungan dengan banyaknya pengguna aktif media sosial? "
         "atau durasi membaca itu mempunyai hubungan dengan waktu seseorang yang dihabiskan di media sosial? "
         "Oleh karena itu, mari kita bahas perlahan-lahan.")

st.header("Dataset")

selectbox_data = st.selectbox(label = "Pilih Dataset", options =["Tanpa Persentase Pengguna Aktif Media Sosial",
                                                                 "Dengan Persentase Pengguna Aktif Media Sosial"])

df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vQWWTMl8xYI_Ket7jIEr_C9UP0b7haqRH8CjLh5QKELHdRBmCHnWUjXp0mkkwZqxw/pub?output=xlsx")

if selectbox_data == "Tanpa Persentase Pengguna Aktif Media Sosial":
    df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vQWWTMl8xYI_Ket7jIEr_C9UP0b7haqRH8CjLh5QKELHdRBmCHnWUjXp0mkkwZqxw/pub?output=xlsx")
    st.dataframe(df)

else:
    df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vQWWTMl8xYI_Ket7jIEr_C9UP0b7haqRH8CjLh5QKELHdRBmCHnWUjXp0mkkwZqxw/pub?output=xlsx")
    df['Jumlah Penduduk (Juta)'] = df['Jumlah Penduduk']/1000000
    df['Jumlah Pengguna Aktif Media Sosial (Juta)'] = df['Jumlah Pengguna Aktif Media Sosial']/1000000  
    df['Pengguna Aktif Media Sosial (%)'] = (df['Jumlah Pengguna Aktif Media Sosial']/df['Jumlah Penduduk']) * 100
    st.dataframe(df)

st.subheader("Statistika Deskriptif")

df['Jumlah Penduduk (Juta)'] = df['Jumlah Penduduk']/1000000
df['Jumlah Pengguna Aktif Media Sosial (Juta)'] = df['Jumlah Pengguna Aktif Media Sosial']/1000000  
df['Pengguna Aktif Media Sosial (%)'] = (df['Jumlah Pengguna Aktif Media Sosial']/df['Jumlah Penduduk']) * 100

st.dataframe(df.describe())

st.write("Dari tabel statistika deskriptif di atas, rata-rata dari durasi rata-rata membaca buku ke-26 negara sebesar 381.69 menit dengan durasi tertinggi sebesar 642 menit dan terendah sebesar 186 menit. "
         "Rata-rata dari durasi rata-rata penggunaan media sosial, yakni 1018.15 menit. Tertinggi sebesar 1785 menit dan terendah dengan durasi 357 menit. "
         "Sedangkan rata-rata persentase dari jumlah pengguna aktif media sosial sebesar 76.76%. Persentase terendah sebesar 33.35% dan tertinggi sebesar 91.21%.")

st.write("Sekarang, hal yang menjadi pertanyaan adalah negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial tertinggi?, "
         "negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial terendah? "
         "serta negara apa saja yang berada di bawah dan di atas rata-rata apabila ditinjau dari durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial?")
st.write("Oleh karena itu, di bawah ini akan ditampilkan beberapa chart untuk menjawab pertanyaan tersebut.")

st.header("Durasi dan Persentase dari 26 Negara")

barchart = px.bar(
    data_frame=df.sort_values('Durasi Membaca', ascending = True),
    x="Durasi Membaca",
    y="Negara",
    color="Durasi Membaca",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="h",              # 'v','h': orientation of the marks
    barmode='overlay',           # in 'overlay' mode, bars are top of one another.
    color_continuous_scale=px.colors.diverging.Portland,       # set marker colors. When color colum is numeric data
    color_continuous_midpoint=100,                           # set desired midpoint. When colors=diverging
    range_color=[1,1000],                                   # set your own continuous color scale
    text='Durasi Membaca',            # values appear in figure as text labels
    labels={"Negara":"",
        "Durasi Membaca":"Durasi Membaca Buku (Menit)"},           # map the labels of the figure
    title='', # figure title
    width=1200,                   # figure width in pixels
    height=840,                   # figure height in pixels
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    )

barchart.update_traces(texttemplate='%{text:.2s}', textposition='outside',
                       textfont_size=12)

barchart.add_annotation(
    x=df['Durasi Membaca'].mean()
    , text=f'rata-rata<br>durasi membaca'
    , yanchor='bottom'
    , showarrow=False
    , arrowhead=1
    , arrowsize=1
    , arrowwidth=2
    , arrowcolor="#636363"
    , ax=-20
    , ay=-30
    , font=dict(size=12, color="black", family="Sans Serif")
    , align="center"
    )

# add vertical lines
barchart.update_layout(shapes=
                  [dict(type= 'line',
                        yref= 'paper', y0= 0, y1= 1,
                        xref= 'x', x0=df['Durasi Membaca'].mean(), x1=df['Durasi Membaca'].mean(),
                        line=dict(color="Blue",
                                  width=3,
                                  dash="dot")
                        )
                  ])

barchart1 = px.bar(
    data_frame=df.sort_values('Durasi Media Sosial', ascending = True),
    x="Durasi Media Sosial",
    y="Negara",
    color="Durasi Media Sosial",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="h",              # 'v','h': orientation of the marks
    barmode='overlay',           # in 'overlay' mode, bars are top of one another.
    color_continuous_scale=px.colors.diverging.oxy,       # set marker colors. When color colum is numeric data
    color_continuous_midpoint=200,                           # set desired midpoint. When colors=diverging
    range_color=[1,2000],                                   # set your own continuous color scale
    text='Durasi Media Sosial',            # values appear in figure as text labels
    labels={"Negara":"",
        "Durasi Media Sosial":"Durasi Penggunaan Media Sosial (Menit)"},           # map the labels of the figure
    title='', # figure title
    width=1200,                   # figure width in pixels
    height=840,                   # figure height in pixels
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    )

barchart1.update_traces(texttemplate='%{text:.s}', textposition='outside',
                       textfont_size=12)

barchart1.add_annotation(
    x=df['Durasi Media Sosial'].mean()
    , text=f'rata-rata<br>durasi penggunaan media sosial'
    , yanchor='bottom'
    , showarrow=False
    , arrowhead=1
    , arrowsize=1
    , arrowwidth=2
    , arrowcolor="#636363"
    , ax=-20
    , ay=-30
    , font=dict(size=12, color="black", family="Sans Serif")
    , align="center"
    )

# add vertical lines
barchart1.update_layout(shapes=
                  [dict(type= 'line',
                        yref= 'paper', y0= 0, y1= 1,
                        xref= 'x', x0=df['Durasi Media Sosial'].mean(), x1=df['Durasi Media Sosial'].mean(),
                        line=dict(color="Blue",
                                  width=3,
                                  dash="dot")
                        )
                  ])

barchart2 = px.bar(
    data_frame=df.sort_values('Pengguna Aktif Media Sosial (%)', ascending = True),
    x="Pengguna Aktif Media Sosial (%)",
    y="Negara",
    color="Pengguna Aktif Media Sosial (%)",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="h",              # 'v','h': orientation of the marks
    barmode='overlay',           # in 'overlay' mode, bars are top of one another.
    color_continuous_scale=px.colors.diverging.Armyrose,       # set marker colors. When color colum is numeric data
    color_continuous_midpoint=10,                           # set desired midpoint. When colors=diverging
    range_color=[1,100],                                   # set your own continuous color scale
    text="Pengguna Aktif Media Sosial (%)",            # values appear in figure as text labels
    labels={"Negara":"",
        "Pengguna Aktif Media Sosial (%)":"Pengguna Aktif Media Sosial (%)"},           # map the labels of the figure
    title='', # figure title
    width=1200,                   # figure width in pixels
    height=840,                   # figure height in pixels
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    )

barchart2.update_traces(texttemplate='%{text:.4s}', textposition='outside',
                       textfont_size=12)

barchart2.add_annotation(
    x=df["Pengguna Aktif Media Sosial (%)"].mean()
    , text=f'rata-rata<br>persentase pengguna aktif media sosial'
    , yanchor='bottom'
    , showarrow=False
    , arrowhead=1
    , arrowsize=1
    , arrowwidth=2
    , arrowcolor="#636363"
    , ax=-20
    , ay=-30
    , font=dict(size=12, color="black", family="Sans Serif")
    , align="center"
    )

# add vertical lines
barchart2.update_layout(shapes=
                  [dict(type= 'line',
                        yref= 'paper', y0= 0, y1= 1,
                        xref= 'x', x0=df["Pengguna Aktif Media Sosial (%)"].mean(), x1=df["Pengguna Aktif Media Sosial (%)"].mean(),
                        line=dict(color="Blue",
                                  width=3,
                                  dash="dot")
                        )
                  ])

selectbox = st.selectbox(label = "Pilih Parameter", options = ['Durasi Membaca', 
                                                               'Durasi Penggunaan Media Sosial',
                                                               'Persentase Pengguna Aktif Media Sosial'])
if selectbox == 'Durasi Membaca':
    st.plotly_chart(barchart, use_container_width = True)
    st.write("Dari chart di atas, terlihat bahwa India merupakan negara tertinggi yang memiliki durasi rata-rata membaca buku per orang dalam sepekan, yaitu sebesar 640 menit "
         "dan terendah diduduki oleh Korea Selatan dengan durasi 186 menit. "
         "Lalu, Ada 11 negara yang memiliki durasi membaca buku di atas rata-rata dari 26 negara yang ada. "
         "Terdapat negara (1) India, (2) Thailand, (3) China, (4) Filipina, (5) Mesir, (6) Rusia "
         "(7) Perancis, (8) Swedia, (9) Saudi Arabia, (10) Hongkong, dan (11) Polandia.")
    st.write("Berarti, terdapat 15 negara yang memiliki durasi membaca buku di bawah rata-rata. "
         "Negara-negara yang dimaksud adalah Australia, Afrika Selatan, Indonesia, Turki, Kanada, Spanyol, "
         "United States, Jerman, Italia, Meksiko, United Kingdom, Brazil, Taiwan, Jepang, dan Korea Selatan dengan durasi masing-masing dapat dilihat melalui chart tersebut.")
elif selectbox == 'Durasi Penggunaan Media Sosial':
    st.plotly_chart(barchart1, use_container_width = True)
    st.write("Filipina menduduki posisi pertama untuk durasi penggunaan media sosial per orang selama 1 pekan, "
         "sedangkan Jepang yang terendah dengan masing-masing durasi, yaitu 1785 menit dan 357 menit.")
    st.write("Negara-negara dengan durasi penggunaan media sosial di atas rata-rata, yaitu "
         "Filipina, Brazil, Afrika Selatan, Meksiko, Indonesia, Korea Selatan, Saudi Arabia, Mesir, Turki, Thailand, dan Rusia. "
         "Sedangkan negara-negara selain 11 negara yang telah disebutkan merupakan negara yang memiliki durasi di bawah rata-rata, seperti India, United States, China, hingga Jepang.")
    
else:
    st.plotly_chart(barchart2, use_container_width = True)
    st.write("Chart di atas menampilkan bahwa Korea Selatan memiliki persentase tertinggi, yaitu 91.21% dibandingkan dengan negara lainnya, "
         "sedangkan India memiliki persentase terendah, yaitu sebesar 33.36%. "
         "Ternyata ada banyak negara yang termasuk ke dalam negara yang memiliki persentase jumlah pengguna aktif media sosial di atas rata-rata. "
         "Negara yang termasuk dimulai dari Korea Selatan (91.21%), Swedia (90.78%), Taiwan (89.44%), Hongkong (88.13%), hingga terbawah yakni Meksiko (78.30%).")
    st.write("Kemudian, negara-negara yang memiliki persentase jumlah pengguna aktif media sosial di bawah rata-rata adalah sisa dari 18 negara pada bar chart sebelumnya. "
        "Negara-negara tersebut adalah Rusia, Polandia, Italia, Indonesia, China, Mesir, Afrika Selatan, dan India.")

st.write("Sekarang, hal yang menjadi pertanyaan adalah "
         "negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial di atas dan di bawah angka rata-rata dari ketiga parameter tersebut? Berikut ini penjelasannya.")

st.subheader("Negara-negara dengan Durasi Membaca, Durasi Penggunaan Media Sosial, dan Persentase Pengguna Aktif Media Sosial di atas dan di bawah Rata-rata")

membaca_atas = df["Durasi Membaca"] > df["Durasi Membaca"].mean()
medsos_atas = df["Durasi Media Sosial"] > df["Durasi Media Sosial"].mean()
pengguna_atas = df['Pengguna Aktif Media Sosial (%)'] > df["Pengguna Aktif Media Sosial (%)"].mean()
data_atas = df[membaca_atas & medsos_atas & pengguna_atas].set_index("Negara")

membaca_bawah = df["Durasi Membaca"] < df["Durasi Membaca"].mean()
medsos_bawah = df["Durasi Media Sosial"] < df["Durasi Media Sosial"].mean()
pengguna_bawah = df['Pengguna Aktif Media Sosial (%)'] < df["Pengguna Aktif Media Sosial (%)"].mean()
data_bawah = df[membaca_bawah & medsos_bawah & pengguna_bawah].set_index("Negara")

selectbox_data_atas_bawah = st.selectbox(label = "Pilih Dataset", options = ["di bawah Rata-rata", "di atas Rata-rata"])

if selectbox_data_atas_bawah == "di atas Rata-rata":
    st.dataframe(data_atas)
    st.write("Dari 26 negara yang terdapat di dataset, hanya ada 3 negara yang memiliki durasi membaca, durasi penggunaan media sosial, "
         "dan persentase jumlah pengguna aktif media sosial di atas rata-rata, yaitu Saudi Arabia, Filipina, dan Thailand.")
else:
    st.dataframe(data_bawah)
    st.write("Dari 26 negara yang terdapat di dataset, hanya ada 1 negara yang memiliki durasi membaca, durasi penggunaan media sosial, "
         "dan persentase jumlah pengguna aktif media sosial di bawah rata-rata, yaitu Italia.")

st.write("Pertanyaan selanjutnya adalah bagaimana perbandingan jumlah penduduk dengan jumlah pengguna aktif media sosial?. Berikut ini disajikan 5 negara teratas dan terbawah berdasarkan jumlah penduduknya.")

st.header("Perbandingan Jumlah Penduduk vs Jumlah Pengguna Aktif Media Sosial dan Durasi Membaca vs Durasi Penggunaan Media Sosial")

# convert to long form (Jumlah)
data_pen1= df[['Negara', 'Jumlah Penduduk (Juta)', 'Jumlah Pengguna Aktif Media Sosial (Juta)']]
data_pen2 = (data_pen1.melt(id_vars='Negara', var_name='Penduduk', value_name='Jumlah')
       .sort_values('Jumlah', ascending=False).reset_index(drop=True))
data_pen2['Penduduk'] = data_pen2['Penduduk'].replace(['Jumlah Penduduk (Juta)','Jumlah Pengguna Aktif Media Sosial (Juta)'],
                                     ['Jumlah Penduduk','Jumlah Pengguna Aktif Media Sosial'])

barchart3 = px.bar(
    data_frame=data_pen2.sort_values('Jumlah', ascending=True),
    x="Jumlah",
    y="Negara",
    color="Penduduk",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="h",              # 'v','h': orientation of the marks
    barmode='group',
    color_discrete_map={"Jumlah Penduduk": "gray" ,"Jumlah Pengguna Aktif Media Sosial":"red"},     # map your chosen colors       
    text="Jumlah",            # values appear in figure as text labels
    labels={"Negara":"",
            "Jumlah": "Juta (Orang)",
            "Penduduk":""},           # map the labels of the figure
    title='', # figure title
    width=1200,                   # figure width in pixels
    height=840,                   # figure height in pixels
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    )

barchart3.update_traces(texttemplate='%{text:.s}', textposition='outside',
                       textfont_size=12)
barchart3.update_layout(yaxis={'categoryorder':'total ascending'})

# convert to long form (durasi)
data_dur1= df[['Negara', 'Durasi Membaca', 'Durasi Media Sosial']]
data_dur2 = (data_dur1.melt(id_vars='Negara', var_name='Durasi', value_name='Jumlah')
       .sort_values('Jumlah', ascending=False).reset_index(drop=True))
data_dur2['Durasi'] = data_dur2['Durasi'].replace(['Durasi Media Sosial','Durasi Membaca'],
                                     ['Durasi Penggunaan Media Sosial','Durasi Membaca Buku'])

barchart4 = px.bar(
    data_frame=data_dur2.sort_values("Jumlah", ascending = True),
    x="Jumlah",
    y="Negara",
    color="Durasi",               # differentiate color of marks
    opacity=0.9,                  # set opacity of markers (from 0 to 1)
    orientation="h",              # 'v','h': orientation of the marks
    barmode='relative',
    color_discrete_map={"Durasi Penggunaan Media Sosial": "gray" ,"Durasi Membaca Buku":"blue"},     # map your chosen colors       
    text="Jumlah",            # values appear in figure as text labels
    labels={"Negara":"",
            "Jumlah": "Durasi (Menit)",
            "Durasi":""},           # map the labels of the figure
    title='', # figure title
    width=1200,                   # figure width in pixels
    height=840,                   # figure height in pixels
    template='ggplot2',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    )

barchart4.update_traces(texttemplate='%{text:.s}', textposition='outside',
                       textfont_size=12)
barchart4.update_layout(yaxis={'categoryorder':'total ascending'})

selectbox_perb = st.selectbox(label = "Pilih Grafik", options = ["Jumlah Penduduk vs Jumlah Pengguna Aktif Media Sosial", "Durasi Membaca vs Durasi Penggunaan Media Sosial"])

if selectbox_perb == "Jumlah Penduduk vs Jumlah Pengguna Aktif Media Sosial":
    st.plotly_chart(barchart3, use_container_width = True)
    st.write("Berdasarkan chart di atas, jumlah pengguna aktif media sosial jika dibandingkan dengan jumlah penduduk di 26 negara tersebut "
         "hampir semuanya memiliki perbandingan lebih dari setengah total penduduknya aktif dalam bermedia sosial.")
else:
    st.plotly_chart(barchart4, use_container_width = True)
    st.write("Berdasarkan bar chart di atas, 26 negara semuanya memiliki durasi rata-rata penggunaan media sosial paling lama jika dibandingkan dengan durasi rata-rata membaca buku per orang dalam 1 pekan. "
         "Hal ini mungkin disebabkan orang-orang di tiap negara lebih intens dalam melakukan komunikasi, mencari informasi, dsb setiap harinya.")
    
st.write("Setelah melihat plot perbandingan antara jumlah dan durasi, kita pasti bertanya-tanya, sebenarnya durasi membaca buku itu memiliki hubungan atau tidak dengan durasi penggunaan media sosial. Lalu, bagaimana juga hubungannya dengan persentase pengguna aktif media sosial?")
st.write("Berikut ini penjelasannya.")

st.header("Hubungan antar 2 Variabel")

selectbox_hub = st.selectbox(label = "Pilih Variabel", options = ["Durasi Membaca dan Durasi Penggunaan Media Sosial",
                                                                  "Durasi Membaca dan Persentase Pengguna Aktif Media Sosial"])
g1 = px.scatter(df, y = "Durasi Membaca", x = "Durasi Media Sosial", labels = {"Durasi Membaca":"Durasi Membaca Buku (Menit)",
                "Durasi Media Sosial":"Durasi Penggunaan Media Sosial (Menit)"}, hover_name= "Negara",trendline = "ols", color_discrete_sequence = ["cyan"],
                width = 600, height = 400)
g2 = px.scatter(df, y = "Durasi Membaca", x = "Pengguna Aktif Media Sosial (%)", labels = {"Durasi Membaca":"Durasi Membaca Buku (Menit)",
                "Pengguna Aktif Media Sosial (%)":"Pengguna Aktif Media Sosial (%)"}, hover_name= "Negara",trendline = "ols", color_discrete_sequence = ["salmon"],
                width = 600, height = 400)
if selectbox_hub == "Durasi Membaca dan Durasi Penggunaan Media Sosial":
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(g1)
    with col2:
        hub1 = scipy.stats.pearsonr(df['Durasi Membaca'], df['Durasi Media Sosial'])
        st.text(hub1)
        st.write("Dari scatter plot di atas, hubungan 2 variabel tersebut menunjukkan plot memiliki hubungan yang positif, "
                 "berarti bahwa semakin lama durasi menggunakan media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. "
                 "Sebaliknya, semakin singkat durasi menggunakan media sosial, maka semakin singkat juga durasi membacanya. "
                 "Kalau secara logika, simpulan itu tentu tidak masuk di nalar kita. Hal ini bisa diperhatikan melalui besar korelasi dan nilai signifikansinya. "
                 "Besar korelasi (hubungan) antar 2 variabel ini sebesar 0.14. Hal ini menandakan bahwa hubungan antar 2 variabel ini cukup lemah untuk menentukan ada tidaknya hubungan yang terjadi. "
                 "Nilai signifikansi sebesar 0.48 menunjukkan bahwa variabel durasi membaca buku dan durasi penggunaan media sosial tidak terdapat hubungan yang signifikan antara Durasi Membaca dengan Durasi Penggunaan Media Sosial.")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(g2)
    with col2:
        hub2 = scipy.stats.pearsonr(df['Durasi Membaca'], df['Pengguna Aktif Media Sosial (%)'])
        st.text(hub2)
        st.write("Dari scatter plot di samping, hubungan 2 variabel tersebut menunjukkan plot memiliki hubungan yang negatif, "
                 "berarti bahwa semakin berkurang pengguna aktif media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. "
                 "Sebaliknya, semakin meningkat pengguna aktif media sosial, maka semakin sedikit durasi membacanya. "
                 "Besar korelasi (hubungan) antar 2 variabel ini sebesar 0.56. Hal ini menandakan bahwa hubungan antar 2 variabel ini cukup kuat untuk menentukan ada tidaknya hubungan yang terjadi. "
                 "Nilai signifikansi sebesar 0.002 menunjukkan bahwa variabel durasi membaca buku dan persentase pengguna aktif media sosial terdapat hubungan yang signifikan antar satu dengan yang lainnya.")

st.header("Simpulan")

st.write("1. Rata-rata dari masing-masing durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial, yaitu "
         "381.69 menit, 1018.15 menit, dan 76.76%.")
st.write("2. Negara yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial di atas angka rata-rata dari ketiga parameter, "
         "yaitu Saudi Arabia, Filipina, dan Thailand, sedangkan negara yang di bawah angka rata-rata adalah Italia.")
st.write("3. Variabel durasi membaca dengan persentase jumlah pengguna aktif media sosial memiliki hubungan yang signifikan dengan besar korelasi (hubungan) 0.56 yang artinya "
            "hubungan persentase jumlah pengguna aktif media sosial dengan durasi membaca buku sebesar 56% sisanya dipengaruhi oleh variabel lain dan berkorelasi negatif, artinya semakin berkurang pengguna aktif media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. "
            "Sebaliknya, semakin meningkat pengguna aktif media sosial, maka semakin sedikit durasi membacanya.")
st.write("4. Variabel durasi membaca buku dan durasi penggunaan media sosial tidak terdapat hubungan yang signifikan.")

st.header("Sumber Data")
st.write("https://booksofbrilliance.com/2022/09/14/which-country-reads-the-most-books/")
st.write("https://datareportal.com/reports/digital-2022")