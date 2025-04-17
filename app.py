from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"  # Ensure this is set correctly

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500


@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.json
    course = data.get("course", "general")
    prompt = f"Generate a word guessing quiz question for {course}. Provide a hint."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    question = response["choices"][0]["message"]["content"]
    return jsonify({"question": question, "hint": "Think about its common use."})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    answer = data.get("answer", "").strip().lower()
    correct_answer = "example"  # Replace with logic to fetch correct answer
    return jsonify({"correct": answer == correct_answer})

if __name__ == '__main__':
    app.run(debug=True)
