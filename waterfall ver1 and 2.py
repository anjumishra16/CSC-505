class Mishra:
    def __init__(self, name):
        self.name = name.lower()

    def process(self):
        if self.name == "waterfall":
            steps = [
                "Communication",
                "Planning",
                "Modeling",
                "Construction",
                "Deployment"]
            description = "Sequential process, each phase must be completed before moving to the next."
        elif self.name == "waterfall_ver2":
            steps = [
                "Meet",
                "Plan",
                "Develop & Test",
                "Evaluate"]
            description = "Iterative, flexible, and adaptable approach with continuous customer involvement."
        else:
            print("\n⚠️ Invalid choice! Please enter 'Waterfall' or 'Waterfall_ver2'.")
            return

        self.display_steps(steps, description)

    def display_steps(self, steps, description):
        print("\n" + "=" * 40)
        print(f"   {self.name.capitalize()} Methodology Steps")
        print("=" * 40)
        for step in steps:
            box_width = max(len(step) + 4, 25)
            print("+" + "-" * (box_width - 2) + "+")
            print(f"| {step.center(box_width - 4)} |")
            print("+" + "-" * (box_width - 2) + "+")
        print("\n" + "-" * 40)
        print(f"📌 Note: {description}")
        print("-" * 40 + "\n")

# Run script with user input
if __name__ == "__main__":
    print("from here")
    user_choice = input("Enter methodology ('Waterfall' or 'Waterfall_ver2'): ").strip()
    methodology = Mishra(user_choice)
    methodology.process()



