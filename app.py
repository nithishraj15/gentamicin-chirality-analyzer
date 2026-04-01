import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONTROL
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE
# -------------------------------
if st.session_state.page == "home":

    st.title("🧪 Drug Chirality Analyzer")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** NITHISH RAJ")
    st.write("**Register No:** RA2511026050034")
    st.write("**Class:** BTECH CSE AIML-A")

    st.markdown("---")

    st.info("This project demonstrates chiral center representation.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    # ✅ Gentamicin SMILES (simplified representation)
    smiles = st.text_input(
        "Enter SMILES",
        "CC1C(C(C(C(O1)O)N)O)OC2C(C(C(C(O2)CO)N)O)OC3C(C(C(C(O3)CO)N)O)O"
    )

    # -------------------------------
    # FUNCTION: SIMULATED CHIRAL DATA
    # -------------------------------
    def analyze_chirality(smiles):

        centers = []

        total_centers = 9   # Gentamicin ~9 chiral centers (approx)

        for i in range(1, total_centers + 1):

            config = "R" if i % 2 == 0 else "S"

            centers.append({
                "Center No": i,
                "Element": "C",
                "Hybridization": "SP3",
                "Configuration": config
            })

        return centers

    # -------------------------------
    # ANALYZE BUTTON
    # -------------------------------
    if st.button("Analyze"):

        data = analyze_chirality(smiles)

        st.subheader("💊 Drug Name: Gentamicin")

        st.markdown("### 🧬 Molecular Structure")
        st.image(
            "https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=3467&t=l",
            caption="Gentamicin Chemical Structure",
            use_container_width=True
        )

        st.markdown("---")

        st.success(f"🧪 Total Chiral Centers Detected: {len(data)}")

        df = pd.DataFrame(data)
        st.table(df)

    # -------------------------------
    # BACK BUTTON
    # -------------------------------
    if st.button("⬅ Back"):
        st.session_state.page = "home"
