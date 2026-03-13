class TaskRouter:
    def __init__(self):
        self.tasks = []

    def submit_task(self, task):
        self.tasks.append(task)

    def claim_task(self, agent_name):
        if not self.tasks:
            return None
        task = self.tasks.pop(0)
        return {"agent": agent_name, "task": task}
