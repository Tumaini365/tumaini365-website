    contact_form_html = f"""
    <form action="https://formsubmit.co{TARGET_EMAIL}" method="POST" style="background-color: #FFFFFF; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
        <!-- Form Setup Controls -->
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
