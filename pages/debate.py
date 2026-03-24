import streamlit as st

st.set_page_config(
    page_title="The Debate · Research War Room",
    page_icon="⚔️",
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
.page-header {
    text-align: center;
    margin-bottom: 48px;
    padding-bottom: 32px;
    border-bottom: 1px solid var(--border);
}

.page-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 12px;
}

.page-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 52px;
    letter-spacing: 2px;
    color: var(--text);
    line-height: 1;
    margin-bottom: 12px;
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

/* ── CHAT MESSAGES ── */
.chat-wrap {
    display: flex;
    flex-direction: column;
    gap: 24px;
    margin-bottom: 48px;
}

.msg-row {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    animation: fadeUp 0.4s ease both;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.msg-avatar {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
    border: 2px solid;
}

.avatar-optimist { border-color: var(--optimist); background: rgba(0,255,136,0.08); }
.avatar-skeptic  { border-color: var(--skeptic);  background: rgba(255,68,102,0.08); }
.avatar-devil    { border-color: var(--devil);    background: rgba(255,153,0,0.08); }

.msg-body { flex: 1; }

.msg-name {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-weight: 700;
}

.name-optimist { color: var(--optimist); }
.name-skeptic  { color: var(--skeptic); }
.name-devil    { color: var(--devil); }

.msg-bubble {
    padding: 20px 24px;
    border-radius: 0 16px 16px 16px;
    border: 1px solid;
    font-size: 14px;
    line-height: 1.8;
    color: var(--text);
}

.bubble-optimist { border-color: rgba(0,255,136,0.2);  background: rgba(0,255,136,0.04); }
.bubble-skeptic  { border-color: rgba(255,68,102,0.2); background: rgba(255,68,102,0.04); }
.bubble-devil    { border-color: rgba(255,153,0,0.2);  background: rgba(255,153,0,0.04); }

/* ── VERDICT BUTTON ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--accent) !important;
    color: var(--accent) !important;
    border-radius: 12px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 20px !important;
    letter-spacing: 3px !important;
    padding: 14px 40px !important;
    width: 100% !important;
    transition: all 0.2s !important;
}

.stButton > button:hover {
    background: var(--accent) !important;
    color: var(--bg) !important;
    box-shadow: 0 8px 32px rgba(68,136,255,0.2) !important;
}

/* ── NO DEBATE MSG ── */
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

/* ── DIVIDER ── */
.debate-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 32px 0;
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
        <div class="no-debate-title">NO DEBATE YET</div>
        Go back to the home page and enter a topic to start the debate.
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
<div class="page-header">
    <div class="page-eyebrow">Live Debate</div>
    <div class="page-title">THE ARGUMENTS</div>
    <div class="topic-badge">⚔ &nbsp; {topic}</div>
</div>
""", unsafe_allow_html=True)

# ── CHAT MESSAGES ────────────────────────────────────────────────────
agents = [
    ("optimist", "🟢", "Optimist", "optimist", results["optimist"]),
    ("skeptic",  "🔴", "Skeptic",  "skeptic",  results["skeptic"]),
    ("devil",    "😈", "Devil",    "devil",    results["devil"]),
]

st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

for key, emoji, name, cls, argument in agents:
    st.markdown(f"""
    <div class="msg-row">
        <div class="msg-avatar avatar-{cls}">{emoji}</div>
        <div class="msg-body">
            <div class="msg-name name-{cls}">{name}</div>
            <div class="msg-bubble bubble-{cls}">{argument.replace(chr(10), '<br>')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="debate-divider"></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── NAVIGATE TO VERDICT ───────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📊  GET THE VERDICT"):
        st.switch_page("pages/verdict.py")