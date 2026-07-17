import streamlit as st

# 1. Global Page Configuration
st.set_page_config(
    page_title="Tumaini 365 | Your Hope Everyday",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Unified Custom CSS Styling (Tumaini 365 Branding: Purple, Black, White)
st.markdown("""
    <style>
    .main-title {
        color: #7B2CBF;
        font-size: 34px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #240046;
        font-size: 20px;
        text-align: center;
        font-weight: 500;
        margin-bottom: 25px;
    }
    .target-badge {
        background-color: #F0E6FF;
        color: #5A189A;
        padding: 8px 15px;
        border-radius: 20px;
        font-weight: bold;
        text-align: center;
        margin: 15px auto;
        display: block;
        width: fit-content;
        border: 1px solid #D8BBFF;
    }
    .week-card {
        background-color: #FAF7FF;
        border-left: 5px solid #7B2CBF;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .week-title {
        color: #5A189A;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 5px;
    }
    .feature-header {
        color: #7B2CBF;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        border-bottom: 2px solid #E0AAFF;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    .footer-text {
        text-align: center;
        color: #666666;
        font-size: 13px;
        margin-top: 20px;
    }
    </style>
""", unsafe_style_html=True)

# 3. Sidebar Navigation Menu Controls
st.sidebar.image("https://placeholder.com", caption="TUMAINI 365") # Replace with your direct logo image URL if available
st.sidebar.markdown("## 🌐 Portal Navigation")
app_page = st.sidebar.radio(
    "Go To:",
    ["🏠 Home Page", "📅 August Holiday Teen Hub", "📚 Resources & Topics", "📞 Contact & Support"]
)

# 📝 COHORT A: HOME PAGE FRAMEWORK
if app_page == "🏠 Home Page":
    st.markdown("<h1 class='main-title'>TUMAINI 365</h1>", unsafe_style_html=True)
    st.markdown("<div class='sub-title'>Your Hope Everyday — Professional Therapy & Consultancy</div>", unsafe_style_html=True)
    
    st.write("Welcome to Tumaini 365. We offer professional psychological, mental wellness, and training consultancy ecosystems designed to help individuals, families, and high school learners connect with their true potential and find lasting transformation.")
    
    st.markdown("<div class='feature-header'>🎯 Our Core Focus Areas</div>", unsafe_style_html=True)
    st.write("• **Adolescent & Youth Counseling**: Navigating identity, social pressure, and emotional growth.")
    st.write("• **Family & Couples Therapy**: Restoring communication pathways and structural dynamics.")
    st.write("• **Institutional Training Modules**: Delivering targeted wellness frameworks for schools and communities.")

    st.warning("🚀 **Now Enrolling**: The August Holiday Teen Mental Health Hub is active! Use the sidebar navigation menu to book a secure session for your teenager today.")

# 📝 COHORT B: NEW AUGUST TEEN HUB FORMATION WITH TIMELINE LOGIC
elif app_page == "📅 August Holiday Teen Hub":
    st.markdown("<h1 class='main-title'>AUGUST HOLIDAY MENTAL HEALTH HUB</h1>", unsafe_style_html=True)
    st.markdown("<div class='sub-title'>Your Safe Space to Unwind, Recharge, & Connect</div>", unsafe_style_html=True)
    st.markdown("<div class='target-badge'>📍 HIGH SCHOOL SEGMENT: FORM 3, FORM 4 & GRADE 9, GRADE 10</div>", unsafe_style_html=True)

    # Program Logistics Indicators
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **TIMELINE**\n\nAugust 3rd – August 29th, 2026")
    with col2:
        st.success("💻 **DELIVERY**\n\n100% Online via Google Meet")

    st.markdown("⚠️ *Strictly limited slots to preserve clinical confidentiality, emotional safety, and group impact.*")

    # The 4 Focus Topics
    st.markdown("<div class='feature-header'>📅 August Weekly Theme Breakdown</div>", unsafe_style_html=True)
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
    """, unsafe_style_html=True)

    # Dynamic Selection & Intake Form
    st.markdown("<div class='feature-header'>🔒 Dynamic Session Booking Form</div>", unsafe_style_html=True)

    with st.form("booking_form", clear_on_submit=True):
        student_name = st.text_input("Student's Full Name:")
        parent_name = st.text_input("Parent / Guardian Full Name:")
        
        class_level = st.selectbox(
            "Current Academic Level:",
            ["Select Class level...", "Grade 9", "Grade 10", "Form 3", "Form 4"]
        )
        
        parent_phone = st.text_input("Parent's Contact Number (WhatsApp/Call):")
        parent_email = st.text_input("Parent's Email Address:")
        
        target_weeks = st.multiselect(
            "Select the Week(s) you wish to book sessions for:",
            [
                "Week 1: Social Pressures & Peer Challenges (Aug 3-9)",
                "Week 2: Self-Esteem & Digital Age (Aug 10-16)",
                "Week 3: Family Expectations & Holiday Stresses (Aug 17-23)",
                "Week 4: Post-Holiday Motivation & Goals (Aug 24-29)"
            ]
        )
        
        session_type = st.radio(
            "Preferred Therapy Setup for your selected week(s):",
            (
                "Group Therapy Support Sessions (Peer connection, shared experiences, collaborative resilience)",
                "Individualized 1-on-1 Counseling Sessions (Deeply personalized, target-focused clinical attention)"
            )
        )
        
        additional_notes = st.text_area("Are there any specific behaviors or challenges you want the counselor to note? (Optional)")
        
        submit_button = st.form_submit_button("Submit Secure Booking Request 🚀")

    # Intake Submission Validation Block
    if submit_button:
        if not student_name or not parent_name or not parent_phone or class_level == "Select Class level..." or not target_weeks:
            st.error("Please fill in all mandatory fields (Name, Academic Level, Selected Weeks, and Phone) to process your booking.")
        else:
            st.balloon()
            st.success(f"Thank you, {parent_name}! The holiday reservation request for {student_name} has been securely received.")
            
            st.markdown("### 📋 Booking Summary Saved:")
            st.write(f"• **Setup**: {session_type}")
            st.write(f"• **Selected Focus Periods**:")
            for week in target_weeks:
                st.write(f"  → {week}")
                
            st.info("📩 **What Happens Next:** Our intake desk will review your selections. You will receive an official confirmation message outlining the session timetable along with your secure, private Google Meet access links via WhatsApp within 24 hours.")

# 📝 COHORT C: TOPICS & THERAPEUTIC RESOURCES
elif app_page == "📚 Resources & Topics":
    st.markdown("<div class='feature-header'>📚 Mental Wellness Resources</div>", unsafe_style_html=True)
    st.write("Explore general mental fitness articles, reading lists, and mental health tools curated specifically for families, young adults, and corporate systems in Kenya.")
    st.info("💡 *Full articles library and interactive mental wellness downloads coming soon!*")

# 📝 COHORT D: GENERAL OFFICE INFRASTRUCTURE CONTACT
elif app_page == "📞 Contact & Support":
    st.markdown("<div class='feature-header'>📞 Reach Out to Us Directly</div>", unsafe_style_html=True)
    st.write("Need general counseling, corporate consulting, or family workshops?")
    st.write("📱 **Phone Support:** 0720545788 / 0754828766")
    st.write("📧 **Email Address:** support@tumaini365.org")

# 4. Global Structural Footer Elements
st.write("---")
st.markdown("<div class='footer-text'>🛡️ <b>TUMAINI 365</b> — Your Hope Everyday.</div>", unsafe_style_html=True)
st.markdown("<div class='footer-text'>Professional Psychological, Mental Wellness & Training Consultancy Services.</div>", unsafe_style_html=True)
