# Final Project Purwadhika Bank Marketing ML Classification

## Source: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#
[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014

#### Abstract: The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

### Data Set Information:

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

### Project Steps:

#### 1). Data Cleaning and EDA

Pada bagian ini, saya melakukan data cleaning seperti mengubah atau me-replace beberapa data yang mengandung value "unknown" dan juga membuang sebagian features yang menurut saya tidak terlalu penting utk dimasukan kedalam model. Utk EDA, saya melakukan beberapa plot utk meng-analisa data dan juga membuat beberapa correlation analysis antara features numerical dan categorical dan dengan target.

#### 2). Data Modeling, Evaluation and Prediction

Saya membuat modeling dengan 4 jenis cara yaitu pertama dengan baseline model, kedua dengan baseline model yang sudah di over-sampling, ketiga dengan tuned model dan keempat dengan tuned model yang sudah di over-sampling.

Utk modeling disini, saya menggunakan 3 model yaitu Logistic Regression, K-Near Neighbor dan Random Forest Classifier. Dan juga saya meng-aplikasikan oversampling dengan bantuan SMOTE oversampling (dikarenakan data set yang highly imbalance).

Utk evaluation, saya menggunakan total 5 metrics yaitu F1-score (Macro), Precision (Macro), Recall (Macro), Matthews Score dan ROC-AUC score. Tetapi utk final decision utk menilai prediction, saya menggunakan F1-score (Macro), yang dimana dia adalah harmonic mean antara Precision dan Recall.

#### 3). Model deployment
      
Dan pada akhirnya, saya membuat 1 notebook khusus ini utk mencoba sedikit lagi merapihkan hyperparameter yang saya sudah dapet dari notebook sebelomnya. Sebelum saya memilih dan menggunakan model terbaik utk di deploy ke dashboard.


### Project Evaluation Reports:

#### 1). Full Table Metrics 

![](images/full%20table%20metrics.png)

#### 2). Final Table Metrics (F1-score (Macro))

![](images/Final%20table%20metrics.png)

#### 3). Feature Importances

![](images/RFC%20feature%20importances.png)

### Project Insights and Recommendation:

1). Dari data, terdapat kebanyakan client bank yang mempunyai persentase tinggi utk membuka term deposit adalah yang berumur masih dibawah 32 tahun (yang berstatus student) dan yang sudah diatas 70 tahun (atau yang sudah retired statusnya). Ini masuk akal, dimana client yang masih cenderung muda dan yang sudah pensiun pada dasarnya memiliki beban finansial yang masih lebih rendah, jadi memungkinkan mereka untuk lebih punya banyak savings yang dapat di investasikan. Bank bisa mereka ulang strategi utk lebih mempromosikan marketing campaign kepada individu" yang masih dalam kategori umur tersebut.

2). Dari segi status marital, bank jga bisa mentargetkan client yang masih single (untuk investasi masa depan) atau yang umurnya sudah mulai mau masuk kategori pensiun (yang dimana client" ini mungkin lebih memikirkan investasi untuk dana pensiun).

3). Kalau dilihat dari months, bank dapat lebih push marketing campaign pada saat periode sebelom mulai ramai acara dan festival di Portugal yaitu seperti dari mulainya musim autumn sampai awal spring, dimana orang tidak melakukan aktivitas banyak dan dapat lebih fokus untuk memikirkan investasi atau cara mengelola keuangan mereka.

4). untuk cost-effective, bank dianjurkan untuk tidak terlalu melakukan pengontakan yang berlebihan terhadap client seperti puluhan kali pengontakan. Dikarenakan, hasil dari data menunjukan bahwa pengontakan yang banyak juga tidak dapat menjamin client utk membuka term deposit. Jadi untuk menghemat waktu dan uang, lebih baik utk mengontak tidak terlalu banyak kecuali ada kepentingan khusus.

5). Dari data social dan economic context attributes, rata" data ini semua berkorelasi tinggi antara satu dengan yang lain dan juga features" ini semua lumayan mempengaruhi apakah seorang client akan menjadi potential client bank atau bukan? Terutama euribor3m yang adalah euribor rate dengan maturiti 3 bulan, data ini sangat mempengaruhi prediksi kita terhadap client. Bank dapat membuat strategi marketing campaign dengan mengacu kepada kondisi social dan economic context attribute pada saat ingin membuat campaign, karena akan membuat dampak yang besar terhadap respon client dalam hal membuka term deposit.

