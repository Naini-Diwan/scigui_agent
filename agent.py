
from perception import VLMPerception
from planning import HierarchicalPlanner
from gui_control import GUIController

class SciGUIAgent:
    def __init__(self):
        self.perception = VLMPerception()
        self.planner = HierarchicalPlanner()
        self.gui = GUIController()

    def run_task(self, screenshot_path, instruction, high_level_task):
        print(f"Instruction: {instruction}")
        elements = self.perception.detect_elements(screenshot_path, instruction)
        subtasks = self.planner.decompose(high_level_task)
        print(f"Subtasks: {subtasks}")
        for subtask in subtasks:
            for elem in elements:
                if subtask in elem['label'].lower():
                    print(f"Executing: {subtask}")
                    self.gui.click(elem['bbox'])
        print("Task complete.")

if __name__ == "__main__":
    agent = SciGUIAgent()
    agent.run_task(
        screenshot_path="dataset/screenshots/celestia_001.png",
        instruction="Load the star catalog and set the view to 2025.",
        high_level_task="load dataset"
    )
