# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Define custom color palette
custom_palette = px.colors.qualitative.Set3

# Create the main program
def run():

    # Add title to the app
    st.title('Exploratory Data Analysis: Loan Status Prediction')
    
    # Tambahkan gambar
    image = Image.open('gambar_1.jpg')  
    st.image(image, caption='Loan Status Prediction Analysis')

    # description
    st.write('''PT. ABC merupakan perusahaan di bidang peminjaman dana (Loan). Bagi perusahaan penting untuk memprediksi pengaju yang melakukan pengajuan peminjaman di approved atau tidak agar tidak terjadi kerugian pada perusahaan. Perusahaan sudah memiliki data 
                untuk di analisa. Data tersebut berisikan Loan ID, Gender, hingga Loan_Status yang mana ditunjukkan pada tabel dibawah ini.
             ''')
    st.markdown('---')

    df = pd.read_csv("loan_data.csv")
    df = df.dropna()
    st.dataframe(df)

    
    # Eksplorasi Target
    st.write("### Eksplorasi Kolom Target")
    target = df["Loan_Status"].value_counts().reset_index()
    fig, ax = plt.subplots(figsize=(7,5))
    df['Loan_Status'].value_counts().plot(kind='pie', autopct='%.2f%%',ax=ax)
    ax.set_title('Pie Chart Loan Status')
    ax.legend(fontsize=12)
    st.pyplot(fig)
    st.dataframe(target)
    st.write("""
    Diagram pie di atas menunjukkan persentase pengaju yang mengajukan loan di approved (Y) dan tidak di approved (N) berdasarkan dataset yang ada. 
    Dari data yang tersedia, dapat dilihat bahwa:
    - 71.10% pengaju loan dalam dataset Approved (disetujui).
    - 28.90% pengaju loan dalam dataset Not approved (tidak disetujui).
    Data ini menunjukkan bahwa mayoritas pengaju loan dalam dataset di approved atau dsetujui oleh perusahaan. Namun akan dilakukan analisa lebih lanjut mengenai faktor-faktor yang mempengaruhi loan status tersebut.
    """)

    # Dropdown for different analysis options
    st.markdown('#### Select Analysis')
    option = st.selectbox('Option:', ('Numerical Analysis','Categorical Analysis','Correlation Heatmap'))

    # Numerical analysis
    if option == 'Numerical Analysis':
    # Eksplorasi Data Numeric
        st.subheader("Numerical Analysis")

        # Applicant Income
        st.write('#### ApplicantIncome')
        fig = plt.figure(figsize=(12, 9))
        sns.histplot(df["ApplicantIncome"])
        plt.title("Count of Applicant Income")
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=18)
        st.pyplot (fig)

        st.write('Nilai maksimum dari ApplicantIncome adalah :  9703')
        st.write('Nilai minimum dari ApplicantIncome adalah :  150')
        st.write('Nilai rata-rata dari ApplicantIncome adalah :  3599.1266233766232')
        st.write('---'*35)
        st.write('Nilai maksimum dari Applicant Income orang yang di approve adalah :  9703')
        st.write('Nilai minimum dari Applicant Income orang yang di approve adalah :  645')
        st.write('Nilai rata-rata dari Applicant Income orang yang di approve adalah :  3630.703196347032')
        st.write('---'*35)
        st.write('Nilai maksimum dari Applicant Income orang yang tidak di approve adalah :  7660')
        st.write('Nilai minimum dari Applicant Income orang yang tidak di approve adalah :  150')
        st.write('Nilai rata-rata dari Applicant Income orang yang tidak di approve adalah :  3521.4269662921347')
        st.write('---'*35)
        st.write('Diperoleh bahwa nilai minimum dari Applicant Income sebesar 150 ribu US Dollar, maksimumnya sebesar 9730 ribu US Dollar dengan rata-rata sebesar 3599.13 ribu US Dollar. Selisih nilai minimum dan maksimum dari applicant income yang diapproved dengan tidak di approved cukup jauh, namun rata-rata dari kedua nya tidak berbeda secara signifikan.')


        # Co Applicant Income
        st.write('#### Loan Amount')
        fig = plt.figure(figsize=(12, 9))
        sns.histplot(df["LoanAmount"])
        plt.title("Count of Loan Amount")
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=18)
        st.pyplot(fig)

        st.write('Nilai maksimum dari Loan Amount adalah :  150.0')
        st.write('Nilai minimum dari Loan Amount adalah :  9.0')
        st.write('Nilai rata-rata dari Loan Amount adalah :  104.62337662337663')
        st.write('---'*35)
        st.write('Nilai maksimum dari Loan Amount yang di approve adalah :  150.0')
        st.write('Nilai minimum dari Loan Amount yang di approve adalah :  17.0')
        st.write('Nilai rata-rata dari Loan Amount yang di approve adalah :  3630.703196347032')
        st.write('---'*35)
        st.write('Nilai maksimum dari Loan Amount yang tidak di approve adalah :  150.0')
        st.write('Nilai minimum dari Loan Amount yang tidak di approve adalah :  9.0')
        st.write('Nilai rata-rata dari Loan Amount yang tidak di approve adalah :  102.17977528089888')
        st.write('---'*35)
        st.write('Diperoleh bahwa nilai minimum dari Loan Amount sebesar 9 ribu US Dollar, maksimumnya sebesar 150 ribu US Dollar dengan rata-rata sebesar 104.623 ribu US Dollar. Selisih nilai minimum dari loan amoount yang diapproved dengan tidak di approved cukup jauh. Namun nilai maksimum keduanya justru sama dan nilai rata-ratanya tidak berbeda secara signifikan.')

        # Loan Amount
        st.write('#### Loan Amount Term')
        fig = plt.figure(figsize=(12, 9))
        sns.histplot(df["Loan_Amount_Term"])
        plt.title("Count of Loan Amount Term")
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=18)
        st.pyplot(fig)
        st.write('Nilai maksimum dari Loan_Amount_Term adalah :  480.0')
        st.write('Nilai minimum dari Loan_Amount_Term adalah :  36.0')
        st.write('Nilai rata-rata dari Loan_Amount_Term adalah :  341.1818181818182')
        st.write('---'*35)
        st.write('Nilai maksimum dari Loan Amount Term yang di approve adalah :  480.0')
        st.write('Nilai minimum dari Loan Amount Term yang di approve adalah :  60.0')
        st.write('Nilai rata-rata dari Loan Amount Term yang di approve adalah :  340.7671232876712')
        st.write('---'*35)
        st.write('Nilai maksimum dari Loan Amount Term yang tidak di approve adalah :  480.0')
        st.write('Nilai minimum dari Loan Amount Term yang tidak di approve adalah :  36.0')
        st.write('Nilai rata-rata dari Loan Amount Term yang tidak di approve adalah :  342.2022471910112')
        st.write('---'*35)
        st.write('Diperoleh bahwa nilai minimum dari Loan Amount Term sebesar 36 bulan (3 tahun), maksimumnya sebesar 480 bulan (40 tahun) dengan rata-rata sebesar 341 tahun (+- 28 tahun). Selisih nilai minimum dari loan amount term yang diapproved dengan tidak di approved cukup jauh. Namun nilai maksimum keduanya justru sama dan nilai rata-ratanya tidak berbeda secara signifikan.')
    
    # Numerical analysis
    elif option == 'Categorical Analysis':
    # Eksplorasi Data Numeric
        st.subheader("Categorical Analysis")
  
        st.write("#### Gender")
        fig = plt.figure(figsize=(7,5))
        # Membuat bar chart
        sns.countplot(x='Gender', hue='Loan_Status', data=df)
        # Memberikan judul dan label sumbu
        plt.title('Distribusi Status Pinjaman berdasarkan Gender', fontsize=14)
        plt.xlabel('Gender', fontsize=12)
        plt.ylabel('Jumlah', fontsize=12)
        st.pyplot(fig)
        st.write('Dari bar chart diatas dapat diketahui bahwa loan banyak diajukan oleh Male (Laki-laki) dibandingkan Female (Perempuan). Kedua jenis kelamin tersebut juga menyatakan loan_status di approved (1) lebih banyak daripada tidak diapproved (0)')

        # Property_Area
        st.write("#### Property_Area")
        fig = plt.figure(figsize=(7,5))
        # Membuat bar chart
        sns.countplot(x='Property_Area', hue='Loan_Status', data=df)
        # Memberikan judul dan label sumbu
        plt.title('Distribusi Status Pinjaman berdasarkan Property Area',  fontsize=14)
        plt.xlabel('Property Area', fontsize=12)
        plt.ylabel('Jumlah', fontsize=12)
        st.pyplot(fig)
        st.write('Berdasarkan barchart diatas diperoleh bahwa loan banyak diajukan di area Semi Urban, diikuti dengan Urban dan Rural. Pada ketiga area tersebut menunjukkan bahwa loan_status lebih banyak di approved (1) daripada tidak di approved (0)')

        # Education
        st.write("#### Education")
        fig = plt.figure(figsize=(7,5))
        # Membuat bar chart
        sns.countplot(x='Education', hue='Loan_Status', data=df)
        # Memberikan judul dan label sumbu
        plt.title('Distribusi Status Pinjaman berdasarkan Education', fontsize=14)
        plt.xlabel('Education', fontsize=12)
        plt.ylabel('Jumlah', fontsize=12)
        st.pyplot(fig)
        st.write('Berdasarkan barchart diatas diperoleh bahwa loan banyak diajukan oleh pengaju dengan edukasi Graduate (sudah lulus). Pada kedua edukasi yaitu Graduate dan Not Graduate menunjukkan bahwa loan_status lebih banyak di approved (1) daripada tidak di approved (0).')

    # Numerical analysis
    elif option == 'Correlation Heatmap':
    # Corellation Heatmap
        st.subheader("Correlation Heatmap")   
        mask = np.triu(np.ones_like(df.select_dtypes(exclude='object').corr(), dtype=bool))
        fig = fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(df.select_dtypes(exclude='object').corr(min_periods=1), annot=True, mask=mask)
        st.pyplot(fig)
        st.write('Kolerasi antar kolom numerik sangat rendah.')


if __name__ == "__app__":
    run()