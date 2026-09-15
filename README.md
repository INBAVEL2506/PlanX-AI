\# 🚀 PlanX AI



\### AI-Powered Personalized Student Project Planning \& Development System



PlanX AI is an intelligent multi-agent project planning system designed to help students transform their project ideas into structured, personalized, and achievable development plans.



Instead of giving students a generic project roadmap, PlanX AI analyzes the student's skills, experience, interests, project requirements, available time, and constraints to generate a customized project plan.



\---



\## 🎯 Problem Statement



Students often have difficulty converting a project idea into a practical development plan.



Common challenges include:



\- Understanding project requirements

\- Identifying the technologies required

\- Knowing which skills they need to learn

\- Estimating how much time each phase will take

\- Finding suitable learning resources

\- Breaking a large project into manageable tasks

\- Maintaining a structured daily development roadmap



PlanX AI addresses these challenges by combining multiple specialized planning agents into one system.



\---



\## 💡 Proposed Solution



PlanX AI analyzes both the \*\*student profile\*\* and \*\*project requirements\*\* and generates a personalized development roadmap.



The system performs:



1\. Project requirement analysis

2\. Technology recommendation

3\. Skill-gap identification

4\. Project timeline generation

5\. Personalized learning planning

6\. Learning resource recommendation

7\. Daily project execution planning



\---



\## 🤖 Multi-Agent Architecture



PlanX AI uses multiple specialized agents, with each agent responsible for a specific planning task.



