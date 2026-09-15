def recommend_technologies(project_description, student_skills):

    description = project_description.lower()
    skills = [skill.lower().strip() for skill in student_skills]

    technologies = []
    reasons = []

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
        technologies.extend([
            "Python",
            "TensorFlow",
            "Scikit-learn",
            "Pandas",
            "NumPy"
        ])

        reasons.extend([
            "Python is widely suitable for AI and machine learning development.",
            "TensorFlow can be used to build and train deep learning models.",
            "Scikit-learn provides machine learning algorithms and model evaluation tools.",
            "Pandas can be used for dataset handling and data preprocessing.",
            "NumPy supports numerical and array-based operations."
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
        technologies.extend([
            "OpenCV",
            "TensorFlow"
        ])

        reasons.extend([
            "OpenCV can be used for image processing and computer vision tasks.",
            "TensorFlow can be used to develop image classification and detection models."
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
        technologies.extend([
            "HTML",
            "CSS",
            "JavaScript",
            "FastAPI",
            "SQLite"
        ])

        reasons.extend([
            "HTML can structure the web application interface.",
            "CSS can be used to design and style the user interface.",
            "JavaScript can provide frontend interaction and functionality.",
            "FastAPI can provide backend APIs and connect application services.",
            "SQLite is suitable for storing data in a small college project."
        ])

    # ---------------------------------
    # MOBILE DEVELOPMENT
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
        technologies.extend([
            "Flutter",
            "Dart",
            "Firebase"
        ])

        reasons.extend([
            "Flutter can be used to build cross-platform mobile applications.",
            "Dart is the programming language used by Flutter.",
            "Firebase can provide authentication, database and cloud services."
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
        technologies.extend([
            "Arduino",
            "ESP32",
            "Python",
            "MQTT"
        ])

        reasons.extend([
            "Arduino can be used for sensor and embedded system development.",
            "ESP32 provides Wi-Fi and Bluetooth capabilities for IoT projects.",
            "Python can be used for IoT data processing and backend integration.",
            "MQTT can support communication between IoT devices and applications."
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
        technologies.extend([
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Scikit-learn"
        ])

        reasons.extend([
            "Python provides a flexible environment for data science.",
            "Pandas can be used for data cleaning and analysis.",
            "NumPy supports numerical data processing.",
            "Matplotlib can create data visualizations.",
            "Scikit-learn can support machine learning and predictive analysis."
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
        technologies.extend([
            "Python",
            "Wireshark",
            "Linux"
        ])

        reasons.extend([
            "Python can be used to develop security analysis and automation tools.",
            "Wireshark can help analyze network traffic.",
            "Linux provides a useful environment for cybersecurity development and testing."
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
        technologies.extend([
            "FastAPI",
            "SQLite",
            "SQL"
        ])

        reasons.extend([
            "FastAPI can provide backend APIs for the management system.",
            "SQLite is lightweight and suitable for small-scale applications.",
            "SQL can be used to create, retrieve and manage structured data."
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
        technologies.extend([
            "Python",
            "FastAPI"
        ])

        reasons.extend([
            "Python can implement automation logic and task processing.",
            "FastAPI can expose automation features through backend APIs."
        ])

    # ---------------------------------
    # DEFAULT TECHNOLOGIES
    # ---------------------------------
    if not technologies:
        technologies.extend([
            "Python",
            "FastAPI",
            "HTML",
            "CSS",
            "JavaScript",
            "SQLite"
        ])

        reasons.extend([
            "Python provides simple and flexible application development.",
            "FastAPI can be used to build backend APIs.",
            "HTML and CSS can create the user interface.",
            "JavaScript can provide frontend interaction.",
            "SQLite is suitable for storing project data."
        ])

    # ---------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------
    technologies = list(dict.fromkeys(technologies))
    reasons = list(dict.fromkeys(reasons))

    # ---------------------------------
    # MATCH STUDENT SKILLS
    # ---------------------------------
    matched_skills = []

    for technology in technologies:
        technology_lower = technology.lower()

        for skill in skills:
            if (
                technology_lower == skill
                or technology_lower in skill
                or skill in technology_lower
            ):
                matched_skills.append(technology)
                break

    matched_skills = list(dict.fromkeys(matched_skills))

    return {
        "recommended_technologies": technologies,
        "reasons": reasons,
        "student_skill_matches": matched_skills
    }