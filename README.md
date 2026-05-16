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

## Critical Insight
- Sleep quality is never determined by a single factor alone.
- An engineer with high stress and poor BMI may sleep worse than a sales rep with low stress and healthy habits.
- This dataset reveals correlations — real sleep health is multidimensional and deeply personal.

## What's Next
This EDA naturally sets up a **machine learning model** that combines
all factors simultaneously to predict sleep quality — far more powerful
than analysing variables in isolation.

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
- Python 3.10
- Pandas — data manipulation
- Seaborn — statistical visualisation
- Matplotlib — plotting
