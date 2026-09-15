def create_execution_roadmap(phases, project_name="", required_skills=None):
    """
    Create a project-aware daily execution roadmap.

    The roadmap uses:
    1. Phase-specific tasks
    2. Project-specific tasks for known project types
    3. Safe fallback tasks for unknown projects
    """

    roadmap = []
    current_day = 1

    if required_skills is None:
        required_skills = []

    project_name_lower = project_name.lower()

    # ---------------------------------------------------------
    # Project-specific task detection
    # ---------------------------------------------------------

    if "waste" in project_name_lower and (
        "classification" in project_name_lower
        or "detection" in project_name_lower
    ):

        project_tasks = {

            "Skill Development": [
                "Study machine learning fundamentals",
                "Learn classification algorithms",
                "Practice dataset preprocessing",
                "Learn model evaluation metrics",
                "Learn computer vision fundamentals",
                "Practice image processing with OpenCV",
                "Build a small image classification example",
                "Evaluate the practice model"
            ],

            "Research and Data Preparation": [
                "Research existing waste classification solutions",
                "Identify suitable waste image datasets",
                "Collect the required waste image dataset",
                "Organize images into classification categories",
                "Clean and preprocess the image dataset",
                "Validate dataset quality and class distribution"
            ],

            "Core Development": [
                "Design the waste classification system architecture",
                "Prepare the image classification pipeline",
                "Implement image preprocessing",
                "Develop the classification model",
                "Train the model using the prepared dataset",
                "Evaluate model performance",
                "Improve model accuracy",
                "Integrate the classification pipeline",
                "Test the complete core functionality"
            ],

            "Backend Development": [
                "Design the backend API structure",
                "Create the image upload endpoint",
                "Implement image preprocessing in the backend",
                "Connect the trained classification model",
                "Return prediction results through the API"
            ],

            "Frontend Development": [
                "Design the waste classification interface",
                "Create the image upload interface",
                "Connect the frontend with the backend API",
                "Display the uploaded image and prediction",
                "Improve the user interface and result display"
            ],

            "Testing and Improvement": [
                "Create test cases for different waste images",
                "Test image upload functionality",
                "Test model predictions",
                "Analyze incorrect predictions",
                "Fix identified errors and improve performance"
            ],

            "Documentation and Presentation": [
                "Prepare the project documentation",
                "Document the problem statement and objectives",
                "Document the system architecture and modules",
                "Document model development and implementation",
                "Prepare screenshots and project results",
                "Prepare presentation slides",
                "Prepare the project demonstration",
                "Review the complete documentation and presentation"
            ]
        }

    else:
        project_tasks = {}

    # ---------------------------------------------------------
    # General phase-specific tasks
    # ---------------------------------------------------------

    phase_task_templates = {

        "Requirement Analysis": [
            "Understand project requirements",
            "Define project objectives",
            "Identify required modules",
            "Analyze project constraints",
            "Finalize functional requirements",
            "Finalize technical requirements",
            "Review and validate requirements"
        ],

        "Skill Development": [
            "Study the fundamentals of the required technology",
            "Learn important concepts",
            "Practice important concepts",
            "Build small examples using the new skill",
            "Apply the learned concepts to the project",
            "Solve practice problems",
            "Review and strengthen the learned skills"
        ],

        "Research and Data Preparation": [
            "Research existing solutions",
            "Identify suitable datasets or data sources",
            "Collect the required data",
            "Organize the project data",
            "Clean and preprocess the data",
            "Validate the collected data",
            "Analyze the prepared data"
        ],

        "Research and Dataset Collection": [
            "Research existing solutions",
            "Identify suitable datasets",
            "Compare available datasets",
            "Download the required dataset",
            "Organize the dataset",
            "Validate dataset quality",
            "Prepare the dataset for development"
        ],

        "Core Development": [
            "Design the core project architecture",
            "Implement the main functionality",
            "Develop the primary project module",
            "Integrate the required technology",
            "Connect the project components",
            "Test the core functionality",
            "Improve the implementation",
            "Review the completed core module"
        ],

        "Backend Development": [
            "Design the backend structure",
            "Create backend modules",
            "Implement API endpoints",
            "Connect backend components",
            "Implement data processing",
            "Test backend APIs",
            "Fix backend errors",
            "Improve backend performance"
        ],

        "Frontend Development": [
            "Design the frontend structure",
            "Create the main user interface",
            "Implement input forms",
            "Connect the frontend with the backend",
            "Display project results",
            "Improve the user interface",
            "Test frontend functionality",
            "Fix interface issues"
        ],

        "Testing and Improvement": [
            "Create test cases",
            "Test individual modules",
            "Test complete project workflow",
            "Identify errors and issues",
            "Fix identified errors",
            "Improve project performance",
            "Perform final testing"
        ],

        "Documentation and Presentation": [
            "Prepare project documentation",
            "Write project introduction and objectives",
            "Document system architecture",
            "Document implementation details",
            "Prepare screenshots and results",
            "Prepare presentation slides",
            "Review the complete documentation",
            "Practice project presentation"
        ]
    }

    # ---------------------------------------------------------
    # Build roadmap
    # ---------------------------------------------------------

    for phase in phases:

        duration = phase.get("duration", 0)
        phase_name = phase.get("name", "Project Phase")
        original_tasks = phase.get("tasks", [])

        try:
            duration = int(duration)
        except (TypeError, ValueError):
            duration = 0

        if duration <= 0:
            continue

        # First priority: project-specific tasks
        if phase_name in project_tasks:
            smart_tasks = project_tasks[phase_name]

        # Second priority: general phase templates
        elif phase_name in phase_task_templates:
            smart_tasks = phase_task_templates[phase_name]

        # Third priority: tasks supplied by Planning Agent
        elif original_tasks:
            smart_tasks = original_tasks

        # Final fallback
        else:
            smart_tasks = [
                f"Work on the {phase_name} phase",
                f"Review the work completed for {phase_name}",
                f"Test the current implementation",
                f"Fix errors and improve the project",
                f"Finalize the {phase_name} phase"
            ]

        for day in range(duration):

            if day < len(smart_tasks):
                task = smart_tasks[day]

            else:
                task = (
                    f"Review, test, and finalize the remaining work "
                    f"for {phase_name}"
                )

            roadmap.append({
                "day": current_day,
                "phase": phase.get("phase", 0),
                "phase_name": phase_name,
                "task": task,
                "status": "Not Started"
            })

            current_day += 1

    return {
        "project_name": project_name,
        "total_execution_days": len(roadmap),
        "daily_roadmap": roadmap
    }


if __name__ == "__main__":

    phases = [
        {
            "phase": 1,
            "name": "Requirement Analysis",
            "duration": 3,
            "tasks": []
        },
        {
            "phase": 2,
            "name": "Skill Development",
            "duration": 8,
            "tasks": []
        },
        {
            "phase": 3,
            "name": "Research and Data Preparation",
            "duration": 6,
            "tasks": []
        }
    ]

    result = create_execution_roadmap(
        phases,
        project_name="AI Waste Classification",
        required_skills=[
            "Python",
            "Machine Learning",
            "Data Processing",
            "Computer Vision",
            "OpenCV"
        ]
    )

    print(result)