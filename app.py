from flask import Flask, render_template, jsonify, request
import markov

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    title_order = int(request.form["title_slider"])
    people_order = int(request.form["people_slider"])
    project_order = int(request.form["project_slider"])

    new_title = markov.markov_generate_from_lines_in_file(title_order, "./nmnt/nmnt-title.txt", 1, "char", max_gen=200)
    new_people = markov.markov_generate_from_lines_in_file(people_order, "./nmnt/nmnt-people.txt", 1, "char", max_gen=200)
    new_project = markov.markov_generate_from_lines_in_file(project_order, "./nmnt/nmnt-content.txt", 1, "word", max_gen=1000)
    
    return jsonify({
        "new_title" : new_title[0],
        "new_people" : new_people[0],
        "new_project" : new_project[0]
    })


if __name__ == "__main__":
    app.run(debug=True)
