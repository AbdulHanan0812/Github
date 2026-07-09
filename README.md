# Alenan AI Resume Analyzer & Career Copilot
Test Link : 

An intelligent web application built with **Flask**, **SQLAlchemy**, and **OpenRouter (Llama 3)** that allows users to upload their resumes, parse the text dynamically, and get standard corporate-level screening feedback, tailored roadmaps, and custom interview preparation questions. It also includes an interactive AI Career Mentor Chat.

---

##  Key Features

* **Secure Authentication System:** User signup, login, and secure session management.
* **Smart Resume Parsing:** Supports dynamic text extraction from both `.pdf` and `.docx` formats, alongside manual text insertion.
* **Deep AI Evaluation:** Tailored analysis filtering out current skills, identifying missing gaps based on target corporate roles, and generating structured roadmaps.
* **Interactive AI Career Mentor:** A live chat system providing instant career guidance and technical domain advice.
* **Persistent History Log:** Beautifully sequences previous evaluations straight from the database into clean, readable point-by-point blocks.
* **Production-Ready Security:** API credentials completely isolated using environment variables (`.env`).

---

##  Tech Stack & Libraries

* **Backend Framework:** Flask (Python)
* **Database & ORM:** SQLite, SQLAlchemy
* **AI Integration:** OpenAI SDK connected via OpenRouter API (`meta-llama/llama-3-8b-instruct`)
* **File Processing:** PyPDF2, python-docx
* **Environment Security:** python-dotenv

---

##  Getting Started

Follow these simple steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/AI-Resume-Analyzer-project.git](https://github.com/your-username/AI-Resume-Analyzer-project.git)
cd AI-Resume-Analyzer-project
.
