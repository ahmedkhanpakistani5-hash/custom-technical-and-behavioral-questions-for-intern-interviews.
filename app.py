import os
import streamlit as st
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="InterviewAI | Smart Interview Generator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.14), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(168, 85, 247, 0.12), transparent 25%),
        #070b18;
    color: #f8fafc;
}

/* Hide Streamlit default elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Main container */

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1020 0%, #0f172a 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.12);
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] label {
    color: #f8fafc !important;
}

/* Hero */

.hero {
    position: relative;
    padding: 45px 45px;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 30px;

    background:
        radial-gradient(circle at 85% 20%, rgba(139, 92, 246, 0.45), transparent 30%),
        radial-gradient(circle at 10% 100%, rgba(59, 130, 246, 0.35), transparent 30%),
        linear-gradient(135deg, #111936, #17113b 55%, #0f172a);

    border: 1px solid rgba(139, 92, 246, 0.3);

    box-shadow:
        0 25px 80px rgba(0, 0, 0, 0.35),
        inset 0 1px 0 rgba(255,255,255,0.06);
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 30px;
    background: rgba(139, 92, 246, 0.16);
    border: 1px solid rgba(167, 139, 250, 0.3);
    color: #c4b5fd;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: 46px;
    line-height: 1.1;
    margin: 0;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #ffffff;
}

.hero h1 span {
    background: linear-gradient(90deg, #a78bfa, #60a5fa, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #cbd5e1;
    font-size: 17px;
    line-height: 1.7;
    max-width: 760px;
    margin-top: 18px;
}

/* Feature cards */

.feature-card {
    padding: 22px;
    border-radius: 18px;
    min-height: 150px;

    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(148, 163, 184, 0.13);

    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 10px;
}

.feature-title {
    font-size: 16px;
    font-weight: 700;
    color: #f8fafc;
}

.feature-text {
    font-size: 13px;
    line-height: 1.5;
    color: #94a3b8;
    margin-top: 6px;
}

/* Section title */

.section-title {
    font-size: 25px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 16px;
    color: #f8fafc;
}

.section-subtitle {
    color: #94a3b8;
    margin-top: -8px;
    margin-bottom: 20px;
}

/* Input card */

.input-card {
    padding: 22px;
    border-radius: 20px;
    background: rgba(15, 23, 42, 0.78);
    border: 1px solid rgba(148, 163, 184, 0.13);
}

/* Text inputs */

.stTextInput input,
.stTextArea textarea {
    background-color: #0b1224 !important;
    color: #f8fafc !important;
    border: 1px solid #26334d !important;
    border-radius: 12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 0 1px #8b5cf6 !important;
}

.stTextInput label,
.stTextArea label {
    color: #cbd5e1 !important;
    font-weight: 600 !important;
}

/* Select boxes */

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #0b1224 !important;
    border-color: #26334d !important;
    color: #f8fafc !important;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    border: 1px solid rgba(139, 92, 246, 0.4);
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    font-weight: 700;
    padding: 13px 20px;
    transition: all 0.25s ease;
    box-shadow: 0 8px 25px rgba(79, 70, 229, 0.25);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(124, 58, 237, 0.4);
    border-color: #a78bfa;
}

/* Download button */

.stDownloadButton > button {
    border-radius: 12px !important;
    background: #111827 !important;
    border: 1px solid #334155 !important;
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* Metrics */

.metric-card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(148, 163, 184, 0.13);
    text-align: center;
}

.metric-number {
    font-size: 30px;
    font-weight: 800;
    color: #a78bfa;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 4px;
}

/* Question cards */

.question-card {
    padding: 24px;
    margin: 14px 0;
    border-radius: 18px;

    background:
        linear-gradient(145deg, rgba(17, 24, 39, 0.95), rgba(15, 23, 42, 0.95));

    border: 1px solid rgba(139, 92, 246, 0.18);

    box-shadow: 0 12px 35px rgba(0,0,0,0.2);
}

.question-card:hover {
    border-color: rgba(139, 92, 246, 0.45);
}

.question-label {
    color: #a78bfa;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.question-text {
    font-size: 18px;
    line-height: 1.55;
    color: #f8fafc;
    font-weight: 600;
    margin-top: 8px;
}

/* Result header */

.result-header {
    padding: 24px;
    border-radius: 20px;
    margin: 20px 0;

    background:
        radial-gradient(circle at 90% 0%, rgba(139,92,246,0.25), transparent 30%),
        #111827;

    border: 1px solid rgba(139,92,246,0.25);
}

.result-header h2 {
    margin: 0;
    color: white;
}

.result-header p {
    color: #94a3b8;
}

/* Info boxes */

.info-box {
    padding: 16px 18px;
    border-radius: 14px;
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(148, 163, 184, 0.12);
    color: #cbd5e1;
    font-size: 14px;
}

/* Footer */

.custom-footer {
    text-align: center;
    padding: 35px 0 10px;
    color: #64748b;
    font-size: 13px;
}

.custom-footer span {
    color: #a78bfa;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-badge">
✦ AI-POWERED RECRUITMENT TOOL
</div>

<h1>
Build Better Interviews<br>
with <span>AI Intelligence</span>
</h1>

<p>
Generate personalized technical, behavioral, and candidate-specific
interview questions based on the role, job description, candidate
profile, and your existing question bank.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FEATURES
# =========================================================

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Role-Specific</div>
        <div class="feature-text">
            Questions tailored to the exact internship or job role.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">AI-Powered</div>
        <div class="feature-text">
            Uses advanced LLM reasoning to create meaningful questions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">👤</div>
        <div class="feature-title">Candidate-Aware</div>
        <div class="feature-text">
            Generates questions from the candidate's profile and projects.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Instant Results</div>
        <div class="feature-text">
            Generate a complete interview set within seconds.
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# GROQ
# =========================================================

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    st.error(
        "⚠️ GROQ_API_KEY is not configured. "
        "Add your API key in Streamlit Secrets."
    )
    st.stop()

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-20b"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ Interview Setup")
    st.caption("Customize your AI-generated interview.")

    st.divider()

    technical_count = st.slider(
        "Technical Questions",
        1,
        15,
        5
    )

    behavioral_count = st.slider(
        "Behavioral Questions",
        1,
        10,
        3
    )

    difficulty = st.select_slider(
        "Difficulty",
        options=[
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        value="Intermediate"
    )

    focus = st.selectbox(
        "Interview Focus",
        [
            "Technical + Behavioral",
            "Technical Only",
            "Behavioral Only"
        ]
    )

    st.divider()

    total_questions = technical_count + behavioral_count + 3

    st.markdown("### 📊 Question Plan")

    st.markdown(
        f"""
        <div class="info-box">
        <b>{total_questions}</b> total questions<br><br>
        🔧 {technical_count} technical<br>
        💬 {behavioral_count} behavioral<br>
        👤 3 candidate-specific
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("Powered by Groq + GPT-OSS-20B")

# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📋 Interview Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Provide the candidate and role information to generate a personalized interview.</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    job_role = st.text_input(
        "💼 Job / Internship Role",
        placeholder="Example: AI / Machine Learning Intern"
    )

    job_description = st.text_area(
        "📝 Job Description",
        height=230,
        placeholder="""Example:

We are looking for an AI intern who understands Python,
machine learning, data preprocessing and basic deep learning.

Responsibilities:
• Prepare datasets
• Train ML models
• Analyze model performance
• Work with the AI development team
"""
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    intern_profile = st.text_area(
        "👤 Intern Profile / Resume",
        height=230,
        placeholder="""Example:

BS Software Engineering student.

Skills:
• Python
• Machine Learning
• Pandas
• Scikit-learn
• Streamlit

Projects:
• AI Resume Assistant
• Student Performance Predictor
"""
    )

    question_bank = st.text_area(
        "📚 Existing Question Bank (Optional)",
        height=230,
        placeholder="""Paste existing interview questions here.

Example:

• What is supervised learning?
• What is overfitting?
• Explain Python lists.
• What is cross-validation?
"""
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# GENERATION FUNCTION
# =========================================================

def generate_questions():

    prompt = f"""
You are an expert technical recruiter, software engineering
interviewer, and AI hiring specialist.

Generate a high-quality, personalized interview question set.

JOB ROLE:
{job_role}

JOB DESCRIPTION:
{job_description}

INTERN PROFILE:
{intern_profile}

EXISTING QUESTION BANK:
{question_bank if question_bank.strip() else "No existing question bank provided."}

DIFFICULTY:
{difficulty}

TECHNICAL QUESTION COUNT:
{technical_count}

BEHAVIORAL QUESTION COUNT:
{behavioral_count}

INTERVIEW FOCUS:
{focus}

REQUIREMENTS:

1. Questions must be directly relevant to the job role.
2. Match the candidate's apparent experience level.
3. Use the job description to identify required technical skills.
4. Use the candidate profile to create personalized questions.
5. Avoid unnecessary duplicates from the existing question bank.
6. Include practical and scenario-based technical questions.
7. Include questions about projects listed in the candidate profile.
8. Behavioral questions should evaluate teamwork, communication,
   problem solving, adaptability and learning ability.
9. Technical questions should test understanding rather than memorization.
10. Keep questions appropriate for an internship interview.
11. Include a short evaluation guide for every question.
12. Do not make answers excessively long.
13. Avoid discriminatory or inappropriate interview questions.

OUTPUT FORMAT:

# 🔧 Technical Questions

For each question:

### Technical Question 1

**Question:** ...

**Why Ask:** ...

**Expected Answer / Key Points:** ...

**What to Evaluate:** ...

Repeat until the requested number of technical questions is reached.

# 💬 Behavioral Questions

For each question:

### Behavioral Question 1

**Question:** ...

**Why Ask:** ...

**What a Strong Answer Should Show:** ...

**What to Evaluate:** ...

Repeat until the requested number of behavioral questions is reached.

# 👤 Candidate-Specific Questions

Generate exactly 3 questions specifically based on
the candidate profile, skills, education or projects.

For each:

### Candidate Question 1

**Question:** ...

**Why Ask:** ...

**What to Evaluate:** ...

# 📊 Interviewer Summary

Provide 3-5 concise bullet points explaining what
the interviewer should focus on when evaluating this candidate.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert technical recruiter and "
                    "AI interview specialist. Generate practical, "
                    "fair and personalized internship interview questions."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.6,
        max_completion_tokens=6000,
        reasoning_effort="medium"
    )

    return response.choices[0].message.content

# =========================================================
# GENERATE BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

generate_button = st.button(
    "🚀 Generate Personalized Interview",
    type="primary",
    use_container_width=True
)

# =========================================================
# GENERATE RESULTS
# =========================================================

if generate_button:

    if not job_role.strip():
        st.warning("⚠️ Please enter the job or internship role.")
        st.stop()

    if not job_description.strip():
        st.warning("⚠️ Please enter the job description.")
        st.stop()

    if not intern_profile.strip():
        st.warning("⚠️ Please enter the intern profile or resume.")
        st.stop()

    st.markdown("""
    <div class="result-header">
        <h2>🤖 AI Interview Analysis</h2>
        <p>
        Analyzing the role, candidate profile and interview requirements...
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("🧠 AI is building your personalized interview..."):

        try:

            result = generate_questions()

            st.success("✅ Interview generated successfully!")

            # Metrics

            m1, m2, m3, m4 = st.columns(4)

            with m1:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-number">{technical_count}</div>
                        <div class="metric-label">Technical</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with m2:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-number">{behavioral_count}</div>
                        <div class="metric-label">Behavioral</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with m3:
                st.markdown(
                    """
                    <div class="metric-card">
                        <div class="metric-number">3</div>
                        <div class="metric-label">Candidate Specific</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with m4:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-number">{difficulty}</div>
                        <div class="metric-label">Difficulty</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                '<div class="section-title">🎯 Generated Interview</div>',
                unsafe_allow_html=True
            )

            st.markdown(result)

            st.divider()

            st.markdown(
                '<div class="section-title">📥 Export Interview</div>',
                unsafe_allow_html=True
            )

            st.download_button(
                label="📄 Download Interview Questions",
                data=result,
                file_name="AI_Interview_Questions.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as e:

            st.error(
                "❌ Something went wrong while generating the interview."
            )

            st.code(str(e))

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="custom-footer">
    Built with <span>AI</span> • Powered by <span>Groq</span> •
    Designed for smarter internship interviews
</div>
""", unsafe_allow_html=True)
