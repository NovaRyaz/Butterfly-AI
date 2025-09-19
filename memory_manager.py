import json
from datetime import datetime

class MemoryManager:
    def __init__(self, db_file="loop_memory.json"):
        self.db_file = db_file
        try:
            with open(self.db_file, "r") as f:
                self.memory = json.load(f)
        except:
            self.memory = []

    def retrieve_context(self):
        if not self.memory:
            return "Initial context."
        return self.memory[-1]["output"]

    def log_loop_cycle(self, state, prompt, output):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "state": state,
            "prompt": prompt,
            "output": output
        }
        self.memory.append(entry)
        with open(self.db_file, "w") as f:
            json.dump(self.memory, f, indent=2)
