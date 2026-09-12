import streamlit as st

# =========================================================
# CAREER MAP AI
# =========================================================

st.set_page_config(
    page_title="Career Map AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 18px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
}

.career-card {
    background: linear-gradient(135deg, #eef2ff, #f5f3ff);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #c7d2fe;
    margin-bottom: 20px;
}

.roadmap {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border-left: 6px solid #667eea;
    margin-bottom: 15px;
}

.badge {
    display: inline-block;
    padding: 7px 12px;
    margin: 4px;
    border-radius: 20px;
    background: #eef2ff;
    color: #4338ca;
    font-weight: 600;
}

.small-text {
    color: #6b7280;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# CAREER DATABASE
# =========================================================

CAREERS = {

    "Artificial Intelligence": {
        "career": "AI / ML Engineer",
        "description": "Build intelligent systems using machine learning, deep learning and AI technologies.",
        "skills": [
            "Python",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "NumPy",
            "Pandas",
            "SQL",
            "TensorFlow / PyTorch"
        ],
        "projects": [
            "Student Performance Prediction",
            "Disease Prediction System",
            "AI Chatbot",
            "Image Classification System"
        ],
        "certifications": [
            "Introduction to Artificial Intelligence",
            "Machine Learning Fundamentals",
            "Deep Learning Fundamentals"
        ],
        "roadmap": [
            ("Step 1", "Programming Basics", "Learn Python and basic programming concepts."),
            ("Step 2", "Mathematics", "Learn statistics, probability and linear algebra basics."),
            ("Step 3", "Machine Learning", "Learn regression, classification, clustering and model evaluation."),
            ("Step 4", "Deep Learning", "Learn neural networks, CNNs and basic NLP."),
            ("Step 5", "Projects", "Build 2–4 practical AI/ML projects."),
            ("Step 6", "Internship", "Apply for AI/ML internships and gain practical experience."),
            ("Step 7", "Job Preparation", "Prepare for coding, ML and technical interviews.")
        ]
    },

    "Software Development": {
        "career": "Software Developer",
        "description": "Design, develop and maintain software applications.",
        "skills": [
            "C / C++ / Java / Python",
            "Data Structures",
            "Algorithms",
            "Object-Oriented Programming",
            "SQL",
            "Git & GitHub",
            "Problem Solving"
        ],
        "projects": [
            "Student Management System",
            "Bank Management System",
            "Library Management System",
            "Online Shopping System"
        ],
        "certifications": [
            "Programming Fundamentals",
            "Java Programming",
            "Data Structures"
        ],
        "roadmap": [
            ("Step 1", "Programming", "Become strong in one programming language."),
            ("Step 2", "OOP", "Learn classes, objects, inheritance and polymorphism."),
            ("Step 3", "DSA", "Practice arrays, strings, linked lists, stacks, queues and trees."),
            ("Step 4", "Database", "Learn SQL and database concepts."),
            ("Step 5", "Projects", "Build real-world software projects."),
            ("Step 6", "Internship", "Apply for software development internships."),
            ("Step 7", "Placement", "Practice coding tests and technical interviews.")
        ]
    },

    "Data Science": {
        "career": "Data Scientist / Data Analyst",
        "description": "Use data, statistics and machine learning to solve business problems.",
        "skills": [
            "Python",
            "Statistics",
            "SQL",
            "Pandas",
            "NumPy",
            "Data Visualization",
            "Machine Learning",
            "Excel"
        ],
        "projects": [
            "Sales Data Analysis",
            "Student Data Analysis",
            "Customer Churn Prediction",
            "House Price Prediction"
        ],
        "certifications": [
            "Python for Data Science",
            "SQL Fundamentals",
            "Data Analytics"
        ],
        "roadmap": [
            ("Step 1", "Python", "Learn Python programming."),
            ("Step 2", "Statistics", "Understand statistics and probability."),
            ("Step 3", "Data Analysis", "Learn Pandas, NumPy and data cleaning."),
            ("Step 4", "Visualization", "Create meaningful charts and dashboards."),
            ("Step 5", "Machine Learning", "Learn predictive models."),
            ("Step 6", "Projects", "Build data analysis and prediction projects."),
            ("Step 7", "Career", "Apply for data analyst and data science roles.")
        ]
    },

    "Web Development": {
        "career": "Web Developer",
        "description": "Create websites and web applications for users and businesses.",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python / Java",
            "SQL",
            "Git & GitHub"
        ],
        "projects": [
            "Portfolio Website",
            "College Website",
            "E-Commerce Website",
            "Online Food Ordering System"
        ],
        "certifications": [
            "Web Development Fundamentals",
            "JavaScript",
            "React"
        ],
        "roadmap": [
            ("Step 1", "HTML", "Learn webpage structure."),
            ("Step 2", "CSS", "Learn styling and responsive design."),
            ("Step 3", "JavaScript", "Learn programming for interactive websites."),
            ("Step 4", "Frontend", "Learn React or another frontend framework."),
            ("Step 5", "Backend", "Learn Python/Java and databases."),
            ("Step 6", "Projects", "Build complete web applications."),
            ("Step 7", "Career", "Apply for web development internships.")
        ]
    },

    "Cyber Security": {
        "career": "Cyber Security Analyst",
        "description": "Protect systems, networks and applications from cyber threats.",
        "skills": [
            "Networking",
            "Linux",
            "Python",
            "Cyber Security",
            "Ethical Hacking",
            "Cryptography",
            "Security Tools"
        ],
        "projects": [
            "Password Strength Checker",
            "Phishing Detection System",
            "Network Scanner",
            "Secure Login System"
        ],
        "certifications": [
            "Cyber Security Fundamentals",
            "Networking Basics",
            "Ethical Hacking Fundamentals"
        ],
        "roadmap": [
            ("Step 1", "Networking", "Learn TCP/IP, DNS, HTTP and networking basics."),
            ("Step 2", "Linux", "Learn Linux commands and system basics."),
            ("Step 3", "Security", "Understand common cyber attacks and defenses."),
            ("Step 4", "Ethical Hacking", "Learn security testing concepts."),
            ("Step 5", "Projects", "Build security-related projects."),
            ("Step 6", "Certification", "Complete a suitable beginner certification."),
            ("Step 7", "Career", "Apply for cyber security internships.")
        ]
    },

    "Cloud Computing": {
        "career": "Cloud Engineer",
        "description": "Design, deploy and manage applications and infrastructure in the cloud.",
        "skills": [
            "Linux",
            "Networking",
            "AWS / Azure",
            "Docker",
            "Cloud Security",
            "Python",
            "Git"
        ],
        "projects": [
            "Cloud Storage Application",
            "Website Deployment",
            "Cloud Monitoring System",
            "Serverless Application"
        ],
        "certifications": [
            "AWS Cloud Fundamentals",
            "Microsoft Azure Fundamentals",
            "Cloud Computing Basics"
        ],
        "roadmap": [
            ("Step 1", "Linux", "Learn Linux fundamentals."),
            ("Step 2", "Networking", "Understand cloud networking."),
            ("Step 3", "Cloud", "Learn AWS or Azure fundamentals."),
            ("Step 4", "Containers", "Learn Docker basics."),
            ("Step 5", "Projects", "Deploy applications to the cloud."),
            ("Step 6", "Certification", "Complete a beginner cloud certification."),
            ("Step 7", "Career", "Apply for cloud internships.")
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "result" not in st.session_state:
    st.session_state.result = None


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 Career Map AI")
st.sidebar.caption("Your personalized career guide")

st.sidebar.divider()

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "Home"

if st.sidebar.button("👤 Profile", use_container_width=True):
    st.session_state.page = "Profile"

if st.sidebar.button("🎯 Career Recommendation", use_container_width=True):
    st.session_state.page = "Recommendation"

if st.sidebar.button("🗺️ Career Roadmap", use_container_width=True):
    st.session_state.page = "Roadmap"

if st.sidebar.button("📚 Skills & Projects", use_container_width=True):
    st.session_state.page = "Skills"

if st.sidebar.button("🤖 AI Career Assistant", use_container_width=True):
    st.session_state.page = "Assistant"

st.sidebar.divider()

st.sidebar.info(
    "💡 Tip: Select your interests and skills to get a personalized career roadmap."
)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🎓 Career Map AI</h1>
        <p>
        Discover the right career path, learn the required skills,
        build projects and prepare for your dream job.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("🚀 Start Your Career Journey")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h2>🎯</h2>
        <h3>Find Your Career</h3>
        <p>Get career recommendations based on your interests and skills.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h2>🗺️</h2>
        <h3>Build Your Roadmap</h3>
        <p>Follow a step-by-step path from learning to internship and jobs.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h2>💼</h2>
        <h3>Prepare for Jobs</h3>
        <p>Discover skills, projects and certifications you should complete.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("🌟 Popular Career Paths")

    cols = st.columns(3)

    careers = list(CAREERS.keys())

    for i, career in enumerate(careers):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="card">
                <h3>💻 {career}</h3>
                <p>{CAREERS[career]["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    st.success(
        "👈 Use the Profile page to enter your details and start your career journey."
    )


# =========================================================
# PROFILE
# =========================================================

elif st.session_state.page == "Profile":

    st.title("👤 Student Profile")

    st.write("Tell us about yourself.")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        degree = st.selectbox(
            "Degree",
            [
                "B.Tech",
                "B.Sc",
                "BCA",
                "MCA",
                "MBA",
                "Other"
            ]
        )

        branch = st.selectbox(
            "Branch",
            [
                "AI & Machine Learning",
                "Computer Science",
                "Information Technology",
                "Data Science",
                "Electronics",
                "Mechanical",
                "Civil",
                "Other"
            ]
        )

    with col2:

        year = st.selectbox(
            "Current Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year",
                "Graduate"
            ]
        )

        interests = st.multiselect(
            "Your Interests",
            [
                "Artificial Intelligence",
                "Software Development",
                "Data Science",
                "Web Development",
                "Cyber Security",
                "Cloud Computing"
            ]
        )

        current_skills = st.multiselect(
            "Your Current Skills",
            [
                "Python",
                "C",
                "C++",
                "Java",
                "SQL",
                "Machine Learning",
                "Data Analysis",
                "Communication",
                "Problem Solving",
                "Git & GitHub"
            ]
        )

    if st.button("💾 Save Profile", type="primary"):

        st.session_state.profile = {
            "name": name,
            "degree": degree,
            "branch": branch,
            "year": year,
            "interests": interests,
            "skills": current_skills
        }

        st.success("Profile saved successfully! 🎉")


# =========================================================
# RECOMMENDATION
# =========================================================

elif st.session_state.page == "Recommendation":

    st.title("🎯 AI Career Recommendation")

    st.write(
        "Select an area you are interested in and Career Map AI "
        "will recommend a career path."
    )

    interest = st.selectbox(
        "What career area interests you?",
        list(CAREERS.keys())
    )

    selected_skills = st.multiselect(
        "Select your current skills",
        [
            "Python",
            "C",
            "C++",
            "Java",
            "SQL",
            "Machine Learning",
            "Data Analysis",
            "Communication",
            "Problem Solving",
            "Git & GitHub"
        ]
    )

    if st.button("🚀 Generate Recommendation", type="primary"):

        result = CAREERS[interest]

        st.session_state.result = result

        # Simple match score
        skill_count = len(selected_skills)

        score = min(
            95,
            50 + (skill_count * 7)
        )

        st.session_state.score = score

        st.success("Your personalized career recommendation is ready! 🎉")

        st.markdown(
            f"""
            <div class="career-card">
                <h2>🎯 {result["career"]}</h2>
                <p>{result["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Career Match", f"{score}%")

        with col2:
            st.metric("Skills Recommended", len(result["skills"]))

        with col3:
            st.metric("Project Ideas", len(result["projects"]))

        st.subheader("📚 Skills You Should Learn")

        for skill in result["skills"]:
            st.markdown(
                f'<span class="badge">✓ {skill}</span>',
                unsafe_allow_html=True
            )


# =========================================================
# ROADMAP
# =========================================================

elif st.session_state.page == "Roadmap":

    st.title("🗺️ Your Career Roadmap")

    if st.session_state.result is None:

        st.warning(
            "Please generate a career recommendation first."
        )

        st.info(
            "Go to 🎯 Career Recommendation from the sidebar."
        )

    else:

        result = st.session_state.result

        st.markdown(
            f"""
            <div class="career-card">
                <h2>🎯 {result["career"]}</h2>
                <p>{result["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        for step, title, description in result["roadmap"]:

            st.markdown(
                f"""
                <div class="roadmap">
                    <h3>🔵 {step}: {title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.success(
            "🎉 Follow the roadmap consistently and keep building practical experience."
        )


# =========================================================
# SKILLS & PROJECTS
# =========================================================

elif st.session_state.page == "Skills":

    st.title("📚 Skills & Projects")

    if st.session_state.result is None:

        st.warning(
            "Generate your career recommendation first."
        )

    else:

        result = st.session_state.result

        st.header("📚 Skills")

        for skill in result["skills"]:
            st.write("✅", skill)

        st.divider()

        st.header("💡 Recommended Projects")

        for project in result["projects"]:
            st.markdown(
                f"""
                <div class="card">
                <h3>💻 {project}</h3>
                <p>Build this project and add it to your portfolio.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.header("🏆 Recommended Certifications")

        for certification in result["certifications"]:
            st.write("🏅", certification)


# =========================================================
# AI ASSISTANT
# =========================================================

elif st.session_state.page == "Assistant":

    st.title("🤖 AI Career Assistant")

    st.write(
        "Ask a career-related question."
    )

    question = st.text_area(
        "Your Question",
        placeholder="Example: What skills should I learn for an AI/ML job?"
    )

    if st.button("🤖 Ask Career AI", type="primary"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            q = question.lower()

            st.subheader("💡 Career AI Response")

            if "python" in q:

                st.info("""
                Python is very useful for AI, Machine Learning,
                Data Science and Software Development.

                Start with:
                1. Variables
                2. Conditions
                3. Loops
                4. Functions
                5. Lists and dictionaries
                6. Object-Oriented Programming
                7. NumPy and Pandas
                """)

            elif "project" in q:

                st.info("""
                Start with a small project.

                Good beginner projects include:
                • Student Management System
                • Student Performance Prediction
                • Chatbot
                • Sales Data Analysis
                • Library Management System
                """)

            elif "interview" in q:

                st.info("""
                Prepare these areas:

                • Programming basics
                • Data Structures
                • SQL
                • OOP
                • Aptitude
                • Communication
                • Projects on your resume
                """)

            elif "resume" in q:

                st.info("""
                A good student resume should contain:

                • Career objective/summary
                • Education
                • Technical skills
                • Projects
                • Certifications
                • Achievements
                • Contact information

                Keep it simple and preferably one page.
                """)

            else:

                st.info("""
                🎯 My advice:

                Choose one career path, learn the required
                fundamentals, practice regularly, build projects,
                complete certifications and apply for internships.

                Consistency is more important than trying to learn
                everything at once.
                """)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 Career Map AI | Learn • Build • Practice • Get Hired 🚀"
)
