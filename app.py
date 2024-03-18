from flask import Flask, request, jsonify, render_template
import language_tool_python


app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')

""" # Render the HTML form
@app.route('/')
def index():
    return render_template('index.html') """

# Endpoint for processing text
@app.route('/process', methods=['POST'])
def process_text():
    data = request.form
    input_text = data['text']

    # Perform grammar correction
    corrected_text = tool.correct(input_text)

    return jsonify({"processed_text": corrected_text})

if __name__ == '__main__':
    app.run()
