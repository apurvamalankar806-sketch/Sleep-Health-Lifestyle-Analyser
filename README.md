## Overview
An end-to-end Exploratory Data Analysis on the Sleep Health and Lifestyle 
dataset (374 individuals), uncovering how stress, BMI, occupation, and 
physical activity influence sleep quality and duration.

## Dataset
- **Source:** [Kaggle — Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
- **Records:** 374 individuals
- **Features:** 13 variables including age, occupation, sleep duration,
  sleep quality, stress level, BMI, heart rate, and daily steps

## Steps Covered
| Step | Description |
|------|-------------|
| 1 | Setup & imports |
| 2 | Load & explore the data |
| 3 | Data cleaning |
| 4 | Histograms & distributions |
| 5 | Correlation heatmap |
| 6 | Deep analysis — occupation, BMI, stress |
| 7 | Conclusions & summary |

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
| Features used | 10 (stress, age, heart rate, activity, BMI, and more) |
| Target | Sleep Quality Score (4–9) |
| Accuracy | 96.30% on clean deduplicated data |
| Top predictor | Stress Level (importance score 0.30) |

### Feature Importance ranking:
1. Stress Level — 0.30
2. Age — 0.19
3. Heart Rate — 0.13
4. Physical Activity — 0.08
5. Blood Pressure — 0.07

# Conclusion
Sleep quality is not driven by one factor — it is the result of
multiple variables working together. However, this analysis clearly
shows that **stress management** and **consistent sleep duration**
are the two most actionable levers for improving sleep health.

Occupations with high pressure and irregular schedules consistently
produce worse sleepers, while structured, stable work environments
correlate with better rest. BMI adds another layer — poor metabolic
health quietly undermines sleep consistency even when other factors
look fine.

## Tools Used
`Python` `Pandas` `Seaborn` `Matplotlib` `Scikit-learn` `Joblib` `Streamlit`
