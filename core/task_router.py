```python
class TaskRouter:
    """
    A task router class that manages a queue of tasks and assigns them to agents.
    """

    def __init__(self):
        """
        Initializes the task router with an empty task queue.
        """
        # Initialize an empty list to store tasks
        self.tasks = []

    def submit_task(self, task):
        """
        Adds a task to the task queue.

        Args:
            task (str): The task to be added to the queue.
        """
        # Append the task to the end of the queue
        self.tasks.append(task)

    def claim_task(self, agent_name):
        """
        Claims the next task in the queue for the given agent.

        Args:
            agent_name (str): The name of the agent claiming the task.

        Returns:
            dict or None: A dictionary containing the agent's name and the claimed task, or None if the queue is empty.
        """
        # Check if the task queue is empty
        if not self.tasks:
            # If the queue is empty, return None
            return None
        # Remove and return the first task from the queue
        task = self.tasks.pop(0)
        # Return a dictionary containing the agent's name and the claimed task
        return {"agent": agent_name, "task": task}
```