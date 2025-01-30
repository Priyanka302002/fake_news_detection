# 📰 Fake News Detection System 🕵️‍♂️

## 📌 Project Overview
The **Fake News Detection System** is a machine learning-based application that determines whether a given news article is **real** or **fake**. Built with Python, this project uses a **Logistic Regression** model and **TF-IDF Vectorizer** to classify news articles effectively.

The system processes news articles, extracts features, and classifies them as either **Fake** or **Real**. This project can help in identifying misinformation, making it a valuable tool for media outlets and consumers.

## 🔧 Tools and Technologies ⚙️
- **Programming Language**: Python 🐍
- **Libraries**: 
  - **Scikit-learn** 🤖
  - **Pandas** 📊
  - **NumPy** 🔢
  - **Streamlit** 💻
  - **Joblib** 💾
- **IDE/Tools**: Visual Studio Code 🖥️, Jupyter Notebook 📓

## 🖼️ Detection Screen Before and After

**Project Interface Before Prediction:**  
![Project Interface](images/screen.png)

**Before Detection:**  
![Before Detection](images/before.png)

**After Detection - News is Real:**  
![News is Real](images/real.png)

**After Detection - News is Fake:**  
![News is Fake](images/fake.png)

## 📂 Dataset Description 🗂️
The **Fake News Dataset** contains labeled news articles, with the following columns:
- **id** 🔢: Unique identifier for the article
- **title** 📰: The title of the article
- **author** ✍️: The author of the article
- **text** 📝: The content of the article
- **label** 🏷️: The classification (Fake or Real)

You can download the dataset from the link below:
- **[Download Dataset](https://drive.google.com/drive/folders/1wPzbhNSGQo2I3NqJFEK80eFnE26yzMWK?usp=sharing)**  

## 🛠️ Project Workflow 🔄

### 1. Data Loading and Importing Libraries 📥
The first step involves importing the necessary Python libraries and loading the dataset to start the analysis.

### 2. Data Preprocessing 🧹
This step involves cleaning the data by handling missing values, removing unwanted characters, and converting text to lowercase.

### 3. Feature Extraction 🔎
We use the **TF-IDF Vectorizer** to convert text into numerical features, which can be fed into the machine learning model.

### 4. Model Training 🧠
We train a **Logistic Regression** model on the processed data to classify the news articles as either **Fake** or **Real**.

### 5. Model Evaluation 📝
The model is evaluated using accuracy and other performance metrics to ensure its effectiveness in predicting fake news.

## 📊 Visualizations 🎨
- **Word Cloud** 🌀: Visualize the most frequent words in the fake and real news articles.
- **Confusion Matrix** 🧩: Display the performance of the classification model.

## 💡 Key Insights 🔑
- The model performs well in detecting fake news, with an accuracy of **XX%**.
- Common words in fake news articles include **"scandal"**, **"conspiracy"**, and **"shocking"**.

## 🚀 Future Improvements 🔮
- Implement additional models (e.g., Random Forest, SVM) and compare performance.
- Enhance the model by incorporating more advanced NLP techniques (e.g., BERT, Word2Vec).

## 📜 License 📝
This project is licensed under the MIT License.

## 📥 Clone the Project 🖇️
You can clone this project to your local machine using the link below:
- **[Clone this Repository](https://github.com/Priyanka302002/Fake_News_Detection)**

---

Feel free to explore, contribute, or modify the project. Happy detecting! 😊
