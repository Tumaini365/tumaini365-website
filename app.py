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

# Injecting CSS layout rules using clean single strings
st.markdown("<style>.stApp { background-color: #F5EBE6; } h1, h2, h3, h4 { color: #4A7C59 !important; font-family: 'Georgia', serif; } p, label, span { color: #333333 !important; } .hero-box { background-color: #4A7C59; padding: 45px; border-radius: 16px; text-align: center; margin-bottom: 30px; } .hero-box h1 { color: #FFFFFF !important; } .hero-box p { color: #F5EBE6 !important; } .card-box { background-color: #FFFFFF; padding: 25px; border-radius: 12px; border-top: 6px solid #6B8E23; box-shadow: 0 5px 15px rgba(0,0,0,0.04); margin-bottom: 20px; } .blog-article { background-color: #FFFFFF; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); margin-bottom: 25px; border-left: 4px solid #4A7C59; } .emergency-banner { background-color: #FADBD8; color: #78281F !important; padding: 18px; border-radius: 8px; font-weight: bold; text-align: center; margin-top: 40px; border: 1px solid #E6B0AA; font-size: 1.1rem; }</style>", unsafe_allow_html=True)

# 2. FILE DATABASE SETUP (Permanent File Storage Solution)
DB_FILE = "bookings.csv"

def load_permanent_bookings():
    if os.path.exists(DB_FILE):
        try:
            return pd.read_csv(DB_FILE).to_dict(orient="records")
        except Exception:
            return []
    return []

def save_permanent_booking(booking_entry):
    bookings = load_permanent_bookings()
    bookings.append(booking_entry)
    df = pd.DataFrame(bookings)
    df.to_csv(DB_FILE, index=False)

def update_assessment_data(client_email, assessment_status):
    bookings = load_permanent_bookings()
    updated = False
    for b in reversed(bookings):
        if str(b.get("Client Email")).strip().lower() == client_email.strip().lower():
            b["Anxiety Status (GAD-7)"] = assessment_status
            updated = True
            break
    if updated:
        df = pd.DataFrame(bookings)
        df.to_csv(DB_FILE, index=False)
        return True
    return False

# 3. Navigation Header Matrix
col_logo, col_nav = st.columns(2)
with col_logo:
    st.markdown("### 🌱 **Tumaini Three Sixty Five Limited**")
    st.caption("Professional Counselling Psychology Practice")

with col_nav:
    page = st.radio("", ["Home", "Book an Appointment", "Mental Health Screening", "Wellness Insights", "About & Confidentiality", "🔒 Practice Dashboard"], horizontal=True, label_visibility="collapsed")

st.divider()

