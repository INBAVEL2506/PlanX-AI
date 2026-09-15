def create_project_plan(
    project_name,
    available_days,
    difficulty,
    student_skills,
    required_skills
):

    student_skill_names = [skill.lower().strip() for skill in student_skills]

    # ---------------------------------
    # SKILL GAP ANALYSIS
    # ---------------------------------
    skill_gap = [
        skill for skill in required_skills
        if skill.lower().strip() not in student_skill_names
    ]

    # ---------------------------------
    # BASE PHASES
    # ---------------------------------
    phases = [
        {
            "name": "Requirement Analysis",
            "tasks": [
                "Understand project requirements",
                "Define project objectives",
                "Identify required modules"
            ]
        },
        {
            "name": "Skill Development",
            "tasks": [
                f"Learn {skill}" for skill in skill_gap
            ]
        },
        {
            "name": "Research and Data Preparation",
            "tasks": [
                "Research existing solutions",
                "Collect required data or dataset",
                "Organize the project data"
            ]
        },
        {
            "name": "Core Development",
            "tasks": [
                "Design the main project architecture",
                "Implement core project functionality",
                "Integrate required technologies"
            ]
        },
        {
            "name": "Backend Development",
            "tasks": [
                "Create backend API",
                "Implement application logic",
                "Connect required services"
            ]
        },
        {
            "name": "Frontend Development",
            "tasks": [
                "Create user interface",
                "Implement user interaction",
                "Display project results"
            ]
        },
        {
            "name": "Testing and Improvement",
            "tasks": [
                "Test different inputs",
                "Fix errors",
                "Improve project performance"
            ]
        },
        {
            "name": "Documentation and Presentation",
            "tasks": [
                "Prepare project documentation",
                "Create presentation",
                "Prepare project demonstration"
            ]
        }
    ]

    # ---------------------------------
    # REMOVE EMPTY SKILL DEVELOPMENT
    # ---------------------------------
    if not skill_gap:
        phases = [
            phase for phase in phases
            if phase["name"] != "Skill Development"
        ]

    # ---------------------------------
    # DIFFICULTY FACTOR
    # ---------------------------------
    difficulty_lower = difficulty.lower()

    if "advanced" in difficulty_lower:
        difficulty_factor = 1.25
    elif "intermediate" in difficulty_lower:
        difficulty_factor = 1.10
    else:
        difficulty_factor = 0.90

    # ---------------------------------
    # EXPERIENCE FACTOR
    # ---------------------------------
    if len(student_skills) <= 2:
        experience_factor = 1.20
    elif len(student_skills) <= 4:
        experience_factor = 1.10
    else:
        experience_factor = 1.00

    # ---------------------------------
    # INITIAL DURATION ESTIMATION
    # ---------------------------------
    base_durations = {
        "Requirement Analysis": 3,
        "Skill Development": 4,
        "Research and Data Preparation": 5,
        "Core Development": 8,
        "Backend Development": 4,
        "Frontend Development": 4,
        "Testing and Improvement": 4,
        "Documentation and Presentation": 3
    }

    estimated_durations = []

    for phase in phases:

        base_duration = base_durations[phase["name"]]

        # Skill development depends on number of missing skills
        if phase["name"] == "Skill Development":
            base_duration = max(2, min(8, len(skill_gap) * 2))

        duration = round(
            base_duration * difficulty_factor * experience_factor
        )

        duration = max(1, duration)

        estimated_durations.append(duration)

    # ---------------------------------
    # ADAPT TO AVAILABLE DAYS
    # ---------------------------------
    minimum_days = len(phases)

    if available_days < minimum_days:
        planned_days = available_days
    else:
        planned_days = min(
            available_days,
            sum(estimated_durations)
        )

    # ---------------------------------
    # SCALE DURATIONS TO AVAILABLE TIME
    # ---------------------------------
    total_estimated = sum(estimated_durations)

    if total_estimated > 0:

        scaled_durations = []

        for duration in estimated_durations:
            scaled = round(
                duration * planned_days / total_estimated
            )

            scaled = max(1, scaled)

            scaled_durations.append(scaled)

        # Fix rounding differences
        difference = planned_days - sum(scaled_durations)

        index = 0

        while difference != 0:

            if difference > 0:
                scaled_durations[index % len(scaled_durations)] += 1
                difference -= 1

            else:
                target_index = index % len(scaled_durations)

                if scaled_durations[target_index] > 1:
                    scaled_durations[target_index] -= 1
                    difference += 1

            index += 1

    else:
        scaled_durations = estimated_durations

    # ---------------------------------
    # BUILD FINAL PHASES
    # ---------------------------------
    final_phases = []

    for index, phase in enumerate(phases):

        final_phases.append({
            "phase": index + 1,
            "name": phase["name"],
            "duration": scaled_durations[index],
            "tasks": phase["tasks"]
        })

    total_days = sum(
        phase["duration"] for phase in final_phases
    )

    # ---------------------------------
    # RETURN PLAN
    # ---------------------------------
    return {
        "project_name": project_name,
        "available_days": available_days,
        "difficulty": difficulty,
        "student_skills": student_skills,
        "required_skills": required_skills,
        "skill_gap": skill_gap,
        "total_planned_days": total_days,
        "phases": final_phases
    }