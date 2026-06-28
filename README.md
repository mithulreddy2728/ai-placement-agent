# AI Placement Preparation Agent

An AI-powered web application that helps students prepare for technical placements through personalized interview practice, company-specific questions, progress tracking, and AI-generated study plans.

## Features

- User Authentication
- Company-specific Interview Preparation
- AI Mock Interviews
- Resume Analysis
- Personalized Study Plans
- Progress Dashboard
- Secure Password Hashing
- REST API with FastAPI
- MySQL Database Integration

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy

### Database
- MySQL

### AI
- Google Gemini API
- LangChain (planned)

### Tools
- Git
- GitHub
- VS Code

---

## Project Structure

```
ai-placement-agent/
│
├── backend/
│   ├── database/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│
├── docs/
│
└── README.md
```

---

## Current Progress

- [x] Project structure
- [x] GitHub repository
- [x] FastAPI setup
- [x] MySQL connection
- [x] SQLAlchemy integration
- [ ] User Registration
- [ ] JWT Authentication
- [ ] Resume Upload
- [ ] AI Interview Generator
- [ ] Study Plan Generator
- [ ] Progress Dashboard
- [ ] Frontend Integration

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mithulreddy2728/ai-placement-agent.git
```

Navigate to the project:

```bash
cd ai-placement-agent
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## Author

**Mithilesh Reddy**

GitHub:
https://github.com/mithulreddy2728
