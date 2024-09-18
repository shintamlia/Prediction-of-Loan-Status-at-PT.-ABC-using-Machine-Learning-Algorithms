# Problem Statement

Saya merupakan seorang data analyst di PT. ABC yang bergerak di bidang peminjaman dana. Saya diberikan data dalam format csv berjudul `loan_data.csv` yang nantinya akan dibuat model guna mempelajari pola dalam memprediksi apakah loan atau pengajuan peminjaman di approve atau tidak. Model tersebut juga akan di simpan sehingga digunakan untuk memprediksi data baru.

# Objective

File ini berisi model prediksi klasifikasi menggunakan KNN, SVM, Decision Tree, Random Forest, dan XGBooster yang nantinya akan dipilih model terbaik. Model-model tersebut dibuat menggunakan pipeline dan dilengkapi dengan cross-validation dan hyperparameter tuning.

# Kesimpulan

Guna memperoleh hasil prediksi yang optimal pada loan status yaitu di approved atau tidak, model SVM adalah model terbaik untuk digunakan. Hal tersebut ditinjau dari precision score yang dihasilkan sebesar 83% pada train dan 81% pada test dengan selisih 3% < 5% yang menyatakan bahwa model yang dihasilkan tergolong goodfit. Dengan demikia, model SVM yang telah teruji dapat segera diimplementasikan ke dalam sistem persetujuan peminjaman perusahaan untuk mendukung proses pengambilan keputusan.

# URL 

- [Kaggle datasets](https://www.kaggle.com/datasets/bhavikjikadara/loan-status-prediction)
- [Hugging Face](https://huggingface.co/spaces/shintamlia/Loan_Status_Prediction)
