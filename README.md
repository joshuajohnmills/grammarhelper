A simple web-based quiz application that generates language practice questions using OpenAI's GPT API. The app randomly selects a topic and exercise from predefined files, creates a concise quiz question (in French or involving English-to-French translation), and then validates your answer with detailed feedback.


## Features
### Dynamic Question Generation:
Uses OpenAI's GPT model to generate a single-line grammar practice question based on randomly selected topics and exercises.

### Interactive Quiz Interface:
A user-friendly web interface where you can view questions, submit answers, and receive immediate feedback.

### Answer Feedback:
When you submit an answer, the app evaluates it via OpenAI and returns the correct answer with an explanation in English, including praise if your answer is correct.

### Status Dashboard:
Displays status numbers indicating the remaining questions, revisions, and recaps.

### Prereqs
Python 3.7+
Flask
OpenAI Python Library
You will also need an OpenAI API key. Make sure you have it set as an environment variable or configure it as required in your application.

### Installation

```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows use: set OPENAI_API_KEY=your-api-key-here
```

Alternatively, update the code in question_generator.py to include your API key as needed.
Running the Application
Start the Flask application by running:

```bash
python app.py
```
The app will run on http://127.0.0.1:5000/ by default. Open this URL in your browser to begin the quiz.



### How it works
When you click the "Get Question" button, the front-end sends a request to the /question endpoint.
The TopicGenerator randomly selects a topic and exercise from the topics directory.
The QuestionGenerator uses OpenAI's GPT model to generate a quiz question based on the selected topic.
The generated question is displayed on the web page.

### Answer Submission and Feedback:

Enter your answer in the input field and click "Submit Answer".
The answer is sent to the /answer endpoint, where the QuestionGenerator evaluates your answer with OpenAI.
The server responds with the correct answer, a breakdown explanation, and praise if your answer is correct, which is then displayed on the page.
Status Numbers:

**TODO:** 
- Add proper scheduling for the cards using something like the `fsrs` library
- Implment statelessness in the application and a proper database