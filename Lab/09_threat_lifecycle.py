
def identify_stage(activity):
    activity = activity.lower()

    stages = {
        "Direction": ["requirement", "priority", "objective", "planning"],
        "Collection": ["collect", "gather", "capture", "obtain"],
        "Processing": ["clean", "filter", "organize", "normalize"],
        "Analysis": ["analyze", "investigate", "correlate", "interpret"],
        "Dissemination": ["share", "report", "distribute", "communicate"],
        "Feedback": ["feedback", "review", "improve", "suggest"]
    }

    for stage, keywords in stages.items():
        if any(word in activity for word in keywords):
            return stage

    return "Stage not identified"


activity = input("Enter the intelligence team activity: ")
stage = identify_stage(activity)

print("Threat Intelligence Lifecycle Stage:", stage)
