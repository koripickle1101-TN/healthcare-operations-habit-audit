import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Operations Habit Audit | Simulated | No PHI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {WHITE};
        color: {BLACK};
    }}
    h1, h2, h3, h4, h5, h6, p, div, span, label {{
        color: {BLACK};
    }}
    h1 {{
        line-height: 1.05;
        letter-spacing: -0.04em;
    }}
    h2 {{
        letter-spacing: -0.03em;
    }}
    .brand-banner {{
        border: 2px solid {TENNESSEE_ORANGE};
        padding: 26px;
        border-radius: 0px;
        margin-bottom: 24px;
        background-color: {WHITE};
    }}
    .brand-label {{
        color: {TENNESSEE_ORANGE};
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        font-size: 0.84rem;
        margin-bottom: 14px;
    }}
    .disclaimer-box {{
        border: 1.5px solid {TENNESSEE_ORANGE};
        border-left: 8px solid {TENNESSEE_ORANGE};
        padding: 18px;
        background-color: {WHITE};
        margin: 20px 0 34px 0;
        font-size: 1rem;
        line-height: 1.55;
    }}
    .metric-card {{
        border: 1.5px solid {TENNESSEE_ORANGE};
        padding: 18px;
        background-color: {WHITE};
        min-height: 126px;
        margin-bottom: 14px;
    }}
    .metric-label {{
        color: {TENNESSEE_ORANGE};
        font-weight: 800;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }}
    .metric-value {{
        color: {BLACK};
        font-size: 1.85rem;
        font-weight: 850;
        margin-top: 8px;
        line-height: 1.15;
    }}
    .risk-box {{
        border-left: 8px solid {TENNESSEE_ORANGE};
        padding: 18px 18px 18px 24px;
        background-color: {WHITE};
        margin-top: 12px;
        margin-bottom: 24px;
    }}
    .small-note {{
        font-size: 0.9rem;
        line-height: 1.5;
    }}
    div[data-testid="stSlider"] > div > div > div > div {{
        background-color: {TENNESSEE_ORANGE} !important;
    }}
    div[data-testid="stSlider"] [role="slider"] {{
        background-color: {TENNESSEE_ORANGE} !important;
        border-color: {TENNESSEE_ORANGE} !important;
    }}
    @media (max-width: 768px) {{
        .brand-banner {{ padding: 16px; }}
        .metric-value {{ font-size: 1.4rem; }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

categories = {
    "Documentation Accuracy": {
        "default": 3,
        "finding": "Documentation gaps can weaken authorization readiness, medical necessity support, claim readiness, and denial prevention.",
        "action": "Create a pre-service documentation readiness checklist before authorization submission or scheduled service."
    },
    "Data Integrity": {
        "default": 2,
        "finding": "Weak data integrity can create eligibility errors, claim corrections, authorization mismatches, and patient billing confusion.",
        "action": "Standardize insurance verification and demographic accuracy checks before the appointment."
    },
    "Patient-Centered Workflow": {
        "default": 3,
        "finding": "Patient communication gaps can create confusion, missed requirements, no-shows, repeat calls, and access friction.",
        "action": "Create a patient-facing next-step script for authorization, referral, documentation, and visit preparation."
    },
    "Compliance Readiness": {
        "default": 2,
        "finding": "Compliance readiness gaps can create authorization delays, referral problems, audit exposure, and payer requirement issues.",
        "action": "Add an authorization, referral, documentation, and payer requirement review checkpoint before service."
    },
    "Cross-Functional Communication": {
        "default": 2,
        "finding": "Communication gaps between scheduling, registration, authorization, clinical, and billing teams can create rework and downstream claim problems.",
        "action": "Create a documented handoff field that identifies status, owner, next step, and unresolved risk before the workflow moves forward."
    },
    "Continuous Improvement": {
        "default": 3,
        "finding": "When recurring workflow failures are not tracked, preventable errors continue affecting patients, staff, and revenue cycle readiness.",
        "action": "Build a weekly workflow issue log to track repeated errors, root causes, and improvement actions."
    }
}

risk_mapping = {
    1: "Critical Risk",
    2: "High Risk",
    3: "Moderate Risk",
    4: "Low Risk",
    5: "Strong Practice"
}

st.markdown(
    """
    <div class="brand-banner">
        <div class="brand-label">Simulated KPI Dashboard · Synthetic Data · No PHI</div>
        <h1>Healthcare Operations Habit Audit™</h1>
        <p>A simulated workflow risk assessment for patient access, prior authorization, revenue cycle, and denial prevention.</p>
        <p>Created by Kori Pickle<br>BSHA Candidate, University of Phoenix</p>
        <p><em>Where healthcare workflows break before patients, staff, and revenue feel the impact.</em></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="disclaimer-box">
        Simulated educational portfolio project only. No PHI, real patient data, payer data, employer data, real claims data, or real healthcare organization data is used. Scores are practice outputs, not employer results.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("## Simulated Scenario")
st.write(
    "A simulated healthcare organization is experiencing increased authorization delays, eligibility rework, patient confusion, and preventable claim denials. This audit identifies which daily operational habits may be contributing to downstream workflow risk."
)

st.markdown("## Score the Six Operational Habits")
st.caption("Score each habit from 1 to 5. Lower scores indicate greater workflow risk.")

scores = {}
cols = st.columns(2)
for index, (category, info) in enumerate(categories.items()):
    with cols[index % 2]:
        scores[category] = st.slider(
            category,
            min_value=1,
            max_value=5,
            value=info["default"],
            help="1 = Critical Risk, 2 = High Risk, 3 = Moderate Risk, 4 = Low Risk, 5 = Strong Practice"
        )

score_values = list(scores.values())
average_score = round(sum(score_values) / len(score_values), 2)
workflow_reliability = round(average_score * 20, 1)
denial_prevention_readiness = round(
    (
        scores["Documentation Accuracy"]
        + scores["Data Integrity"]
        + scores["Compliance Readiness"]
        + scores["Cross-Functional Communication"]
    ) / 4,
    2
)
patient_friction_risk_score = round(
    (scores["Patient-Centered Workflow"] + scores["Cross-Functional Communication"]) / 2,
    2
)
lowest_score = min(score_values)
lowest_categories = [category for category, score in scores.items() if score == lowest_score]
improvement_priority = ", ".join(lowest_categories)

if average_score < 2:
    overall_risk = "Critical Workflow Risk"
elif average_score < 3:
    overall_risk = "High Workflow Risk"
elif average_score < 4:
    overall_risk = "Moderate Workflow Risk"
elif average_score < 5:
    overall_risk = "Low Workflow Risk"
else:
    overall_risk = "Strong Operational Habit Maturity"

st.markdown("## Simulated Scoring Dashboard")
metric_cols = st.columns(3)
metric_data = [
    ("Average Habit Score", f"{average_score} / 5"),
    ("Workflow Reliability Score", f"{workflow_reliability} / 100"),
    ("Overall Risk Level", overall_risk),
    ("Denial Prevention Readiness", f"{denial_prevention_readiness} / 5"),
    ("Patient Friction Risk Indicator", f"{patient_friction_risk_score} / 5"),
    ("Improvement Priority", improvement_priority),
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
            unsafe_allow_html=True
        )

st.markdown("## Audit Results Table")
results_df = pd.DataFrame(
    [
        {
            "Category": category,
            "Score": score,
            "Risk Level": risk_mapping[score],
            "Downstream Risk": categories[category]["finding"],
            "Prevention Action": categories[category]["action"],
        }
        for category, score in scores.items()
    ]
)
st.dataframe(results_df, use_container_width=True, hide_index=True)

st.markdown("## Key Risk Finding")
for category in lowest_categories:
    st.markdown(
        f"""
        <div class="risk-box">
            <h3>{category}</h3>
            <p>{categories[category]['finding']}</p>
            <p>Recommended Action: {categories[category]['action']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("## 30-Day Improvement Plan")
plan_df = pd.DataFrame(
    [
        {"Timeline": "Week 1", "Action": "Review top three workflow risks", "Purpose": "Identify where the process first loses control"},
        {"Timeline": "Week 1", "Action": "Create front-end checklist", "Purpose": "Standardize documentation and verification"},
        {"Timeline": "Week 2", "Action": "Map communication handoffs", "Purpose": "Reduce department-to-department breakdowns"},
        {"Timeline": "Week 2", "Action": "Create patient instruction script", "Purpose": "Improve patient-centered communication"},
        {"Timeline": "Week 3", "Action": "Track repeated errors", "Purpose": "Find patterns causing rework and denials"},
        {"Timeline": "Week 4", "Action": "Review progress and update workflow", "Purpose": "Build continuous improvement habit"},
    ]
)
st.dataframe(plan_df, use_container_width=True, hide_index=True)

st.markdown("## Portfolio Positioning")
st.write(
    "This simulated app demonstrates how operational habits can be scored to identify workflow risk before it becomes a patient access delay, authorization gap, denial risk, documentation problem, or staff rework issue. It is designed as a student portfolio project and does not represent formal healthcare employment experience."
)
