```python
# core/task_router.py
class TaskRouter:
    """
    A class responsible for routing tasks to agents based on their capabilities.

    Attributes:
        tasks (dict): A dictionary mapping task names to agent names.
        capabilities (dict): A dictionary mapping agent names to their capabilities.
    """

    def __init__(self):
        """
        Initializes the task router with empty task and capability dictionaries.
        """
        self.tasks = {}
        self.capabilities = {}

    def submit_task(self, task_name, task_requirements):
        """
        Submits a task to the task router.

        Args:
            task_name (str): The name of the task to submit.
            task_requirements (dict): A dictionary of task requirements (e.g., capabilities).

        Returns:
            None
        """
        # Find the most suitable agent for the task
        suitable_agents = [agent for agent, capabilities in self.capabilities.items() if all(requirement in capabilities for requirement in task_requirements)]
        if suitable_agents:
            self.tasks[task_name] = suitable_agents[0]
        else:
            raise Exception(f"No agent available with required capabilities for task '{task_name}'")

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

    def add_agent_capability(self, agent_name, capabilities):
        """
        Adds an agent's capabilities to the task router.

        Args:
            agent_name (str): The name of the agent.
            capabilities (dict): A dictionary of the agent's capabilities.

        Returns:
            None
        """
        self.capabilities[agent_name] = capabilities

    def get_agent_capabilities(self, agent_name):
        """
        Returns an agent's capabilities.

        Args:
            agent_name (str): The name of the agent.

        Returns:
            dict: The agent's capabilities.
        """
        return self.capabilities.get(agent_name)

def main():
    """
    Demonstrates the usage of the TaskRouter class.
    """
    # Initialize the task router
    task_router = TaskRouter()

    # Define agent capabilities
    task_router.add_agent_capability("analysis_agent", {"data_analysis": True, "machine_learning": False})
    task_router.add_agent_capability("report_agent", {"data_analysis": False, "machine_learning": False})
    task_router.add_agent_capability("idle_agent", {"data_analysis": True, "machine_learning": True})

    # Submit tasks to the task router
    tasks_to_submit = [
        {"name": "analyze_market_data", "requirements": {"data_analysis": True}},
        {"name": "generate_report", "requirements": {"data_analysis": False}},
        {"name": "train_model", "requirements": {"machine_learning": True}}
    ]
    for task in tasks_to_submit:
        task_router.submit_task(task["name"], task["requirements"])

    # Attempt to claim tasks by agent name
    agents = ["analysis_agent", "report_agent", "idle_agent"]
    for agent in agents:
        print(f"Agent claim {agents.index(agent) + 1}: {task_router.claim_task(agent)}")

if __name__ == "__main__":
    main()
```