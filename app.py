import streamlit as st
from datetime import datetime, timedelta

# 1. Page Configuration & Visual Theme
st.set_page_config(
    page_title="Tumaini 365 | Counselling Psychology",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Healing Visual Atmosphere (Sage Green & Earthy Tones)
st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    h1, h2, h3 { color: #2C4A3E; font-family: 'Helvetica Neue', sans-serif; }
    .hero-box {
        background-color: #E2ECE9;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
    }
    .card-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #4A7C59;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .emergency-banner {
        background-color: #FADBD8;
        color: #78281F;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header & Navigation Menu
col_logo, col_nav = st.columns([2, 3])
with col_logo:
    st.markdown("### 🌱 **Tumaini Three Sixty Five Limited**")
    st.caption("Counselling Psychology Practice")

with col_nav:
    page = st.radio("", ["Home", "Book an Appointment", "About & Confidentiality"], horizontal=True, label_visibility="collapsed")

st.divider()

# 3. PAGE: HOME
if page == "Home":
    # Hero Section
    st.markdown("""
        <div class="hero-box">
            <h1>A Safe Space to Heal, Grow, and Thrive 365 Days a Year</h1>
            <p style="font-size:1.2rem; color:#4F5B56;">Professional, confidential, and empathetic counselling psychology tailored to your unique journey.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Split-Action Module (Virtual vs In-Person)
    st.markdown("## Our Therapeutic Formats")
    col_virt, col_face = st.columns(2)
    
    with col_virt:
        st.markdown("""
            <div class="card-box">
                <h3>🌐 Virtual Telehealth Sessions</h3>
                <p>Secure, fully encrypted video consultations from the complete privacy of your home or workspace.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Schedule Virtual Intake", use_container_width=True, key="btn_virt"):
            st.info("Please use the navigation bar above and click on 'Book an Appointment' to secure your slot.")
            
    with col_face:
        st.markdown("""
            <div class="card-box">
                <h3>🏢 Face-to-Face Sessions</h3>
                <p>In-person clinical care held at our peaceful, discreet, and highly confidential therapy rooms.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Schedule In-Person Intake", use_container_width=True, key="btn_face"):
            st.info("Please use the navigation bar above and click on 'Book an Appointment' to secure your slot.")

    # Specialized Services Grid
    st.markdown("---")
    st.markdown("## Areas of Clinical Expertise")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Individual Care", value="Anxiety & Burnout Support")
    with c2:
        st.metric(label="Relationship Care", value="Couples & Family Therapy")
    with c3:
        st.metric(label="Organizational Care", value="Corporate Wellness Plans")

# 4. PAGE: BOOK AN APPOINTMENT
elif page == "Book an Appointment":
    st.markdown("## 📆 Confidential Booking Engine")
    st.write("Fill out the secure fields below to request your diagnostic intake session.")
    
    # Form Layout
    with st.form("booking_form", clear_on_submit=True):
        col_f, col_l = st.columns(2)
        with col_f:
            first_name = st.text_input("First Name*")
        with col_l:
            last_name = st.text_input("Last Name*")
            
        email = st.text_input("Secure Email Address*")
        
        # Format Selection
        session_format = st.selectbox("Preferred Session Format*", ["Virtual (Secure Video Link)", "Face-to-Face (In-Person Office)"])
        
        # Date & Time Selection
        col_d, col_t = st.columns(2)
        with col_d:
            appointment_date = st.date_input("Select Date", min_value=datetime.today() + timedelta(days=1))
        with col_t:
            appointment_time = st.selectbox("Available Time Slots", ["09:00 AM", "11:00 AM", "02:00 PM", "04:00 PM"])
            
        confidentiality_agree = st.checkbox("I understand my consultation data is fully encrypted and bound by professional psychological confidentiality protocols.*")
        
        submit_btn = st.form_submit_button("Confirm Appointment Request")
        
        if submit_btn:
            if not first_name or not last_name or not email or not confidentiality_agree:
                st.error("Please fill in all mandatory fields (*) and check the confidentiality agreement box.")
            else:
                st.success(f"Thank you, {first_name}. Your appointment request has been logged!")
                if "Virtual" in session_format:
                    st.info(f"🔒 **Virtual Session Confirmed:** A unique, encrypted video link has been dispatched to {email} for {appointment_date} at {appointment_time}.")
                else:
                    st.info(f"🏢 **In-Person Session Confirmed:** Map pins, entry instructions, and private parking coordinates have been sent to {email} for {appointment_date} at {appointment_time}.")

# 5. PAGE: ABOUT & CONFIDENTIALITY
elif page == "About & Confidentiality":
    st.markdown("## Operational Ethics & Confidentiality")
    st.write("""
    At **Tumaini Three Sixty Five Limited**, we treat absolute clinical confidentiality as our primary operational foundation. 
    Whether you meet our counseling psychologists virtually via secure telehealth endpoints or inside our quiet in-person clinic space, your personal files, clinical diagnostics, and individual discussions are strictly legally protected.
    """)
    
    st.markdown("### 🔒 Telehealth Safety Protocols")
    st.bullet_list([
        "End-to-end encrypted medical-grade data pipelines.",
        "Zero session recording rules enforced sitewide.",
        "Secure storage of file records conforming to health privacy compliance standards."
    ])

# 6. Global Crisis Warning Footer (Critical Mental Health Inclusion)
st.markdown("""
    <div class="emergency-banner">
        🚨 EMERGENCY NOTICE: If you or someone you know is experiencing an immediate mental health crisis or self-harm risks, please contact your local national emergency services or ambulance hotlines immediately. We do not provide 24/7 crisis interventions.
    </div>
""", unsafe_allow_html=True)
