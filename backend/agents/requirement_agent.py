def analyze_project(project_description: str):
    description = project_description.lower()

    requirements = []
    modules = []
    skills = []
    categories = []

    # ---------------------------------
    # AI / MACHINE LEARNING
    # ---------------------------------
    if any(word in description for word in [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        " ai ",
        " ml ",
        "prediction",
        "predictive"
    ]):
        categories.append("AI / Machine Learning")

        requirements.extend([
            "Data collection",
            "Data preprocessing",
            "Machine learning model",
            "Model training",
            "Prediction and evaluation"
        ])

        modules.extend([
            "Data Collection",
            "Data Preprocessing",
            "Model Training",
            "Prediction",
            "Result Analysis"
        ])

        skills.extend([
            "Python",
            "Machine Learning",
            "Data Processing",
            "Model Evaluation"
        ])

    # ---------------------------------
    # COMPUTER VISION
    # ---------------------------------
    if any(word in description for word in [
        "image",
        "image classification",
        "computer vision",
        "object detection",
        "face detection",
        "face recognition",
        "opencv",
        "video processing",
        "waste classification"
    ]):
        categories.append("Computer Vision")

        requirements.extend([
            "Image or video input",
            "Image preprocessing",
            "Feature extraction",
            "Computer vision processing",
            "Classification or detection output"
        ])

        modules.extend([
            "Image / Video Input",
            "Image Processing",
            "Feature Extraction",
            "Computer Vision Processing",
            "Result Display"
        ])

        skills.extend([
            "Python",
            "Computer Vision",
            "OpenCV",
            "Machine Learning",
            "Data Processing"
        ])

    # ---------------------------------
    # WEB DEVELOPMENT
    # ---------------------------------
    if any(word in description for word in [
        "website",
        "web application",
        "web app",
        "web development",
        "frontend",
        "backend",
        "html",
        "css",
        "javascript"
    ]):
        categories.append("Web Development")

        requirements.extend([
            "User interface",
            "Backend API",
            "Data management",
            "User interaction",
            "Testing"
        ])

        modules.extend([
            "Frontend",
            "Backend",
            "Database",
            "Authentication",
            "Testing"
        ])

        skills.extend([
            "HTML",
            "CSS",
            "JavaScript",
            "Backend Development",
            "Database Basics"
        ])

    # ---------------------------------
    # MOBILE APPLICATION
    # ---------------------------------
    if any(word in description for word in [
        "mobile app",
        "mobile application",
        "android",
        "android app",
        "ios",
        "flutter",
        "react native"
    ]):
        categories.append("Mobile Development")

        requirements.extend([
            "Mobile user interface",
            "Application logic",
            "Data storage",
            "User interaction",
            "Application testing"
        ])

        modules.extend([
            "Mobile Interface",
            "Application Logic",
            "Database",
            "Authentication",
            "Testing"
        ])

        skills.extend([
            "Mobile Development",
            "Programming",
            "Database Basics",
            "UI Design"
        ])

    # ---------------------------------
    # IOT
    # ---------------------------------
    if any(word in description for word in [
        "iot",
        "internet of things",
        "sensor",
        "smart device",
        "embedded",
        "arduino",
        "esp32",
        "raspberry pi"
    ]):
        categories.append("IoT")

        requirements.extend([
            "Sensor or device input",
            "Data collection",
            "Device communication",
            "Data processing",
            "Monitoring system"
        ])

        modules.extend([
            "Sensor Module",
            "Data Collection",
            "Device Communication",
            "Data Processing",
            "Monitoring Dashboard"
        ])

        skills.extend([
            "IoT",
            "Programming",
            "Sensors",
            "Data Processing",
            "Embedded Systems"
        ])

    # ---------------------------------
    # DATA SCIENCE
    # ---------------------------------
    if any(word in description for word in [
        "data science",
        "data analysis",
        "data analytics",
        "dataset",
        "data visualization",
        "analytics"
    ]):
        categories.append("Data Science")

        requirements.extend([
            "Dataset collection",
            "Data cleaning",
            "Data analysis",
            "Data visualization",
            "Insight generation"
        ])

        modules.extend([
            "Data Collection",
            "Data Cleaning",
            "Data Analysis",
            "Visualization",
            "Report Generation"
        ])

        skills.extend([
            "Python",
            "Data Analysis",
            "Pandas",
            "Data Visualization",
            "Statistics"
        ])

    # ---------------------------------
    # CYBERSECURITY
    # ---------------------------------
    if any(word in description for word in [
        "cybersecurity",
        "cyber security",
        "network security",
        "intrusion detection",
        "phishing",
        "malware"
    ]):
        categories.append("Cybersecurity")

        requirements.extend([
            "Security analysis",
            "Threat detection",
            "Data monitoring",
            "Security validation",
            "Alert generation"
        ])

        modules.extend([
            "Data Monitoring",
            "Threat Detection",
            "Security Analysis",
            "Alert System",
            "Reporting"
        ])

        skills.extend([
            "Cybersecurity",
            "Networking",
            "Programming",
            "Security Fundamentals"
        ])

    # ---------------------------------
    # DATABASE / MANAGEMENT SYSTEM
    # ---------------------------------
    if any(word in description for word in [
        "database",
        "management system",
        "student management",
        "inventory",
        "employee management",
        "hospital management",
        "library management"
    ]):
        categories.append("Database / Management System")

        requirements.extend([
            "User interface",
            "Database design",
            "Data storage",
            "Data retrieval",
            "Data validation"
        ])

        modules.extend([
            "User Interface",
            "Database",
            "Data Entry",
            "Data Management",
            "Reports"
        ])

        skills.extend([
            "Programming",
            "SQL",
            "Database Management",
            "Problem Solving"
        ])

    # ---------------------------------
    # AUTOMATION
    # ---------------------------------
    if any(word in description for word in [
        "automation",
        "automated system",
        "workflow",
        "task automation",
        "automate"
    ]):
        categories.append("Automation")

        requirements.extend([
            "Input processing",
            "Automation logic",
            "Task execution",
            "Error handling",
            "Result monitoring"
        ])

        modules.extend([
            "Input Module",
            "Automation Engine",
            "Task Execution",
            "Error Handling",
            "Monitoring"
        ])

        skills.extend([
            "Programming",
            "Automation",
            "Problem Solving",
            "API Integration"
        ])

    # ---------------------------------
    # GENERIC SOFTWARE PROJECT
    # ---------------------------------
    if not categories:
        categories.append("General Software")

        requirements.extend([
            "Requirement analysis",
            "Core application logic",
            "User interface",
            "Data management",
            "Testing"
        ])

        modules.extend([
            "User Interface",
            "Core Logic",
            "Data Management",
            "Testing"
        ])

        skills.extend([
            "Programming",
            "Problem Solving",
            "Database Basics"
        ])

    # ---------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------
    requirements = list(dict.fromkeys(requirements))
    modules = list(dict.fromkeys(modules))
    skills = list(dict.fromkeys(skills))
    categories = list(dict.fromkeys(categories))

    # ---------------------------------
    # DIFFICULTY CALCULATION
    # ---------------------------------
    if len(categories) >= 3:
        difficulty = "Advanced"
    elif "AI / Machine Learning" in categories or "Computer Vision" in categories:
        difficulty = "Intermediate"
    elif "Cybersecurity" in categories:
        difficulty = "Intermediate to Advanced"
    elif "Web Development" in categories or "Mobile Development" in categories:
        difficulty = "Beginner to Intermediate"
    else:
        difficulty = "Intermediate"

    return {
        "difficulty": difficulty,
        "requirements": requirements,
        "modules": modules,
        "required_skills": skills
    }