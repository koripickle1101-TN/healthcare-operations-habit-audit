import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Operations Habit Audit | Student Portfolio",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM_GRAY = "#F7F3EE"
LINE_GRAY = "#E8DED2"
DARK_GRAY = "#2A2623"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: {BLACK};
        background: {WHITE};
    }}

    .stApp {{
        background-color: {WHITE};
        color: {BLACK};
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3 {{
        font-family: 'Newsreader', Georgia, serif;
        color: {BLACK};
    }}

    h1 {{
        line-height: .95;
        letter-spacing: -.035em;
    }}

    h2 {{
        letter-spacing: -.02em;
    }}

    .hero {{
        border: 1px solid {LINE_GRAY};
        border-radius: 30px;
        padding: 46px 48px;
        margin-bottom: 24px;
        background: linear-gradient(135deg, #FFFFFF 0%, #FFFFFF 66%, #FFF4EA 100%);
        box-shadow: 0 14px 40px rgba(0,0,0,.04);
    }}

    .eyebrow {{
        color: {BLACK};
        display: inline-block;
        border-bottom: 3px solid {TENNESSEE_ORANGE};
        padding-bottom: 4px;
        font-weight: 700;
        letter-spacing: .13em;
        text-transform: uppercase;
        font-size: .78rem;
        margin-bottom: 14px;
    }}

    .hero h1 {{
        font-size: clamp(3rem, 6vw, 5.7rem);
        max-width: 900px;
        margin: 0 0 18px 0;
    }}

    .hero p {{
        max-width: 860px;
        font-size: 1.03rem;
        line-height: 1.72;
        color: {DARK_GRAY};
    }}

    .integrity-box, .perspective-box {{
        border-left: 5px solid {TENNESSEE_ORANGE};
        background: {WARM_GRAY};
        border-radius: 0 20px 20px 0;
        padding: 22px 26px;
        margin: 18px 0 28px 0;
        line-height: 1.7;
    }}

    .metric-card {{
        border: 1px solid {LINE_GRAY};
        border-radius: 22px;
        padding: 22px;
        min-height: 138px;
        background: {WHITE};
        margin-bottom: 14px;
    }}

    .metric-label {{
        color: {BLACK};
        border-left: 3px solid {TENNESSEE_ORANGE};
        padding-left: 8px;
        font-weight: 700;
        font-size: .76rem;
        text-transform: uppercase;
        letter-spacing: .09em;
    }}

    .metric-value {{
        color: {BLACK};
        font-family: 'Newsreader', Georgia, serif;
        font-size: 2.05rem;
        font-weight: 600;
        margin-top: 10px;
        line-height: 1.08;
    }}

    .risk-box {{
        border-left: 5px solid {TENNESSEE_ORANGE};
        background: {WARM_GRAY};
        border-radius: 0 20px 20px 0;
        padding: 20px 24px;
        margin: 12px 0 20px 0;
        line-height: 1.65;
    }}

    .footer-note {{
        margin-top: 42px;
        padding-top: 24px;
        border-top: 1px solid {LINE_GRAY};
        font-size: .92rem;
        line-height: 1.65;
        color: {DARK_GRAY};
    }}

    div[data-testid="stSlider"] [role="slider"] {{
        background-color: {TENNESSEE_ORANGE} !important;
        border-color: {TENNESSEE_ORANGE} !important;
    }}

    div[data-testid="stSliderThumbValue"] {{
        color: {BLACK} !important;
        font-weight: 700;
    }}

    .footer-note a {{
        color: {BLACK};
        font-weight: 700;
        text-decoration: none;
        border-bottom: 2px solid {TENNESSEE_ORANGE};
    }}

    .metric-value {{
        overflow-wrap: normal;
        word-break: normal;
        hyphens: none;
    }}
    .result-card {{
        border: 1px solid {LINE_GRAY};
        border-left: 4px solid {TENNESSEE_ORANGE};
        border-radius: 0 16px 16px 0;
        padding: 18px 20px;
        margin: 12px 0;
        background: {WHITE};
        overflow-wrap: break-word;
    }}
    .result-card h3 {{ margin: 0 0 10px; font-size: 1.35rem; line-height: 1.25; }}
    .result-card p {{ margin: 8px 0; line-height: 1.6; }}
    @media (max-width: 768px) {{
        .block-container {{ padding: 1rem 1rem 2rem; }}
        .hero {{ padding: 24px 20px; border-radius: 18px; }}
        .hero h1 {{ font-size: 2.15rem; line-height: 1.1; }}
        .hero p, .integrity-box, .perspective-box, .risk-box, .result-card {{ font-size: 1rem; line-height: 1.6; }}
        .metric-card {{ padding: 18px; min-height: 0; }}
        .metric-label {{ font-size: .82rem; letter-spacing: .035em; }}
        .metric-value {{ font-size: 1.65rem; line-height: 1.2; overflow-wrap: normal; }}
        .eyebrow {{ font-size: .72rem; letter-spacing: .055em; }}
        div[data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; }}
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
            flex: 1 1 100% !important;
            width: 100% !important;
            min-width: 0 !important;
        }}
        div[data-testid="stSlider"] {{ padding-bottom: .5rem; }}
        div[data-testid="stSlider"] [role="slider"] {{ min-width: 22px; min-height: 22px; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
        *, *::before, *::after {{ scroll-behavior: auto !important; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

categories = {
    "Documentation Accuracy": {
        "default": 3,
        "finding": "When documentation is incomplete or unclear, the next person in the workflow may have to stop, investigate, or ask for information again.",
        "action": "Practice using a pre-service documentation checklist that confirms the information needed for the next workflow step."
    },
    "Data Integrity": {
        "default": 2,
        "finding": "Inconsistent demographic, insurance, or workflow information may create eligibility rework, authorization mismatches, claim corrections, or patient confusion.",
        "action": "Practice a structured review of demographic and insurance information before the workflow moves forward."
    },
    "Patient-Centered Workflow": {
        "default": 3,
        "finding": "When patients are not sure what is needed or what happens next, an administrative gap can become repeated calls, missed preparation, delay, or frustration.",
        "action": "Draft a plain-language patient next-step script for referral, authorization, documentation, and visit preparation."
    },
    "Compliance Readiness": {
        "default": 2,
        "finding": "If referral, authorization, documentation, or payer requirements are not reviewed early, the workflow may carry unresolved risk into later steps.",
        "action": "Practice using a requirements-review checkpoint before service. This is an educational workflow exercise, not a formal compliance assessment."
    },
    "Cross-Functional Communication": {
        "default": 2,
        "finding": "When status, ownership, next steps, or unresolved issues are not carried across handoffs, the next team may inherit a problem without enough context to resolve it efficiently.",
        "action": "Practice a handoff structure that records status, owner, next action, and unresolved risk."
    },
    "Continuous Improvement": {
        "default": 3,
        "finding": "When recurring workflow problems are corrected one case at a time but never reviewed as a pattern, the same friction may continue for patients and staff.",
        "action": "Use a simple weekly issue log to record repeated problems, likely causes, and follow-up actions."
    },
}

risk_mapping = {
    1: "Critical modeled weakness",
    2: "High modeled workflow risk",
    3: "Moderate / inconsistent practice",
    4: "Mostly reliable modeled practice",
    5: "Strong modeled practice",
}

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Healthcare Operations Intelligence Engine™ · Student Portfolio</div>
        <h1>Healthcare Operations Habit Audit™</h1>
        <p>
            I built this simulated audit to study a question that sits across my other portfolio projects:
            what repeated day-to-day habits can make a healthcare workflow more reliable—or make the same problems keep coming back?
        </p>
        <p>
            As I work toward my Bachelor's of Science degree in Healthcare Administration, I use this app to practice reviewing
            documentation, data integrity, patient communication, requirement readiness, handoffs, and continuous improvement without
            presenting student work as professional healthcare employment or a validated audit tool.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="integrity-box">
        <strong>Student-developed, simulated, educational, no-PHI healthcare operations portfolio project.</strong><br>
        This app uses no real patient, payer, employer, claim, EHR, or healthcare organization data. The scoring model is an educational
        structure I created for practice. It is not a validated healthcare benchmark, formal compliance assessment, accreditation review,
        legal determination, or prediction of real-world performance.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("## Why I Built This")
st.write(
    "The other projects in my portfolio follow specific workflow problems. This one steps back and asks whether repeated habits in documentation, data quality, communication, patient preparation, requirement review, and follow-through could be creating the conditions for those problems to recur."
)

st.markdown(
    """
    <div class="perspective-box">
        <strong>Patient-to-professional perspective:</strong> Patients usually experience the result of an operational habit, not the internal process name. What looks like a documentation, handoff, or data-integrity problem inside the workflow may feel like another call, another request for information, a delayed authorization, a confusing bill, or uncertainty about what happens next.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("## Score the Six Simulated Workflow Habits")
st.caption(
    "Choose a score from 1 to 5 for each category. These scores are educational inputs, not measurements of a real healthcare organization."
)

scores = {}
cols = st.columns(2)
for index, (category, info) in enumerate(categories.items()):
    with cols[index % 2]:
        scores[category] = st.slider(
            category,
            min_value=1,
            max_value=5,
            value=info["default"],
            help="1 = Critical modeled weakness, 2 = High modeled risk, 3 = Moderate/inconsistent, 4 = Mostly reliable, 5 = Strong modeled practice",
        )

score_values = list(scores.values())
average_score = round(sum(score_values) / len(score_values), 2)
workflow_practice_score = round(average_score * 20, 1)
denial_prevention_practice = round(
    (
        scores["Documentation Accuracy"]
        + scores["Data Integrity"]
        + scores["Compliance Readiness"]
        + scores["Cross-Functional Communication"]
    ) / 4,
    2,
)
patient_centered_indicator = round(
    (scores["Patient-Centered Workflow"] + scores["Cross-Functional Communication"]) / 2,
    2,
)
lowest_score = min(score_values)
lowest_categories = [category for category, score in scores.items() if score == lowest_score]
improvement_priority = ", ".join(lowest_categories)

if average_score < 2:
    overall_interpretation = "Critical modeled workflow concern"
elif average_score < 3:
    overall_interpretation = "High modeled workflow concern"
elif average_score < 4:
    overall_interpretation = "Moderate / inconsistent modeled practice"
elif average_score < 5:
    overall_interpretation = "Mostly reliable modeled practice"
else:
    overall_interpretation = "Strong modeled practice"

st.markdown("## Student-Designed Scoring View")
st.caption(
    "I use these indicators to practice organizing qualitative observations into a consistent review. They are not validated healthcare performance measures."
)

metric_cols = st.columns(3)
metric_data = [
    ("Average Habit Score", f"{average_score} / 5"),
    ("Modeled Workflow Practice Score", f"{workflow_practice_score} / 100"),
    ("Overall Interpretation", overall_interpretation),
    ("Denial-Prevention Practice Indicator", f"{denial_prevention_practice} / 5"),
    ("Patient-Centered Workflow Indicator", f"{patient_centered_indicator} / 5"),
    ("Lowest-Scoring Review Area", improvement_priority),
]

for i, (label, value) in enumerate(metric_data):
    with metric_cols[i % 3]:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("## Audit Results")
results_df = pd.DataFrame(
    [
        {
            "Category": category,
            "Score": score,
            "Educational Interpretation": risk_mapping[score],
            "Why I Would Review It": categories[category]["finding"],
            "Practice Action": categories[category]["action"],
        }
        for category, score in scores.items()
    ]
)
# Responsive, fully readable results; display only, scoring and source data unchanged.
for _, result in results_df.iterrows():
    st.markdown(
        f"""
        <div class="result-card">
            <h3>{result['Category']}</h3>
            <p><strong>Score:</strong> {result['Score']} / 5</p>
            <p><strong>Educational interpretation:</strong> {result['Educational Interpretation']}</p>
            <p><strong>Why I would review it:</strong> {result['Why I Would Review It']}</p>
            <p><strong>Practice action:</strong> {result['Practice Action']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("## Where I Would Look First")
st.write(
    "The lowest-scoring category is not automatically the root cause of a real workflow problem. In this learning model, it simply tells me where I would start asking more questions and looking for evidence."
)

for category in lowest_categories:
    st.markdown(
        f"""
        <div class="risk-box">
            <h3>{category}</h3>
            <p><strong>Why I would review it:</strong> {categories[category]['finding']}</p>
            <p><strong>Practice action:</strong> {categories[category]['action']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("## 30-Day Improvement Exercise")
st.caption("This is a simulated learning plan, not an implementation plan for a real healthcare organization.")

plan_df = pd.DataFrame(
    [
        {"Timeline": "Week 1", "Practice Action": "Review the three lowest-scoring areas", "Purpose": "Focus the investigation before trying to change everything at once"},
        {"Timeline": "Week 1", "Practice Action": "Build a front-end checklist", "Purpose": "Practice standardizing documentation and verification"},
        {"Timeline": "Week 2", "Practice Action": "Map workflow handoffs", "Purpose": "Look for unclear status, ownership, and next steps"},
        {"Timeline": "Week 2", "Practice Action": "Draft a patient next-step script", "Purpose": "Practice clearer patient-facing communication"},
        {"Timeline": "Week 3", "Practice Action": "Track repeated workflow issues", "Purpose": "Look for patterns instead of isolated corrections"},
        {"Timeline": "Week 4", "Practice Action": "Review the scores and notes again", "Purpose": "Practice continuous-improvement thinking"},
    ]
)
# Full-width cards avoid truncated plan details on narrow screens.
for _, step in plan_df.iterrows():
    st.markdown(
        f"""
        <div class="result-card">
            <h3>{step['Timeline']}</h3>
            <p><strong>Practice action:</strong> {step['Practice Action']}</p>
            <p><strong>Purpose:</strong> {step['Purpose']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("## What I Am Practicing Through This App")
st.write(
    "I use this project to practice recognizing workflow patterns, organizing qualitative observations, building a simple scoring model, connecting operational findings to patient and staff impact, and communicating improvement ideas without overstating what simulated data can prove."
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    .kp-habit-brand-footer {text-align:center;background:#FFFFFF;color:#000000;padding:32px 12px;border-top:1px solid #000000;margin-top:3rem}
    .kp-habit-brand-footer .kp-credit {font:600 .82rem Inter,Arial,sans-serif;letter-spacing:.08em}
    .kp-habit-brand-footer .kp-signature {font:400 clamp(2.7rem,5vw,3.8rem) 'Great Vibes','Brush Script MT',cursive;color:#000000;display:block;transform:rotate(-3deg);line-height:1.4;margin:.5rem 0}
    .kp-habit-brand-footer .kp-links {display:flex;gap:20px;justify-content:center;align-items:center;margin-top:12px}
    .kp-habit-brand-footer a {color:#000000;font:600 .8rem Inter,Arial,sans-serif;text-decoration:none;display:inline-flex;align-items:center;gap:7px}
    .kp-habit-brand-footer svg {width:17px;height:17px;fill:currentColor}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("## How It Fits in My Portfolio")
st.write(
    "EVIS follows eligibility and intake risk. PARCS follows prior authorization workflow risk. DPIS works backward from denial and claim-readiness risk. SBI looks for the first cross-workflow control loss. The Habit Audit sits across all of them and asks whether repeated operational habits could be making those risks more likely."
)

st.markdown(
    """
    <div class="footer-note">
        <div class="kp-habit-brand-footer" aria-label="Created by Kori Pickle">
            <div class="kp-credit">Created by Kori Pickle</div>
            <span class="kp-signature">Kori Pickle</span>
            <div class="kp-links">
                <a href="https://www.linkedin.com/in/kori-pickle" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn profile"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 2H3.6C2.7 2 2 2.7 2 3.6v16.8c0 .9.7 1.6 1.6 1.6h16.8c.9 0 1.6-.7 1.6-1.6V3.6c0-.9-.7-1.6-1.6-1.6ZM8 18.5H5.5V9H8Zm-1.25-10.7a1.45 1.45 0 1 1 0-2.9 1.45 1.45 0 0 1 0 2.9ZM18.5 18.5H16v-4.7c0-1.1 0-2.45-1.5-2.45s-1.8 1.2-1.8 2.4v4.75h-2.5V9h2.4v1.3h.05A2.64 2.64 0 0 1 15.05 9c2.5 0 3.45 1.6 3.45 3.8Z"/></svg>LinkedIn</a>
                <a href="https://github.com/koripickle1101-TN" target="_blank" rel="noopener noreferrer" aria-label="GitHub profile"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.77.6-3.35-1.18-3.35-1.18-.45-1.14-1.1-1.44-1.1-1.44-.9-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.89 1.52 2.34 1.08 2.91.82.09-.64.35-1.08.64-1.33-2.21-.25-4.54-1.11-4.54-4.94 0-1.09.39-1.99 1.03-2.69-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.03A9.58 9.58 0 0 1 12 6.47c.85 0 1.7.12 2.5.34 1.9-1.3 2.74-1.03 2.74-1.03.55 1.38.2 2.4.1 2.65.64.7 1.03 1.6 1.03 2.69 0 3.84-2.34 4.68-4.57 4.93.36.31.68.91.68 1.84v2.72c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>GitHub</a>
            </div>
        </div>
        <strong>Created by Kori Pickle</strong><br>
        Student-developed, simulated, educational, no-PHI healthcare operations portfolio project. Synthetic data only · Not employer experience · Not a formal compliance, clinical, coding, payer, legal, or accreditation assessment.<br><br>
        <a href="https://healthcare-operations-portfolio-hub.vercel.app/" target="_blank" rel="noopener noreferrer">Portfolio Hub</a> ·
        <a href="https://www.linkedin.com/in/kori-pickle" target="_blank" rel="noopener noreferrer">LinkedIn</a> ·
        <a href="https://github.com/koripickle1101-TN" target="_blank" rel="noopener noreferrer">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)
