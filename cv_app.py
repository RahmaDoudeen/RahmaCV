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
# 2. DESIGN SYSTEM (CSS)
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

    /* HEADERS & TYPOGRAPHY */
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
    
    /* MOBILE OPTIMIZATION */
    @media only screen and (max-width: 600px) {
        h1 { font-size: 1.8rem !important; text-align: center; }
        .role-title { font-size: 1.0rem !important; text-align: center; }
        .sub-header { font-size: 0.9rem !important; text-align: center; font-style: italic;}
        img { margin: 0 auto !important; width: 140px !important; }
    }

    /* SPECIFIC TITLE SIZES */
    .role-title {
        font-family: 'Lato', sans-serif; 
        color: #FB7185; /* Rose-Terracotta */
        font-size: 1.7rem; /* LARGER FONT */
        font-weight: 900; 
        letter-spacing: 3px;
        margin-top: 5px;
    }
    .sub-header {
        font-family: 'Playfair Display', serif;
        color: #38BDF8; /* Cyan Blue */
        font-size: 1.4rem; /* LARGER FONT */
        font-weight: 700;
        margin-top: 5px;
        font-style: italic;
    }

    /* GENERAL TEXT STYLING */
    h3 {
        font-family: 'Playfair Display', serif;
        color: #FFFFFF !important;
        border-bottom: 2px solid #F0C642;
        padding-bottom: 15px;
        margin-top: 60px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 1.8rem;
    }
    h4 {
        color: #F0C642 !important;
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 1.25rem !important;
        min-height: 4.5rem;
        line-height: 1.3 !important;
    }

    /* CARD STYLING */
    div[data-testid="column"] {
        background: rgba(20, 50, 40, 0.4); 
        border: 1px solid rgba(240, 198, 66, 0.15); 
        border-radius: 4px;
        padding: 25px;
        backdrop-filter: blur(5px);
    }
    .institution-text-card {
        color: #F0C642 !important; 
        font-size: 1.05rem;
        font-weight: 700;
    }
    .experience-institute {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem !important; 
        font-weight: 600;
        color: #22D3EE !important;
    }

    /* BUTTONS */
    .art-btn {
        display: block; width: 100%; background: linear-gradient(135deg, #BE123C 0%, #9F1239 100%); 
        color: white !important; padding: 14px; border-radius: 2px; font-weight: 700;
        text-transform: uppercase; font-size: 0.85rem; margin-top: 15px; border: 1px solid #BE123C;
    }
    
    .ver-btn {
        display: block; width: 100%; background: transparent; border: 1px solid #FB7185; 
        color: #FB7185 !important; padding: 10px; border-radius: 2px; font-size: 0.8rem;
        margin-top: 8px; text-transform: uppercase; font-weight: 600;
    }

    /* PROFILE PIC */
    img {
        border-radius: 50%;
        border: 4px solid #F0C642; 
        box-shadow: 0 0 40px rgba(34, 211, 238, 0.5), 0 0 15px rgba(240, 198, 66, 0.6);
        display: block;
        object-fit: cover;
    }

    /* FOOTER FONT */
    .footer-label {
        color: #FB7185 !important;
        font-size: 1.3rem !important; 
        font-weight: 900 !important;
    }
    .footer-text {
        color: #E2E8F0 !important;
        font-size: 1.15rem !important; 
    }

    /* HIDE UI */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .block-container { padding-top: 3rem; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. GLOBAL DATA (Content)
# -----------------------------------------------------------------------------
# Map Data setup
map_data = {
    "Region": ["North America", "Europe", "Middle East", "Oceania", "Global"],
    "lat": [45, 50, 31, -25, 0],
    "lon": [-100, 15, 36, 135, 0],
    "Hover_Text": [
        "<b>NORTH AMERICA:</b><br>• SNMMI<br>• ACNM<br>• ASNC<br>• SCCT<br>• ASCO<br>• ARRS<br>• CANM",
        "<b>EUROPE:</b><br>• EANM<br>• EACVI<br>• ESMO<br>• ESR<br>• BNMS",
        "<b>MIDDLE EAST:</b><br>• ARSNM<br>• Jordan Medical Assoc.",
        "<b>OCEANIA:</b><br>• ANZSNM",
        "<b>GLOBAL:</b><br>• WiN Global<br>• IC-OS<br>• SIIM"
    ]
}
df = pd.DataFrame(map_data)
# Plotly figure initialization is done in the section 

# -----------------------------------------------------------------------------
# 4. IDENTITY SECTION (CONTENT)
# -----------------------------------------------------------------------------
c_pic, c_text = st.columns([1.2, 3.8])

with c_pic:
    try:
        image = Image.open('profile_pic.png')
        st.image(image, width=230) 
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
    
    # CV Button (CENTERED)
    st.markdown(f'''<div style="text-align:center; width:100%;"><a href="{URL_FULL_CV}" target="_blank" class="art-btn" style="width:fit-content; padding: 12px 40px; background: #F0C642; color:#0F201B!important; border-color:#F0C642; font-weight:800; margin-top:25px; font-size:1rem;">📄 VIEW FULL CV</a></div>''', unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 5. TIER 1: BOARD CERTIFICATIONS (Pillars)
# -----------------------------------------------------------------------------
st.markdown("<h3>📜 Board Certifications</h3>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

def card_btn(url, text, style="primary"):
    cls = "art-btn" if style == "primary" else "ver-btn"
    return f'<a href="{url}" target="_blank" class="{cls}">{text}</a>'

with c1:
    st.markdown("#### European Fellowship in Nuclear Medicine (Hamburg, Germany)")
    st.markdown('<div class="institution-text-card">UEMS/EBNM (Hamburg, Germany)</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="institution-text-card">EACVI (Nuclear Cardiology)</div>', unsafe_allow_html=True)
    st.markdown("**Status: Fully Certified**")
    st.markdown(card_btn(URL_EACVI_CERT, "View Certificate"), unsafe_allow_html=True)
    st.markdown(card_btn(URL_EACVI_VERIFY, "Verification", "sec"), unsafe_allow_html=True)

with c4:
    st.markdown("#### Jordanian Board of Nuclear Medicine")
    st.markdown('<div class="institution-text-card">Jordanian Medical Council (JMC)</div>', unsafe_allow_html=True)
    st.markdown("**Status: Board Certified Specialist**")
    st.markdown(card_btn(URL_JORDAN_BOARD, "View Board Certificate"), unsafe_allow_html=True)
    st.markdown(card_btn(URL_JORDAN_LICENSE, "My Professional License", "sec"), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. TIER 2: CLINICAL EXPERIENCE
# -----------------------------------------------------------------------------
st.markdown("<h3>🏥 Clinical Experience & Residency</h3>", unsafe_allow_html=True)

e1, e2 = st.columns(2)

with e1:
    st.markdown("""
    <div class="exp-card">
        <div style="font-size:2rem; color:#FB7185;">🎓</div>
        <h4 style="margin-top:0;">Joint Nuclear Medicine Residency Program</h4>
        <p class="experience-institute">King Hussein Cancer Center (KHCC) & University of Jordan</p>
        <p>Comprehensive residency training covering theranostics, advanced oncological and general nuclear medicine.</p>
    </div>
    """, unsafe_allow_html=True)

with e2:
    st.markdown("""
    <div class="exp-card">
        <div style="font-size:2rem; color:#FB7185;">⚕️</div>
        <h4 style="margin-top:0;">Clinical Training in Nuclear Medicine</h4>
        <p class="experience-institute">National Center for Diabetes, Endocrinology and Genetics (NCDEG)</p>        
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# -----------------------------------------------------------------------------
# 7. TIER 3: GLOBAL MAP (Distributed Text)
# -----------------------------------------------------------------------------
st.markdown("<h3>🌍 Global Professional Affiliations</h3>", unsafe_allow_html=True)

list_col1, map_col, list_col2 = st.columns([1.2, 3.5, 1.2])

with list_col1:
    st.markdown("""
    <div style="background:rgba(0,0,0,0.2); padding:15px; border-radius:10px; border:1px solid #F0C642; margin-top:25px; height: 500px;">
    <p style="color:#F0C642; font-weight:bold; font-size:1.1rem;">AMERICA & EUROPE</p>
    <ul style="list-style-type: '🌿 '; padding-left: 20px; font-size: 1.05rem;">
        <li>SNMMI (Soc. of NM & MI)</li>
        <li>ACNM (Amer. College of NM)</li>
        <li>ASNC (Amer. Soc. of NC)</li>
        <li>EANM (European Assoc. of NM)</li>
        <li>BNMS (British NM Society)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with map_col:
    # Map Data
    lats = [45, 50, 31, -25, 0]
    lons = [-100, 15, 36, 135, 0]
    hover_txt = ["North America", "Europe", "Middle East", "Oceania", "Global"]

    fig = go.Figure(data=go.Scattergeo(
        lon = lons, lat = lats, text = hover_txt, mode = 'markers',
        marker = dict(size=25, color='#F0C642', line=dict(width=2, color='#22D3EE'))
    ))

    # 3D Globe Style
    fig.update_geos(
        projection_type="orthographic", showcountries=True, countrycolor="#555",
        showland=True, landcolor="#14332A", 
        showocean=True, oceancolor="#0F172A", 
        bgcolor="#0F172A"
    )
    fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#0F172A", font=dict(color="white"))

    st.plotly_chart(fig, use_container_width=True)

with list_col2:
    st.markdown("""
    <div style="background:rgba(0,0,0,0.2); padding:15px; border-radius:10px; border:1px solid #F0C642; margin-top:25px; height: 500px;">
    <p style="color:#F0C642; font-weight:bold; font-size:1.1rem;">MIDDLE EAST & GLOBAL</p>
    <ul style="list-style-type: '🌿 '; padding-left: 20px; font-size: 1.05rem;">
        <li>ARSNM (Arab Soc. of NM)</li>
        <li>JMA (Jordan Medical Assoc.)</li>
        <li>ANZSNM (Australia/NZ Soc.)</li>
        <li>WiN Global (Women in Nuclear)</li>
        <li>IC-OS (Cardio-Oncology Soc.)</li>
        <li>SIIM (Imaging Informatics)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 8. TIER 4: COMPETENCIES & HONORS
# -----------------------------------------------------------------------------
st.markdown("<h3>☢️ Clinical Competencies & Honors</h3>", unsafe_allow_html=True)
z1, z2, z3 = st.columns(3)

with z1:
    st.markdown("""
    <div class="exp-card">
    <div style="font-size:2rem; color:#FB7185;">🫀</div>
    <h4>Nuclear Cardiology</h4>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Modalities:</p>
    <ul>
    <li>Cardiac Amyloidosis & Sarcoidosis</li>
    <li>Myocardial Blood Flow (MBF) incl. F-18 PET</li>
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
    <div class="exp-card">
    <div style="font-size:2rem; color:#FB7185;">🧠</div>
    <h4>Nuclear Neurology</h4>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Modalities:</p>
    <ul>
    <li>Neuro-PET (Dementia/Epilepsy)</li>
    <li>DaTscan Imaging</li>
    <li>FDG-PET in Non-Alzheimer’s</li>
    <li>Amyloid PET/CT</li>
    </ul>
    <p style="color:#22D3EE; font-weight:bold; margin-bottom: 5px;">Software:</p>
    <ul>
    <li>MIMneuro™ SOFTWARE</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with z3:
    st.markdown("""
    <div class="exp-card">
    <div style="font-size:2rem; color:#FB7185;">🏆</div>
    <h4>Professional Honors & Society Involvement</h4>
    <ul>
    <li>ASNC Future Leaders Program: Selected as one of the "Next Generation of Nuclear Cardiology" leaders, Toronto, Canada</li>
    <li>Speaker & Faculty Member: Nuclear Cardiology Now Middle East Conference (ASNC)</li>
    <li>Grant Reviewer: 2025 SNMMI Molecular Imaging Research Grant for Junior Academic Faculty ($105,000 grant)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. FOOTER (Elegant)
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
        <div>ASNC International Committee & ACNM Radiopharmaceutical Therapy Committee.</div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div style="border-left:4px solid #F0C642; padding-left:15px;">
        <div class="footer-label">Publications 📚</div>
        <div>10+ Peer-Reviewed Articles, Abstracts, and Learning Modules (First Author/Co-Author).</div>
    </div>
    """, unsafe_allow_html=True)