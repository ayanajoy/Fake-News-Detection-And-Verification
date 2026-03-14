# Fake News Detection & Verification Tool

The **Fake News Detection & Verification Tool** is an AI-based web application designed to detect whether a news article is **REAL or FAKE** using Natural Language Processing (NLP), Machine Learning, and Transformer-based models.

The system analyzes textual content, extracts meaningful linguistic features, classifies the article using a trained model, and verifies factual claims using external fact-checking sources.

This project was developed in **multiple milestones**, where each milestone adds new functionality to the system.

---

# Project Objectives

- Detect fake news automatically using AI
- Process and analyze text using NLP techniques
- Extract important claims from articles
- Verify claims using trusted fact-checking sources
- Provide confidence scores for predictions
- Build a user-friendly web interface for news verification

---

# Milestones

## Milestone 1 – Machine Learning Model Development

In this milestone, a basic fake news detection model was developed.

Features implemented:

- Dataset preprocessing
- TF-IDF text vectorization
- Logistic Regression classifier
- Model training and evaluation
- Saving the trained model using Joblib
- Basic prediction system
- Simple web interface using FastAPI

Output:
- Prediction: **Real News / Fake News**
- Fake confidence score
- Real confidence score

---

## Milestone 2 – NLP Processing Pipeline

This milestone focuses on **text analysis and feature extraction** using NLP techniques.

Features implemented:

- Text cleaning
- Tokenization
- Lemmatization
- Named Entity Recognition (NER)
- Processing of news articles using spaCy
- Storage of processed data in SQLite database

This stage prepares the data for advanced AI analysis.

---

## Milestone 3 – Transformer Model & Claim Verification

Milestone 3 introduces **deep learning and fact verification**.

Features implemented:

- Transformer-based fake news classification (RoBERTa)
- Probability scores for fake and real predictions
- Extraction of factual claims from news articles
- Verification using **Google Fact Check API**
- NLP preprocessing metrics display
- Storage of prediction results in database
- Advanced web interface with result visualization

Output includes:

- Fake/Real classification
- Model confidence scores
- Extracted claims
- Verification results for each claim
- NLP processing statistics

---

## Milestone 4 – System Integration & UI Enhancement

The final milestone integrates all components into a complete working system.

Features implemented:

- Full web-based news verification portal
- User-friendly interface
- Visualization of model predictions
- Claim verification results
- Processing pipeline display
- Final AI-powered fake news detection system

---

# Technologies Used

## Programming Language
- Python

## Backend Frameworks
- FastAPI
- Flask

## Machine Learning
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer

## Deep Learning
- PyTorch
- Hugging Face Transformers
- RoBERTa Model

## Natural Language Processing
- spaCy
- NLTK

## Database
- SQLite

## Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## APIs
- Google Fact Check Tools API

## Tools
- Git
- GitHub
- Joblib

---

# System Workflow

1. User enters a news article in the web interface
2. The system cleans and preprocesses the text
3. NLP techniques extract linguistic features
4. The trained model analyzes the article
5. The system predicts whether the news is **REAL or FAKE**
6. Important claims are extracted from the text
7. Claims are verified using external fact-checking APIs
8. Results are displayed with confidence scores and verification status

---
