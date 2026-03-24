import streamlit as st

st.set_page_config(
    page_title="Research War Room",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg:         #080810;
    --bg2:        #0e0e1a;
    --border:     #1e1e35;
    --optimist:   #00ff88;
    --skeptic:    #ff4466;
    --devil:      #ff9900;
    --accent:     #4488ff;
    --text:       #e8e8f0;
    --muted:      #555570;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }
header[data-testid="stHeader"] { background: transparent !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
footer { display: none !important; }

/* ── BACKGROUND EFFECTS ── */
.bg-effects {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background:
        radial-gradient(ellipse 80% 50% at 20% 20%, rgba(0,255,136,0.06) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(255,68,102,0.06) 0%, transparent 60%),
        radial-gradient(ellipse 50% 60% at 50% 50%, rgba(68,136,255,0.04) 0%, transparent 70%);
}

.bg-grid {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-image:
        linear-gradient(rgba(68,136,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(68,136,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
}

/* ── HERO ── */
.hero {
    min-height: 55vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 24px 32px;
    position: relative;
    overflow: hidden;
}

.hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    max-width: 820px;
    width: 100%;
}

.eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 24px;
    opacity: 0.8;
}

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(72px, 12vw, 140px);
    line-height: 0.9;
    letter-spacing: 2px;
    color: var(--text);
    margin-bottom: 8px;
}

.hero-title span.war  { color: var(--skeptic); }
.hero-title span.room { color: var(--optimist); }

.hero-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 2px;
    margin-bottom: 48px;
}

/* ── AGENT PILLS ── */
.agent-row {
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 12px;
}

.agent-pill {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 100px;
    border: 1px solid;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.pill-optimist { border-color: var(--optimist); color: var(--optimist); background: rgba(0,255,136,0.05); }
.pill-skeptic  { border-color: var(--skeptic);  color: var(--skeptic);  background: rgba(255,68,102,0.05); }
.pill-devil    { border-color: var(--devil);    color: var(--devil);    background: rgba(255,153,0,0.05); }
.pill-summary  { border-color: var(--accent);   color: var(--accent);   background: rgba(68,136,255,0.05); }

/* ── INPUT BOX ── */
.stTextInput > div > div > input {
    background: var(--bg2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px !important;
    padding: 18px 24px !important;
    width: 100% !important;
    transition: border-color 0.2s !important;
}

.stTextInput > div > div > input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(68,136,255,0.1) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: var(--muted) !important;
}

/* ── BUTTON ── */
.stButton > button {
    width: 100% !important;
    background: var(--text) !important;
    color: var(--bg) !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 22px !important;
    letter-spacing: 3px !important;
    padding: 16px 40px !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    display: block !important;
    margin: 0 auto !important;
}

.stButton > button:hover {
    background: var(--optimist) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(0,255,136,0.2) !important;
}

/* ── STATS ROW ── */
.stats-row {
    display: flex;
    gap: 32px;
    justify-content: center;
    margin-top: 48px;
    margin-bottom: 48px;
    flex-wrap: wrap;
}

.stat-item { text-align: center; }

.stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px;
    color: var(--text);
    line-height: 1;
}

.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* ── STATUS MSG ── */
.status-msg {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--accent);
    text-align: center;
    padding: 16px;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: rgba(68,136,255,0.05);
    margin: 16px auto 0;
    letter-spacing: 1px;
}

.stTextInput label { display: none !important; }
.stSpinner > div { border-top-color: var(--optimist) !important; }
</style>

<div class="bg-effects"></div>
<div class="bg-grid"></div>
""", unsafe_allow_html=True)

# ── SESSION STATE INIT ──────────────────────────────────────────────
if "debate_results" not in st.session_state:
    st.session_state.debate_results = None
if "debate_topic" not in st.session_state:
    st.session_state.debate_topic = ""
if "debate_ready" not in st.session_state:
    st.session_state.debate_ready = False

# ── HERO SECTION ────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-content">
    <div class="eyebrow">⚔ &nbsp; AI · RAG · MCP · Multi-Agent</div>
    <div class="hero-title">
      RESEARCH<br>
      <span class="war">WAR</span>&nbsp;<span class="room">ROOM</span>
    </div>
    <div class="hero-sub">Four AI agents. Real papers. One brutal debate.</div>
    <div class="agent-row">
      <div class="agent-pill pill-optimist">🟢 &nbsp; Optimist</div>
      <div class="agent-pill pill-skeptic">🔴 &nbsp; Skeptic</div>
      <div class="agent-pill pill-devil">😈 &nbsp; Devil</div>
      <div class="agent-pill pill-summary">📊 &nbsp; Summarizer</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── INPUT + BUTTON ───────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    topic = st.text_input(
        "topic",
        placeholder="e.g. 'Can AI replace doctors?' or 'Does social media harm teens?'",
        key="topic_input"
    )

    start = st.button("⚔  ENTER THE WAR ROOM")

    if start and topic.strip():
        with st.spinner("Fetching papers from ArXiv & loading agents..."):
            from orchestrator import orchestratorAgent
            results = orchestratorAgent(topic.strip())
            st.session_state.debate_results = results
            st.session_state.debate_topic   = topic.strip()
            st.session_state.debate_ready   = True
        # ── Navigate straight to the Debate page ──
        st.switch_page("pages/debate.py")

    elif start and not topic.strip():
        st.markdown("""
        <div class="status-msg" style="border-color:#ff4466; color:#ff4466; background:rgba(255,68,102,0.05)">
            ⚠ &nbsp; Please enter a topic first
        </div>
        """, unsafe_allow_html=True)

# ── STATS ROW ───────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-item">
        <div class="stat-num">4</div>
        <div class="stat-label">AI Agents</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">25+</div>
        <div class="stat-label">Real Papers</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">0</div>
        <div class="stat-label">Hallucinations</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">$0</div>
        <div class="stat-label">Cost to Run</div>
    </div>
</div>
""", unsafe_allow_html=True)