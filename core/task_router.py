class Task:
    """A task with optional capability requirements."""

    def __init__(self, name: str, required_capabilities: list[str] | None = None):
        self.name = name
        self.required_capabilities = required_capabilities or []

    def __repr__(self):
        caps = ", ".join(self.required_capabilities) if self.required_capabilities else "any"
        return f"Task({self.name\!r}, requires={caps})"


class Agent:
    """An agent with a defined set of capabilities."""

    def __init__(self, name: str, capabilities: list[str] | None = None):
        self.name = name
        self.capabilities = set(capabilities or [])

    def can_handle(self, task: Task) -> bool:
        """Return True if this agent has all capabilities required by the task."""
        return all(cap in self.capabilities for cap in task.required_capabilities)

    def __repr__(self):
        return f"Agent({self.name\!r}, capabilities={sorted(self.capabilities)})"


class TaskRouter:
    """Routes tasks to agents based on capability matching."""

    def __init__(self):
        self.tasks: list[Task] = []
        self.agents: dict[str, Agent] = {}

    def register_agent(self, agent: Agent) -> None:
        """Register an agent with its capabilities."""
        self.agents[agent.name] = agent

    def submit_task(self, task: str | Task, required_capabilities: list[str] | None = None) -> None:
        """Submit a task to the queue.

        Parameters
        ----------
        task : str | Task
            Task name string or a Task object.
        required_capabilities : list[str] | None
            Capabilities required to handle the task. Ignored if task is a Task object.
        """
        if isinstance(task, str):
            task = Task(task, required_capabilities)
        self.tasks.append(task)

    def claim_task(self, agent_name: str) -> dict | None:
        """Claim the first task this agent is capable of handling.

        Iterates through the task queue in order and returns the first task
        whose required capabilities are all present in the agent's capability set.
        Falls back to the first available task if the agent has no capabilities registered.

        Parameters
        ----------
        agent_name : str
            Name of the claiming agent.

        Returns
        -------
        dict | None
            A dict with keys 'agent' and 'task', or None if no suitable task exists.
        """
        if not self.tasks:
            return None

        agent = self.agents.get(agent_name)

        if agent is None:
            # Unknown agent: fall back to FIFO (original behaviour)
            task = self.tasks.pop(0)
            return {"agent": agent_name, "task": task}

        # Find first task this agent can handle
        for i, task in enumerate(self.tasks):
            if agent.can_handle(task):
                self.tasks.pop(i)
                return {"agent": agent_name, "task": task}

        return None  # No suitable task found
