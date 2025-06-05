class HierarchicalPlanner:
    def __init__(self):
        self.templates = {
            "load dataset": ["open file", "select file", "confirm load"],
            "manipulate view": ["select view", "adjust slider", "apply colormap"],
            "export visualization": ["open export", "choose format", "confirm export"]
        }

    def decompose(self, high_level_task):
        return self.templates.get(high_level_task, [])
