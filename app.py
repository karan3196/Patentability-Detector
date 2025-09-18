import os
import tempfile
import git
from flask import Flask, request, render_template
from code_analyzer.py import analyze_repo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    repo_url = ""
    if request.method == "POST":
        repo_url = request.form.get("repo_url")
        if repo_url:
            try:
                with tempfile.TemporaryDirectory() as tmpdirname:
                    git.Repo.clone_from(repo_url, tmpdirname)
                    result = analyze_repo(tmpdirname)
            except Exception as e:
                error = str(e)
    return render_template("index.html", result=result, error=error, repo_url=repo_url)

if __name__ == "__main__":
    app.run(debug=True)