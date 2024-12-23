
import random

def generate_enhanced_recommendations(student, mentors, tasks):
    """
    Generate enhanced personalized recommendations for a student.

    Args:
        student (dict): A dictionary containing student data.
        mentors (list): A list of mentor profiles (dictionaries).
        tasks (list): A list of daily tasks.

    Returns:
        dict: Enhanced recommendations including workshops, daily tasks, and mentors.
    """
    # Predefined workshops
    workshops = [
        {"name": "Robotics Workshop", "tags": ["robotics", "programming"]},
        {"name": "Creative Writing", "tags": ["writing", "creativity"]},
        {"name": "AI Bootcamp", "tags": ["AI", "programming"]}
    ]

    # Suggest workshops based on student's interests
    suggested_workshops = [
        w["name"] for w in workshops if any(interest in w["tags"] for interest in student["interests"])
    ]

    # Select a daily task matching student's weaknesses and preferences
    suggested_task = next((task for task in tasks if task["focus"] in student["weaknesses"]), random.choice(tasks))

    # Match a mentor based on shared interests or skill needs
    suggested_mentor = next(
        (mentor for mentor in mentors if any(skill in student["interests"] for skill in mentor["skills"])),
        random.choice(mentors)
    )

    return {
        "workshops": suggested_workshops,
        "daily_task": suggested_task["description"],
        "mentor": suggested_mentor["name"]
    }

# Example usage
student_example = {
    "id": "student_001",
    "name": "John Doe",
    "strengths": ["creativity", "communication"],
    "weaknesses": ["time management", "focus"],
    "interests": ["robotics", "performing arts"],
    "preferences": {"learning_style": "visual", "preferred_topics": ["AI", "programming"]}
}

mentors_example = [
    {"name": "Dr. A (AI Specialist)", "skills": ["AI", "programming"]},
    {"name": "Mr. B (Robotics Expert)", "skills": ["robotics", "engineering"]},
    {"name": "Ms. C (Creative Writing Coach)", "skills": ["writing", "creativity"]}
]

tasks_example = [
    {"description": "Complete a quiz on AI basics", "focus": "focus"},
    {"description": "Build a small robot model", "focus": "time management"},
    {"description": "Write a short story", "focus": "creativity"}
]

# Generate recommendations
recommendations = generate_enhanced_recommendations(student_example, mentors_example, tasks_example)
print(recommendations)
