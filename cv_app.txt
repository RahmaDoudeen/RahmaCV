import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import pandas as pd

# -----------------------------------------------------------------------------
# 1. CONFIGURATION (LINKS)
# -----------------------------------------------------------------------------
URL_FULL_CV = "https://drive.google.com/file/d/1d5LCtourYdfl9p8DVOUazQ-ujXO6Wlui/view?usp=drive_link" 
URL_EBNM_CERT = "https://drive.google.com/file/d/16GgpQUfCD224tQaeaANb5xJeVNbrEfd2/view?usp=drive_link"
URL_EBNM_VERIFY = "https://uems.eanm.org/commitees/fellowship-committee/ebnm-fellows/" 
URL_CBNC_CERT = "https://drive.google.com/file/d/1xa6w0kkShKW4O9D6juKX8l0I9owjpHdI/view?usp=drive_link"
URL_APCA_VERIFY = "https://www.apca.org/directory-of-registrants/" 
URL_EACVI_CERT = "https://drive.google.com/file/d/1BrIAQ-QpXh5CyKcbhPul5mjn4Tct-wZm/view?usp=drive_link"
URL_EACVI_VERIFY = "https://www.escardio.org/Education/Career-Development/Certification/certified-healthcare-professionals-in-imaging" 
URL_JORDAN_BOARD = "https://drive.google.com/file/d/1ABGIAeb2NJ6m_Eg03s46khF30f6aji9W/view?usp=drive_link"
URL_JORDAN_LICENSE = "https://drive.google.com/file/d/18Wd9dLfqa2MwPcgjN9l8jjEDYhFqrhtr/view?usp=drive_link"

# -----------------------------------------------------------------------------
# 2. DESIGN SYSTEM: "GENSLER BIO-NUCLEAR LUXURY"
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Dr. Rahma Doudeen", page_icon="🌿", layout="wide")

