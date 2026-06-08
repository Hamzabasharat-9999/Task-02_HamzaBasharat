# 🔬 DecodeLabs Industrial Data Analytics Track (Batch 2026)

Welcome to my professional portfolio repository tracking enterprise business intelligence, data sanitization, and programmatic data forensics executed during my industrial placement.

---

## 🛠️ Project 1: Automated Data Cleaning & Sanitization
* **Objective:** Fulfill the 0% data error verification gate threshold by handling missing values, standardizing variations, and scrubbing corruption.
* **Core Mechanisms:**
  * Automated character symbol stripping and structural value imputation on primary monetary features via numerical column Medians.
  * Executed a strict duplicate primary key verification check on transactional logs (`OrderID`), reducing replication anomalies down to a perfect 0% error margin.
  * Standardized diverse chronological tracking entries into the global uniform ISO 8601 standard (`YYYY-MM-DD`).

---

## 🕵️‍♂️ Project 2: Exploratory Data Analysis (EDA) Forensic Audit
* **Objective:** Transition past surface-level reporting to interrogate operational center of gravity distributions, trace relationship vectors, and separate commercial signals from background data noise.
* **Core Forensic Mechanisms:**
  * Generated descriptive statistics and five-number summary profiles mapping asset ceilings and transactional velocities over 1,200 unique records.
  * Implemented non-parametric Interquartile Range (IQR) fence algorithms ($Q3 + 1.5 \times IQR$) to isolate 8 hyper-critical high-value bulk corporate enterprise purchase streams above a strict $3,330.41 boundary.
  * Computed a Pearson Product-Moment Matrix discovering that product valuation (`UnitPrice`) dictates a dominant positive linear velocity signature ($r = 0.7171$) over simple volume size manipulations ($r = 0.6153$).

---

## 💻 Technical Framework & Execution Controls

### Core Environment Requirements
Ensure your workspace contains a stable deployment of Python 3.x along with the necessary enterprise numerical packages:
```bash
pip install pandas numpy


# Execute Week 1 Data Sanitization Engine
python clean_data.py

# Execute Week 2 Forensic Extraction Audit
python eda_forensics.py
