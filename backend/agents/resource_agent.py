def recommend_resources(skills_to_learn, experience_level):

    resources = {

        "Python": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Python Documentation",
                    "url": "https://docs.python.org/3/"
                },
                {
                    "type": "Tutorial",
                    "title": "Python for Beginners",
                    "url": "https://www.python.org/about/gettingstarted/"
                }
            ],
            "practice_tasks": [
                "Practice variables and data types",
                "Write functions",
                "Work with lists and dictionaries",
                "Build a small Python program"
            ]
        },

        "Machine Learning": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Scikit-learn User Guide",
                    "url": "https://scikit-learn.org/stable/user_guide.html"
                },
                {
                    "type": "Tutorial",
                    "title": "Google Machine Learning Crash Course",
                    "url": "https://developers.google.com/machine-learning/crash-course"
                }
            ],
            "practice_tasks": [
                "Learn basic classification",
                "Train a simple classification model",
                "Evaluate model accuracy"
            ]
        },

        "Computer Vision": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "OpenCV Documentation",
                    "url": "https://docs.opencv.org/"
                }
            ],
            "practice_tasks": [
                "Understand basic computer vision concepts",
                "Read and process an image",
                "Apply basic image transformations",
                "Build a simple image processing program"
            ]
        },

        "OpenCV": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "OpenCV Documentation",
                    "url": "https://docs.opencv.org/"
                },
                {
                    "type": "Tutorial",
                    "title": "OpenCV Python Tutorials",
                    "url": "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html"
                }
            ],
            "practice_tasks": [
                "Read an image using OpenCV",
                "Resize an image",
                "Convert an image to grayscale",
                "Apply basic image preprocessing"
            ]
        },

        "Data Processing": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Pandas Documentation",
                    "url": "https://pandas.pydata.org/docs/"
                }
            ],
            "practice_tasks": [
                "Load a dataset",
                "Clean missing or invalid data",
                "Organize dataset data",
                "Split data into training and testing sets"
            ]
        },

        "Model Evaluation": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Scikit-learn Model Evaluation",
                    "url": "https://scikit-learn.org/stable/modules/model_evaluation.html"
                }
            ],
            "practice_tasks": [
                "Calculate model accuracy",
                "Understand precision and recall",
                "Calculate F1-score",
                "Interpret a confusion matrix"
            ]
        },

        "Pandas": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Pandas Documentation",
                    "url": "https://pandas.pydata.org/docs/"
                }
            ],
            "practice_tasks": [
                "Create a DataFrame",
                "Load a CSV dataset",
                "Filter and sort data",
                "Clean missing values"
            ]
        },

        "NumPy": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "NumPy Documentation",
                    "url": "https://numpy.org/doc/stable/"
                }
            ],
            "practice_tasks": [
                "Create NumPy arrays",
                "Perform array operations",
                "Practice numerical calculations",
                "Manipulate multidimensional arrays"
            ]
        },

        "Scikit-learn": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Scikit-learn User Guide",
                    "url": "https://scikit-learn.org/stable/user_guide.html"
                }
            ],
            "practice_tasks": [
                "Load a sample dataset",
                "Split data into training and testing sets",
                "Train a classification model",
                "Evaluate the trained model"
            ]
        },

        "TensorFlow": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "TensorFlow Documentation",
                    "url": "https://www.tensorflow.org/learn"
                }
            ],
            "practice_tasks": [
                "Learn TensorFlow basics",
                "Create a simple neural network",
                "Train a model",
                "Make predictions"
            ]
        },

        "HTML": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "MDN HTML Guide",
                    "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"
                }
            ],
            "practice_tasks": [
                "Create an HTML page",
                "Build forms",
                "Use semantic HTML",
                "Create a simple webpage"
            ]
        },

        "CSS": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "MDN CSS Guide",
                    "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"
                }
            ],
            "practice_tasks": [
                "Practice CSS selectors",
                "Style HTML elements",
                "Create layouts",
                "Build a responsive webpage"
            ]
        },

        "JavaScript": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "MDN JavaScript Guide",
                    "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
                }
            ],
            "practice_tasks": [
                "Practice JavaScript variables and functions",
                "Manipulate the DOM",
                "Handle user events",
                "Build an interactive webpage"
            ]
        },

        "Backend Development": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "FastAPI Documentation",
                    "url": "https://fastapi.tiangolo.com/"
                }
            ],
            "practice_tasks": [
                "Create a basic API",
                "Handle GET and POST requests",
                "Work with JSON data",
                "Connect frontend and backend"
            ]
        },

        "Database Basics": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "SQLite Documentation",
                    "url": "https://www.sqlite.org/docs.html"
                }
            ],
            "practice_tasks": [
                "Create a database",
                "Create tables",
                "Insert and retrieve data",
                "Practice CRUD operations"
            ]
        },

        "SQL": {
            "resources": [
                {
                    "type": "Tutorial",
                    "title": "SQL Tutorial",
                    "url": "https://www.w3schools.com/sql/"
                }
            ],
            "practice_tasks": [
                "Write SELECT queries",
                "Insert records",
                "Update records",
                "Filter and sort database results"
            ]
        },

        "Programming": {
            "resources": [
                {
                    "type": "Tutorial",
                    "title": "Python Documentation",
                    "url": "https://docs.python.org/3/tutorial/"
                }
            ],
            "practice_tasks": [
                "Practice variables and conditions",
                "Practice loops",
                "Write functions",
                "Solve simple programming problems"
            ]
        },

        "Problem Solving": {
            "resources": [
                {
                    "type": "Tutorial",
                    "title": "CodeChef Practice",
                    "url": "https://www.codechef.com/practice"
                }
            ],
            "practice_tasks": [
                "Solve simple programming problems",
                "Practice logical thinking",
                "Write basic algorithms",
                "Debug programming solutions"
            ]
        },

        "Mobile Development": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Flutter Documentation",
                    "url": "https://docs.flutter.dev/"
                }
            ],
            "practice_tasks": [
                "Create a basic Flutter application",
                "Design a mobile interface",
                "Add navigation",
                "Test the application"
            ]
        },

        "IoT": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Arduino Documentation",
                    "url": "https://docs.arduino.cc/"
                }
            ],
            "practice_tasks": [
                "Connect a basic sensor",
                "Read sensor data",
                "Process sensor values",
                "Build a simple IoT prototype"
            ]
        },

        "Cybersecurity": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "OWASP Web Security Testing Guide",
                    "url": "https://owasp.org/www-project-web-security-testing-guide/"
                }
            ],
            "practice_tasks": [
                "Learn common security threats",
                "Understand basic web security",
                "Study secure coding practices",
                "Identify common vulnerabilities"
            ]
        },

        "Networking": {
            "resources": [
                {
                    "type": "Tutorial",
                    "title": "Cisco Networking Basics",
                    "url": "https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/networking-basics.html"
                }
            ],
            "practice_tasks": [
                "Learn IP addresses",
                "Understand basic network protocols",
                "Study client-server communication",
                "Practice basic network troubleshooting"
            ]
        },

        "Statistics": {
            "resources": [
                {
                    "type": "Tutorial",
                    "title": "Khan Academy Statistics",
                    "url": "https://www.khanacademy.org/math/statistics-probability"
                }
            ],
            "practice_tasks": [
                "Calculate mean and standard deviation",
                "Understand basic probability",
                "Analyze simple datasets",
                "Interpret statistical results"
            ]
        },

        "Data Analysis": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Pandas Documentation",
                    "url": "https://pandas.pydata.org/docs/"
                }
            ],
            "practice_tasks": [
                "Explore a dataset",
                "Clean data",
                "Find patterns",
                "Generate useful insights"
            ]
        },

        "Data Visualization": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Matplotlib Documentation",
                    "url": "https://matplotlib.org/stable/users/index.html"
                }
            ],
            "practice_tasks": [
                "Create bar charts",
                "Create line charts",
                "Create scatter plots",
                "Visualize dataset insights"
            ]
        },

        "Automation": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "Python Documentation",
                    "url": "https://docs.python.org/3/"
                }
            ],
            "practice_tasks": [
                "Identify repetitive tasks",
                "Write a simple automation script",
                "Automate file operations",
                "Add error handling"
            ]
        },

        "API Integration": {
            "resources": [
                {
                    "type": "Documentation",
                    "title": "MDN Fetch API",
                    "url": "https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"
                }
            ],
            "practice_tasks": [
                "Understand REST APIs",
                "Send HTTP requests",
                "Work with JSON responses",
                "Connect an application to an API"
            ]
        }
    }

    recommendations = []

    # ---------------------------------
    # MATCH SKILLS
    # ---------------------------------

    for item in skills_to_learn:

        skill = item["skill"]

        if skill in resources:

            recommendations.append({
                "skill": skill,
                "experience_level": experience_level,
                "resources": resources[skill]["resources"],
                "practice_tasks": resources[skill]["practice_tasks"]
            })

        else:

            # Generic fallback for unknown skills
            recommendations.append({
                "skill": skill,
                "experience_level": experience_level,
                "resources": [
                    {
                        "type": "Search",
                        "title": f"{skill} Learning Resources",
                        "url": f"https://www.google.com/search?q={skill.replace(' ', '+')}+tutorial"
                    }
                ],
                "practice_tasks": [
                    f"Learn the fundamentals of {skill}",
                    f"Practice basic {skill} concepts",
                    f"Build a small project using {skill}"
                ]
            })

    return {
        "experience_level": experience_level,
        "recommendations": recommendations
    }


if __name__ == "__main__":

    skills = [
        {
            "skill": "Machine Learning"
        },
        {
            "skill": "OpenCV"
        },
        {
            "skill": "Data Processing"
        },
        {
            "skill": "Computer Vision"
        },
        {
            "skill": "Model Evaluation"
        }
    ]

    result = recommend_resources(
        skills,
        "Beginner"
    )

    print(result)