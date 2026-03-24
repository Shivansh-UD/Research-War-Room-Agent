import streamlit as st

st.set_page_config(
    page_title="Verdict · Research War Room",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg:       #080810;
    --bg2:      #0e0e1a;
    --border:   #1e1e35;
    --optimist: #00ff88;
    --skeptic:  #ff4466;
    --devil:    #ff9900;
    --accent:   #4488ff;
    --text:     #e8e8f0;
    --muted:    #555570;
}

* { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] { display:none; }
[data-testid="collapsedControl"] { display:none; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding: 40px 24px !important; max-width: 960px !important; margin: 0 auto !important; }
footer { display: none !important; }

/* ── PAGE HEADER ── */
.verdict-header {
    text-align: center;
    margin-bottom: 48px;
    padding-bottom: 32px;
    border-bottom: 1px solid var(--border);
}

.verdict-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 12px;
}

.verdict-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 72px;
    letter-spacing: 4px;
    line-height: 1;
    margin-bottom: 12px;
    background: linear-gradient(135deg, var(--optimist), var(--accent), var(--skeptic));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.topic-badge {
    display: inline-block;
    padding: 8px 20px;
    border: 1px solid var(--accent);
    border-radius: 100px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    background: rgba(68,136,255,0.08);
    letter-spacing: 1px;
}

/* ── VERDICT CARD ── */
.verdict-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 48px;
    position: relative;
    overflow: hidden;
}

.verdict-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--optimist), var(--accent), var(--skeptic));
}

.verdict-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 20px;
}

.verdict-text {
    font-size: 15px;
    line-height: 1.9;
    color: var(--text);
}

/* ── AGENT RECAP CARDS ── */
.summary-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-bottom: 48px;
}

.summary-card {
    background: var(--bg2);
    border: 1px solid;
    border-radius: 16px;
    padding: 24px;
}

.summary-card-optimist { border-color: rgba(0,255,136,0.2); }
.summary-card-skeptic  { border-color: rgba(255,68,102,0.2); }
.summary-card-devil    { border-color: rgba(255,153,0,0.2); }

.summary-card-name {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
    font-weight: 700;
}

.name-optimist { color: var(--optimist); }
.name-skeptic  { color: var(--skeptic); }
.name-devil    { color: var(--devil); }

.summary-card-text {
    font-size: 13px;
    line-height: 1.7;
    color: rgba(232,232,240,0.7);
}

/* ── BUTTONS ── */
.stButton > button {
    border-radius: 12px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 18px !important;
    letter-spacing: 3px !important;
    padding: 14px 32px !important;
    transition: all 0.2s !important;
    width: 100% !important;
    background: transparent !important;
    border: 1px solid var(--accent) !important;
    color: var(--accent) !important;
}

.stButton > button:hover {
    background: var(--accent) !important;
    color: var(--bg) !important;
    box-shadow: 0 8px 32px rgba(68,136,255,0.2) !important;
}

.stDownloadButton > button {
    background: var(--optimist) !important;
    color: var(--bg) !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 18px !important;
    letter-spacing: 3px !important;
    padding: 14px 32px !important;
    width: 100% !important;
    transition: all 0.2s !important;
}

.stDownloadButton > button:hover {
    box-shadow: 0 8px 32px rgba(0,255,136,0.25) !important;
    transform: translateY(-2px) !important;
}

/* ── DIVIDER ── */
.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 40px 0;
}

/* ── NO DEBATE ── */
.no-debate {
    text-align: center;
    padding: 80px 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 1px;
}

.no-debate-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 48px;
    color: var(--border);
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ── INIT SESSION STATE ───────────────────────────────────────────────
if "debate_results" not in st.session_state:
    st.session_state.debate_results = None
if "debate_topic" not in st.session_state:
    st.session_state.debate_topic = ""
if "debate_ready" not in st.session_state:
    st.session_state.debate_ready = False

# ── GUARD: no debate yet ─────────────────────────────────────────────
if not st.session_state.debate_ready or st.session_state.debate_results is None:
    st.markdown("""
    <div class="no-debate">
        <div class="no-debate-title">NO VERDICT YET</div>
        Go back to the home page and run a debate first.
    </div>
    """, unsafe_allow_html=True)
    if st.button("← BACK TO HOME"):
        st.switch_page("ui.py")
    st.stop()

# ── DATA ─────────────────────────────────────────────────────────────
topic   = st.session_state.debate_topic
results = st.session_state.debate_results

# ── PAGE HEADER ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="verdict-header">
    <div class="verdict-eyebrow">Final Verdict</div>
    <div class="verdict-title">THE VERDICT</div>
    <div class="topic-badge">⚔ &nbsp; {topic}</div>
</div>
""", unsafe_allow_html=True)

# ── VERDICT CARD ─────────────────────────────────────────────────────
st.markdown(f"""
<div class="verdict-card">
    <div class="verdict-label">📊 &nbsp; Summarizer Agent — Full Analysis</div>
    <div class="verdict-text">{results["summary"].replace(chr(10), '<br>')}</div>
</div>
""", unsafe_allow_html=True)

# ── AGENT RECAP CARDS ────────────────────────────────────────────────
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:4px;
            color:#555570; text-transform:uppercase; text-align:center; margin-bottom:24px;">
    Agent Recap
</div>
""", unsafe_allow_html=True)

opt_preview   = results["optimist"][:280] + "..."
skep_preview  = results["skeptic"][:280]  + "..."
devil_preview = results["devil"][:280]    + "..."

st.markdown(f"""
<div class="summary-grid">
    <div class="summary-card summary-card-optimist">
        <div class="summary-card-name name-optimist">🟢 &nbsp; Optimist</div>
        <div class="summary-card-text">{opt_preview}</div>
    </div>
    <div class="summary-card summary-card-skeptic">
        <div class="summary-card-name name-skeptic">🔴 &nbsp; Skeptic</div>
        <div class="summary-card-text">{skep_preview}</div>
    </div>
    <div class="summary-card summary-card-devil">
        <div class="summary-card-name name-devil">😈 &nbsp; Devil</div>
        <div class="summary-card-text">{devil_preview}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── DOWNLOAD + NEW TOPIC BUTTONS ─────────────────────────────────────
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

download_text = f"""RESEARCH WAR ROOM — DEBATE REPORT
{'='*60}
TOPIC: {topic}
{'='*60}

🟢 OPTIMIST ARGUMENT
{'-'*60}
{results['optimist']}

🔴 SKEPTIC ARGUMENT
{'-'*60}
{results['skeptic']}

😈 DEVIL'S ARGUMENT
{'-'*60}
{results['devil']}

📊 SUMMARIZER VERDICT
{'-'*60}
{results['summary']}

{'='*60}
Generated by Research War Room — AI Multi-Agent Debate System
"""

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label="📥  DOWNLOAD REPORT",
        data=download_text,
        file_name=f"debate_{topic[:30].replace(' ', '_')}.txt",
        mime="text/plain"
    )

with col2:
    if st.button("🔄  NEW TOPIC"):
        st.session_state.debate_results = None
        st.session_state.debate_topic   = ""
        st.session_state.debate_ready   = False
        st.switch_page("ui.py")