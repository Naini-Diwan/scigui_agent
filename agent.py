from perception import VLMPerception
from planning import HierarchicalPlanner
from gui_control import GUIController

class SciGUIAgent:
    def __init__(self, mode="desktop"):
        self.perception = VLMPerception()
        self.planner = HierarchicalPlanner()
        self.gui = GUIController(mode=mode)

    def run_task(self, screenshot_path, high_level_task):
        elements = self.perception.detect_elements(screenshot_path)
        workflow = self.planner.decompose(high_level_task)
        for step in workflow:
            if step["step"] == "detect_gui_elements":
                print(f"Detected elements: {elements}")
            elif step["step"] == "find_target_element":
                # Example: find element with label matching task
                target = next((e for e in elements if high_level_task in e['label'].lower()), None)
                if target:
                    print(f"Target element: {target}")
            elif step["step"] == "execute_action":
                if target:
                    self.gui.click(target['bbox'])
        print("Workflow complete.")

if __name__ == "__main__":
    agent = SciGUIAgent()
    agent.run_task("dataset/screenshots/celestia_001.png", "open file")
