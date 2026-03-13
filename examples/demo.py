```python
from core.task_router import TaskRouter

def main():
    """
    Demonstrates the usage of the TaskRouter class.
    """
    # Initialize the task router
    task_router = TaskRouter()

    # Submit tasks to the task router
    tasks_to_submit = ["analyze_market_data", "generate_report"]
    for task in tasks_to_submit:
        task_router.submit_task(task)

    # Attempt to claim tasks by agent name
    agents = ["analysis_agent", "report_agent", "idle_agent"]
    for agent in agents:
        print(f"Agent claim {agents.index(agent) + 1}: {task_router.claim_task(agent)}")

if __name__ == "__main__":
    main()
```

```python
# core/task_router.py
class TaskRouter:
    """
    A class responsible for routing tasks to agents.

    Attributes:
        tasks (dict): A dictionary mapping task names to agent names.
    """

    def __init__(self):
        """
        Initializes the task router with an empty task dictionary.
        """
        self.tasks = {}

    def submit_task(self, task_name):
        """
        Submits a task to the task router.

        Args:
            task_name (str): The name of the task to submit.

        Returns:
            None
        """
        # For demonstration purposes, we'll just assign the task to the first available agent
        # In a real implementation, this would likely involve more complex logic
        self.tasks[task_name] = self.get_first_available_agent()

    def claim_task(self, agent_name):
        """
        Attempts to claim a task by agent name.

        Args:
            agent_name (str): The name of the agent attempting to claim the task.

        Returns:
            str: The name of the task claimed by the agent, or None if no task is available.
        """
        # For demonstration purposes, we'll just return a task name if the agent is available
        # In a real implementation, this would likely involve more complex logic
        if agent_name in self.tasks.values():
            for task, agent in self.tasks.items():
                if agent == agent_name:
                    del self.tasks[task]
                    return task
        return None

    def get_first_available_agent(self):
        """
        Returns the name of the first available agent.

        Returns:
            str: The name of the first available agent.
        """
        # For demonstration purposes, we'll just return the first agent in the list
        # In a real implementation, this would likely involve more complex logic
        return "analysis_agent"
```