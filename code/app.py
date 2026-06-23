from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Unfiltered Lens</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, sans-serif;
        }

        body{
            background:#0f172a;
            color:white;
            min-height:100vh;
        }

        .hero{
            background:linear-gradient(135deg,#2563eb,#7c3aed);
            padding:40px;
            text-align:center;
        }

        .container{
            width:90%;
            max-width:900px;
            margin:auto;
            margin-top:30px;
        }

        .card{
            background:#1e293b;
            padding:20px;
            border-radius:15px;
            margin-top:20px;
        }

        input{
            width:100%;
            padding:12px;
            margin-top:10px;
            border:none;
            border-radius:10px;
        }

        button{
            width:100%;
            padding:12px;
            margin-top:15px;
            border:none;
            border-radius:10px;
            background:#2563eb;
            color:white;
            cursor:pointer;
            font-size:16px;
        }

        button:hover{
            background:#1d4ed8;
        }

        .success{
            background:#10b981;
            padding:20px;
            border-radius:15px;
            text-align:center;
            margin-top:20px;
        }

        .grid{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:15px;
            margin-top:20px;
        }

        iframe{
            width:100%;
            height:300px;
            border:none;
            border-radius:15px;
        }

    </style>
</head>
<body>

<div class="hero">
    <h1>📸 Unfiltered Lens</h1>
    <h3>Unlock Creative Projects & Content</h3>
</div>

<div class="container">

{% if not registered %}

<div class="card">

    <h2>Register</h2>

    <form method="POST">

        <input
            type="text"
            name="name"
            placeholder="Enter your name"
            required
        >

        <input
            type="email"
            name="email"
            placeholder="Enter your email"
            required
        >

        <button type="submit">
            Unlock Projects
        </button>

    </form>

</div>

{% else %}

<div class="success">
    <h1>🎉 Welcome {{name}}</h1>
    <h2>🔓 Projects Unlocked Successfully</h2>
</div>

<div class="grid">

    <div class="card">
        <h2>🚀 AI Reel Generator</h2>
        <p>Create viral Instagram reels.</p>
    </div>

    <div class="card">
        <h2>🎨 Pencil Art Studio</h2>
        <p>Convert images into sketch art.</p>
    </div>

    <div class="card">
        <h2>📈 Instagram Growth Blueprint</h2>
        <p>Learn content growth strategies.</p>
    </div>

</div>

<div class="card">
    <h2>📰 Latest News</h2>

    <p>
        Congratulations! You have unlocked
        premium creator resources from
        Unfiltered Lens.
    </p>

    <br>

    <p>
        New AI-powered editing tools and
        viral content frameworks are now
        available for creators.
    </p>
</div>

<div class="card">

    <h2>🎥 Tutorial Videos</h2>

    <br>

    <iframe
    src="https://www.youtube.com/embed/wexY1fURaTs">
    </iframe>

    <br><br>

    <iframe
    src="https://www.youtube.com/embed/C3jlOlzSL8I">
    </iframe>

</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")

        return render_template_string(
            HTML,
            registered=True,
            name=name
        )

    return render_template_string(
        HTML,
        registered=False
    )

if __name__ == "__main__":
    app.run(debug=True)