st.markdown("""
    <style>
    /* FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;800&family=Montserrat:wght@300;400;600;800&display=swap');

    /* BACKGROUND: Deep Botanical Forest Green */
    .stApp {
        background-color: #0F201B; 
        background-image: linear-gradient(170deg, #0A1A15 0%, #14332A 100%);
        color: #E8F5E9;
        font-family: 'Montserrat', sans-serif;
    }

    /* HEADERS: CHAMPAGNE GOLD */
    h1 {
        font-family: 'Playfair Display', serif;
        color: #F0C642 !important; /* Champagne Gold */
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 3.5rem !important;
        margin-bottom: 0px;
        line-height: 1.1;
        text-shadow: 0 0 25px rgba(240, 198, 66, 0.3);
    }
    
    /* ROLE TITLE (Cyan) */
    .role-title {
        font-family: 'Montserrat', sans-serif; 
        color: #22D3EE; /* Electric Cyan */
        font-size: 1.7rem; 
        font-weight: 900;
        letter-spacing: 3px;
        margin-top: 5px;
        text-transform: uppercase;
        text-shadow: 0 0 10px rgba(34, 211, 238, 0.3);
    }
    
    /* SUB-HEADER (Bold & Larger) */
    .sub-header {
        font-family: 'Playfair Display', serif;
        color: #E07A5F; /* Pink Terracotta (Warmth) */
        font-size: 1.5rem; 
        font-weight: 800;
        margin-top: 10px;
        font-style: italic;
    }

    /* SECTION DIVIDERS */
    h3 {
        font-family: 'Playfair Display', serif;
        color: #FFFFFF !important;
        border-bottom: 2px solid #F0C642;
        padding-bottom: 15px;
        margin-top: 60px;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 1.8rem;
    }

    /* CARD TITLES */
    h4 {
        color: #F0C642 !important;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 1.25rem !important;
        min-height: 4.5rem;
        line-height: 1.3 !important;
    }

    /* INSTITUTION NAMES (Bold & Clear) */
    .institution-text-card {
        color: #E07A5F !important; /* Pink Terracotta */
        font-size: 1.1rem;
        font-weight: 700;
    }
    
    /* EXPERIENCE INSTITUTION (Larger & Distinct) */
    .experience-institute {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem !important; 
        font-weight: 700;
        color: #22D3EE !important; /* Cyan */
        line-height: 1.4;
    }

    /* CARDS: ARCHITECTURAL GLASS */
    div[data-testid="column"] {
        background: rgba(20, 50, 40, 0.4); 
        border: 1px solid rgba(240, 198, 66, 0.15); 
        border-radius: 4px;
        padding: 25px;
        backdrop-filter: blur(5px);
    }

    /* BUTTONS: GOLD & CYAN PRIMARY */
    .art-btn {
        display: block; width: 100%; 
        background: linear-gradient(135deg, #F0C642 0%, #D9A800 100%); /* Gold */
        color: #0F201B !important; padding: 14px; border-radius: 4px; font-weight: 800;
        text-transform: uppercase; font-size: 0.85rem; margin-top: 15px; border: 1px solid #F0C642;
        text-decoration: none; text-align: center;
    }
    
    /* BUTTONS: VERIFICATION */
    .ver-btn {
        display: block; width: 100%; background: transparent; border: 1px solid #22D3EE; 
        color: #22D3EE !important; padding: 10px; border-radius: 4px; font-size: 0.8rem;
        margin-top: 8px; text-transform: uppercase; font-weight: 600; text-decoration: none; text-align: center;
    }

    /* FIX: PHOTO RADIATING HALO & POSITION */
    /* Forces image specifically inside Streamlit columns */
    div[data-testid="stImage"] img {
        border-radius: 50% !important;
        border: 4px solid #F0C642 !important; /* Gold Ring */
        /* Radiating Glow (Not pulsating, just strong static radiation) */
        box-shadow: 0 0 20px #22D3EE, 0 0 40px #22D3EE, 0 0 60px rgba(34, 211, 238, 0.4) !important;
        object-fit: cover !important;
        margin-top: 35px !important; /* Displace Downward */
    }

    /* GLOBAL LIST TEXT */
    .global-list {
        font-size: 0.95rem;
        color: #E8F5E9;
        line-height: 1.6;
    }
    .global-header {
        color: #F0C642;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 10px;
        border-bottom: 1px solid #22D3EE;
        padding-bottom: 5px;
    }
    
    /* FOOTER FONT - WAY LARGER */
    .footer-label {
        color: #FB7185 !important;
        font-size: 1.3rem !important; 
        font-weight: 900 !important;
    }
    .footer-text {
        color: #E2E8F0 !important;
        font-size: 1.15rem !important; 
    }

    /* MOBILE OPTIMIZATION */
    @media only screen and (max-width: 600px) {
        h1 { font-size: 1.8rem !important; text-align: center; }
        .role-title { font-size: 1.1rem !important; text-align: center; }
        .sub-header { font-size: 1.0rem !important; text-align: center; }
        /* Reset margins on mobile so it centers properly */
        div[data-testid="stImage"] img { margin: 0 auto !important; width: 160px !important; margin-top: 0px !important; }
        .experience-institute { font-size: 1.2rem !important; }
    }

    /* HIDE UI */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. IDENTITY SECTION (Photo Left, Text Right)
# -----------------------------------------------------------------------------
c_pic, c_text = st.columns([1.2, 3.8])

with c_pic:
    try:
        image = Image.open('profile_pic.png')
        # Scaled to fit nearby text
        st.image(image, width=220) 
    except:
        st.warning("⚠️ Add 'profile_pic.png'")

with c_text:
    st.markdown("<h1>Rahma M. Doudeen, MD, FEBNM, CBNC</h1>", unsafe_allow_html=True)
    st.markdown('<div class="role-title">Nuclear Medicine Physician</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Board Certified in Nuclear Medicine & Nuclear Cardiology</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 25px; color: #C1C7C5; font-size: 1.1rem; font-family: 'Montserrat', sans-serif;">
    📞 +962795050618 &nbsp;&nbsp; ✉️ rahma_doudeen@yahoo.com &nbsp;&nbsp; 📍 Amman, Jordan
    </div>
    """, unsafe_allow_html=True)
    
    # FIX: Button aligned to the LEFT (Removed "center" tags)
    st.markdown(f'<a href="{URL_FULL_CV}" target="_blank" class="art-btn" style="width:fit-content; padding: 12px 40px; background: #F0C642; color:#0F201B!important; border-color:#F0C642; font-weight:800; margin-top:25px; font-size:1rem;">📄 VIEW FULL CV</a>', unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 4. BOARD CERTIFICATIONS
# -----------------------------------------------------------------------------
st.markdown("<h3>📜 Board Certifications</h3>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

def card_btn(url, text, style="primary"):
    cls = "art-btn" if style == "primary" else "ver-btn"
    return f'<a href="{url}" target="_blank" class="{cls}">{text}</a>'

with c1:
    st.markdown("#### European Fellowship in Nuclear Medicine (Hamburg, Germany)")
    st.markdown('<div class="institution-text-card">UEMS/EBNM</div>', unsafe_allow_html=True)
    st.markdown("**Status: FEBNM Fellow**")
    st.markdown(card_btn(URL_EBNM_CERT, "View Fellowship Certificate"), unsafe_allow_html=True)
    st.markdown(card_btn(URL_EBNM_VERIFY, "Verification", "sec"), unsafe_allow_html=True)

with c2:
    st.markdown("#### Certification Board of Nuclear Cardiology (CBNC)")
    st.markdown('<div class="institution-text-card">American Board / APCA</div>', unsafe_allow_html=True)
    st.markdown("**Status: Diplomate**")
    st.markdown(card_btn(URL_CBNC_CERT, "View CBNC Certificate"), unsafe_allow_html=True)
    st.markdown(card_btn(URL_APCA_VERIFY, "Verification", "sec"), unsafe_allow_html=True)

with c3:
    st.markdown("#### European Board of Nuclear Cardiology")
    st.markdown('<div class="institution-text-card">EACVI Nuclear Cardiology Certification</div>', unsafe_allow_html=True)
    st.markdown("**Status: Fully Certified**")
    st.markdown(card_btn(URL_EACVI_CERT, "View Certificate"), unsafe_allow_html=True)
    st.markdown(card_btn(URL_EACVI_VERIFY, "Verification", "sec"), unsafe_allow_html=True)

with c4:
    st.markdown("#### Jordanian Board of Nuclear Medicine")
    st.markdown('<div class="institution-text-card">Jordanian Medical Council</div>', unsafe_allow_html=True)
    st.markdown("**Status: Board Certified Specialist**")
    st.markdown(card_btn(URL_JORDAN_BOARD, "View Board Certificate"), unsafe_allow_html=True)
    # FIX: Button is now Primary Style with text "Professional License"
    st.markdown(card_btn(URL_JORDAN_LICENSE, "Professional License"), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. CLINICAL EXPERIENCE
# -----------------------------------------------------------------------------
st.markdown("<h3>🏥 Clinical Experience & Residency</h3>", unsafe_allow_html=True)

e1, e2 = st.columns(2)

with e1:
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.03); padding:25px; border-radius:10px; border-left:4px solid #22D3EE; height:100%;">
        <div style="font-size:2rem;">🎓</div>
        <h4 style="margin-top:0;">Joint Nuclear Medicine Residency Program</h4>
        <p class="experience-institute">King Hussein Cancer Center (KHCC) & University of Jordan</p>
        <p>Comprehensive residency training covering theranostics, advanced oncological and general nuclear medicine.</p>
    </div>
    """, unsafe_allow_html=True)

with e2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.03); padding:25px; border-radius:10px; border-left:4px solid #22D3EE; height:100%;">
        <div style="font-size:2rem;">⚕️</div>
        <h4 style="margin-top:0;">Clinical Training in Nuclear Medicine</h4>
        <p class="experience-institute">National Center for Diabetes, Endocrinology and Genetics (NCDEG)</p>        
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 6. GLOBAL MAP (Pinned Associations)
# -----------------------------------------------------------------------------
st.markdown("<h3>🌍 Global Professional Memberships</h3>", unsafe_allow_html=True)

list_col1, map_col, list_col2 = st.columns([1.5, 3, 1.5])

# FIX: Added coordinates for ALL associations to populate the globe
lats = [38.9, 48.2, 31.9, -35.3, 51.5, 45.4, 46.2, 39.0] 
lons = [-77.0, 16.3, 35.9, 149.1, -0.1, -75.7, 6.1, -77.4]
hover_txt = [
    "<b>USA:</b> SNMMI, ACNM, ASNC, SCCT, ASCO, ARRS",
    "<b>EUROPE:</b> EANM, EACVI, ESMO, ESR",
    "<b>JORDAN/ME:</b> ARSNM, JMA",
    "<b>OCEANIA:</b> ANZSNM",
    "<b>UK:</b> BNMS",
    "<b>CANADA:</b> CANM",
    "<b>GLOBAL:</b> WiN Global, IC-OS",
    "<b>INFORMATICS:</b> SIIM"
]

fig = go.Figure(data=go.Scattergeo(
    lon = lons, lat = lats, text = hover_txt, mode = 'markers',
    marker = dict(size=15, color='#F0C642', line=dict(width=2, color='#22D3EE'))
))

fig.update_geos(
    projection_type="orthographic", showcountries=True, countrycolor="#555",
    showland=True, landcolor="#14332A", 
    showocean=True, oceancolor="#0F201B", 
    bgcolor="#0F201B"
)
fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#0F201B", font=dict(color="white"))

# List 1 (North America & Europe)
with list_col1:
    st.markdown("""
    <div style="background:rgba(0,0,0,0.2); padding:15px; border-radius:10px; border:1px solid #F0C642; margin-top:25px;">
    <div class="global-header">North America & Europe</div>
    <div class="global-list">
    • Society of Nuclear Medicine and Molecular Imaging (SNMMI)<br>
    • American College of Nuclear Medicine (ACNM)<br>    
    • American Society of Nuclear Cardiology (ASNC)<br>    
    • Society of Cardiovascular Computed Tomography (SCCT)<br>
    • American Society of Clinical Oncology (ASCO)<br>
    • American Roentgen Ray Society (ARRS)<br>
    • The Canadian Association of Nuclear Medicine (CANM)<br>
    <hr style="border-color:#22D3EE;">
    • European Association of Nuclear Medicine (EANM)<br>
    • European Association of Cardiovascular Imaging (EACVI)<br>
    • European Society for Medical Oncology (ESMO)<br>
    • European Society of Radiology (ESR)<br>
    • British Nuclear Medicine Society (BNMS)<br>
    </div>
    </div>
    """, unsafe_allow_html=True)

with map_col:
    st.plotly_chart(fig, use_container_width=True)

# List 2 (Middle East & Global)
with list_col2:
    st.markdown("""
    <div style="background:rgba(0,0,0,0.2); padding:15px; border-radius:10px; border:1px solid #F0C642; margin-top:25px;">
    <div class="global-header">MIDDLE EAST & GLOBAL</div>
    <div class="global-list">
    • Arab Society of Nuclear Medicine (ARSNM)<br>
    • Jordan Medical Association<br>
    <hr style="border-color:#22D3EE;">
    • Australian and New Zealand Society of Nuclear Medicine (ANZSNM)<br>
    <hr style="border-color:#22D3EE;">
    • Women in Nuclear Global (WiN Global)<br>
    • International Cardio-Oncology Society (IC-OS)<br>
    • Society for Imaging Informatics in Medicine (SIIM)<br>
    </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. COMPETENCIES & HONORS
# -----------------------------------------------------------------------------
st.markdown("<h3>☢️ Clinical Competencies & Hands-On Training</h3>", unsafe_allow_html=True)
z1, z2, z3 = st.columns(3)

with z1:
    st.markdown("""
    <div style="background:rgba(20,50,40,0.4); padding:25px; border-radius:4px; border-left:4px solid #22D3EE; height:100%;">
    <div style="font-size:2rem; color:#FB7185;">🫀</div>
    <h4>Nuclear Cardiology</h4>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Diagnostic Application and Modalities:</p>
    <ul>
    <li>Cardiac Amyloidosis</li>
    <li>Cardiac Sarcoidosis</li>
    <li>Myocardial Blood Flow (MBF) including F-18 myocardial perfusion PET</li>
    <li>D-SPECT</li>
    </ul>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Software:</p>
    <ul>
    <li>Cedars-Sinai - The Cardiac Suite Utilized</li>
    <li>Emory Toolbox Software Utilized</li>
    <li>4DM by INVIA Utilized</li>
    <li>ImagenQ by CVIT Software Utilized</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with z2:
    st.markdown("""
    <div style="background:rgba(20,50,40,0.4); padding:25px; border-radius:4px; border-left:4px solid #22D3EE; height:100%;">
    <div style="font-size:2rem; color:#FB7185;">🧠</div>
    <h4>Nuclear Neurology</h4>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Diagnostic Application and Modalities:</p>
    <ul>
    <li>Neuro-PET (Dementia/Epilepsy)</li>
    <li>DaTscan Imaging</li>
    <li>FDG-PET in Non-Alzheimer’s Dementia</li>
    <li>FDG-PET/CT in Dementia</li>
    <li>FDG-PET/CT in Temporal Lobe Epilepsy</li>
    <li>Amyloid PET/CT Imaging in Dementia</li>
    </ul>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Software:</p>
    <ul>
    <li>MIMneuro™ SOFTWARE</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with z3:
    st.markdown("""
    <div style="background:rgba(20,50,40,0.4); padding:25px; border-radius:4px; border-left:4px solid #22D3EE; height:100%;">
    <div style="font-size:2rem; color:#FB7185;">🏆</div>
    <h4>Professional Honors & Society Involvement</h4>
    <ul>
    <li><b>ASNC Future Leaders Program:</b> Selected as one of the "Next Generation of Nuclear Cardiology" carefully selected individuals, Toronto, Canada.</li><br>
    <li><b>Speaker & Faculty Member:</b> Nuclear Cardiology Now: Middle East Conference, American Society of Nuclear Cardiology (ASNC).</li><br>
    <li><b>Grant Reviewer:</b> 2025 SNMMI Molecular Imaging Research Grant for Junior Academic Faculty ($105,000 grant).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 8. FOOTER
# -----------------------------------------------------------------------------
st.write("---")
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div style="border-left:4px solid #F0C642; padding-left:15px;">
        <div class="footer-label">Editorial Role 📝</div>
        <div class="footer-text">Reviewer for high-impact journals including Journal of Clinical Oncology (JCO) (Q1, 43.4 IF).</div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div style="border-left:4px solid #F0C642; padding-left:15px;">
        <div class="footer-label">Committee Membership 🤝</div>
        <div class="footer-text">ASNC International Committee & ACNM Radiopharmaceutical Therapy Committee.</div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div style="border-left:4px solid #F0C642; padding-left:15px;">
        <div class="footer-label">Publications 📚</div>
        <div class="footer-text">10+ Peer-Reviewed Articles, Abstracts, and Learning Modules (First Author/Co-Author).</div>
    </div>
    """, unsafe_allow_html=True)