
import random

def generate_recommendations(student):
    """
    Generate personalized recommendations for a student.

    Args:
        student (dict): A dictionary containing student data.

    Returns:
        dict: Recommendations including workshops, daily tasks, and mentors.
    """
    workshops = ["Robotics Workshop", "Creative Writing", "AI Bootcamp"]
    tasks = ["Complete a quiz on AI basics", "Build a small robot model", "Write a short story"]
    mentors = ["Dr. A (AI Specialist)", "Mr. B (Robotics Expert)", "Ms. C (Creative Writing Coach)"]

    # Mock logic to suggest based on interests and preferences
    suggested_workshops = [w for w in workshops if any(interest in w for interest in student["interests"])]
    suggested_task = random.choice(tasks)
    suggested_mentor = random.choice(mentors)

    return {
        "workshops": suggested_workshops,
        "daily_task": suggested_task,
        "mentor": suggested_mentor
    }

# Example usage
student_example = {
    "id": "student_001",
    "name": "John Doe",
    "strengths": ["creativity", "communication"],
    "weaknesses": ["time management", "focus"],
    "interests": ["robotics", "performing arts"],
    "preferences": {
        "learning_style": "visual",
        "preferred_topics": ["AI", "programming"]
    }
}

recommendations = generate_recommendations(student_example)
print("Recommendations for the student:", recommendations)
