from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Text Analyzer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f3ff;
            margin: 0;
            padding: 40px 15px;
        }

        .container {
            max-width: 750px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px #d5d5e5;
        }

        h1 {
            text-align: center;
            color: #5145cd;
        }

        p {
            text-align: center;
            color: #666;
        }

        textarea {
            width: 100%;
            height: 180px;
            padding: 12px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
            resize: vertical;
        }

        button {
            background: #5145cd;
            color: white;
            border: none;
            padding: 12px 22px;
            margin: 12px 5px;
            border-radius: 7px;
            cursor: pointer;
            font-size: 15px;
        }

        button:hover {
            background: #372ca8;
        }

        .buttons {
            text-align: center;
        }

        .results {
            margin-top: 25px;
            padding: 20px;
            background: #f1f0ff;
            border-radius: 10px;
        }

        .results h2 {
            color: #5145cd;
        }

        .result-item {
            background: white;
            padding: 12px;
            margin: 8px 0;
            border-radius: 6px;
        }

        .message {
            color: green;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Text Analyzer</h1>
    <p>Analyze your text quickly and easily!</p>

    <form method="POST">

        <textarea name="text"
        placeholder="Enter or paste your text here..."
        required>{{ text }}</textarea>

        <div class="buttons">
            <button type="submit" name="action"
            value="save">Save Text</button>

            <button type="submit" name="action"
            value="analyze">Analyze Text</button>
        </div>

    </form>

    {% if message %}
        <p class="message">{{ message }}</p>
    {% endif %}

    {% if results %}
    <div class="results">

        <h2>Analysis Results</h2>

        <div class="result-item">
            Total Words: {{ results.words }}
        </div>

        <div class="result-item">
            Total Characters: {{ results.characters }}
        </div>

        <div class="result-item">
            Total Lines: {{ results.lines }}
        </div>

        <div class="result-item">
            Longest Word: {{ results.longest }}
        </div>

    </div>
    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    text = ""
    message = ""
    results = None

    if request.method == "POST":

        text = request.form.get("text", "")
        action = request.form.get("action")

        if action == "save":

            with open("text.txt", "w") as file:
                file.write(text)

            message = "Text saved successfully!"

        elif action == "analyze":

            words = text.split()
            lines = text.splitlines()

            if words:
                longest = max(words, key=len)
            else:
                longest = "No words found"

            results = {
                "words": len(words),
                "characters": len(text),
                "lines": len(lines),
                "longest": longest
            }

    return render_template_string(
        HTML,
        text=text,
        message=message,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)
