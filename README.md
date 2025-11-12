# Sentiment Analysis Web Application

## 📋 Project Description

A Flask web application that uses IBM Watson NLP (Natural Language Processing) API to perform real-time sentiment analysis. Users can input text and instantly receive sentiment classification (positive, negative, or neutral) along with a confidence score.

---

## 🎯 Features

- ✅ **Real-time sentiment analysis** using Watson NLP
- ✅ **Responsive web interface** with Bootstrap
- ✅ **Sentiment classification:** Positive, Negative, Neutral
- ✅ **Confidence score** for each prediction
- ✅ **Input validation** on both server and client side
- ✅ **Robust error handling**
- ✅ **Code meets standards:** Pylint 10/10
- ✅ **Unit tests included**

---

## 🏗️ Project Architecture

```
Sentiment-Analysis--Practice/
│
├── server.py                      # Main Flask server
├── test_sentiment_analysis.py     # Unit tests
├── README.md                      # Documentation
├── LICENSE                        # Apache 2.0 License
│
├── SentimentAnalysis/             # Analysis package
│   ├── __init__.py               # Package initialization
│   └── sentiment_analysis.py     # Analysis logic with Watson API
│
├── templates/                     # HTML templates
│   └── index.html                # User interface
│
└── static/                        # Static files
    └── mywebscript.js            # JavaScript AJAX logic
```

---

## 🔧 Technologies Used

### Backend:
- **Flask 3.x** - Python web framework
- **Requests** - HTTP client for Watson API
- **Python 3.8+** - Programming language

### Frontend:
- **HTML5** - Structure
- **Bootstrap 4.5** - Responsive styles
- **JavaScript (ES6+)** - Interactivity (AJAX with XMLHttpRequest)
- **jQuery 3.5.1** - DOM manipulation

### External API:
- **Watson NLP API** - IBM sentiment analysis service

### Quality Tools:
- **Pylint** - Static code analysis
- **Unittest** - Testing framework

---

## 📦 Installation

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (to access Watson API)

### Step 1: Clone the repository
```bash
git clone <repository-url>
cd Sentiment-Analysis--Practice
```

### Step 2: Create virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install flask requests
```

---

## 🚀 Usage

### Run the server:

**On Windows:**
```powershell
python server.py
```

**On Linux/Mac or IBM Skills Network Labs:**
```bash
python3 server.py
```

### Access the application:

Open your browser at:
```
http://localhost:5000
```
or
```
http://127.0.0.1:5000
```

### Use the application:

1. Enter text in the text area
2. Click "Analyze Sentiment"
3. Wait for the result which will show:
   - **Sentiment:** positive/negative/neutral
   - **Score:** confidence level (0.0 - 1.0)

**Examples:**
```
Input: "I love working with Python!"
Output: The given text has been identified as positive with a score of 0.92

Input: "This is terrible and awful"
Output: The given text has been identified as negative with a score of 0.87

Input: "Python is a programming language"
Output: The given text has been identified as neutral with a score of 0.15
```

---

## 🧪 Testing

### Run unit tests:

```bash
# Windows
python test_sentiment_analysis.py

# Linux/Mac
python3 test_sentiment_analysis.py
```

### Included tests:

- ✅ **Positive** sentiment test
- ✅ **Negative** sentiment test
- ✅ **Neutral** sentiment test

**Expected result:**
```
...
----------------------------------------------------------------------
Ran 3 tests in 2.345s

OK
```

---

## 📊 Code Analysis with Pylint

### Run analysis:

```bash
# Analyze all files
pylint server.py
pylint test_sentiment_analysis.py
pylint SentimentAnalysis/

