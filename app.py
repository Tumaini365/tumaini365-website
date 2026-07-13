import streamlit as st

# 1. Page Configuration & Brand Styling
st.set_page_config(
    page_title="Tumaini 365 | Counselling Psychology",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS injecting the brand color palette (Sage Green, Sand, Slate Blue)
st.markdown("""
    <style>
    /* Main Background & Typography colors */
    .stApp { background-color: #F5EBE6; } /* Soft Earthy Sand Background */
    h1, h2, h3 { color: #4A7C59 !important; font-family: 'Georgia', serif; } /* Calming Sage Green Headers */
    p, label, span { color: #333333 !important; }
    
    /* Custom Components Visual Styling */
    .hero-box {
        background-color: #4A7C59;
        padding: 45px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero-box h1 { color: #FFFFFF !important; }
    .hero-box p { color: #F5EBE6 !important; }
    
    .card-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        border-top: 6px solid #6B8E23; /* Gentle Slate Olive Blue Anchor */
        box-shadow: 0 5px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    
    .emergency-banner {
        background-color: #FADBD8;
        color: #78281F !important;
        padding: 18px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        margin-top: 40px;
        border: 1px solid #E6B0AA;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Navigation Header Matrix (Fixed by adding column count)
col_logo, col_nav = st.columns(2)
with col_logo:
    st.markdown("### 🌱 **Tumaini Three Sixty Five Limited**")
    st.caption("Professional Counselling Psychology Practice")

with col_nav:
    page = st.radio("", ["Home", "Book an Appointment", "About & Confidentiality"], horizontal=True, label_visibility="collapsed")

st.divider()

# TARGET INBOX EMAIL CONFIGURATION
TARGET_EMAIL = "tumaini365ltd@gmail.com"

# 3. PAGE VIEW: HOME
if page == "Home":
    st.markdown("""
        <div class="hero-box">
            <h1>A Safe Space to Heal, Grow, and Thrive 365 Days a Year</h1>
            <p style="font-size:1.25rem;">Confidential and empathetic counselling psychology tailored for individuals, couples, and corporate institutions.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Our Therapeutic Formats")
    col_v, col_f = st.columns(2)
    
    with col_v:
        st.markdown("""
            <div class="card-box">
                <h3>🌐 Virtual Telehealth Sessions</h3>
                <p>Secure, fully encrypted video sessions accessible from the total privacy of your home or private workspace.</p>
            </div>
        """, unsafe_allow_html=True)
            
    with col_f:
        st.markdown("""
            <div class="card-box">
                <h3>🏢 Face-to-Face Sessions</h3>
                <p>In-person clinical appointments hosted inside our quiet, warm, and highly discreet consulting offices.</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("## Areas of Clinical Expertise")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card-box'><h4>Individual Care</h4><p>Anxiety management, burnout recovery, depression therapy, and lifestyle adjustment transitions.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card-box'><h4>Relationship Care</h4><p>Couples counseling, family rebuilding frameworks, and healthy communication skills.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card-box'><h4>Corporate Wellness</h4><p>Workplace mental health design workshops, leadership trauma training, and staff care plans.</p></div>", unsafe_allow_html=True)

# 4. PAGE VIEW: BOOK AN APPOINTMENT
elif page == "Book an Appointment":
    st.markdown("## 📆 Secure Booking Engine")
    st.write("Please fill out your consultation details. Submitting this form routes data straight to our practice desk securely.")
    
    contact_form_html = f"""
    <form action="https://formsubmit.co{TARGET_EMAIL}" method="POST" style="background-color: #FFFFFF; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
        <input type="hidden" name="_replyto" value="%email%">
        <input type="hidden" name="_subject" value="New Tumaini 365 Booking Request!">
        <input type="hidden" name="_honeypot" style="display:none">
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight:bold; display:block; margin-bottom:5px;">Full Client Name *</label>
            <input type="text" name="name" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" required>
        </div>
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight:bold; display:block; margin-bottom:5px;">Your Secure Email Address *</label>
            <input type="email" name="email" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" required>
        </div>
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight:bold; display:block; margin-bottom:5px;">Preferred Session Format *</label>
            <select name="format" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" required>
                <option value="Virtual (Secure Zoom/Meet Link)">Virtual (Secure Zoom/Meet Link)</option>
                <option value="Face-to-Face (In-Person Office)">Face-to-Face (In-Person Office)</option>
            </select>
        </div>
        
        <div style="margin-bottom: 20px;">
            <label style="font-weight:bold; display:block; margin-bottom:5px;">Preferred Appointment Date & Time *</label>
            <input type="text" name="datetime" placeholder="e.g., Next Tuesday at 2:00 PM" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" required>
        </div>
        
        <div style="margin-bottom: 20px;">
            <input type="checkbox" required> <span style="font-size:0.9rem; color:#555;">I confirm I am requesting a confidential clinical intake appointment.</span>
        </div>
        
        <button type="submit" style="background-color: #4A7C59; color: white; padding: 12px 24px; border: none; border-radius: 6px; cursor: pointer; font-size: 1rem; width: 100%;">
            Submit Secure Request
        </button>
    </form>
    """
    st.components.v1.html(contact_form_html, height=520, scrolling=False)

# 5. PAGE VIEW: ABOUT & CONFIDENTIALITY
elif page == "About & Confidentiality":
    st.markdown("## Operational Ethics & Trust Matrix")
    st.markdown("""
    <div class="card-box">
        <p>At <b>Tumaini Three Sixty Five Limited</b>, we process clinical confidentiality protocols as our highest priority structure. 
        Whether you interface with our practicing counseling psychologists online via video endpoints or directly at our physical rooms, your file notes, treatment strategies, and discussions are protected under medical record custody provisions.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. Critical Emergency Clinical Notice Block
st.markdown("""
    <div class="emergency-banner">
        🚨 EMERGENCY NOTICE: If you are experiencing a severe mental health crisis or immediate self-harm emergency, please contact your local community public health authorities or national helplines instantly. We do not operate a 24/7 emergency dispatch response desk.
    </div>
""", unsafe_allow_html=True)
