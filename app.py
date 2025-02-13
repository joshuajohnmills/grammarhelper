from flask import Flask, render_template, jsonify, request

from question_generator import QuestionGenerator

from topic_generator import TopicGenerator

app = Flask(__name__)


topic_generator = TopicGenerator()

question_generator = QuestionGenerator()

@app.route('/')
def quiz():
    return render_template('index.html')

@app.route('/numbers')
def numbers():
    # You can replace these hard-coded numbers with dynamic values as needed.
    data = {
        "questions_to_go": 10,
        "revisions_to_go": 5,
        "recaps_to_go": 2
    }
    return jsonify(data)

@app.route('/question')
def question():
    topic = topic_generator.get_topic()
    question = question_generator.get_question(topic)

    print(question)
    return jsonify({"question": question})

@app.route('/answer', methods=['POST'])
def answer():
    #get the data from the request
    data = request.get_json()
    print(data)
    #use the question generatorcorrect_question to get the correct answer
    correct_answer = question_generator.correct_question(data['answer'])
    return jsonify({"feedback": correct_answer})


if __name__ == '__main__':
    app.run(debug=True)
