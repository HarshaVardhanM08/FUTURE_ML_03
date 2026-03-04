# 🚀 AI Resume Screening & Job Matching Dashboard

## 📌 Project Overview

The **AI Resume Screening & Job Matching Dashboard** is an intelligent recruitment analytics system designed to automate and enhance the resume screening process using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

In modern recruitment workflows, organizations often receive **hundreds or even thousands of resumes** for a single job position. Manually reviewing these resumes is not only time-consuming but also prone to human bias and inefficiencies. Recruiters must read through large volumes of documents, identify relevant skills, compare candidate qualifications, and match them with job requirements.

This project addresses that challenge by developing an **AI-powered Resume Screening and Candidate Ranking System** capable of automatically analyzing resume content and matching candidates with relevant job descriptions.

The system uses **TF-IDF (Term Frequency–Inverse Document Frequency)** for text feature extraction and **Cosine Similarity** to measure how closely a candidate's resume matches a job description.

An interactive **Streamlit dashboard** is used to visualize the analysis results with multiple graphs, insights, and recruiter-friendly analytics.

### Key Capabilities

* 📊 Interactive data visualization dashboards
* 🧠 Machine learning based resume-job similarity analysis
* 📄 Resume dataset exploration
* 📈 Job market analytics
* 🏆 Candidate ranking and recommendation system

The dashboard transforms raw recruitment data into **actionable insights**, helping recruiters and HR teams make **data-driven hiring decisions quickly and efficiently**.

---

# 🎯 Project Objectives

The primary goals of this project are:

### 1️⃣ Automate Resume Screening

Reduce manual effort by automatically analyzing resumes using machine learning.

### 2️⃣ Improve Candidate Matching

Use NLP techniques to match resumes with job descriptions accurately.

### 3️⃣ Provide Data Insights

Visualize recruitment data through interactive dashboards.

### 4️⃣ Enhance Recruitment Efficiency

Allow recruiters to shortlist candidates faster.

### 5️⃣ Demonstrate Real-World AI Applications

Showcase how machine learning and NLP can be applied in HR Technology (HRTech).

---

# 🧠 Core Technologies Used

The system integrates several technologies across **Machine Learning, Data Science, and Web Applications**.

| Technology                      | Purpose                           |
| ------------------------------- | --------------------------------- |
| **Python**                      | Core programming language         |
| **Streamlit**                   | Interactive dashboard development |
| **Pandas**                      | Data manipulation and analysis    |
| **Scikit-learn**                | Machine learning algorithms       |
| **TF-IDF Vectorization**        | Text feature extraction           |
| **Cosine Similarity**           | Resume-job similarity scoring     |
| **Plotly**                      | Interactive visualizations        |
| **Matplotlib / Seaborn**        | Statistical plotting              |
| **WordCloud**                   | Text visualization                |
| **Natural Language Processing** | Resume content analysis           |

---

# 📊 Datasets Used

This project uses **two datasets** for resume analysis and job matching.

---

## 1️⃣ Resume Dataset

**File:** `Resume.csv`

⚠️ **Note:**
Due to GitHub file size limitations, the dataset is provided as a compressed file **Resume.zip**.

### Dataset Structure

| Column      | Description                       |
| ----------- | --------------------------------- |
| ID          | Unique identifier for each resume |
| Resume_str  | Complete resume text              |
| Resume_html | HTML version of resume            |
| Category    | Job category                      |

### Dataset Characteristics

* ~2500 resumes
* Multiple job categories
* Rich textual data
* Suitable for NLP analysis

### Use Cases

* Resume classification
* Skill extraction
* Resume screening
* Candidate ranking
* Job matching systems

---

## 2️⃣ Job Description Dataset

**File:** `training_data.csv`

### Dataset Structure

| Column             | Description               |
| ------------------ | ------------------------- |
| company_name       | Hiring company            |
| position_title     | Job title                 |
| job_description    | Detailed job description  |
| description_length | Length of job description |
| model_response     | Structured AI response    |

### Dataset Characteristics

* Multiple job postings
* Different industries
* Text-based job requirements
* Useful for resume-job matching analysis

---

# ⚠️ Dataset Size Note

The original **Resume.csv dataset is approximately 56.3 MB**, which exceeds GitHub's recommended file upload size limits.

GitHub generally recommends keeping files **below 25 MB** for better repository performance.

Because of this limitation, the dataset was **compressed into a ZIP archive** before uploading.

### Solution Implemented

* `Resume.csv` → compressed into `Resume.zip`
* The compressed dataset is included in the repository
* Users must **extract the dataset before running the application**

### Steps to Use the Dataset

1. Download or clone the repository
2. Locate the dataset file

```
Resume.zip
```

3. Extract the ZIP file

4. After extraction you will obtain

```
Resume.csv
```

5. Place it inside the project directory

```
FUTURE_ML_03
│
├── app.py
├── Resume.csv
├── training_data.csv
```

This approach ensures the repository remains **GitHub-friendly while still providing the full dataset required for the AI system**.

---

# 📊 Dashboard Features

The Streamlit dashboard provides **multiple analytical modules organized into interactive tabs**.

