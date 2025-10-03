import streamlit as st

st.set_page_config(page_title="Rayhan Hussain | Portfolio", page_icon="👨‍💻", layout="wide")

# ------------------------------
# Custom CSS (use .stApp instead of body)
st.markdown("""
<style>
/* Background applied to Streamlit root */
.stApp {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(120deg,#89f7fe,#66a6ff,#fbc2eb,#a6c1ee);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
    overflow-x: hidden;
}
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Floating Emojis */
.emoji-container {
    position: absolute;
    top: 0;
    left: 0;
    width:100%;
    height:100%;
    pointer-events: none;
    overflow:hidden;
    z-index:0;
}
.emoji {
    position: absolute;
    bottom: -50px;
    font-size: 32px;
    opacity: 0.8;
    animation: floatUp 12s linear infinite;
}
@keyframes floatUp {
    0% {transform: translateY(0) scale(1); opacity:1;}
    100% {transform: translateY(-120vh) scale(1.6); opacity:0;}
}

/* Hero Section */
.hero {
    text-align:center;
    padding:80px 20px 40px 20px;
    color:#fff;
    text-shadow: 2px 3px 12px rgba(0,0,0,0.3);
    z-index:2;
    position: relative;
}
.hero h1{font-size:60px; animation: fadeIn 2s ease-in-out;}
.hero p{font-size:22px; animation: fadeIn 3s ease-in-out;}

/* Profile Card */
.profile-card {
    max-width:320px;
    margin:auto;
    padding:25px;
    border-radius:25px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    text-align:center;
    box-shadow:0px 10px 30px rgba(0,0,0,0.3);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    position: relative;
    z-index:2;
}
.profile-card:hover{transform: translateY(-12px); box-shadow:0px 20px 40px rgba(0,0,0,0.5);}
.profile-card img{width:130px;height:130px;border-radius:50%;border:4px solid rgba(255,255,255,0.7);object-fit:cover;}
.profile-card h2{margin:15px 0 5px 0;color:#fff;}
.profile-card p{color:#eee;}

/* Skills */
.skills {padding:60px 20px;text-align:center;position:relative;z-index:2;}
.skill-bar {position:relative;height:25px;width:80%;background: rgba(255,255,255,0.2);border-radius:25px;margin:15px auto;overflow:hidden;}
.skill-bar-fill {height:100%;width:0;background: linear-gradient(90deg,#ff9966,#ff5e62);border-radius:25px;animation: fillBar 2s forwards;}
@keyframes fillBar {from {width:0;} to {width: var(--skill-level);}}

/* Projects */
.projects {padding:60px 20px;display:flex;flex-wrap:wrap;justify-content:center;gap:30px;z-index:2;position:relative;}
.project-card {width:280px;background: rgba(255,255,255,0.15);backdrop-filter: blur(12px);border-radius:25px;padding:20px;color:#fff;text-align:center;transition: transform 0.4s ease, box-shadow 0.4s ease;}
.project-card:hover{transform: translateY(-10px);box-shadow:0px 15px 35px rgba(0,0,0,0.45);}
.project-card h3{margin:10px 0;color:#fff;}
.project-card p{color:#eee;}

/* Contact */
.contact {text-align:center;padding:60px 20px;z-index:2;position:relative;}
.contact a{display:inline-block;padding:14px 28px;margin:10px;border-radius:20px;color:#fff;background: linear-gradient(90deg,#00c6ff,#0072ff);text-decoration:none;font-weight:bold;transition: all 0.4s ease;}
.contact a:hover{transform: scale(1.12);box-shadow:0px 12px 28px rgba(0,0,0,0.5);}

/* Footer */
.footer{text-align:center;padding:25px;color:#fff;background: rgba(0,0,0,0.3);backdrop-filter: blur(8px);z-index:2;position:relative;}

@keyframes fadeIn{from{opacity:0;}to{opacity:1;}}
@media(max-width:768px){.hero h1{font-size:42px;}.hero p{font-size:18px;}.project-card{width:90%;}}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Floating Emoji Layer
emoji_list = ["🚀","✨","🌟","🔥","💡","😊","💻","🎯","🌈","🧠","📱","⚡"]
emoji_html = "<div class='emoji-container'>"
for i, emoji in enumerate(emoji_list):
    emoji_html += f"<div class='emoji' style='left:{i*8+5}%; animation-delay:{i*2}s;'>{emoji}</div>"
emoji_html += "</div>"
st.markdown(emoji_html, unsafe_allow_html=True)

# ------------------------------
# Hero
st.markdown("""
<div class="hero">
<h1>👋 Hi, I'm Rayhan Hussain</h1>
<p>AI Enthusiast | Full Stack Developer | Tech Creator</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Profile (replace image path with your own)
st.markdown("""
<div class="profile-card">
<img src="your_image.jpg" alt="Profile">
<h2>Rayhan Hussain</h2>
<p>Passionate about AI, Web & App Development, Open Source Contributor</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Skills
st.markdown("<div class='skills'><h2>💻 My Skills</h2></div>", unsafe_allow_html=True)
skills = {"Python":"90%","Streamlit":"85%","AI/ML":"80%","OpenCV":"80%","Web Dev":"75%"}
for skill, level in skills.items():
    st.markdown(f"""
    <p style='text-align:center; color:#fff;'>{skill}</p>
    <div class='skill-bar' style='--skill-level:{level};'>
        <div class='skill-bar-fill'></div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------
# Projects
st.markdown("<div class='projects'><h2 style='width:100%; text-align:center; color:#fff;'>🚀 Projects</h2></div>", unsafe_allow_html=True)
projects = [
    {"title":"Emotion Detector","desc":"Real-time face emotion detection using AI & Streamlit."},
    {"title":"Portfolio Website","desc":"Interactive personal website hosted on Streamlit."},
    {"title":"Chatbot AI","desc":"AI chatbot that understands and responds intelligently."}
]
st.markdown("<div class='projects'>", unsafe_allow_html=True)
for p in projects:
    st.markdown(f"""
    <div class='project-card'>
    <h3>{p['title']}</h3>
    <p>{p['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Contact
st.markdown("""
<div class='contact'>
<h2>📬 Get in Touch</h2>
<a href='mailto:rayhan@example.com'>Email Me</a>
<a href='https://www.linkedin.com/in/Rayhanhcse' target='_blank'>LinkedIn</a>
<a href='https://github.com/Rayhanhcse' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Footer
st.markdown("<div class='footer'>Copyright © 2025 | Rayhan Hussain</div>", unsafe_allow_html=True)
