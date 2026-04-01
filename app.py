import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# App configuration
st.set_page_config(page_title="Brucine Chirality Analyzer", page_icon="🧪", layout="centered")

st.title("🧪 Brucine Chirality Analyzer")

# Student Details
st.markdown("""
### 👨‍🎓 Student Details
**NAME:** NALLA HARI HARA KRISHNA  
**REGISTER NUMBER:** RA2511026050036
""")

st.markdown("Welcome to the **Brucine Chirality Analyzer**! This educational web app calculates and identifies all chiral centers in the chemical compound **Brucine**.")
st.markdown("---")

st.header("🧬 Compound: Brucine")

# Hardcoded Brucine SMILES
BRUCINE_SMILES = "COC1=C(C=C2C(=C1)[C@]34CCN5[C@H]3C[C@@H]6[C@@H]7[C@@H]4N2C(=O)C[C@@H]7OCC=C6C5)OC"

st.subheader("SMILES String")
st.code(BRUCINE_SMILES, language="text")

# Initialize and process molecule
mol = Chem.MolFromSmiles(BRUCINE_SMILES)

if mol is None:
    st.error("🚨 Error: Invalid SMILES string. Could not generate the molecule.")
else:
    # 1. Add hydrogens properly
    mol = Chem.AddHs(mol)
    
    # 2. Assign stereochemistry properly
    Chem.AssignStereochemistry(mol, cleanIt=True, force=True, flagPossibleStereoCenters=True)
    
    # 3. Detect all chiral centers
    # includeUnassigned=True ensures we catch potential centers lacking distinct R/S
    chiral_centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
    
    st.subheader("🔍 Chiral Analysis Results")
    st.success(f"**Total number of chiral centers detected:** `{len(chiral_centers)}`")
    
    if len(chiral_centers) > 0:
        st.markdown("### 📋 List of Chiral Centers")
        
        # Display format as a table structure
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Atom Index**")
        with col2:
            st.markdown("**R/S Configuration**")
            
        st.markdown("---")
            
        for atom_idx, config in chiral_centers:
            # Handle unassigned cases gracefully
            config_label = config if config != "?" else "Unassigned"
            
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"`{atom_idx}`")
            with c2:
                # Add a little emoji based on R or S (optional visual touch)
                if config == "R":
                    st.write(f"🔄 **{config_label}**")
                elif config == "S":
                    st.write(f"🔁 **{config_label}**")
                else:
                    st.write(f"❓ **{config_label}**")
    else:
        st.info("No chiral centers were detected in this molecule.")

    st.markdown("---")
    st.subheader("🖼️ Molecular Structure representation")
    try:
        mol_image = Draw.MolToImage(mol, size=(500, 500))
        st.image(mol_image, caption="Brucine Chemical Structure (with Hydrogens)", use_container_width=False)
    except Exception as e:
        st.warning("⚠️ Could not generate the 2D molecule image.")

st.markdown("---")
st.caption("👨‍🔬 Built with 🎈 Streamlit and 🧩 RDKit for Chemistry Education.")
