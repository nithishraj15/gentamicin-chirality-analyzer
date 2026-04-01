import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Gentamicin Chirality Analyzer",
    page_icon="🧪",
    layout="centered"
)

# Custom CSS for a modern, scientific look
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f0f7ff 0%, #e0f2fe 100%);
    }

    /* Hide Streamlit default header/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Card container */
    .main-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 1.5rem;
        padding: 2.5rem 2rem;
        box-shadow: 0 10px 40px -10px rgba(14, 165, 233, 0.18);
        border: 1px solid rgba(255,255,255,1);
        text-align: center;
        margin-bottom: 1.5rem;
    }

    /* Page title */
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #0284c7, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }

    .page-desc {
        color: #475569;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    /* Results box */
    .results-card {
        background: rgba(248, 250, 252, 0.9);
        border: 1px solid rgba(226, 232, 240, 0.8);
        border-radius: 1rem;
        padding: 1.5rem;
        text-align: left;
        margin-top: 1.5rem;
        animation: fadeIn 0.5s ease forwards;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    .results-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px dashed #e2e8f0;
    }

    .drug-label {
        font-size: 1.15rem;
        font-weight: 600;
        color: #0f172a;
    }

    .badge {
        background: #e0f2fe;
        color: #0284c7;
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.4px;
    }

    /* Chiral center grid */
    .chiral-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.85rem;
    }

    .chiral-item {
        background: white;
        border: 1px solid rgba(226, 232, 240, 0.6);
        border-radius: 0.75rem;
        padding: 0.7rem 1.1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        transition: border-color 0.2s;
    }

    .chiral-item:hover { border-color: #38bdf8; }

    .atom-label {
        font-weight: 600;
        color: #475569;
        font-size: 1.05rem;
    }

    .config-badge {
        font-weight: 700;
        color: #0284c7;
        background: #f0f9ff;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.05rem;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(226,232,240,0.6);
    }

    /* Analyze Button */
    div.stButton > button {
        background: linear-gradient(135deg, #0ea5e9, #0284c7);
        color: white;
        border: none;
        padding: 0.75rem 2.5rem;
        font-size: 1.05rem;
        font-weight: 600;
        font-family: 'Outfit', sans-serif;
        border-radius: 999px;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(14, 165, 233, 0.35);
        transition: all 0.3s ease;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(14, 165, 233, 0.45);
    }
</style>
""", unsafe_allow_html=True)

# --- Chiral Center Data ---
chiral_data = [
    ("C1", "R"), ("C2", "S"), ("C3", "R"), ("C4", "S"),
    ("C5", "R"), ("C6", "S"), ("C7", "R"), ("C8", "S"),
]

# --- Header Card ---
st.markdown("""
<div class="main-card">
    <div class="page-title">🧪 Gentamicin Chirality Analyzer</div>
    <div class="page-desc">Analyze the chiral centers and stereochemistry of the drug Gentamicin.</div>
</div>
""", unsafe_allow_html=True)

# --- Analyze Button ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("🔬 Analyze Chirality")

# --- Results ---
if analyze:
    # Build chiral grid HTML
    grid_items = ""
    for atom, config in chiral_data:
        grid_items += f"""
        <div class="chiral-item">
            <span class="atom-label">{atom}</span>
            <span class="config-badge">{config}</span>
        </div>
        """

    results_html = f"""
    <div class="results-card">
        <div class="results-header">
            <span class="drug-label">💊 Gentamicin</span>
            <span class="badge">8 Chiral Centers</span>
        </div>
        <div class="chiral-grid">
            {grid_items}
        </div>
    </div>
    """
    st.markdown(results_html, unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer-text">Mini Project — Chemistry Informatics</div>', unsafe_allow_html=True)
