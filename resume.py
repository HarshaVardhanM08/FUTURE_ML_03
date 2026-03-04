import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud

st.set_page_config(page_title="AI Resume Screening Dashboard", layout="wide")

st.title("AI Resume Screening & Job Matching Dashboard")

# Load Data
@st.cache_data
def load_data():
    resume = pd.read_csv("Resume.csv")
    jobs = pd.read_csv("training_data.csv")
    return resume, jobs

resume_df, job_df = load_data()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
"Dataset Overview",
"Resume Analysis",
"Job Analysis",
"Resume Matching",
"Executive Report"
])

# -----------------------------------
# TAB 1 DATASET OVERVIEW
# -----------------------------------

with tab1:

    st.header("Dataset Overview")

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Resumes", len(resume_df))
    col2.metric("Total Jobs", len(job_df))
    col3.metric("Unique Categories", resume_df["Category"].nunique())

    st.subheader("Resume Dataset Preview")
    st.dataframe(resume_df.head())

    st.subheader("Job Dataset Preview")
    st.dataframe(job_df.head())

    st.subheader("Resume Category Distribution")

    fig = px.bar(
        resume_df["Category"].value_counts(),
        title="Resumes per Category"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------------
# TAB 2 RESUME ANALYSIS
# -----------------------------------

with tab2:

    st.header("Resume Dataset Analysis")

    resume_df["resume_length"] = resume_df["Resume_str"].str.len()

    col1,col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            resume_df,
            x="resume_length",
            nbins=50,
            title="Resume Length Distribution"
        )

        st.plotly_chart(fig)

    with col2:

        fig = px.pie(
            values=resume_df["Category"].value_counts().values,
            names=resume_df["Category"].value_counts().index,
            title="Category Distribution"
        )

        st.plotly_chart(fig)

    st.subheader("Word Cloud of Resume Text")

    text = " ".join(resume_df["Resume_str"].astype(str))

    wc = WordCloud(width=800,height=400).generate(text)

    fig,ax = plt.subplots()

    ax.imshow(wc)
    ax.axis("off")

    st.pyplot(fig)


# -----------------------------------
# TAB 3 JOB ANALYSIS
# -----------------------------------

with tab3:

    st.header("Job Dataset Analysis")

    job_df["desc_length"] = job_df["job_description"].str.len()

    col1,col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            job_df,
            x="desc_length",
            title="Job Description Length"
        )

        st.plotly_chart(fig)

    with col2:

        fig = px.bar(
            job_df["company_name"].value_counts().head(10),
            title="Top Hiring Companies"
        )

        st.plotly_chart(fig)

    st.subheader("Job Titles")

    fig = px.bar(
        job_df["position_title"].value_counts().head(10),
        title="Top Job Roles"
    )

    st.plotly_chart(fig)


# -----------------------------------
# TAB 4 RESUME MATCHING
# -----------------------------------

with tab4:

    st.header("Resume – Job Matching System")

    job_titles = job_df["position_title"].unique()

    selected_job = st.selectbox("Select Job Role", job_titles)

    job_text = job_df[job_df["position_title"] == selected_job]["job_description"].iloc[0]

    vectorizer = TfidfVectorizer(stop_words="english")

    resume_vectors = vectorizer.fit_transform(resume_df["Resume_str"])

    job_vector = vectorizer.transform([job_text])

    similarity = cosine_similarity(job_vector, resume_vectors)[0]

    resume_df["match_score"] = similarity

    ranked = resume_df.sort_values(by="match_score",ascending=False).head(10)

    st.subheader("Top 10 Matching Candidates")

    st.dataframe(ranked[["Category","match_score"]])

    fig = px.bar(
        ranked,
        x="match_score",
        y="Category",
        orientation="h",
        title="Candidate Ranking"
    )

    st.plotly_chart(fig)


# -----------------------------------
# TAB 5 EXECUTIVE REPORT
# -----------------------------------

with tab5:

    st.header("Executive Summary")

    top_category = resume_df["Category"].value_counts().idxmax()

    top_company = job_df["company_name"].value_counts().idxmax()

    st.markdown(f"""

### Key Insights

**Most common resume category:** {top_category}

**Company posting most jobs:** {top_company}

**Total resumes analyzed:** {len(resume_df)}

**Total job postings:** {len(job_df)}

### System Capabilities

- Resume classification
- Job matching
- Candidate ranking
- NLP based similarity

### Recommendation

Recruiters can shortlist candidates automatically using AI similarity scoring.

""")