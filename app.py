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
    
    .blog-article {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        margin-bottom: 25px;
        border-left: 4px solid #4A7C59;
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
    page = st.radio("", ["Home", "Book an Appointment", "Wellness Insights", "About & Confidentiality", "🔒 Practice Dashboard"], horizontal=True, label_visibility="collapsed")

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

# 6. NEW PAGE VIEW: WELLNESS INSIGHTS (BLOG SECTION)
elif page == "Wellness Insights":
    st.markdown("## 📖 Wellness Insights & Psychological Advice")
    st.write("Explore evidence-based mental health articles curated by the clinical team at Tumaini 365.")
    st.markdown("---")
    
    # Article 1
    st.markdown("""
        <div class="blog-article">
            <h3>1. Navigating Workplace Burnout: Recognizing the Silent Signs</h3>
            <p style="color: #666; font-size: 0.9rem;"><i>Published by Tumaini 365 Clinical Desk</i></p>
            <p>Workplace burnout goes far beyond simple physical fatigue. It is a state of emotional, mental, and physical exhaustion caused by excessive and prolonged stress. In today's fast-paced corporate environments, burnout often flies under the radar until it severely impacts emotional regulation.</p>
            <h4>Key Coping Strategies:</h4>
            <ul>
                <li><b>Establish Hard Boundaries:</b> Create strict disconnect times where corporate emails and work tasks are entirely unreachable.</li>
                <li><b>Practice Micro-Breaks:</b> Use the 50-10 rule—work dynamically for 50 minutes, then completely step away for 10 minutes to reset your nervous system.</li>
                <li><b>Speak to a Specialist:</b> Burnout changes cognitive processing; early professional therapy provides structural behavioral recovery frameworks.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Article 2
    st.markdown("""
        <div class="blog-article">
            <h3>2. Grounding Techniques for Managing Acute Anxiety</h3>
            <p style="color: #666; font-size: 0.9rem;"><i>Published by Tumaini 365 Clinical Desk</i></p>
            <p>Anxiety pulls our attention into terrifying projections of the future. When acute anxiety or a panic episode strikes, physical grounding exercises work rapidly to signal safety directly to your brain's emotional center (the amygdala).</p>
            <h4>The 5-4-3-2-1 Grounding Method:</h4>
            <p>Slow your breathing down completely and actively identify the following items in your immediate physical environment:</p>
            <ul>
                <li><b>5 things</b> you can physically see around the room.</li>
                <li><b>4 things</b> you can physically touch or feel (e.g., your feet on the floor, clothing fabric).</li>
                <li><b>3 things</b> you can distinctly hear in the background.</li>
                <li><b>2 things</b> you can distinctly smell.</li>
                <li><b>1 thing</b> you can taste.</li>
            </ul>
            <p>This systematic sensory activation shifts your brain out of survival mode and safely anchors you back into the present moment.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Article 3
    st.markdown("""
        <div class="blog-article">
            <h3>3. Building Emotional Resilience in Relationships</h3>
            <p style="color: #666; font-size: 0.9rem;"><i>Published by Tumaini 365 Clinical Desk</i></p>
            <p>Healthy relationships are not defined by the absolute absence of conflict, but rather by the presence of a strong emotional recovery system. Couples who practice intentional psychological communication preserve safety even during deep disagreements.</p>
            <h4>Core Frameworks for Healthy Conflict:</h4>
            <ul>
                <li><b>Shift from "You" to "I" Statements:</b> Replace accusatory phrases like <i>"You always ignore me"</i> with empathetic ownership: <i>"I feel disconnected when we don't catch up after work."</i></li>
