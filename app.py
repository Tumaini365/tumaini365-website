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

current_bookings = load_permanent_bookings()

# 3. Navigation Header Matrix
col_logo, col_nav = st.columns(2)
with col_logo:
    st.markdown("### 🌱 **Tumaini Three Sixty Five Limited**")
    st.caption("Professional Counselling Psychology Practice")

with col_nav:
    page = st.radio("", ["Home", "Book an Appointment", "Wellness Insights", "About & Confidentiality", "🔒 Practice Dashboard"], horizontal=True, label_visibility="collapsed")

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
            "08:00 AM - 09:00 AM",
            "09:30 AM - 10:30 AM",
            "11:00 AM - 12:00 PM",
            "02:00 PM - 03:00 PM",
            "03:30 PM - 04:30 PM",
            "05:00 PM - 06:00 PM"
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
                    "Requested Date/Time": formatted_datetime
                }
                save_permanent_booking(new_booking)
                st.success("🎉 Your appointment request has been securely locked into our system! Our clinical desk will reach out to you via email or mobile shortly.")

# 6. PAGE VIEW: WELLNESS INSIGHTS (BLOG SECTION)
elif page == "Wellness Insights":
    st.markdown("## 📖 Wellness Insights & Psychological Advice")
    st.write("Explore evidence-based mental health articles curated by the clinical team at Tumaini 365.")
    st.markdown("---")
    
    art_1 = '<div class="blog-article"><h3>1. Navigating Workplace Burnout</h3><p style="color: #666;"><i>Published by Tumaini 365 Clinical Desk</i></p><p>Workplace burnout goes far beyond simple physical fatigue. It is a state of emotional, mental, and physical exhaustion caused by excessive and prolonged stress. In today corporate environments, burnout often flies under the radar until it severely impacts emotional regulation.</p><h4>Key Coping Strategies:</h4><ul><li><b>Establish Hard Boundaries:</b> Create strict disconnect times where corporate emails and work tasks are entirely unreachable.</li><li><b>Practice Micro-Breaks:</b> Use the 50-10 rule—work dynamically for 50 minutes, then completely step away for 10 minutes to reset your nervous system.</li><li><b>Speak to a Specialist:</b> Burnout changes cognitive processing; early professional therapy provides structural behavioral recovery frameworks.</li></ul></div>'
    art_2 = '<div class="blog-article"><h3>2. Grounding Techniques for Managing Acute Anxiety</h3><p style="color: #666;"><i>Published by Tumaini 365 Clinical Desk</i></p><p>Anxiety pulls our attention into terrifying projections of the future. When acute anxiety or a panic episode strikes, physical grounding exercises work rapidly to signal safety directly to your brain emotional center.</p><h4>The 5-4-3-2-1 Grounding Method:</h4><p>Slow your breathing down completely and actively identify these items in your room: Identify 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste. This shifts your nervous system out of survival mode.</p></div>'
    art_3 = '<div class="blog-article"><h3>3. Building Emotional Resilience in Relationships</h3><p style="color: #666;"><i>Published by Tumaini 365 Clinical Desk</i></p><p>Healthy relationships are not defined by the absolute absence of conflict, but rather by the presence of a strong emotional recovery system. Couples who practice intentional communication preserve safety even during deep disagreements.</p><h4>Core Frameworks:</h4><ul><li><b>Shift to "I" Statements:</b> Replace accusatory phrases with empathetic ownership: "I feel disconnected when we don not catch up."</li><li><b>Validate Before Reacting:</b> Confirm clear comprehension: "What I hear you saying is that you feel overwhelmed."</li></ul></div>'
    
    st.markdown(art_1, unsafe_allow_html=True)
    st.markdown(art_2, unsafe_allow_html=True)
    st.markdown(art_3, unsafe_allow_html=True)

# 7. PAGE VIEW: ABOUT & CONFIDENTIALITY
elif page == "About & Confidentiality":
    st.markdown("## Operational Ethics & Trust Matrix")
    st.markdown("<div class='card-box'><p>At <b>Tumaini Three Sixty Five Limited</b>, we process clinical confidentiality protocols as our highest priority structure. Whether you interface with our practicing counseling psychologists online via video endpoints or directly at our physical rooms, your file notes, treatment strategies, and discussions are protected under medical record custody provisions.</p></div>", unsafe_allow_html=True)

# 8. PRIVATE DASHBOARD PAGE (Fixed Indentation Formatting)
elif page == "🔒 Practice Dashboard":
    st.markdown("## 🔒 Internal Practice Administration Dashboard")
    password_input = st.text_input("Enter Practice Admin Password to Unlock Client Log", type="password")
    
    if password_input == "tumaini365":
        st.success("Access Granted.")
        if len(current_bookings) == 0:
            st.info("No appointment requests have been logged yet.")
        else:
            df = pd.DataFrame(current_bookings)
            st.dataframe(df, use_container_width=True)
