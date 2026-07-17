import streamlit as st
import pandas as pd
import datetime

# 1. Global Page Configuration
st.set_page_config(
    page_title="Tumaini 365 | Your Hope Everyday",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🔒 LINK YOUR PERMANENT GOOGLE SHEETS DATABASE HERE
# This is now locked directly to your official tumaini365ltd@gmail.com spreadsheet asset
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1wTLvxTjyZE-Q5hHAkoQygNOz5QavSvmLar8QTt9-S_c/edit?usp=sharing"

# Function to safely convert sharing link to a direct CSV reading link
def get_clean_url(url):
    try:
        if "edit" in url:
            return url.split("/edit")[0] + "/gviz/tq?tqx=out:csv"
        return url
    except:
        return url

# Function to read permanent records from Google Sheets securely
def load_permanent_bookings():
    try:
        clean_url = get_clean_url(GOOGLE_SHEET_URL)
        df = pd.read_csv(clean_url)
        df.dropna(how="all", inplace=True)
        return df.to_dict(orient="records")
    except:
        return []

# 2. Complete Corporate UI Styling (Tumaini 365: Purple & Dark-Theme Vibe)
st.markdown("""
    <style>
    .main-title { color: #5A189A; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #240046; font-size: 20px; text-align: center; font-weight: 500; margin-bottom: 25px; }
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
    ["🏠 Home Page", "📅 August Holiday Teen Hub", "📚 Resources & Topics", "📞 Contact & Support"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔒 Clinical Administration")
show_dashboard = st.sidebar.checkbox("👁️ Open Clinical Window")

# 🏠 HOME PAGE
if app_page == "🏠 Home Page" and not show_dashboard:
    st.markdown("<h1 class='main-title'>TUMAINI 365</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Your Hope Everyday — Professional Therapy & Consultancy</div>", unsafe_allow_html=True)
    
    st.write("Welcome to Tumaini 365. We offer professional psychological, mental wellness, and training consultancy ecosystems designed to help individuals, families, and high school learners connect with their true potential and find lasting transformation.")
    
    st.markdown("<div class='feature-header'>🎯 Our Core Focus Areas</div>", unsafe_allow_html=True)
    st.write("• **Adolescent & Youth Counseling**: Navigating identity, social pressure, and emotional growth.")
    st.write("• **Family & Couples Therapy**: Restoring communication pathways and structural dynamics.")
    st.write("• **Institutional Training Modules**: Delivering targeted wellness frameworks for schools and communities.")
    st.warning("🚀 **Now Enrolling**: The August Holiday Teen Mental Health Hub is active! Use the sidebar navigation menu to book a secure session for your teenager today.")

# 📅 AUGUST TEEN HUB
elif app_page == "📅 August Holiday Teen Hub" and not show_dashboard:
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

    st.markdown("<div class='feature-header'>🔒 Dynamic Session Booking Form</div>", unsafe_allow_html=True)

    with st.form("booking_form", clear_on_submit=True):
        student_name = st.text_input("Student's Full Name:")
        parent_name = st.text_input("Parent / Guardian Full Name:")
        class_level = st.selectbox("Current Academic Level:", ["Select Class level...", "Grade 9", "Grade 10", "Form 3", "Form 4"])
        parent_phone = st.text_input("Parent's Contact Number (WhatsApp/Call):")
        parent_email = st.text_input("Parent's Email Address:")
        
        target_weeks = st.multiselect(
            "Select the Week(s) you wish to book sessions for:",
            ["Week 1: Social Pressures & Peer Challenges (Aug 3-9)", "Week 2: Self-Esteem & Digital Age (Aug 10-16)", "Week 3: Family Expectations & Holiday Stresses (Aug 17-23)", "Week 4: Post-Holiday Motivation & Goals (Aug 24-29)"]
        )
        session_type = st.radio("Preferred Therapy Setup:", ("Group Therapy Support Sessions", "Individualized 1-on-1 Counseling Sessions"))
        additional_notes = st.text_area("Any specific challenges to note? (Optional)")
        
        submit_button = st.form_submit_button("Submit Secure Booking Request 🚀")

    if submit_button:
        if not student_name or not parent_name or not parent_phone or class_level == "Select Class level..." or not target_weeks:
            st.error("Please fill in all mandatory fields to process your booking.")
        else:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            weeks_str = " | ".join(target_weeks)
            
            st.balloons()
            st.success(f"Thank you, {parent_name}! Secure booking request generated successfully.")
            st.info(f"📋 **Action Required to Log Row Permanently:** Please text this summary block to your counselor via WhatsApp to update the Master Intake Book instantly!")
            st.code(f"Booking: {student_name} ({class_level}) - Parent: {parent_name}, Phone: {parent_phone}, Setup: {session_type}, Focus Weeks: {weeks_str}")

# 📚 RESOURCES & TOPICS
elif app_page == "📚 Resources & Topics" and not show_dashboard:
    st.markdown("<h1 class='main-title'>THERAPEUTIC RESOURCES & INSIGHTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Clinical Perspectives on Adolescent Dynamics During School Breaks</div>", unsafe_allow_html=True)
    st.markdown("<div class='article-box'><div class='article-title'>📖 Topic 1: Navigating Peer Pressures and Adolescent Identity</div><p>During extended school breaks, teenagers experience a sudden break from structured academic validation, turning heavily toward peer networks to build their identity...</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='article-box'><div class='article-title'>📖 Topic 2: Deconstructing Digital Loops and Screen Dependency</div><p>Unstructured vacation time frequently triggers compulsive tech use as a coping mechanism for boredom...</p></div>", unsafe_allow_html=True)

# 📞 CONTACT & SUPPORT
elif app_page == "📞 Contact & Support" and not show_dashboard:
    st.markdown("<div class='feature-header'>📞 Reach Out to Us Directly</div>", unsafe_allow_html=True)
    st.write("📱 **Phone Support:** 0720545788 / 0754828766")
    st.write(f"📧 **Email Address:** tumaini365ltd@gmail.com")

# 🔒 RE-CONFIGURED ADMINISTRATIVE CLINICAL MONITOR
if show_dashboard:
    st.markdown("<h1 class='main-title'>🔒 CLINICAL INTAKE MONITOR</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Tumaini 365 Cloud-Linked Master Database</div>", unsafe_allow_html=True)
    
    permanent_records = load_permanent_bookings()
    
    if not permanent_records:
        st.info("📭 No permanent rows detected inside your cloud document yet, or sheet URL permissions are loading.")
        st.write(f"🔗 [Click here to open and verify your Master Google Sheet Database directly]({GOOGLE_SHEET_URL})")
    else:
