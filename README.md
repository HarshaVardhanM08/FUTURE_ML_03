# 🚀 AI Resume Screening & Job Matching Dashboard

## 📌 Project Overview

The **AI Resume Screening & Job Matching Dashboard** is an intelligent recruitment analytics system designed to automate and enhance the resume screening process using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

Modern recruitment often involves reviewing **hundreds or thousands of resumes** for a single job opening. Manually screening these resumes is time-consuming, error-prone, and inefficient. This project solves that problem by building an **AI-powered resume analysis and candidate ranking system** that can automatically evaluate resumes and match them with relevant job descriptions.

The system uses **TF-IDF vectorization** and **cosine similarity** to measure how closely a candidate's resume matches a job description. It also provides **interactive visual analytics dashboards** using **Streamlit** to help recruiters analyze data through multiple charts and insights.

The application integrates:

* 📊 Interactive data visualization dashboards
* 🧠 Machine learning based resume-job similarity analysis
* 📄 Resume dataset exploration
* 📈 Job market analytics
* 🏆 Candidate ranking system

The dashboard transforms raw recruitment data into **actionable insights**, enabling HR professionals and recruiters to make **data-driven hiring decisions** efficiently.

---

# 🎯 Project Objectives

The main objectives of this project are:

1️⃣ **Automate Resume Screening**
Reduce manual effort by automatically analyzing and filtering resumes.

2️⃣ **Improve Candidate Matching**
Use NLP techniques to match resumes with job descriptions accurately.

3️⃣ **Provide Data Insights**
Visualize recruitment data through interactive dashboards.

4️⃣ **Enhance Recruitment Efficiency**
Help recruiters shortlist the most relevant candidates quickly.

5️⃣ **Demonstrate Practical AI Applications**
Showcase real-world use of machine learning in HR technology.

---

# 🧠 Core Technologies Used

The system integrates several technologies across **Data Science, Machine Learning, and Web Applications**.

| Technology               | Purpose                           |
| ------------------------ | --------------------------------- |
| **Python**               | Core programming language         |
| **Streamlit**            | Interactive dashboard development |
| **Pandas**               | Data manipulation and analysis    |
| **Scikit-learn**         | Machine learning algorithms       |
| **TF-IDF Vectorization** | Text feature extraction           |
| **Cosine Similarity**    | Resume-job similarity scoring     |
| **Plotly**               | Interactive visualizations        |
| **Matplotlib / Seaborn** | Statistical plotting              |
| **WordCloud**            | Text visualization                |
| **NLP Techniques**       | Resume content analysis           |

---

# 📊 Datasets Used

This project utilizes two primary datasets:

---

## 1️⃣ Resume Dataset

**File:** `Resume.csv`

This dataset contains structured resume data categorized by job roles.

### Dataset Structure

| Column      | Description                       |
| ----------- | --------------------------------- |
| ID          | Unique identifier for each resume |
| Resume_str  | Complete resume text              |
| Resume_html | HTML version of the resume        |
| Category    | Job category label                |

### Dataset Characteristics

* ~2500 resumes
* Multiple job categories
* Rich textual data for NLP analysis
* Suitable for resume classification and screening

### Use Cases

* Resume classification
* Skill extraction
* Candidate ranking
* Job matching systems

---

## 2️⃣ Job Description Dataset

**File:** `training_data.csv`

This dataset contains job descriptions from various companies.

### Dataset Structure

| Column             | Description                |
| ------------------ | -------------------------- |
| company_name       | Name of the hiring company |
| position_title     | Job title                  |
| job_description    | Detailed job description   |
| description_length | Length of job description  |
| model_response     | Structured AI response     |

### Dataset Characteristics

* Multiple job postings
* Different industries
* Text-based job requirements
* Useful for job matching analysis

---

---

# ⚠️ Dataset Size Note

The original **`Resume.csv` dataset is approximately 56.3 MB in size**, which exceeds GitHub’s recommended file upload limit for standard repository files.

GitHub typically recommends keeping individual files **below 25 MB** for smooth repository performance. Due to this limitation, uploading the raw dataset directly to the repository was not feasible.

### 📦 Solution Implemented

To ensure the dataset could still be included in the project repository:

* The **`Resume.csv` file was compressed into a ZIP archive**
* The compressed file was uploaded as **`Resume.zip`**
* Users must **extract the ZIP file before running the application**

### 📂 Steps to Use the Dataset

1. Download the repository
2. Locate the file:

```
Resume.zip
```

3. Extract the ZIP file

4. After extraction, you will obtain:

```
Resume.csv
```

5. Place the extracted file in the project directory:

```
resume-screening-dashboard/
│
├── app.py
├── Resume.csv   ← extracted file
├── training_data.csv
```

### 📌 Why This Was Necessary

Large datasets can slow down repository performance and increase clone time. Compressing the dataset allows the project to remain **GitHub-friendly while still providing access to the full dataset required for the AI resume screening system.**

---


# 📊 Dashboard Features

The Streamlit dashboard provides **multiple analytical modules** organized into interactive tabs.

---

# 🖥️ Dashboard Architecture

```
AI Resume Screening Dashboard
│
├── Dataset Overview
├── Resume Analysis
├── Job Analysis
├── Resume–Job Matching
└── Executive Report
```

