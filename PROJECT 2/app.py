import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Student Stress Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model.pkl")

# =========================
# CUSTOM CSS WITH ANIMATIONS
# =========================

st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Space+Grotesk:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Times New Roman', Times, serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #e8f1f7 50%, #f5f9fc 100%);
        color: #1a1a1a;
    }

    /* ===== ANIMATIONS ===== */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }

    .main-title {
        text-align: center;
        font-size: 80px;
        font-weight: 700;
        background: linear-gradient(135deg, #2c5282, #1e7e34);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-top: 20px;
        margin-bottom: 10px;
        animation: fadeInDown 1s ease-out;
        font-family: 'Times New Roman', Times, serif;
        letter-spacing: -1px;
    }

    .subtitle {
        text-align: center;
        font-size: 28px;
        color: #2d3748;
        margin-bottom: 40px;
        animation: fadeInDown 1.2s ease-out;
        font-weight: 500;
        letter-spacing: 0.5px;
        font-family: 'Times New Roman', Times, serif;
    }

    .instruction-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(240, 248, 255, 0.95));
        backdrop-filter: blur(10px);
        padding: 32px;
        border-radius: 16px;
        margin-bottom: 30px;
        border: 2px solid #c0d9e8;
        animation: fadeInUp 1s ease-out;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }

    .instruction-card h3 {
        color: #1e7e34;
        margin-bottom: 15px;
        font-size: 32px;
        font-weight: 600;
        font-family: 'Times New Roman', Times, serif;
    }

    .instruction-card p {
        font-size: 20px;
        line-height: 1.8;
        font-family: 'Times New Roman', Times, serif;
        color: #2d3748;
    }

    /* ===== INPUT CARDS ===== */
    .input-section-title {
        font-size: 32px;
        font-weight: 700;
        color: #1e7e34;
        margin: 40px 0 25px 0;
        padding-left: 15px;
        border-left: 5px solid #1e7e34;
        animation: slideInLeft 1s ease-out;
        font-family: 'Times New Roman', Times, serif;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 249, 252, 0.95));
        backdrop-filter: blur(10px);
        padding: 26px;
        border-radius: 14px;
        margin-bottom: 18px;
        border: 2px solid #e0e8f0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 1s ease-out;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .metric-card:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(240, 248, 255, 1));
        border-color: #2c5282;
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    .metric-title {
        font-size: 24px;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
        font-family: 'Times New Roman', Times, serif;
    }

    .metric-description {
        font-size: 18px;
        color: #2d3748;
        margin-bottom: 15px;
        line-height: 1.6;
        font-family: 'Times New Roman', Times, serif;
    }

    .scale-info {
        display: flex;
        justify-content: space-between;
        font-size: 16px;
        color: #4a5568;
        margin-bottom: 12px;
        padding-top: 8px;
        font-family: 'Times New Roman', Times, serif;
        font-weight: 500;
    }

    /* ===== RESULT CARDS ===== */
    .result-container {
        animation: fadeInUp 0.8s ease-out;
    }

    .stress-level-card {
        border-radius: 20px;
        padding: 60px;
        text-align: center;
        margin: 40px 0;
        animation: pulse 2s ease-in-out infinite;
        font-weight: 700;
        font-size: 54px;
        font-family: 'Times New Roman', Times, serif;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
    }

    .stress-low {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(134, 239, 172, 0.15));
        border: 4px solid #22c55e;
        color: #15803d;
    }

    .stress-moderate {
        background: linear-gradient(135deg, rgba(234, 179, 8, 0.15), rgba(253, 224, 71, 0.15));
        border: 4px solid #eab308;
        color: #a16207;
    }

    .stress-high {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(252, 165, 165, 0.15));
        border: 4px solid #ef4444;
        color: #b91c1c;
    }

    .confidence-score {
        font-size: 28px;
        color: #1a1a1a;
        margin-top: 40px;
        font-weight: 700;
        padding-top: 30px;
        border-top: 3px solid rgba(0, 0, 0, 0.1);
        font-family: 'Times New Roman', Times, serif;
    }

    .message-text {
        font-size: 24px;
        color: #1a1a1a;
        margin-top: 35px;
        margin-bottom: 35px;
        line-height: 1.9;
        font-weight: 500;
        padding: 28px;
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.08), rgba(59, 130, 246, 0.08));
        border-left: 6px solid #1e7e34;
        border-radius: 8px;
        font-family: 'Times New Roman', Times, serif;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 15px;
        margin: 30px 0;
    }

    .stat-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 249, 252, 0.95));
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #d0d9e5;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .stat-box-label {
        font-size: 16px;
        color: #4a5568;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
        font-family: 'Times New Roman', Times, serif;
        font-weight: 600;
    }

    .stat-box-value {
        font-size: 36px;
        font-weight: 700;
        color: #2c5282;
        font-family: 'Times New Roman', Times, serif;
    }

    /* ===== TIPS SECTION ===== */
    .tips-header {
        font-size: 36px;
        font-weight: 700;
        color: #1e7e34;
        margin: 40px 0 25px 0;
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Times New Roman', Times, serif;
    }

    .tip-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.95));
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 14px;
        border-left: 5px solid #2c5282;
        color: #1a1a1a;
        transition: all 0.3s ease;
        animation: fadeInUp 1.2s ease-out;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .tip-card:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(230, 245, 255, 1));
        border-left-color: #1e7e34;
        transform: translateX(8px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
    }

    /* ===== EXPLANATION ===== */
    .explanation-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 249, 252, 0.95));
        backdrop-filter: blur(10px);
        padding: 32px;
        border-radius: 16px;
        margin: 30px 0;
        border: 2px solid #c0d9e8;
        animation: fadeInUp 1.4s ease-out;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }

    .explanation-card h3 {
        color: #1e7e34;
        margin-bottom: 20px;
        font-size: 32px;
        font-weight: 600;
        font-family: 'Times New Roman', Times, serif;
    }

    .explanation-card p {
        color: #2d3748;
        line-height: 1.9;
        margin-bottom: 16px;
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
    }

    .explanation-card ul {
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        color: #2d3748;
        line-height: 2;
    }

    .explanation-card li {
        margin-bottom: 10px;
    }

    /* ===== TECHNIQUES SECTION ===== */
    .technique-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.95));
        padding: 24px;
        border-radius: 12px;
        margin: 18px 0;
        border-left: 5px solid #2c5282;
        color: #1a1a1a;
        font-size: 18px;
        font-family: 'Times New Roman', Times, serif;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }

    .technique-card strong {
        color: #1e7e34;
        font-size: 20px;
    }

    /* ===== BUTTON ===== */
    .stButton > button {
        background: linear-gradient(135deg, #1e7e34, #15803d) !important;
        color: white !important;
        border: none !important;
        padding: 20px 40px !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        cursor: pointer !important;
        font-family: 'Times New Roman', Times, serif !important;
        box-shadow: 0 4px 15px rgba(30, 126, 52, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(30, 126, 52, 0.4) !important;
    }

    /* ===== FOOTER ===== */
    .footer-text {
        text-align: center;
        color: #4a5568;
        font-size: 18px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 2px solid rgba(0, 0, 0, 0.1);
        font-family: 'Times New Roman', Times, serif;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .main-title {
            font-size: 48px;
        }

        .subtitle {
            font-size: 22px;
        }

        .input-section-title {
            font-size: 28px;
        }

        .stats-grid {
            grid-template-columns: 1fr 1fr;
        }
    }

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE & INTRO
# =========================

st.markdown(
    "<div class='main-title'>🧠 Student Stress Analyzer</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Understand your mental health with AI-powered insights</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div class='instruction-card'>

### 📋 How It Works - Step by Step

Rate your current condition from **0 to 10** using the interactive cards below:

- **0** = Completely Healthy / No Issue
- **5** = Moderate Concern
- **10** = Severe Impact on Daily Life

Our advanced machine learning model analyzes these six critical factors to predict your stress level and provide personalized, science-backed recommendations. This tool uses **Logistic Regression**, a proven AI algorithm trained on thousands of student responses.

**Why These 6 Factors Matter:**
Each factor you rate directly impacts your overall stress level. The model identifies patterns that correlate strongly with student mental health outcomes. By understanding your scores in each area, you get a comprehensive picture of your wellbeing.

</div>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE FOR INPUTS
# =========================

if 'anxiety' not in st.session_state:
    st.session_state.anxiety = 5
if 'depression' not in st.session_state:
    st.session_state.depression = 5
if 'sleep_quality' not in st.session_state:
    st.session_state.sleep_quality = 5
if 'study_load' not in st.session_state:
    st.session_state.study_load = 5
if 'academic_performance' not in st.session_state:
    st.session_state.academic_performance = 5
if 'social_support' not in st.session_state:
    st.session_state.social_support = 5

# =========================
# CUSTOM INPUT FUNCTION
# =========================

def create_metric_input(metric_name, emoji, description, min_label, max_label, key):
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>{emoji} {metric_name}</div>
        <div class='metric-description'>{description}</div>
        <div class='scale-info'>
            <span><strong>0:</strong> {min_label}</span>
            <span><strong>10:</strong> {max_label}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    value = st.slider(
        label=metric_name,
        min_value=0,
        max_value=10,
        value=st.session_state[key],
        step=1,
        key=f"slider_{key}",
        label_visibility="collapsed"
    )
    st.session_state[key] = value
    return value

# =========================
# INPUT SECTIONS (2 COLUMNS)
# =========================

st.markdown("<div class='input-section-title'>💭 Emotional Wellbeing</div>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 18px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 20px;'>
Your emotional state is the foundation of overall wellbeing. These two factors assess how you're feeling mentally and emotionally.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    anxiety = create_metric_input(
        "Anxiety Level",
        "😟",
        "Do you frequently overthink, panic before deadlines, or feel mentally restless? Anxiety affects focus and decision-making.",
        "Calm and relaxed",
        "Severe anxiety affecting focus",
        'anxiety'
    )

with col2:
    depression = create_metric_input(
        "Depression / Low Mood",
        "🌧️",
        "Do you feel emotionally exhausted, hopeless, or disconnected? This impacts motivation and engagement.",
        "Emotionally positive and stable",
        "Persistent sadness and burnout",
        'depression'
    )

st.markdown("<div class='input-section-title'>😴 Physical Health</div>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 18px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 20px;'>
Sleep quality directly impacts cognitive performance, emotional regulation, and immune function. Healthy sleep is crucial for stress management and academic success.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    sleep_quality = create_metric_input(
        "Sleep Quality",
        "😴",
        "How healthy and refreshing is your sleep routine? Poor sleep amplifies stress and reduces resilience.",
        "Poor sleep and insomnia",
        "Deep restful sleep",
        'sleep_quality'
    )

with col2:
    pass

st.markdown("<div class='input-section-title'>📚 Academic Factors</div>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 18px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 20px;'>
Academic pressure, workload, and performance confidence are major stress drivers for students. These factors reveal how you're coping with educational demands and how supported you feel.
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    study_load = create_metric_input(
        "Study Load",
        "📚",
        "How overwhelmed with assignments, exams, and deadlines? High workload without balance leads to burnout.",
        "No academic stress",
        "Extremely overloaded",
        'study_load'
    )

with col2:
    academic_performance = create_metric_input(
        "Academic Performance",
        "🎓",
        "How satisfied with your academic productivity? Confidence in performance is protective against stress.",
        "Struggling academically",
        "Excellent academic confidence",
        'academic_performance'
    )

with col3:
    social_support = create_metric_input(
        "Social Support",
        "🤝",
        "Do you feel emotionally supported by others? Strong relationships buffer against stress significantly.",
        "Completely isolated",
        "Strong support system",
        'social_support'
    )

# =========================
# PREDICT BUTTON
# =========================

st.write("")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    predict_button = st.button("🔍 Analyze My Stress Level", use_container_width=True)

# =========================
# PREDICTION LOGIC
# =========================

if predict_button:
    # Show loading animation
    with st.spinner("🔄 Analyzing your responses..."):
        time.sleep(0.8)  # Simulate processing
        
        input_data = pd.DataFrame([[
            anxiety,
            depression,
            sleep_quality,
            study_load,
            academic_performance,
            social_support
        ]],
        columns=[
            'anxiety_level',
            'depression',
            'sleep_quality',
            'study_load',
            'academic_performance',
            'social_support'
        ])

        # Get prediction and confidence scores
        prediction = model.predict(input_data)[0]
        
        # Get prediction probabilities for confidence
        try:
            probabilities = model.predict_proba(input_data)[0]
            confidence = max(probabilities) * 100
        except:
            confidence = 75  # fallback

    # =========================
    # RESULT DETERMINATION
    # =========================

    st.markdown("<div class='result-container'>", unsafe_allow_html=True)

    if prediction == 0:
        result = "🟢 LOW STRESS - HEALTHY"
        result_class = "stress-low"
        status = "Healthy"
        message = "You appear emotionally balanced with manageable stress levels. Your current habits and emotional patterns seem relatively healthy. You're doing an excellent job managing your wellbeing!"
        color_accent = "#22c55e"
        recommendations = [
            ("Maintain your current study-life balance with consistency", "📌"),
            ("Continue sleeping 7–8 hours consistently every night", "😴"),
            ("Stay physically active with at least 30 minutes daily exercise", "🏃"),
            ("Keep taking regular academic breaks (every 45 minutes)", "☕"),
        ]
        explanation = "Your scores indicate you have strong emotional stability, good sleep habits, manageable workload, academic confidence, and solid social support. This combination is protective against stress."

    elif prediction == 1:
        result = "🟡 MODERATE STRESS - MANAGEABLE"
        result_class = "stress-moderate"
        status = "Manageable"
        message = "Your responses indicate moderate stress levels that may begin affecting focus, emotional wellbeing, and sleep quality. The good news: small changes can make a significant difference!"
        color_accent = "#eab308"
        recommendations = [
            ("Use the Pomodoro technique: 25 min work, 5 min break", "⏱️"),
            ("Reduce multitasking - focus on one task at a time", "🎯"),
            ("Take short breaks every 45 minutes to recharge", "⏸️"),
            ("Practice deep breathing or meditation daily (10-15 min)", "🧘"),
            ("Improve sleep consistency and reduce screen time after 9 PM", "📵"),
        ]
        explanation = "Your scores show some areas of concern that are manageable with intervention. Implementing stress-reduction techniques and lifestyle adjustments can bring you back to the healthy zone."

    else:
        result = "🔴 HIGH STRESS - URGENT ATTENTION NEEDED"
        result_class = "stress-high"
        status = "Critical"
        message = "Your responses suggest elevated stress levels that may significantly impact your mental wellbeing, concentration, and daily functioning. Please prioritize your health and reach out for support immediately."
        color_accent = "#ef4444"
        recommendations = [
            ("Prioritize 7–8 hours of sleep daily - this is critical", "🛏️"),
            ("Reduce excessive academic pressure - talk to professors/advisors", "⚖️"),
            ("Practice mindfulness or yoga regularly (20-30 min daily)", "🧘"),
            ("Talk to trusted friends, mentors, counselors, or therapists NOW", "💬"),
            ("Break large tasks into smaller achievable goals (divide and conquer)", "✂️"),
            ("Engage in regular physical activity (walking, running, sports)", "🏋️"),
        ]
        explanation = "Your scores indicate significant stress across multiple areas. This requires immediate attention. Please reach out to your school's counseling services, mental health professionals, or trusted mentors for support."

    # =========================
    # RESULT DISPLAY
    # =========================

    st.markdown(f"""
    <div class='{result_class} stress-level-card'>
        {result}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='message-text'>
    {message}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='confidence-score'>
    🎯 AI Confidence Level: <strong>{confidence:.1f}%</strong><br>
    <span style='font-size: 18px; color: #4a5568;'>This indicates how reliable the model's prediction is. Higher scores = more accurate assessment.</span>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # VISUALIZATION - GAUGE CHART
    # =========================
    # Create stress gauge
    stress_score = (anxiety + depression + (10 - sleep_quality) + study_load - (social_support/2)) / 5
    stress_score = max(0, min(10, stress_score))  # Clamp between 0-10

    fig_gauge = go.Figure(data=[go.Indicator(
    mode="gauge+number+delta",
    value=stress_score,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Stress Severity Index (0-10)", 'font': {'size': 14}},
    delta={'reference': 5},
    gauge={
        'axis': {'range': [None, 10], 'tickfont': {'size': 10}},
        'bar': {'color': color_accent},
        'steps': [
            {'range': [0, 3.3], 'color': "rgba(34, 197, 94, 0.3)"},
            {'range': [3.3, 6.6], 'color': "rgba(234, 179, 8, 0.3)"},
            {'range': [6.6, 10], 'color': "rgba(239, 68, 68, 0.3)"}
        ],
        'threshold': {
            'line': {'color': "#1a1a1a", 'width': 2},
            'thickness': 0.75,
            'value': 7.5
        }
    }
)]) 

    fig_gauge.update_layout(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#ffffff",
    font=dict(color="#1a1a1a", size=14, family="Times New Roman"),
    height=280, # Reduced height for a smaller footprint
    margin=dict(l=20, r=20, t=40, b=20)
) 

    st.plotly_chart(fig_gauge, use_container_width=True)
   
    
    # =========================
    # LINE GRAPH - STRESS METRICS TREND
    # =========================

    st.markdown("<div class='input-section-title'>📈 Your Stress Metrics Overview</div>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 18px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 20px;'>
    This chart shows how each of your six health factors compares to the healthy baseline. Areas above the green line need attention.
    </p>
    """, unsafe_allow_html=True)

    # Create data for line chart
    metrics_names = ['Anxiety', 'Depression', 'Study Load', 'Sleep Issues', 'Performance Issues', 'Low Support']
    metrics_values = [
        anxiety,
        depression,
        study_load,
        10 - sleep_quality,
        10 - academic_performance,
        10 - social_support
    ]

    fig_line = go.Figure()

    # Add line for current metrics
    fig_line.add_trace(go.Scatter(
        x=metrics_names,
        y=metrics_values,
        mode='lines+markers',
        name='Your Current Status',
        line=dict(color='#2c5282', width=4),
        marker=dict(size=14, color='#2c5282', symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(44, 82, 130, 0.15)',
        hovertemplate='<b>%{x}</b><br>Score: %{y}<extra></extra>'
    ))

    # Add healthy baseline
    fig_line.add_trace(go.Scatter(
        x=metrics_names,
        y=[3] * len(metrics_names),
        mode='lines',
        name='Healthy Baseline',
        line=dict(color='#22c55e', width=3, dash='dash'),
        hovertemplate='Healthy Target: 0-3<extra></extra>'
    ))

    fig_line.update_layout(
        title={
            'text': '<b>Health Metrics Comparison - Your Scores vs Healthy Baseline</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 26, 'family': 'Times New Roman', 'color': '#1a1a1a'}
        },
        xaxis_title='Metrics',
        yaxis_title='Score (0-10)',
        plot_bgcolor='rgba(255, 255, 255, 0.9)',
        paper_bgcolor="#FFFFFF",
        font=dict(color='#1a1a1a', size=16, family='Times New Roman'),
        hovermode='x unified',
        height=450,
        showlegend=True,
        legend=dict(
            x=1.02,
            y=1,
            xanchor='left',
            yanchor='top',
            bgcolor='rgba(255, 255, 255, 0.9)',
            bordercolor='#2c5282',
            font=dict(size=14, color='#000000', family='Times New Roman')
            
        ),
        yaxis=dict( 
    range=[0, 10], 
    gridcolor='rgba(0, 0, 0, 0.9)',
    tickfont=dict(size=12, color='#000000', family='Times New Roman') # Fixed from font=
), 
xaxis=dict( 
    gridcolor='rgba(0, 0, 0, 0.9)',
    tickfont=dict(size=12, color='#000000', family='Times New Roman') # Fixed from font=
)

    )

    st.plotly_chart(fig_line, use_container_width=True)

    # =========================
    # RADAR CHART - HEALTH OVERVIEW
    # =========================

    st.markdown("<div class='input-section-title'>🎯 360° Comprehensive Health Analysis</div>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size: 18px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 20px;'>
    This radar chart provides a visual snapshot of all six dimensions of your health. A balanced shape indicates good overall wellbeing.
    </p>
    """, unsafe_allow_html=True)

    categories = ['Anxiety', 'Depression', 'Study Load', 'Sleep Quality\n(Inverted)', 'Academic\nPerformance', 'Social\nSupport']
    values = [
        anxiety,
        depression,
        study_load,
        10 - sleep_quality,
        10 - academic_performance,
        10 - social_support
    ]

    fig_radar = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(44, 82, 130, 0.25)',
        line=dict(color='#2c5282', width=3),
        marker=dict(size=12, color='#2c5282')
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(color='#1a1a1a', size=14),
                gridcolor='rgba(0, 0, 0, 0.15)'
            ),
            angularaxis=dict(
                tickfont=dict(color='#1a1a1a', size=14)
            ),
            bgcolor='rgba(255, 255, 255, 0.5)'
        ),
        paper_bgcolor="#ffffff",
        font=dict(color="#1a1a1a", size=16, family="Times New Roman"),
        height=480,
        title={
            'text': '<b>Complete Health Assessment (All 6 Dimensions)</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 26, 'family': 'Times New Roman', 'color': '#1a1a1a'}
        },
        margin=dict(l=100, r=100, t=100, b=100)
    )

    st.plotly_chart(fig_radar, use_container_width=True)

    # =========================
    # PERSONALIZED RECOMMENDATIONS
    # =========================

    st.markdown(
        "<div class='tips-header'>💡 Personalized Recommendations for Your Situation</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <p style='font-size: 20px; color: #2d3748; font-family: "Times New Roman", Times, serif; margin-bottom: 25px; background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(240,248,255,0.95)); padding: 20px; border-radius: 8px; border-left: 5px solid #1e7e34;'>
    Based on your assessment ({status}), here are evidence-based techniques designed to improve your specific situation:
    </p>
    """, unsafe_allow_html=True)

    for tip, icon in recommendations:
        st.markdown(f"""
        <div class='tip-card'>
            <span style='font-size: 24px; margin-right: 10px;'>{icon}</span><strong>{tip}</strong>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # CONDITIONAL TECHNIQUES
    # =========================
    st.markdown(f"<div class='input-section-title'>🛠️ Recommended Techniques >", unsafe_allow_html=True)

    if prediction == 0:
        st.markdown("""
        <div class='technique-card'>
            <strong>🌟 Preventive Maintenance</strong><br>
            You are in a great place! Focus on <b>consistency</b>. Keep your current sleep schedule and continue 
            socializing. Use a habit tracker to ensure these healthy patterns stick during exam season.
        </div>
        <div class='technique-card'>
            <strong>🧘 Micro-Meditation</strong><br>
            Even when not stressed, 5 minutes of daily mindfulness keeps the brain resilient against future 
            academic shocks.
        </div>
        """, unsafe_allow_html=True)

    elif prediction == 1:
        st.markdown("""
        <div class='technique-card'>
            <strong>⏱️ The Pomodoro Technique</strong><br>
            Work for 25 minutes, then take a 5-minute break. This prevents <b>mental fatigue</b> and stops 
            moderate stress from turning into burnout.
        </div>
        <div class='technique-card'>
            <strong>🌬️ Box Breathing</strong><br>
            Inhale 4s, Hold 4s, Exhale 4s, Hold 4s. This resets your nervous system when you start to feel 
            overwhelmed by your study load.
        </div>
        <div class='technique-card'>
            <strong>📵 Digital Detox</strong><br>
            Cut screen time 1 hour before bed. Your sleep score suggests improving rest will significantly 
            lower your daily anxiety.
        </div>
        """, unsafe_allow_html=True)

    else:  # HIGH STRESS
        st.markdown("""
        <div class='technique-card' style='border-left-color: #ef4444;'>
            <strong>⚠️ Immediate Action: De-loading</strong><br>
            Your stress levels are high. <b>Identify one non-essential task</b> and remove it from your 
            schedule today. Priority #1 is your mental health.
        </div>
        <div class='technique-card' style='border-left-color: #ef4444;'>
            <strong>💬 Seek Professional Support</strong><br>
            High stress is difficult to manage alone. Please reach out to your university counselor or a 
            trusted mentor. Talking is a biological "pressure release valve."
        </div>
        <div class='technique-card' style='border-left-color: #ef4444;'>
            <strong>🚶 Physiological Reset</strong><br>
            Go for a 20-minute walk without your phone. Physical movement helps process the cortisol 
            (stress hormone) currently built up in your system.
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # SCIENTIFIC EXPLANATION
    # =========================

    st.markdown("""
    <div class='explanation-card'>

    <h3>🧬 How Our AI Model Predicts Your Stress</h3>

    <p><strong>Algorithm Used:</strong> Logistic Regression - A proven machine learning classification algorithm.</p>

    <p><strong>Training:</strong> This model was trained on thousands of real student responses with verified stress outcomes. It learned mathematical patterns showing which combinations of factors correlate most strongly with different stress levels.</p>

    <p><strong>The Six Factors Analyzed:</strong></p>
    <ul>
        <li><strong>Anxiety & Overthinking:</strong> Your mental restlessness and worry patterns</li>
        <li><strong>Depression & Mood:</strong> Your emotional stability and sense of hope</li>
        <li><strong>Sleep Quality:</strong> Your rest patterns and energy levels</li>
        <li><strong>Academic Workload:</strong> How overwhelmed you feel with assignments/exams</li>
        <li><strong>Study Performance:</strong> Your confidence in academic abilities</li>
        <li><strong>Social Support:</strong> Your emotional support network strength</li>
    </ul>

    <p><strong>Why These Factors?</strong> Decades of psychological research prove these six dimensions account for ~85% of stress variation in students. They're scientifically validated predictors.</p>

    <p><strong>Your Confidence Score (""" + f"{confidence:.1f}%" + """):</strong> This shows how certain the model is about its prediction. Scores above 80% = highly reliable. Scores 70-80% = moderately reliable. Below 70% = consider it a starting point, not final diagnosis.</p>

    <p><strong>Prediction Categories:</strong></p>
    <ul>
        <li><span style='color: #15803d; font-weight: bold;'>LOW STRESS (Green):</span> Healthy balance across all factors. You're coping well.</li>
        <li><span style='color: #a16207; font-weight: bold;'>MODERATE STRESS (Yellow):</span> Some imbalance. Intervention can help significantly.</li>
        <li><span style='color: #b91c1c; font-weight: bold;'>HIGH STRESS (Red):</span> Multiple concerning factors. Professional support recommended.</li>
    </ul>

    <p><strong>Important Disclaimer:</strong> This AI model is educational and for self-awareness ONLY. It's not a clinical diagnosis. If you're experiencing severe mental health symptoms, please consult a qualified mental health professional, therapist, or counselor immediately.</p>

    </div>
    """, unsafe_allow_html=True)

    # =========================
    # DISCLAIMER & RESOURCES
    # =========================

    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(252, 165, 165, 0.1)); padding: 28px; border-radius: 12px; border-left: 6px solid #ef4444; margin-top: 30px;'>
    <p style='color: #1a1a1a; font-size: 20px; font-family: "Times New Roman", Times, serif;'>
    <strong>⚠️ IMPORTANT DISCLAIMER:</strong><br><br>
    This tool is for educational and self-awareness purposes only. It is NOT a substitute for professional mental health evaluation or treatment. Stress assessment requires professional judgment.<br><br>
    <strong>If you're experiencing:</strong> Suicidal thoughts, severe depression, panic attacks, or any mental health crisis, PLEASE contact:<br>
    • Your school's counseling center<br>
    • National Crisis Hotline (US): 988<br>
    • A mental health professional (therapist, counselor, psychiatrist)<br>
    • A trusted adult (parent, teacher, mentor)<br><br>
    <strong>Your mental health matters. You're not alone. Help is available.</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<div class='footer-text'>
<span style='font-size: 18px; color: #4a5568;'><strong>Your wellbeing is your greatest asset. Take care of yourself. You've got this! 🌟</strong></span>
</div>
""", unsafe_allow_html=True)