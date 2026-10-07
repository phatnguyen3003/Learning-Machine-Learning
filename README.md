# 📧 Email Classification System - Roadmap & Build Board

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)](#)

A comprehensive, production-ready Machine Learning system for classifying emails (Spam/Ham & Multi-category). This repository serves as both the implementation codebase and a step-by-step project build tracker.

---

## 📊 Overall Progress

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0% Completed
```

- [ ] Phase 1: Problem Definition & Data Collection
- [ ] Phase 2: Exploratory Data Analysis (EDA)
- [ ] Phase 3: Text Preprocessing Pipeline
- [ ] Phase 4: Feature Engineering & Vectorization
- [ ] Phase 5: Class Imbalance Handling
- [ ] Phase 6: Model Training & Experimentation
- [ ] Phase 7: Evaluation & Hyperparameter Tuning
- [ ] Phase 8: Deployment & Monitoring

---

## 🛠️ Build Board & Task Checklist

### Phase 1: Problem Definition & Data Acquisition
> **Goal:** Establish baseline objectives and gather data assets.

- [ ] **Define Core Scope:**
  - [ ] Binary Classification (Spam vs. Ham)
  - [ ] Multi-Class Categorization (Work, Personal, Promotions, Spam)
- [ ] **Dataset Acquisition:**
  - [ ] Download Enron Email Corpus
  - [ ] Fetch SMS Spam Collection dataset
  - [ ] Collect custom domain-specific samples (Optional)
- [ ] **Environment Setup:**
  - [ ] Initialize Git repository
  - [ ] Set up virtual environment (`venv` / `conda`)
  - [ ] Create initial `requirements.txt` (`pandas`, `numpy`, `scikit-learn`)

---

### Phase 2: Exploratory Data Analysis (EDA)
> **Goal:** Understand dataset distribution, missing values, and text properties.

- [ ] **Data Sanitation & Check:**
  - [ ] Check for missing values (`NaN`) and null records
  - [ ] Deduplicate repeating email bodies
- [ ] **Statistical Analysis:**
  - [ ] Calculate class ratio (Check for Class Imbalance)
  - [ ] Measure email length (Character count & Word count distributions)
- [ ] **Text Visualization:**
  - [ ] Generate WordCloud for Spam vs. Ham emails
  - [ ] Plot Top-20 N-grams (Unigrams, Bigrams, Trigram frequencies)

---

### Phase 3: Text Preprocessing Pipeline
> **Goal:** Transform noisy raw email HTML/text into clean, normalized tokens.

- [ ] **Email Structure Parsing:**
  - [ ] Separate Email `Subject` and `Body`
  - [ ] Strip HTML tags using `BeautifulSoup`
- [ ] **String Cleaning & Regular Expressions:**
  - [ ] Remove URLs, email addresses, phone numbers, and special characters
  - [ ] Lowercase conversion
  - [ ] Expand contractions (e.g., *don't* $\rightarrow$ *do not*)
- [ ] **Linguistic Normalization:**
  - [ ] Tokenization via `NLTK` / `SpaCy`
  - [ ] Remove domain-specific & general stopwords
  - [ ] Apply Lemmatization (`WordNetLemmatizer` or `SpaCy POS-based`)
- [ ] **Pipeline Packaging:**
  - [ ] Wrap preprocessing logic into a custom Scikit-Learn `Transformer` class

---

### Phase 4: Feature Engineering & Vectorization
> **Goal:** Convert cleaned text into numerical representation for ML models.

- [ ] **Text Vectorization:**
  - [ ] Implement `TfidfVectorizer` (Unigram + Bigram, `max_features=10000`)
  - [ ] Experiment with Word Embeddings (`Word2Vec` / `FastText`)
  - [ ] Experiment with Contextual Sentence Embeddings (`sentence-transformers`)
- [ ] **Domain-Specific Feature Extraction:**
  - [ ] Extract Capitalization Ratio (Percentage of ALL CAPS words)
  - [ ] Count number of embedded links/URLs
  - [ ] Count presence of high-risk keywords (*"FREE"*, *"URGENT"*, *"CLICK HERE"*)
  - [ ] Binary flag for attachments (`has_attachment`)
- [ ] **Feature Matrix Assembly:**
  - [ ] Combine TF-IDF sparse matrix with numerical domain features using `FeatureUnion` or `ColumnTransformer`

---

### Phase 5: Class Imbalance Handling
> **Goal:** Prevent model bias towards majority classes (e.g., Legitimate emails).

- [ ] **Resampling Strategies:**
  - [ ] Apply **SMOTE** (Synthetic Minority Over-sampling Technique)
  - [ ] Experiment with Random Undersampling for large corpora
- [ ] **Algorithmic Weighting:**
  - [ ] Configure `class_weight='balanced'` in candidate estimators

---

### Phase 6: Model Training & Experimentation
> **Goal:** Train and compare multiple algorithm families from baseline to SOTA.

- [ ] **Baseline Models:**
  - [ ] Multinomial Naive Bayes (`MultinomialNB`)
  - [ ] Logistic Regression (`LogisticRegression`)
  - [ ] Linear Support Vector Classifier (`LinearSVC`)
- [ ] **Ensemble Models:**
  - [ ] Random Forest Classifier
  - [ ] Gradient Boosting (`LightGBM` / `XGBoost`)
- [ ] **Deep Learning / Transformers (Optional Track):**
  - [ ] Fine-tune `DistilBERT` / `RoBERTa` using Hugging Face `Trainer`
- [ ] **Experiment Tracking:**
  - [ ] Log metrics and artifacts using `MLflow` or `Weights & Biases`

---

### Phase 7: Evaluation & Hyperparameter Tuning
> **Goal:** Optimize model metrics with strict focus on minimizing False Positives.

- [ ] **Evaluation Metrics Calculation:**
  - [ ] Generate Confusion Matrix (Track TP, FP, FN, TN)
  - [ ] Measure **Precision** (Priority: Minimize FP to avoid losing critical emails)
  - [ ] Measure **Recall**, **F1-Score**, and **ROC-AUC**
- [ ] **Hyperparameter Optimization:**
  - [ ] Implement 5-Fold `StratifiedKFold` Cross-Validation
  - [ ] Run `Optuna` / `RandomizedSearchCV` for hyperparameter tuning
- [ ] **Model Selection:**
  - [ ] Select champion model based on Precision-Recall Curve trade-off

---

### Phase 8: Deployment, API & Monitoring
> **Goal:** Export the pipeline, build an inference endpoint, and monitor in production.

- [ ] **Model Serialization:**
  - [ ] Export end-to-end pipeline (`TfidfVectorizer` + `Model`) using `joblib`
  - [ ] Convert model to `ONNX` format for optimized inference speed
- [ ] **API Development:**
  - [ ] Build REST API using `FastAPI`
  - [ ] Create Pydantic schemas for request validation (`{"email_text": "..."}`)
  - [ ] Add endpoint `/predict` with output class and probability scores
- [ ] **User Interface / Demo:**
  - [ ] Create a interactive web dashboard using `Streamlit` / `Gradio`
- [ ] **Containerization & Deployment:**
  - [ ] Write `Dockerfile` and `docker-compose.yml`
  - [ ] Deploy container to Cloud Platform (AWS / GCP / HuggingFace Spaces)
- [ ] **Monitoring & Drift Detection:**
  - [ ] Set up `Evidently AI` for monitoring Data & Concept Drift over time

---

## 🧰 Tech Stack Summary

| Layer | Tools & Libraries |
|---|---|
| **Language & Core** | Python 3.9+, NumPy, Pandas |
| **NLP & Preprocessing** | NLTK, SpaCy, BeautifulSoup4, Regex |
| **Feature Engineering** | Scikit-Learn (`TfidfVectorizer`), Sentence-Transformers |
| **ML Algorithms** | Scikit-Learn, LightGBM, XGBoost, Transformers (Hugging Face) |
| **Tuning & Tracking** | Optuna, MLflow |
| **API & Web UI** | FastAPI, Uvicorn, Streamlit |
| **DevOps & Container** | Docker, Joblib, ONNX |

---

## 🚀 Quick Start (Local Setup)

```bash
# 1. Clone the repository
git clone https://github.com/your-username/email-classifier.git
cd email-classifier

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run EDA & Preprocessing Script
python src/preprocess.py

# 5. Launch Web UI Demo
streamlit run app.py
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.