# Analyze specific files
pylint SentimentAnalysis/sentiment_analysis.py
pylint SentimentAnalysis/__init__.py
```

### Current ratings:
- ✅ `server.py`: **10.00/10**
- ✅ `test_sentiment_analysis.py`: **10.00/10**
- ✅ `sentiment_analysis.py`: **10.00/10**
- ✅ `__init__.py`: **10.00/10**

---

## 🔌 API Endpoints

### GET /
- **Description:** Renders the main page
- **Response:** User interface HTML

### GET /sentimentAnalyzer
- **Description:** Analyzes the sentiment of provided text
- **Query Parameters:**
  - `textToAnalyze` (string, required): Text to analyze
- **Responses:**
  - **200 OK:** Text with analysis result
  - **400 Bad Request:** Invalid or empty input
  - **500 Internal Server Error:** Watson service error

**Usage example:**
```
GET /sentimentAnalyzer?textToAnalyze=I%20love%20Python
```

**Response:**
```
The given text has been identified as positive with a score of 0.95.
```

---

## 📁 Main Files Description

### `server.py`
Main Flask server that:
- Defines application routes
- Handles HTTP requests
- Processes sentiment analysis data
- Manages 404 and 500 errors

### `SentimentAnalysis/sentiment_analysis.py`
Analysis module that:
- Connects to Watson NLP API
- Sends POST requests with text to analyze
- Processes JSON responses
- Handles connection and parsing errors
- Returns dictionaries with `label` and `score`

### `templates/index.html`
User interface that:
- Provides form for text input
- Includes Bootstrap for responsive design
- Displays analysis results
- Loads JavaScript script

### `static/mywebscript.js`
JavaScript script that:
- Captures user text
- Makes AJAX requests (XMLHttpRequest)
- Updates DOM with results
- Handles network errors

### `test_sentiment_analysis.py`
Test suite that:
- Verifies correct analyzer functionality
- Tests positive, negative, and neutral cases
- Uses `unittest` framework

---

## 🌐 Watson NLP API

### Endpoint used:
```
https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict
```

### Model:
- **sentiment_aggregated-bert-workflow_lang_multi_stock**
- Multilingual BERT model trained for sentiment analysis

### Response format:
```json
{
  "documentSentiment": {
    "label": "SENT_POSITIVE",
    "score": 0.95
  }
}
```

### Possible labels:
- `SENT_POSITIVE` - Positive sentiment
- `SENT_NEGATIVE` - Negative sentiment
- `SENT_NEUTRAL` - Neutral sentiment

---

## ⚠️ Important Considerations

### API Access:
- ⚠️ Watson API **only works within IBM Skills Network Labs**
- ❌ **NOT accessible** from public internet
- ❌ **Does NOT work** on local machines outside the course
- ✅ **Works** in Coursera/IBM lab environment

### For local development:
If you need to develop locally, consider using alternatives such as:
- **TextBlob** - Python NLP library
- **VADER** - Lexicon-based sentiment analyzer
- **Public Watson API** (requires IBM Cloud account)

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### Error: "ModuleNotFoundError: No module named 'requests'"
```bash
pip install requests
```

### Error: "Connection timeout" or "Max retries exceeded"
- Verify you are running on **IBM Skills Network Labs**
- The API does not work outside the course environment

### Error: "Invalid input! Try again."
- Make sure to enter non-empty text
- Verify the text doesn't contain only spaces

### Tests fail with "AssertionError: None != 'SENT_POSITIVE'"
- Watson API is not responding
- Run tests from IBM Skills Network Labs

---

## 📚 Data Flow Structure

```
User enters text
    ↓
JavaScript captures input
    ↓
AJAX sends GET request to /sentimentAnalyzer
    ↓
Flask receives request
    ↓
sentiment_analyzer() calls Watson API
    ↓
Watson processes with BERT model
    ↓
JSON response with label and score
    ↓
Flask formats response as text
    ↓
JavaScript receives response
    ↓
DOM updated with result
    ↓
User sees the result
```

---

## 👥 Contributions

This is an educational project from the IBM course on Coursera: **"Developing AI Applications with Python and Flask"**.

---

## 📄 License

This project is under the **Apache License 2.0**. See `LICENSE` file for more details.

---

## 🎓 Credits

- **IBM Skills Network** - Provider of Watson NLP API
- **Coursera** - Educational platform
- **IBM** - Developer of BERT sentiment model

---

## 🔄 Version

**v1.0.0** - Initial version of the practice project

---

## 📝 Additional Notes

- The project is designed for **educational purposes**
- Not suitable for **production** without modifications
- Watson API is **free only for course students**
- Code complies with **PEP 8** and Python quality standards

---

**Enjoy analyzing sentiments with Watson NLP! 🎉🤖📊**