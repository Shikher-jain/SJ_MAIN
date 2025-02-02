from flask import Flask, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shikher Jain - Portfolio</title>
    <style>
        body { background-color: #282a36; color: #f8f8f2; font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #bd93f9; }
        p { color: #50fa7b; }
        .links a { color: #ff79c6; text-decoration: none; font-size: 20px; margin: 10px; display: inline-block; }
        .links a:hover { color: #f1fa8c; }
        .projects { background-color: #44475a; padding: 20px; border-radius: 10px; max-width: 600px; margin: 20px auto; }
        .project-item { background-color: #6272a4; padding: 10px; margin: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Shikher Jain</h1>
    <p>Full Stack Developer | ML Enthusiast</p>
    <div class="links">
        <a href="https://github.com/shikherjain786" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/shikher-jain-0bb8a8259" target="_blank">LinkedIn</a>
        <a href="https://www.youtube.com/@shikherjain0906" target="_blank">YouTube</a>
        <a href="https://www.cloudskillsboost.google/public_profiles/ec9eb266-a3ec-472d-a1ec-1015892b92f2" target="_blank">Google Cloud Skill Boost</a>
        <a href="https://www.instagram.com/shikher.09?igsh=NGxmNXJ3a2lmeHhl" target="_blank">Instagram</a>
        <a href="https://www.instagram.com/unofficial.sayzz/profilecard/?igsh=MThkams4OHZ1bGtweQ==" target="_blank">Instagram (Unofficial Sayzz)</a>
        <a href="https://www.hackerrank.com/profile/shikherjain786" target="_blank">HackerRank</a>
        <a href="https://www.geeksforgeeks.org/user/shikherj/" target="_blank">GeeksforGeeks</a>
        <a href="https://leetcode.com/u/shikherJain09/" target="_blank">LeetCode</a>
    </div>
    <div class="projects">
        <h2>Projects</h2>
        <div class="project-item">✅ YouTube Clone</div>
        <div class="project-item">✅ Bill Generator (Tkinter)</div>
        <div class="project-item">✅ To-Do List App</div>
        <div class="project-item">✅ Password Generator</div>
    </div>
</body>
</html>
"""

@app.route('/')
def portfolio():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
