def create_learning_plan(skill_gap, experience_level):

    learning_resources = {

        "Python": {
            "topics": [
                "Python fundamentals",
                "Functions and modules",
                "Lists, dictionaries and data structures",
                "File handling and error handling"
            ],
            "duration": 3
        },

        "Machine Learning": {
            "topics": [
                "Machine Learning fundamentals",
                "Classification algorithms",
                "Model training",
                "Model evaluation"
            ],
            "duration": 4
        },

        "Computer Vision": {
            "topics": [
                "Computer vision fundamentals",
                "Image representation",
                "Image preprocessing",
                "Basic image analysis"
            ],
            "duration": 3
        },

        "OpenCV": {
            "topics": [
                "Image reading",
                "Image resizing",
                "Image preprocessing",
                "Image manipulation"
            ],
            "duration": 3
        },

        "Data Processing": {
            "topics": [
                "Dataset cleaning",
                "Data organization",
                "Train and test data splitting",
                "Data preprocessing"
            ],
            "duration": 3
        },

        "Model Evaluation": {
            "topics": [
                "Model performance metrics",
                "Accuracy and precision",
                "Recall and F1-score",
                "Confusion matrix"
            ],
            "duration": 2
        },

        "Pandas": {
            "topics": [
                "DataFrames and Series",
                "Loading datasets",
                "Data filtering",
                "Data cleaning"
            ],
            "duration": 2
        },

        "NumPy": {
            "topics": [
                "Arrays",
                "Array operations",
                "Numerical calculations",
                "Data manipulation"
            ],
            "duration": 2
        },

        "Scikit-learn": {
            "topics": [
                "Machine learning algorithms",
                "Training models",
                "Train-test splitting",
                "Model evaluation"
            ],
            "duration": 3
        },

        "TensorFlow": {
            "topics": [
                "TensorFlow fundamentals",
                "Neural network basics",
                "Model training",
                "Model prediction"
            ],
            "duration": 4
        },

        "HTML": {
            "topics": [
                "HTML structure",
                "Forms and input elements",
                "Semantic HTML",
                "Building web pages"
            ],
            "duration": 2
        },

        "CSS": {
            "topics": [
                "CSS fundamentals",
                "Selectors and properties",
                "Layouts",
                "Responsive design"
            ],
            "duration": 2
        },

        "JavaScript": {
            "topics": [
                "JavaScript fundamentals",
                "Variables and functions",
                "DOM manipulation",
                "Event handling"
            ],
            "duration": 3
        },

        "Backend Development": {
            "topics": [
                "Backend fundamentals",
                "REST APIs",
                "Request and response handling",
                "API integration"
            ],
            "duration": 3
        },

        "Database Basics": {
            "topics": [
                "Database fundamentals",
                "Tables and relationships",
                "CRUD operations",
                "Basic database design"
            ],
            "duration": 3
        },

        "SQL": {
            "topics": [
                "SQL fundamentals",
                "SELECT queries",
                "INSERT, UPDATE and DELETE",
                "Filtering and sorting data"
            ],
            "duration": 2
        },

        "Programming": {
            "topics": [
                "Programming fundamentals",
                "Variables and data types",
                "Conditions and loops",
                "Functions and problem solving"
            ],
            "duration": 3
        },

        "Problem Solving": {
            "topics": [
                "Problem decomposition",
                "Logical thinking",
                "Algorithm design",
                "Debugging techniques"
            ],
            "duration": 2
        },

        "Mobile Development": {
            "topics": [
                "Mobile application fundamentals",
                "UI design",
                "Application navigation",
                "Mobile application testing"
            ],
            "duration": 4
        },

        "IoT": {
            "topics": [
                "IoT fundamentals",
                "Sensors and devices",
                "Device communication",
                "IoT data processing"
            ],
            "duration": 4
        },

        "Cybersecurity": {
            "topics": [
                "Cybersecurity fundamentals",
                "Common security threats",
                "Network security basics",
                "Security best practices"
            ],
            "duration": 4
        },

        "Networking": {
            "topics": [
                "Networking fundamentals",
                "IP addresses",
                "Network protocols",
                "Basic network troubleshooting"
            ],
            "duration": 3
        },

        "Statistics": {
            "topics": [
                "Statistics fundamentals",
                "Mean and standard deviation",
                "Probability basics",
                "Data interpretation"
            ],
            "duration": 3
        },

        "Data Analysis": {
            "topics": [
                "Data analysis fundamentals",
                "Data exploration",
                "Finding patterns in data",
                "Generating insights"
            ],
            "duration": 3
        },

        "Data Visualization": {
            "topics": [
                "Visualization fundamentals",
                "Charts and graphs",
                "Choosing suitable visualizations",
                "Presenting data insights"
            ],
            "duration": 2
        },

        "Automation": {
            "topics": [
                "Automation fundamentals",
                "Task automation",
                "Workflow design",
                "Error handling"
            ],
            "duration": 3
        },

        "API Integration": {
            "topics": [
                "API fundamentals",
                "HTTP requests",
                "Working with JSON",
                "Connecting external services"
            ],
            "duration": 2
        }
    }

    learning_plan = []

    # ---------------------------------
    # EXPERIENCE LEVEL FACTOR
    # ---------------------------------

    experience = experience_level.lower()

    if "beginner" in experience:
        duration_factor = 1.0
    elif "intermediate" in experience:
        duration_factor = 0.8
    elif "advanced" in experience:
        duration_factor = 0.6
    else:
        duration_factor = 1.0

    # ---------------------------------
    # CREATE LEARNING PLAN
    # ---------------------------------

    for skill in skill_gap:

        if skill in learning_resources:

            base_duration = learning_resources[skill]["duration"]

            duration = max(
                1,
                round(base_duration * duration_factor)
            )

            learning_plan.append({
                "skill": skill,
                "experience_level": experience_level,
                "topics": learning_resources[skill]["topics"],
                "duration": duration
            })

    # ---------------------------------
    # HANDLE UNKNOWN SKILLS
    # ---------------------------------

    for skill in skill_gap:

        already_added = any(
            item["skill"].lower() == skill.lower()
            for item in learning_plan
        )

        if not already_added:

            learning_plan.append({
                "skill": skill,
                "experience_level": experience_level,
                "topics": [
                    f"Introduction to {skill}",
                    f"Fundamentals of {skill}",
                    f"Practical application of {skill}"
                ],
                "duration": 2
            })

    # ---------------------------------
    # TOTAL LEARNING DAYS
    # ---------------------------------

    total_learning_days = sum(
        item["duration"]
        for item in learning_plan
    )

    return {
        "experience_level": experience_level,
        "skills_to_learn": learning_plan,
        "total_learning_days": total_learning_days
    }


# ---------------------------------
# TESTING
# ---------------------------------

if __name__ == "__main__":

    skill_gap = [
        "Machine Learning",
        "OpenCV",
        "Data Processing",
        "Computer Vision"
    ]

    result = create_learning_plan(
        skill_gap,
        "Beginner"
    )

    print(result)