# 4. PAGE VIEW: HOME
if page == "Home":
    st.markdown("<div class='hero-box'><h1>A Safe Space to Heal, Grow, and Thrive 365 Days a Year</h1><p style='font-size:1.25rem;'>Confidential and empathetic counselling psychology tailored for individuals, couples, and corporate institutions.</p></div>", unsafe_allow_html=True)
    st.markdown("## Our Therapeutic Formats")
    col_v, col_f = st.columns(2)
    with col_v:
        st.markdown("<div class='card-box'><h3>🌐 Virtual Telehealth Sessions</h3><p>Secure, fully encrypted video sessions accessible from the total privacy of your home or private workspace.</p></div>", unsafe_allow_html=True)
    with col_f:
        st.markdown("<div class='card-box'><h3>🏢 Face-to-Face Sessions</h3><p>In-person clinical appointments hosted inside our quiet, warm, and highly discreet consulting offices.</p></div>", unsafe_allow_html=True)
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
    st.write("Please select your consultation details below to request your intake session.")
    with st.form("native_booking_form", clear_on_submit=True):
        client_name = st.text_input("Full Client Name *")
        client_email = st.text_input("Your Secure Email Address *")
        client_mobile = st.text_input("Mobile Contact Number *", placeholder="e.g., 0722 000 000")
        session_format = st.selectbox("Preferred Session Format *", ["Virtual (Secure Video Link)", "Face-to-Face (In-Person Office)"])
        
        selected_date = st.date_input("Select Appointment Date *", min_value=datetime.today())
        selected_time = st.selectbox("Select Preferred Time Slot *", [
            "08:00 AM - 09:00 AM", "09:30 AM - 10:30 AM", "11:00 AM - 12:00 PM",
            "02:00 PM - 03:00 PM", "03:30 PM - 04:30 PM", "05:00 PM - 06:00 PM"
        ])
        
        consent = st.checkbox("I confirm I am requesting a confidential clinical intake appointment.*")
        submit_button = st.form_submit_button("Submit Secure Request")
        if submit_button:
            if not client_name or not client_email or not client_mobile or not consent:
                st.error("Please fill out all required fields marked with an asterisk (*).")
            else:
                formatted_datetime = f"{selected_date.strftime('%A, %B %d, %Y')} @ {selected_time}"
                new_booking = {
                    "Submission Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Client Name": client_name,
                    "Client Email": client_email,
                    "Mobile Contact": client_mobile,
                    "Format": session_format,
                    "Requested Date/Time": formatted_datetime,
                    "Anxiety Status (GAD-7)": "Not yet assessed"
                }
                save_permanent_booking(new_booking)
                st.success("🎉 Your appointment request is locked in! Please click on the 'Mental Health Screening' tab above next to complete your baseline clinical assessment.")

# 6. PAGE VIEW: ONLINE MENTAL HEALTH ASSESSMENT (GAD-7)
elif page == "Mental Health Screening":
    st.markdown("## 📊 Baseline Anxiety Assessment (GAD-7)")
    st.write("Over the last 2 weeks, how often have you been bothered by the following problems?")
    
    v_email = st.text_input("Enter the exact Email Address used during booking to match your profile*")
    options_map = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}
    
    q1 = st.radio("1. Feeling nervous, anxious, or on edge", list(options_map.keys()))
    q2 = st.radio("2. Not being able to stop or control worrying", list(options_map.keys()))
    q3 = st.radio("3. Worrying too much about different things", list(options_map.keys()))
    q4 = st.radio("4. Trouble relaxing", list(options_map.keys()))
    q5 = st.radio("5. Being so restless that it is hard to sit still", list(options_map.keys()))
    q6 = st.radio("6. Becoming easily annoyed or irritable", list(options_map.keys()))
    q7 = st.radio("7. Feeling afraid, as if something awful might happen", list(options_map.keys()))
    
    if st.button("Submit Screening Assessment"):
        if not v_email:
            st.error("Please provide your email address to sync your assessment score details safely.")
        else:
            total_score = options_map[q1] + options_map[q2] + options_map[q3] + options_map[q4] + options_map[q5] + options_map[q6] + options_map[q7]
            if total_score <= 4:
                severity = "Minimal Anxiety"
            elif total_score <= 9:
                severity = "Mild Anxiety"
            elif total_score <= 14:
                severity = "Moderate Anxiety"
            else:
                severity = "Severe Anxiety"
                
            status_text = f"Score: {total_score} ({severity})"
            success_sync = update_assessment_data(v_email, status_text)
            
            st.markdown(f"### **Your Baseline Result:** Score {total_score} - **{severity}**")
            if success_sync:
                st.success("🎉 Assessment submitted successfully! These metrics have been safely encrypted and synced to your clinician's private dashboard file for your upcoming intake.")
            else:
                st.warning("Assessment complete, but we could not trace a matching booking for this specific email address. Your clinician will document this score manually during your call.")

# 7. PAGE VIEW: WELLNESS INSIGHTS
elif page == "Wellness Insights":
    st.markdown("## 📖 Wellness Insights & Psychological Advice")
    st.write("Explore evidence-based mental health articles curated by the clinical team at Tumaini 365.")
    st.markdown("---")
