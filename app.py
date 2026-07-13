import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Tumaini 365 | Counselling Psychology",
    page_icon="🌱",
    layout="wide"
)

# 2. RESTORING BRAND COLOR CODES
st.markdown("""
    <style>
    .stApp { background-color: #F5EBE6 !important; } 
    h1, h2, h3, h4 { color: #4A7C59 !important; font-family: 'Georgia', serif; } 
    p, label, span { color: #333333 !important; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 8px;
        border-top: 3px solid #6B8E23; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .custom-emergency-banner {
        background-color: #FADBD8;
        color: #78281F !important;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #E6B0AA;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. FILE DATABASE SETUP
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

current_bookings = load_permanent_bookings()

# 4. Title Header
st.title("🌱 Tumaini Three Sixty Five Limited")
st.caption("Professional Counselling Psychology Practice")

# 5. HORIZONTAL NAVIGATION BUTTONS
tab_home, tab_book, tab_screen, tab_blog, tab_about, tab_dash = st.tabs([
    "🏠 Home", 
    "📆 Book an Appointment", 
    "📊 Mental Health Screening", 
    "📖 Wellness Insights", 
    "💡 About & Confidentiality", 
    "🔒 Practice Dashboard"
])

# 6. TAB BLOCKS

# HOME SECTION
with tab_home:
    st.header("A Safe Space to Heal, Grow, and Thrive 365 Days a Year")
    st.write("Confidential and empathetic counselling psychology tailored for individuals, couples, and corporate institutions.")
    
    st.subheader("Our Therapeutic Formats")
    col_v, col_f = st.columns(2)
    with col_v:
        st.info("🌐 **Virtual Telehealth Sessions:** Secure, fully encrypted video sessions accessible from the total privacy of your home or private workspace.")
    with col_f:
        st.info("🏢 **Face-to-Face Sessions:** In-person clinical appointments hosted inside our quiet, warm, and highly discreet consulting offices.")
        
    st.divider()
    st.subheader("Areas of Clinical Expertise")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("**Individual Care:** Anxiety management, burnout recovery, depression therapy, and lifestyle adjustment transitions.")
    with c2:
        st.success("**Relationship Care:** Couples counseling, family rebuilding frameworks, and healthy communication skills.")
    with c3:
        st.success("**Corporate Wellness:** Workplace mental health design workshops, leadership trauma training, and staff care plans.")

# BOOKING SECTION
with tab_book:
    st.subheader("📆 Secure Booking Engine")
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
                st.success("🎉 Your appointment request is locked in! Please open the 'Mental Health Screening' tab above to complete your baseline clinical assessment.")

# SCREENING SECTION
with tab_screen:
    st.subheader("📊 Baseline Anxiety Assessment (GAD-7)")
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
                st.success("🎉 Assessment submitted successfully! These metrics have been safely synced to your clinician's private dashboard.")
            else:
                st.warning("Assessment complete, but we could not trace a matching booking for this specific email address.")

# BLOG SECTION (Rewritten without HTML string bugs)
with tab_blog:
    st.subheader("📖 Wellness Insights & Psychological Advice")
    st.write("Explore evidence-based mental health articles curated by the clinical team at Tumaini 365.")
    st.divider()
    
    st.markdown("### 1. Navigating Workplace Burnout: Recognizing the Silent Signs")
    st.write("Workplace burnout goes far beyond simple physical fatigue. It is a state of emotional, mental, and physical exhaustion caused by excessive and prolonged stress. In today's corporate environments, burnout often flies under the radar until it severely impacts emotional regulation.")
    st.markdown("**Key Coping Strategies:**")
    st.write("- **Establish Hard Boundaries:** Create strict disconnect times where corporate emails and work tasks are entirely unreachable.")
    st.write("- **Practice Micro-Breaks:** Use the 50-10 rule—work dynamically for 50 minutes, then completely step away for 10 minutes to reset your nervous system.")
    st.write("- **Speak to a Specialist:** Burnout changes cognitive processing; early professional therapy provides structural behavioral recovery frameworks.")
    st.divider()
    
    st.markdown("### 2. Grounding Techniques for Managing Acute Anxiety")
    st.write("Anxiety pulls our attention into terrifying projections of the future. When acute anxiety or a panic episode strikes, physical grounding exercises work rapidly to signal safety directly to your brain's emotional center.")
    st.markdown("**The 5-4-3-2-1 Grounding Method:**")
    st.write("Slow your breathing down completely and actively identify these items in your room: Identify 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste. This shifts your nervous system out of survival mode.")
    st.divider()
    
