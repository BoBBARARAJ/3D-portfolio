
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Rajkeerth Bobbara | AI Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# COLORS AND STYLING
# =========================================================
BG = "#080817"
PURPLE = "#9B5CFF"
CYAN = "#00E5FF"
PINK = "#FF4FD8"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(ellipse at 5% 10%, #24104b 0%, transparent 35%),
            radial-gradient(ellipse at 95% 35%, #071e40 0%, transparent 35%),
            {BG};
        color: #F5F3FF;
    }}

    #MainMenu, footer, header {{
        visibility: hidden;
    }}

    .block-container {{
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }}

    .topbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 14px 4px 22px;
        border-bottom: 1px solid #282653;
        margin-bottom: 25px;
    }}

    .brand {{
        font-size: 21px;
        font-weight: 800;
        color: #FFFFFF;
    }}

    .brand span {{
        color: {CYAN};
    }}

    .eyebrow {{
        color: {CYAN};
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}

    .hero-title {{
        font-size: clamp(38px, 5vw, 66px);
        line-height: 1.08;
        font-weight: 800;
        letter-spacing: -2px;
        color: #FFFFFF;
        margin: 15px 0;
    }}

    .gradient-text {{
        background: linear-gradient(90deg, {PURPLE}, {PINK}, {CYAN});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .subtext {{
        color: #C6C4E5;
        font-size: 16px;
        line-height: 1.8;
    }}

    .glass-card {{
        background: linear-gradient(140deg,
            rgba(33, 25, 72, 0.86),
            rgba(8, 13, 37, 0.88));
        border: 1px solid #39306E;
        border-radius: 18px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 0 24px rgba(104, 62, 255, 0.07);
        transition: transform 0.25s, border-color 0.25s;
    }}

    .glass-card:hover {{
        border-color: {CYAN};
        transform: translateY(-4px);
    }}

    .project-icon {{
        font-size: 29px;
        margin-bottom: 12px;
    }}

    .project-title {{
        color: #FFFFFF;
        font-size: 21px;
        font-weight: 800;
        margin-bottom: 12px;
    }}

    .project-description {{
        color: #C5C3E3;
        font-size: 14px;
        line-height: 1.8;
        min-height: 75px;
    }}

    .tech {{
        display: inline-block;
        padding: 6px 10px;
        margin: 4px 3px 4px 0;
        color: #BFEFFF;
        background: rgba(0, 229, 255, 0.07);
        border: 1px solid rgba(0, 229, 255, 0.35);
        border-radius: 20px;
        font-size: 11px;
    }}

    .section-title {{
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 4px;
        margin-bottom: 8px;
    }}

    .stat {{
        background: rgba(17, 18, 48, 0.75);
        border: 1px solid #302C62;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
    }}

    .stat-number {{
        font-size: 23px;
        font-weight: 800;
        color: {CYAN};
    }}

    .stat-label {{
        color: #C2C0E2;
        font-size: 12px;
        margin-top: 5px;
    }}

    .skill-pill {{
        display: inline-block;
        margin: 5px;
        padding: 10px 15px;
        border-radius: 25px;
        border: 1px solid #494080;
        background: rgba(30, 23, 68, 0.7);
        color: #EAE7FF;
        font-size: 13px;
    }}

    .contact-card {{
        padding: 30px;
        border-radius: 20px;
        border: 1px solid {PURPLE};
        background: linear-gradient(110deg,
            rgba(93, 35, 180, 0.45),
            rgba(0, 160, 220, 0.13));
    }}

    a {{
        color: {CYAN} !important;
        text-decoration: none !important;
    }}

    .footer {{
        text-align: center;
        padding: 25px 0 10px;
        color: #8D8BAE;
        font-size: 12px;
    }}

    div[data-testid="stButton"] button {{
        border-radius: 25px;
        border: 1px solid {PURPLE};
        color: white;
        background: linear-gradient(90deg, #743BFF, #087FE8);
        font-weight: 700;
        padding: 10px 20px;
    }}

    div[data-testid="stButton"] button:hover {{
        border-color: {CYAN};
        color: white;
    }}

    div[data-testid="stPlotlyChart"] {{
        border-radius: 20px;
    }}

    @media (max-width: 700px) {{
        .hero-title {{
            letter-spacing: -1px;
        }}
        .topbar {{
            flex-direction: column;
            gap: 10px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# INTERACTIVE 3D ARTWORK
# =========================================================
@st.cache_data
def create_3d_figure():
    rng = np.random.default_rng(42)

    # Particle sphere
    count = 1800
    z = rng.uniform(-1, 1, count)
    theta = rng.uniform(0, 2 * np.pi, count)
    radius = np.sqrt(1 - z**2)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    colors = np.arctan2(y, x) + z * 2
    colors = (colors - colors.min()) / (
        colors.max() - colors.min()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode="markers",
            marker=dict(
                size=2.5,
                color=colors,
                colorscale=[
                    [0, "#6D38FF"],
                    [0.45, "#00DFFF"],
                    [0.75, "#FF4FD8"],
                    [1, "#FFFFFF"],
                ],
                opacity=0.9,
            ),
            hoverinfo="skip",
            showlegend=False,
        )
    )

    # Glowing orbital rings
    t = np.linspace(0, 2 * np.pi, 300)

    for tilt, color, width in [
        (0.0, "#00E5FF", 5),
        (0.8, "#FF4FD8", 4),
        (-0.8, "#8655FF", 4),
    ]:
        ox = 1.55 * np.cos(t)
        oy = 1.55 * np.sin(t) * np.cos(tilt)
        oz = 1.55 * np.sin(t) * np.sin(tilt)

        fig.add_trace(
            go.Scatter3d(
                x=ox,
                y=oy,
                z=oz,
                mode="lines",
                line=dict(color=color, width=width),
                hoverinfo="skip",
                showlegend=False,
            )
        )

    # Small orbiting planets
    px = [1.65, -1.5, 0.1, -0.6, 1.2]
    py = [0.2, -0.5, 1.7, 1.2, -1.0]
    pz = [0.8, 0.7, -0.3, -1.2, 0.3]

    fig.add_trace(
        go.Scatter3d(
            x=px,
            y=py,
            z=pz,
            mode="markers",
            marker=dict(
                size=[9, 7, 8, 6, 7],
                color=[
                    "#00E5FF",
                    "#FF4FD8",
                    "#9B5CFF",
                    "#FFD166",
                    "#00E5FF",
                ],
                opacity=1,
                line=dict(color="#FFFFFF", width=1),
            ),
            hoverinfo="skip",
            showlegend=False,
        )
    )

    fig.update_layout(
        height=410,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        scene=dict(
            bgcolor="rgba(0,0,0,0)",
            xaxis=dict(visible=False, range=[-2.1, 2.1]),
            yaxis=dict(visible=False, range=[-2.1, 2.1]),
            zaxis=dict(visible=False, range=[-2.1, 2.1]),
            aspectmode="cube",
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.15)),
        ),
    )

    return fig


# =========================================================
# NAVIGATION
# =========================================================
st.markdown(
    """
    <div class="topbar">
        <div class="brand"><span>✳</span> RAJKEERTH BOBBARA</div>
        <div style="color:#C8B9FF;font-size:12px;">
            ABOUT &nbsp;&nbsp; PROJECTS &nbsp;&nbsp;
            SKILLS &nbsp;&nbsp; CONTACT
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HERO SECTION
# =========================================================
left, right = st.columns([1.08, 0.92], gap="large")

with left:
    st.markdown(
        """
        <div class="glass-card">
            <div class="eyebrow">AI DEVELOPER · CREATIVE TECHNOLOGIST</div>
            <div class="hero-title">
                Turning ideas<br>
                into <span class="gradient-text">reality.</span>
            </div>
            <div class="subtext">
                Hey, I'm <b>Rajkeerth Bobbara</b>. I build intelligent
                AI experiences, automation tools, and data-driven
                applications that make technology useful.
            </div>
            <br>
            <span class="tech">DATA SCIENCE</span>
            <span class="tech">GENERATIVE AI</span>
            <span class="tech">AGENTIC AI</span>
            <span class="tech">PYTHON</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button("Explore My Projects ↓", use_container_width=True):
        st.session_state["show_projects"] = True
        st.toast("Explore the projects section below!")

with right:
    st.plotly_chart(
        create_3d_figure(),
        use_container_width=True,
        config={
            "displayModeBar": False,
            "scrollZoom": False,
        },
    )
    st.markdown(
        """
        <div style="text-align:center;color:#A9A5D5;font-size:12px;">
            ✦ Interactive 3D artwork — drag to rotate
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# QUICK INTRODUCTION
# =========================================================
st.write("")

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(
        """
        <div class="stat">
            <div class="stat-number">AI + Data</div>
            <div class="stat-label">MY FOCUS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s2:
    st.markdown(
        """
        <div class="stat">
            <div class="stat-number">Automation</div>
            <div class="stat-label">MY INTEREST</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s3:
    st.markdown(
        """
        <div class="stat">
            <div class="stat-number">Always Learning</div>
            <div class="stat-label">MY APPROACH</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# ABOUT SECTION
# =========================================================
st.write("")
st.write("")

st.markdown(
    """
    <div class="eyebrow">01 / ABOUT ME</div>
    <div class="section-title">
        Building at the intersection of
        <span class="gradient-text">AI & imagination.</span>
    </div>
    <div class="subtext">
        I am developing skills in Data Science, Machine Learning,
        Generative AI, and Agentic AI. My goal is to turn these
        skills into practical applications and useful automation tools.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

about1, about2 = st.columns(2, gap="large")

with about1:
    st.markdown(
        """
        <div class="glass-card">
            <div class="eyebrow">MY APPROACH</div>
            <h3 style="color:white;">More than code.<br>A better experience.</h3>
            <div class="subtext" style="font-size:14px;">
                I enjoy learning how AI models, data, and software
                can work together to solve real-world problems.
                I focus on clean interfaces, practical workflows,
                and continuous improvement.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with about2:
    st.markdown(
        """
        <div class="glass-card">
            <div class="eyebrow">WHAT I WANT TO BUILD</div>
            <h3 style="color:white;">Intelligent solutions</h3>
            <div class="subtext" style="font-size:14px;">
                ✦ AI-powered applications<br>
                ✦ Workflow automation<br>
                ✦ Document question-answering systems<br>
                ✦ Data-driven applications<br>
                ✦ Interactive portfolio experiences
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# PROJECTS SECTION
# =========================================================
st.write("")
st.write("")

st.markdown(
    """
    <div class="eyebrow">02 / SELECTED WORK</div>
    <div class="section-title">
        Projects made <span class="gradient-text">useful.</span>
    </div>
    <div class="subtext">
        Explore my AI, automation, and data project portfolio.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

projects = [
    {
        "icon": "🎯",
        "category": "AI · CAREER TOOLS",
        "title": "AI ATS Job Hunter",
        "description": (
            "A resume analysis and job-search assistant designed "
            "to help candidates review their resumes and explore "
            "relevant job opportunities."
        ),
        "tech": [
            "Python",
            "Streamlit",
            "Scikit-learn",
        ],
        "github": "https://github.com/",
    },
    {
        "icon": "🏥",
        "category": "GENERATIVE AI · AUTOMATION",
        "title": "AI Hospital Receptionist",
        "description": (
            "An AI receptionist concept for answering common "
            "hospital questions and helping users find information "
            "through a conversational interface."
        ),
        "tech": [
            "Python",
            "FastAPI",
            "Streamlit",
            "Gemini API",
            "SQLite",
        ],
        "github": "https://github.com/",
    },
    {
        "icon": "🧠",
        "category": "GENERATIVE AI · RAG",
        "title": "RAG Systems",
        "description": (
            "Retrieval-Augmented Generation applications that "
            "retrieve relevant information from documents or a "
            "knowledge base to support context-aware AI answers."
        ),
        "tech": [
            "Python",
            "LLMs",
            "Embeddings",
            "FAISS",
            "Pinecone",
        ],
        "github": "https://github.com/",
    },
]

project_columns = st.columns(3, gap="medium")

for column, project in zip(project_columns, projects):
    with column:
        tech_html = "".join(
            f'<span class="tech">{tech}</span>'
            for tech in project["tech"]
        )

        st.markdown(
            f"""
            <div class="glass-card">
                <div class="project-icon">{project["icon"]}</div>
                <div class="eyebrow">{project["category"]}</div>
                <div class="project-title">{project["title"]}</div>
                <div class="project-description">
                    {project["description"]}
                </div>
                <div style="margin-top:14px;">
                    {tech_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        st.link_button(
            "GitHub ↗",
            project["github"],
            use_container_width=True,
        )

st.caption(
    "Note: The GitHub buttons currently use generic GitHub links. "
    "Replace them with the actual repository URLs for your projects."
)

# =========================================================
# SKILLS SECTION
# =========================================================
st.write("")
st.write("")

st.markdown(
    """
    <div class="eyebrow">03 / MY TOOLKIT</div>
    <div class="section-title">
        Tools for making <span class="gradient-text">things happen.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

skill_groups = {
    "Programming": ["Python", "SQL"],
    "Data Science": [
        "Statistics",
        "Pandas",
        "NumPy",
        "Data Preprocessing",
        "Feature Engineering",
        "Scikit-learn",
    ],
    "Machine Learning & Deep Learning": [
        "Machine Learning",
        "Neural Networks",
        "ANN",
        "CNN",
    ],
    "Generative AI": [
        "LLMs",
        "RAG",
        "Embeddings",
        "LangChain",
        "LangGraph",
        "FAISS",
        "Pinecone",
    ],
    "Development & Deployment": [
        "Streamlit",
        "FastAPI",
        "REST APIs",
        "Docker",
        "SQLite",
        "Microsoft Azure",
        "Plotly",
    ],
}

for group_name, skills in skill_groups.items():
    st.markdown(
        f"<h4 style='color:#C9C1FF;margin-top:18px;'>{group_name}</h4>",
        unsafe_allow_html=True,
    )

    skill_html = "".join(
        f'<span class="skill-pill">{skill}</span>'
        for skill in skills
    )

    st.markdown(skill_html, unsafe_allow_html=True)

# =========================================================
# CONTACT SECTION
# =========================================================
st.write("")
st.write("")

st.markdown(
    """
    <div class="contact-card">
        <div class="eyebrow">04 / LET'S CONNECT</div>
        <h2 style="color:white;font-size:32px;">
            Let's build something
            <span class="gradient-text">amazing.</span>
        </h2>
        <div class="subtext">
            Interested in AI applications, automation, or data-driven
            projects? Let's connect and explore ideas.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

contact1, contact2 = st.columns(2)

with contact1:
    st.link_button(
        "Explore GitHub ↗",
        "https://github.com/",
        use_container_width=True,
    )

with contact2:
    st.link_button(
        "Explore LinkedIn ↗",
        "https://www.linkedin.com/",
        use_container_width=True,
    )

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        <b style="color:#EAE7FF;">RAJKEERTH BOBBARA</b><br><br>
        Built with Python · Streamlit · Plotly<br>
        Designed with curiosity ✦
    </div>
    """,
    unsafe_allow_html=True,
)