---

# 📈 Dashboard Modules

---

# 1️⃣ Dataset Overview

This section provides a high-level overview of the datasets used in the system.

### Features

* Total number of resumes
* Total number of job postings
* Number of unique job categories
* Raw dataset preview
* Resume category distribution visualization

### Insights Provided

* Most common job categories
* Dataset size and structure
* Data quality overview

---

# 2️⃣ Resume Dataset Analysis

This module performs exploratory data analysis on the resume dataset.

### Visualizations Included

📊 Resume Category Distribution
📊 Resume Length Distribution
📊 Word Cloud of Resume Content

### Analytical Insights

* Distribution of job categories
* Text complexity of resumes
* Frequently occurring words in resumes
* Resume content patterns

---

# 3️⃣ Job Dataset Analysis

This section analyzes the job description dataset.

### Visualizations Included

📊 Job Description Length Distribution
📊 Top Hiring Companies
📊 Job Role Frequency

### Analytical Insights

* Companies posting the most jobs
* Most common job roles
* Job description complexity

---

# 4️⃣ Resume–Job Matching System

This is the **core AI component** of the project.

The system matches resumes with job descriptions using **Natural Language Processing techniques**.

### Algorithm Used

The system applies:

1️⃣ **TF-IDF Vectorization**

This converts textual data into numerical vectors based on word importance.

```
Term Frequency – Inverse Document Frequency
```

2️⃣ **Cosine Similarity**

Measures similarity between two text vectors.

```
Similarity Score Range:
0 → Completely different
1 → Perfect match
```

### Matching Pipeline

```
Job Description
        ↓
TF-IDF Vectorization
        ↓
Resume Vectorization
        ↓
Cosine Similarity
        ↓
Ranking of Candidates
```

### Output

* Top matching resumes
* Candidate ranking scores
* Visual candidate ranking charts

---

# 🏆 Candidate Ranking System

The ranking system identifies the **most suitable candidates** for a selected job role.

### Process

1️⃣ Convert resumes and job descriptions to TF-IDF vectors
2️⃣ Compute cosine similarity scores
3️⃣ Rank candidates based on similarity score

### Output

| Rank | Resume Category  | Match Score |
| ---- | ---------------- | ----------- |
| 1    | Data Science     | 0.89        |
| 2    | Python Developer | 0.85        |
| 3    | AI Engineer      | 0.82        |

---

# 📑 Executive Summary Module

The executive report provides **high-level insights** from the entire analysis.

### Key Metrics

* Most common resume category
* Top hiring company
* Total resumes analyzed
* Total job postings

### Business Insights

The dashboard helps recruiters:

✔ Identify talent pools
✔ Analyze hiring trends
✔ Evaluate job market demand
✔ Automate candidate screening

---

# ⚙️ Installation Guide

## Step 1 — Clone Repository

```
git clone https://github.com/yourusername/resume-screening-dashboard.git
```

---

## Step 2 — Install Dependencies

```
pip install streamlit pandas scikit-learn plotly seaborn matplotlib wordcloud
```

---

## Step 3 — Run the Application

```
streamlit run app.py
```

The dashboard will launch automatically in your browser.

---

# 📁 Project Structure

```
resume-screening-dashboard
│
├── app.py
├── Resume.csv
├── training_data.csv
├── requirements.txt
└── README.md
```

---

# 📊 Types of Graphs Included

The dashboard integrates multiple visualization techniques.

### Charts Implemented

* Bar Charts
* Pie Charts
* Histograms
* Word Clouds
* Ranking Charts
* Distribution Graphs
* Interactive Plotly Charts

These visualizations help users easily interpret recruitment data.

---

# 🌍 Real-World Applications

This project demonstrates how AI can be applied in **Human Resource Technology (HRTech)**.

### Practical Applications

* Applicant Tracking Systems (ATS)
* Automated Resume Screening
* Candidate Skill Matching
* Recruitment Analytics
* Talent Intelligence Platforms

Companies can integrate such systems to significantly **reduce recruitment time and costs**.

---

# 🔮 Future Enhancements

The system can be further improved with additional AI features.

### Planned Improvements

* 📄 Resume PDF parsing
* 🧠 Skill extraction using Named Entity Recognition
* 🤖 AI-powered resume summaries
* 📊 Advanced analytics dashboards
* 🧑‍💼 Recruiter authentication system
* 🌐 Cloud deployment
* 🧠 Deep learning resume matching

---

# 📚 Learning Outcomes

This project demonstrates knowledge of:

* Natural Language Processing
* Machine Learning pipelines
* Data visualization
* Interactive dashboard development
* Real-world AI system design

It serves as a **practical example of AI applied in recruitment technology**.

---

# 👨‍💻 Author

**Harsha Vardhan Maradana**

Python Full Stack Developer (In Progress) | Game Development Enthusiast | Focused on Creating Immersive & Innovative Digital Experiences

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

# 📜 License

This project is open-source and available under the **MIT License**.

---

# 🚀 Final Note

The **AI Resume Screening & Job Matching Dashboard** showcases how artificial intelligence can transform traditional recruitment workflows into intelligent, data-driven systems.

By combining **machine learning, NLP, and interactive visualization**, the project demonstrates a scalable approach to building next-generation recruitment platforms.
