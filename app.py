import streamlit as st
import pandas as pd
import os
from datetime import datetime

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
    .stApp { background-color: #F5EBE6; } 
    h1, h2, h3, h4 { color: #4A7C59 !important; font-family: 'Georgia', serif; } 
    p, label, span { color: #333333 !important; }
    
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
        border-top: 6px solid #6B8E23; 
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
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. FILE DATABASE SETUP (Permanent File Storage Solution)
DB_FILE = "bookings.csv"

def load_permanent_bookings():
    """Loads bookings from the file or creates an empty database table structure if missing."""
    if os.path.exists(DB_FILE):
        try:
            return pd.read_csv(DB_FILE).to_dict(orient="records")
        except Exception:
            return []
    return []

def save_permanent_booking(booking_entry):
    """Appends a new client entry permanently into the CSV storage file."""
    bookings = load_permanent_bookings()
    bookings.append(booking_entry)
    df = pd.DataFrame(bookings)
    df.to_csv(DB_FILE, index=False)

# Load existing bookings into local runtime memory context
current_bookings = load_permanent_bookings()

# 3. Navigation Header Matrix
col_logo, col_nav = st.columns(2)
with col_logo:
    st.markdown("### 🌱 **Tumaini Three Sixty Five Limited**")
    st.caption("Professional Counselling Psychology Practice")

with col_nav:
    page = st.radio("", ["Home", "Book an Appointment", "About & Confidentiality", "🔒 Practice Dashboard"], horizontal=True, label_visibility="collapsed")

st.divider()

# 4. PAGE VIEW: HOME
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

# 5. PAGE VIEW: BOOK AN APPOINTMENT
elif page == "Book an Appointment":
    st.markdown("## 📆 Secure Booking Engine")
    st.write("Please fill out your consultation details below to request your intake session.")
    
    with st.form("native_booking_form", clear_on_submit=True):
        client_name = st.text_input("Full Client Name *")
        client_email = st.text_input("Your Secure Email Address *")
        session_format = st.selectbox("Preferred Session Format *", ["Virtual (Secure Video Link)", "Face-to-Face (In-Person Office)"])
        booking_time = st.text_input("Preferred Appointment Date & Time *", placeholder="e.g., Next Tuesday at 2:00 PM")
        consent = st.checkbox("I confirm I am requesting a confidential clinical intake appointment.*")
        
        submit_button = st.form_submit_button("Submit Secure Request")
        
        if submit_button:
            if not client_name or not client_email or not booking_time or not consent:
                st.error("Please fill out all required fields marked with an asterisk (*).")
            else:
                new_booking = {
                    "Submission Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Client Name": client_name,
                    "Client Email": client_email,
                    "Format": session_format,
                    "Requested Date/Time": booking_time
                }
                save_permanent_booking(new_booking)
                st.success("🎉 Your appointment request has been securely locked into our system! Our clinical desk will reach out to you via email.")

# 6. PAGE VIEW: ABOUT & CONFIDENTIALITY
elif page == "About & Confidentiality":
    st.markdown("## Operational Ethics & Trust Matrix")
    st.markdown("""
    <div class="card-box">
        <p>At <b>Tumaini Three Sixty Five Limited</b>, we process clinical confidentiality protocols as our highest priority structure. 
        Whether you interface with our practicing counseling psychologists online via video endpoints or directly at our physical rooms, your file notes, treatment strategies, and discussions are protected under medical record custody provisions.</p>
    </div>
    """, unsafe_allow_html=True)

# 7. PRIVATE DASHBOARD PAGE (With Password Protection Screen)
elif page == "🔒 Practice Dashboard":
    st.markdown("## 🔒 Internal Practice Administration Dashboard")
    
    password_input = st.text_input("Enter Practice Admin Password to Unlock Client Log", type="password")
    
    if password_input == "tumaini365":
        st.success("Access Granted.")
        st.write("Intake records below are safely preserved in the file system across sessions.")
        
        if len(current_bookings) == 0:
            st.info("No appointment requests have been logged yet.")
        else:
            st.markdown("### Permanent Appointment Log")
            df = pd.DataFrame(current_bookings)
            st.dataframe(df, use_container_width=True)
            
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Log as CSV (Excel Spreadsheet)",
                data=csv_data,
                file_name=f"tumaini365_bookings_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )
            
            st.markdown("---")
            if st.button("Clear All System Bookings Permanently"):
                if os.path.exists(DB_FILE):
                    os.remove(DB_FILE)
                st.rerun()
    elif password_input != "":
        st.error("Incorrect Administration Password. Access Denied.")

# 8. Critical Emergency Clinical Notice Block (Updated with your custom contacts)
st.markdown("""
    <div class="emergency-banner">
        🚨 EMERGENCY NOTICE: If you are experiencing a severe mental health crisis, urgent trauma, or immediate risk of self-harm, please contact our emergency response crisis lines instantly at 📞 <b>0720 545 788</b> or 📞 <b>0754 828 766</b>, or reach out to your nearest community public health hospital.
    </div>
""", unsafe_allow_html=True)
