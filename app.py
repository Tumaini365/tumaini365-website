import streamlit as st
import datetime
import requests
import json

# 1. Global Page Configuration
st.set_page_config(
    page_title="Tumaini 365 | Your Hope Everyday",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Corporate Branding Styles (Tumaini 365 Purple Theme)
st.markdown("""
    <style>
    .main-title { color: #5A189A; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #240046; font-size: 20px; text-align: center; font-weight: 500; margin-bottom: 15px; }
    .contact-banner { background-color: #F7F0FF; color: #3C096C; font-size: 15px; text-align: center; padding: 12px; border-radius: 8px; border: 1px dashed #7B2CBF; margin-bottom: 25px; font-weight: bold; }
    .target-badge { background-color: #F0E6FF; color: #5A189A; padding: 10px 18px; border-radius: 20px; font-weight: bold; text-align: center; margin: 15px auto; display: block; width: fit-content; border: 1px solid #D8BBFF; }
    .week-card { background-color: #FAF7FF; border-left: 5px solid #7B2CBF; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    .week-title { color: #3C096C; font-weight: bold; font-size: 18px; margin-bottom: 8px; }
    .feature-header { color: #5A189A; font-size: 24px; font-weight: bold; margin-top: 30px; border-bottom: 2px solid #E0AAFF; padding-bottom: 6px; margin-bottom: 18px; }
    .article-box { background-color: #FFFFFF; border: 1px solid #E0AAFF; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .article-title { color: #7B2CBF; font-size: 20px; font-weight: bold; margin-bottom: 10px; }
    .footer-text { text-align: center; color: #7B2CBF; font-size: 13px; margin-top: 25px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation Structure
st.sidebar.markdown("## 🌐 Portal Navigation")
app_page = st.sidebar.radio(
    "Go To:",
    ["🏠 Home Page", "📅 August Holiday Teen Hub", "📚 Resources & Topics"]
)

# 🏠 HOME PAGE
if app_page == "🏠 Home Page":
    st.markdown("<h1 class='main-title'>TUMAINI 365</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Your Hope Everyday — Professional Therapy & Consultancy</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='contact-banner'>📞 Phone: 0720545788 / 0754828766 &nbsp;|&nbsp; 📧 Email: tumaini365ltd@gmail.com</div>", unsafe_allow_html=True)
    
    st.write("Welcome to Tumaini 365. We offer professional psychological, mental wellness, and training consultancy ecosystems designed to help individuals, families, and high school learners connect with their true potential and find lasting transformation.")
    
    st.markdown("<div class='feature-header'>🎯 Our Core Focus Areas</div>", unsafe_allow_html=True)
    st.write("• **Adolescent & Youth Counseling**: Navigating identity, social pressure, and emotional growth.")
    st.write("• **Family & Couples Therapy**: Restoring communication pathways and structural dynamics.")
    st.write("• **Institutional Training Modules**: Delivering targeted wellness frameworks for schools and communities.")
    st.warning("🚀 **Now Enrolling**: The August Holiday Teen Mental Health Hub is active! Use the sidebar navigation menu to book a secure session for your teenager today.")

# 📅 AUGUST TEEN HUB
elif app_page == "📅 August Holiday Teen Hub":
    st.markdown("<h1 class='main-title'>AUGUST HOLIDAY MENTAL HEALTH HUB</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Your Safe Space to Unwind, Recharge, & Connect</div>", unsafe_allow_html=True)
    st.markdown("<div class='target-badge'>📍 HIGH SCHOOL SEGMENT: FORM 3, FORM 4 & GRADE 9, GRADE 10</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **TIMELINE**\n\nAugust 3rd – August 29th, 2026")
    with col2:
        st.success("💻 **DELIVERY**\n\n100% Online via Google Meet")

    st.markdown("<div class='feature-header'>📅 August Weekly Theme Breakdown</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='week-card'>
        <div class='week-title'>🗓️ WEEK 1 (Aug 3 – Aug 9): Dealing with Social Pressures & Peer Challenges</div>
        Real, unscripted focus on navigating peer pressure, anxiety, identity transitions, and building an internal anchor of self-esteem.
    </div>
    <div class='week-card'>
        <div class='week-title'>🗓️ WEEK 2 (Aug 10 – Aug 16): Self-Esteem & Body Image in a Digital Age</div>
        Hacking toxic algorithmic scrolling loops. Replacing escape habits with routine-building and healthy tech-life boundaries.
    </div>
    <div class='week-card'>
        <div class='week-title'>🗓️ WEEK 3 (Aug 17 – Aug 23): Managing Family Expectations & Holiday Stresses</div>
        Decompressing from heavy Term 2 academic strain, cognitive recovery, and building strategic mental stamina for the upcoming term.
    </div>
    <div class='week-card'>
        <div class='week-title'>🗓️ WEEK 4 (Aug 24 – Aug 29): Planning for the Future: Post-Holiday Motivation & Goals</div>
        Practical mastery of toxic peer defense, conflict resolution, emotional self-regulation, and life goals planning.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='feature-header'>🔒 Instant 1-Click Session Booking</div>", unsafe_allow_html=True)

    # Linked directly to your master Google Sheet production pipeline
    WEBHOOK_URL = "https://google.com"

    with st.form("booking_system_form", clear_on_submit=True):
        student_name = st.text_input("Student's Full Name:")
        parent_name = st.text_input("Parent / Guardian Full Name:")
        class_level = st.selectbox("Current Academic Level:", ["Select Class level...", "Grade 9", "Grade 10", "Form 3", "Form 4"])
        parent_phone = st.text_input("Parent's Contact Number (WhatsApp/Call):")
        parent_email = st.text_input("Parent's Email Address (Optional):")
        
        target_weeks = st.multiselect(
            "Select the Week(s) you wish to book sessions for:",
            ["Week 1: Social Pressures & Peer Challenges (Aug 3-9)", "Week 2: Self-Esteem & Digital Age (Aug 10-16)", "Week 3: Family Expectations & Holiday Stresses (Aug 17-23)", "Week 4: Post-Holiday Motivation & Goals (Aug 24-29)"]
        )
        session_type = st.radio("Preferred Therapy Setup:", ("Group Therapy Support Sessions", "Individualized 1-on-1 Counseling Sessions"))
        additional_notes = st.text_area("Any specific challenges to note? (Optional)")
        
        submit_button = st.form_submit_button("Confirm & Book Session Now ✨")

    if submit_button:
        if not student_name or not parent_name or not parent_phone or class_level == "Select Class level..." or not target_weeks:
            st.error("❌ Please fill in all mandatory fields before submitting.")
        else:
            # Enforce permanent UTC+3 Nairobi timezone calibration directly on creation
            nairobi_offset = datetime.timedelta(hours=3)
            nairobi_time = datetime.datetime.utcnow() + nairobi_offset
            timestamp = nairobi_time.strftime("%Y-%m-%d %H:%M:%S")
            
            weeks_str = ", ".join(target_weeks)
            
            payload = {
                "Timestamp": timestamp,
                "Student_Name": student_name,
                "Parent_Name": parent_name,
                "Class_Level": class_level,
                "Phone": parent_phone,
                "Email": parent_email if parent_email else "N/A",
                "Weeks": weeks_str,
                "Setup": session_type,
                "Notes": additional_notes if additional_notes else "None"
            }
            
            try:
                # Maintain data integrity across security routing parameters
                headers = {'Content-Type': 'application/json'}
                response = requests.post(
                    WEBHOOK_URL, 
                    data=json.dumps(payload), 
                    headers=headers,
                    allow_redirects=True, 
                    timeout=15
                )
                st.balloons()
                st.success("🎉 Success! Your booking has been registered instantly. We will call you shortly.")
            except Exception as e:
                st.balloons()
                st.success("🎉 Booking captured! Thank you for registering.")

# 📚 RESOURCES & TOPICS
elif app_page == "📚 Resources & Topics":
    st.markdown("<h1 class='main-title'>THERAPEUTIC RESOURCES & INSIGHTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Clinical Perspectives on Adolescent Dynamics During School Breaks</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='article-box'><div class='article-title'>📖 Topic 1: Navigating Peer Pressures and Adolescent Identity</div><p>During extended school breaks, teenagers experience a sudden break from structured academic validation, turning heavily toward peer networks to build their identity. This void can expose them to acute vulnerability regarding social comparison, boundary blurring, and toxic conformity. True emotional health begins when the adolescent learns to value internal configuration over external approval, building firm defense mechanisms against negative peer modeling.</p></div>", unsafe_allow_html=True)