---

# 🖥️ Dashboard Architecture

```
AI Resume Screening Dashboard
│
├── Dataset Overview
├── Resume Analysis
├── Job Analysis
├── Resume-Job Matching
└── Executive Report
```

---

# 📷 Dashboard Preview

*(You can add screenshots here after running the app)*

```
screenshots/
│
├── overview.png
├── resume_analysis.png
├── job_analysis.png
├── candidate_ranking.png
```

---

# 📈 Dashboard Modules

---

# 1️⃣ Dataset Overview

Provides high-level insights about both datasets.

### Features

* Total resumes
* Total job postings
* Unique job categories
* Raw dataset preview
* Resume category distribution graph

---

# 2️⃣ Resume Dataset Analysis

Performs exploratory analysis on resume content.

### Visualizations

* Resume category distribution
* Resume length distribution
* Resume word cloud

### Insights

* Resume category frequency
* Text complexity
* Most common words in resumes

---

# 3️⃣ Job Dataset Analysis

Analyzes job descriptions.

### Visualizations

* Job description length distribution
* Top hiring companies
* Most common job roles

---

# 4️⃣ Resume–Job Matching System

This is the **core AI functionality** of the system.

The algorithm measures how well a resume matches a job description.

### Algorithm Used

#### TF-IDF Vectorization

Converts text into numerical vectors.

```
Term Frequency – Inverse Document Frequency
```

#### Cosine Similarity

Measures similarity between vectors.

```
Score Range
0 → No similarity
1 → Perfect match
```

---

### Matching Pipeline

```
Job Description
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Resume Vectorization
        ↓
Cosine Similarity
        ↓
Candidate Ranking
```

---

# 🏆 Candidate Ranking System

The system ranks candidates based on similarity scores.

### Process

1. Convert resumes and job descriptions into TF-IDF vectors
2. Compute cosine similarity scores
3. Rank candidates by highest similarity

### Example Output

| Rank | Resume Category  | Match Score |
| ---- | ---------------- | ----------- |
| 1    | Data Science     | 0.89        |
| 2    | Python Developer | 0.85        |
| 3    | AI Engineer      | 0.82        |

---

# 📑 Executive Summary Module

The executive report provides high-level insights for recruiters.

### Key Metrics

* Most common resume category
* Top hiring company
* Total resumes analyzed
* Total job postings

### Business Insights

The dashboard enables recruiters to:

✔ Identify talent pools
✔ Analyze hiring trends
✔ Evaluate job demand
✔ Automate candidate screening

---

# ⚙️ Installation Guide

## Step 1 — Clone Repository

```
git clone https://github.com/HarshaVardhanM08/FUTURE_ML_03.git
```

---

## Step 2 — Install Dependencies

```
pip install streamlit pandas scikit-learn plotly seaborn matplotlib wordcloud
```

---

## Step 3 — Extract Dataset

Extract the compressed dataset.

```
Resume.zip → Resume.csv
```

---

## Step 4 — Run the Application

```
streamlit run app.py
```

The Streamlit dashboard will open automatically in your browser.

---

# 📁 Project Structure

```
FUTURE_ML_03
│
├── app.py
├── Resume.zip
├── training_data.csv
├── requirements.txt
├── README.md
└── screenshots
```

---

# 📊 Types of Graphs Included

The dashboard integrates multiple visualization techniques.

### Graph Types

* Bar Charts
* Pie Charts
* Histograms
* Word Clouds
* Ranking Graphs
* Distribution Charts
* Interactive Plotly Charts

These visualizations allow users to **understand recruitment data quickly and clearly**.

---

# 🌍 Real-World Applications

This system demonstrates how AI can transform recruitment systems.

### Use Cases

* Applicant Tracking Systems (ATS)
* Resume screening automation
* Skill matching systems
* Recruitment analytics platforms
* Talent intelligence systems

Organizations can use such systems to **reduce hiring time and costs significantly**.

---

# 🔮 Future Enhancements

Potential improvements for future versions include:

* 📄 Resume PDF parsing
* 🧠 Skill extraction using Named Entity Recognition
* 🤖 AI resume summaries
* 📊 Advanced recruiter analytics
* 🧑‍💼 Recruiter authentication
* 🌐 Cloud deployment
* 🧠 Deep learning based resume matching

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge in:

* Natural Language Processing
* Machine Learning pipelines
* Data visualization
* Interactive dashboards
* AI system design

It serves as a **real-world example of AI applied to recruitment technology**.

---

# 👨‍💻 Author

**Harsha Vardhan Maradana**

Python Full Stack Developer (In Progress)
Game Development Enthusiast
Focused on creating **innovative AI-powered digital solutions**.

GitHub Profile
https://github.com/HarshaVardhanM08

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

# 📜 License

This project is open source and available under the **MIT License**.

---

# 🚀 Final Note

The **AI Resume Screening & Job Matching Dashboard** demonstrates how machine learning and NLP can revolutionize traditional recruitment processes.

By combining **data science, natural language processing, and interactive visualization**, this system provides a scalable approach to building intelligent recruitment platforms.
