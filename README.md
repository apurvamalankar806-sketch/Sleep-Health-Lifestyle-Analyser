# Sleep Health & Lifestyle Analyser


![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![Model](https://img.shields.io/badge/Model-Random%20Forest-green)
![Accuracy](https://img.shields.io/badge/Accuracy-96.30%25-brightgreen)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

## About
An end-to-end Data Science project combining Exploratory Data Analysis
and Machine Learning to understand and predict sleep quality based on
lifestyle and health factors.

Built on a dataset of 374 individuals, the project features an
interactive Streamlit web app where users can explore data visually
and take a smart quiz to predict their own sleep quality score —
no medical jargon required.

##  Live App
Deployment coming soon on Streamlit Cloud

## Key Findings

| Factor | Correlation | Insight |
|--------|-------------|---------|
| Stress Level | -0.90 | Strongest negative predictor |
| Sleep Duration | +0.88 | Strongest positive predictor |
| Heart Rate | -0.66 | High rate = worse sleep |
| Age | +0.47 | Older = slightly better sleep |
| BMI Category | moderate | Obese individuals sleep least consistently |
| Daily Steps | +0.02 | Almost no impact — surprising! |

## Project Structure

## EDA Notebook

| Step | Description |
|------|-------------|
| 1 | Setup & imports |
| 2 | Load & explore the data |
| 3 | Data cleaning & deduplication |
| 4 | Distribution analysis — histograms & KDE |
| 5 | Correlation heatmap |
| 6 | Deep dive — occupation, BMI, stress |
| 7 | Conclusions & recommendations |

## Key Findings

**1. Stress is the #1 predictor of poor sleep (-0.90 correlation)**
High stress almost guarantees poor sleep quality — the strongest
relationship found in the entire dataset.

**2. Sleep duration drives quality (+0.88 correlation)**
Longer sleep consistently means better quality. The sweet spot
is 7–8 hours per night.

**3. Occupation reflects underlying stress patterns**
Engineers average 8.4/10 sleep quality while Sales Representatives
average just 4.0/10 — a 4+ point gap driven by job stress differences.

**4. BMI silently affects sleep consistency**
Obese individuals show the most inconsistent sleep patterns.
Normal weight individuals sleep the most stably.

**5. Daily steps have almost no impact (0.02 correlation)**
Surprising finding — casual walking barely affects sleep.
Structured physical activity matters far more.

## ML Model

| Detail | Value |
|--------|-------|
| Algorithm | Random Forest Classifier |
| Features | 10 lifestyle & health inputs |
| Target | Sleep Quality Score (4–9) |
| Training data | 132 unique records |
| Duplicates removed | 242 out of 374 |
| Accuracy | 96.30% on clean deduplicated data |
| Top predictor | Stress Level (importance: 0.30) |

### Feature Importance Ranking
| Rank | Feature | Score |
|------|---------|-------|
| 1 | Stress Level | 0.30 |
| 2 | Age | 0.19 |
| 3 | Heart Rate | 0.13 |
| 4 | Physical Activity Level | 0.08 |
| 5 | Blood Pressure | 0.07 |
| 6 | Daily Steps | 0.07 |
| 7 | Occupation | 0.06 |
| 8 | BMI Category | 0.05 |
| 9 | Gender | 0.02 |
| 10 | Sleep Disorder | 0.01 |

## Streamlit App Features
- Interactive EDA dashboard with occupation, BMI and gender filters
- Real-time metric cards — sleep quality, stress, duration
- Smart sleep quality quiz — natural questions, no technical inputs
- ML-powered prediction with personalised recommendations
- Two tab layout — Data Explorer and Sleep Quiz

## Limitations
- Only 132 unique records after deduplication — small dataset
- 96.30% accuracy may not generalise to larger populations
- Self-reported data may contain response bias
- A larger, more diverse dataset would improve model reliability

## Conclusion
Sleep quality is never determined by a single factor — it is the
result of multiple variables working together. This project shows
that stress management and consistent sleep duration are the two
most actionable levers for better sleep health.

## Tools & Libraries
`Python` `Pandas` `NumPy` `Seaborn` `Matplotlib`
`Scikit-learn` `Joblib` `Streamlit`

## Dataset
[Sleep Health and Lifestyle — Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