```text

&#x20;                   ┌──────────────────────┐

&#x20;                   │      Student         │

&#x20;                   │       Profile        │

&#x20;                   └──────────┬───────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌──────────────────────┐

&#x20;                   │     Project Idea     │

&#x20;                   └──────────┬───────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │   Requirement Agent        │

&#x20;                │ Requirements \& Skills     │

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │   Technology Agent        │

&#x20;                │ Technology Recommendations│

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │     Planning Agent        │

&#x20;                │ Timeline \& Project Phases │

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │     Learning Agent        │

&#x20;                │ Personalized Skill Plan   │

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │     Resource Agent        │

&#x20;                │ Learning Resources        │

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                ┌───────────────────────────┐

&#x20;                │    Execution Agent        │

&#x20;                │ Daily Execution Roadmap   │

&#x20;                └─────────────┬─────────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌──────────────────────┐

&#x20;                   │ Personalized Project │

&#x20;                   │       Roadmap        │

&#x20;                   └──────────────────────┘

🧠 AI Agents

1\. Requirement Agent



Analyzes the project description and identifies:



Project requirements

Required modules

Required technical skills

Project category

Estimated difficulty

2\. Technology Agent



Recommends suitable technologies based on the project requirements.



It also compares the recommended technologies with the student's existing skills.



3\. Planning Agent



Creates an adaptive project timeline based on:



Available project duration

Project difficulty

Student skills

Required skills

Skill gaps



The timeline is divided into development phases.



4\. Learning Agent



Identifies the skills the student needs to learn and creates a personalized learning plan.



Existing skills are not unnecessarily added to the learning plan.



5\. Resource Agent



Recommends learning resources for the identified skill gaps.



Examples include:



Documentation

Courses

Tutorials

Practice tasks

6\. Execution Agent



Converts the project phases into a daily execution roadmap.



Each day contains a specific task and status.



✨ Key Features

👨‍🎓 Student profile analysis

📋 Automated project requirement analysis

🛠️ Technology recommendations

🧠 Skill-gap analysis

📅 Adaptive project planning

📚 Personalized learning roadmap

🔗 Learning resource recommendations

🗓️ Daily execution roadmap

📥 Downloadable project plan

📄 PDF generation

🖨️ Print project plan

🔄 Plan another project

🌙 Modern dark-themed user interface

📱 Responsive frontend design

🛠️ Technology Stack

Frontend

HTML5

CSS3

JavaScript

Backend

Python

FastAPI

Uvicorn

AI / Planning Logic

Python-based multi-agent architecture

Rule-based project analysis

Skill-gap analysis

Adaptive planning logic

Development Tools

Visual Studio Code

Git

GitHub

Python Virtual Environment

🏗️ Project Structure

PlanX-AI/

│

├── backend/

│   │

│   ├── agents/

│   │   ├── execution\_agent.py

│   │   ├── learning\_agent.py

│   │   ├── planning\_agent.py

│   │   ├── requirement\_agent.py

│   │   ├── resource\_agent.py

│   │   └── technology\_agent.py

│   │

│   ├── frontend/

│   │   ├── index.html

│   │   ├── script.js

│   │   └── style.css

│   │

│   ├── main.py

│   ├── models.py

│   └── requirements.txt

│

├── .gitignore

└── README.md

⚙️ How PlanX AI Works



The user provides:



Student name

Academic year

Existing skills

Experience level

Interests

Project name

Project description

Project type

Available development days

Technology preferences

Project constraints



PlanX AI processes this information through its specialized agents.



The system then produces:



Project Analysis

&#x20;      ↓

Required Skills

&#x20;      ↓

Technology Recommendations

&#x20;      ↓

Skill Gap

&#x20;      ↓

Learning Plan

&#x20;      ↓

Project Timeline

&#x20;      ↓

Learning Resources

&#x20;      ↓

Daily Execution Roadmap

🚀 Installation \& Setup

1\. Clone the repository

git clone https://github.com/INBAVEL2506/PlanX-AI.git

2\. Open the project

cd PlanX-AI

3\. Create a Python virtual environment

cd backend

py -m venv venv

4\. Activate the virtual environment



On Windows PowerShell:



.\\venv\\Scripts\\Activate.ps1



If PowerShell blocks script execution:



Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass



Then activate again:



.\\venv\\Scripts\\Activate.ps1

5\. Install dependencies

pip install -r requirements.txt

▶️ Running the Backend



From:



PlanX-AI/backend



run:



python -m uvicorn main:app --reload



The backend will run at:



http://127.0.0.1:8000

🌐 Running the Frontend



Open a second terminal.



Navigate to:



cd D:\\PlanX-AI\\backend\\frontend



Run:



py -m http.server 5500



Open:



http://127.0.0.1:5500

🔌 Frontend–Backend Connection



The frontend communicates with the FastAPI backend through:



Frontend

http://127.0.0.1:5500

&#x20;       │

&#x20;       │ POST /project

&#x20;       ▼

Backend

http://127.0.0.1:8000



This allows the frontend to send student and project information to the backend and receive the generated project roadmap.



📊 Example Project

Project



AI Waste Classification



Student Skills

Java

Python

HTML

CSS

Experience

Beginner

Project Duration

45 Days

Required Skills Identified

Machine Learning

Data Processing

Model Evaluation

Computer Vision

OpenCV

Recommended Technologies

Python

TensorFlow

Scikit-learn

Pandas

NumPy

OpenCV

Generated Planning Phases

Requirement Analysis          → 3 Days

Skill Development             → 8 Days

Research \& Data Preparation   → 6 Days

Core Development              → 9 Days

Backend Development           → 5 Days

Frontend Development          → 5 Days

Testing \& Improvement         → 5 Days

Documentation \& Presentation  → 4 Days



Total:



45 Days

📄 Generated Output



PlanX AI generates:



Project difficulty

Required skills

Skill gaps

Recommended technologies

Learning plan

Learning resources

Development phases

Daily execution roadmap

Project timeline



The generated plan can also be:



Downloaded

Exported as PDF

Printed

Replaced with a new project plan

🔐 Security \& Privacy



The current prototype is designed for local development.



Important practices:



Virtual environments are excluded from Git

Environment files are excluded from Git

Secrets should never be committed

API keys should be stored in environment variables

Personal project information should be handled responsibly

⚠️ Current Limitations



The current version of PlanX AI uses rule-based intelligent agents rather than large language model-powered autonomous agents.



Current planning decisions are primarily based on predefined rules, keyword matching, skill mappings, and adaptive planning logic.



🔮 Future Enhancements



Future versions can include:



🤖 LLM-powered project analysis

🧠 More advanced autonomous agents

🎯 Personalized AI project recommendations

📊 Student progress tracking

🔄 Dynamic roadmap adjustment

💬 AI project mentor/chatbot

📈 Project performance analytics

👥 Team project planning

☁️ Cloud deployment

🔐 User authentication

🗄️ MongoDB database integration

📱 Mobile application

🎓 College project recommendation system

🎓 Academic Purpose



PlanX AI is developed as an academic project to explore:



Artificial Intelligence

Multi-Agent Systems

Software Engineering

Personalized Learning

Project Management

Web Application Development

Intelligent Decision Support Systems

👨‍💻 Author



INBAVEL V



Computer Science Engineering Student



GitHub:

https://github.com/INBAVEL2506



LinkedIn:

https://www.linkedin.com/in/inbavel-v-057a7a384



Portfolio:

https://inbavel-v-portfolio.lovable.app



⭐ Project Status

Version: 1.0.0

Status: Working Prototype



PlanX AI is continuously being improved with new intelligent planning capabilities and user-focused features.



📜 License



This project is currently intended for academic and educational purposes.

