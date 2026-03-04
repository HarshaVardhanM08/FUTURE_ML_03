# 🚀 AI Resume Screening & Job Matching Dashboard

## 📌 Project Overview

The **AI Resume Screening & Job Matching Dashboard** is an intelligent recruitment analytics system designed to automate and enhance the resume screening process using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

In modern recruitment workflows, organizations often receive **hundreds or even thousands of resumes** for a single job position. Manually reviewing these resumes is time-consuming, inefficient, and prone to human bias. Recruiters must evaluate candidate skills, compare qualifications, and match them with job requirements.

This project addresses that challenge by developing an **AI-powered Resume Screening and Candidate Ranking System** capable of automatically analyzing resume content and matching candidates with relevant job descriptions.

The system uses **TF-IDF (Term Frequency–Inverse Document Frequency)** for text feature extraction and **Cosine Similarity** to measure how closely a candidate's resume matches a job description.

An interactive **Streamlit dashboard** visualizes the analysis results with graphs, insights, and recruiter-friendly analytics.

### Key Capabilities

* 📊 Interactive data visualization dashboard
* 🧠 Machine learning based resume-job similarity analysis
* 📄 Resume dataset exploration
* 📈 Recruitment analytics
* 🏆 Automated candidate ranking system

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

Showcase how machine learning and NLP can be applied in **HR Technology (HRTech)**.

---

# ✨ Key Features

* 🔍 Automated resume analysis using NLP techniques
* 🤖 AI-based candidate matching system
* 📊 Interactive Streamlit dashboard with analytics graphs
* 📈 Resume and job dataset exploration
* 🏆 Candidate ranking based on similarity scores
* 📑 Executive insights for recruitment analysis

---

# 💻 System Requirements

### Software Requirements

* Python **3.8 or higher**
* pip (Python package manager)
* Git
* Web browser

### Recommended Development Environment

* VS Code / PyCharm
* Virtual environment (`venv` or `conda`)

---

# 🧠 Core Technologies Used

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
| **Natural Language Processing** | Resume text analysis              |

---

# 📊 Datasets Used

This project uses **two datasets** for resume analysis and job matching.

---

## 1️⃣ Resume Dataset

**File:** `Resume.csv`

⚠️ **Note:**
Due to GitHub file size limitations, the dataset is provided as a compressed file.

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

The original dataset **`Resume.csv` is approximately 56.3 MB**, which exceeds GitHub's recommended upload limits.

GitHub generally recommends keeping files **below 25 MB** for better repository performance.

To solve this issue:

* The original dataset `Resume.csv` was compressed into **Resume.csv.zip**
* The compressed dataset is included in the repository
* Users must extract the dataset before running the application

### Steps

1. Download or clone the repository
2. Locate the dataset file

```
Resume.csv.zip
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

# 📈 Dashboard Modules

### 1️⃣ Dataset Overview

Provides a high-level overview of both datasets.

Features:

* Total resumes
* Total job postings
* Unique job categories
* Dataset preview
* Category distribution visualization

---

### 2️⃣ Resume Dataset Analysis

Performs exploratory analysis on resume content.

Visualizations:

* Resume category distribution
* Resume length distribution
* Resume word cloud

Insights:

* Category frequency
* Resume text complexity
* Most common keywords

---

### 3️⃣ Job Dataset Analysis

Analyzes job descriptions.

Visualizations:

* Job description length distribution
* Top hiring companies
* Most common job roles

---

### 4️⃣ Resume-Job Matching System

The core AI component of the system.

The algorithm evaluates how well a resume matches a job description.

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

# 🧠 Model Workflow

```
Resume Text / Job Description
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Candidate Ranking
```

---

# 🏆 Candidate Ranking System

Candidates are ranked based on similarity scores.

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

# ⚙️ Installation Guide

## Step 1 — Clone Repository

```
git clone https://github.com/HarshaVardhanM08/FUTURE_ML_03.git
```

---

## Step 2 — Install Dependencies

```
pip install -r requirements.txt
```

---

## Step 3 — Extract Dataset

```
Resume.csv.zip → Resume.csv
```

---

## Step 4 — Run the Application

```
streamlit run app.py
```

The Streamlit dashboard will automatically open in your browser.

---

# 📁 Project Structure

```
FUTURE_ML_03
│
├── app.py
├── Resume.csv.zip
├── training_data.csv
├── requirements.txt
└── README.md
```

---

# 🌍 Real-World Applications

This system demonstrates how AI can improve recruitment systems.

Applications include:

* Applicant Tracking Systems (ATS)
* Resume screening automation
* Skill matching systems
* Recruitment analytics platforms
* Talent intelligence systems

Organizations can use such systems to **reduce hiring time and costs significantly**.

---

# 🔮 Future Enhancements

Possible improvements for future versions:

* Resume PDF parsing
* Advanced skill extraction using NLP
* AI-based resume summaries
* Advanced recruiter analytics dashboard
* Authentication system
* Cloud deployment
* Deep learning-based semantic matching

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge in:

* Natural Language Processing
* Machine Learning pipelines
* Data visualization
* Interactive dashboards
* AI system development

---

# 👨‍💻 Author

**Harsha Vardhan Maradana**

Python Full Stack Developer (In Progress)
Machine Learning Enthusiast

GitHub
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

The **AI Resume Screening & Job Matching Dashboard** demonstrates how machine learning and natural language processing can modernize recruitment workflows.

By combining **data science, NLP techniques, and interactive visualization**, this system provides a scalable solution for building intelligent recruitment platforms.
