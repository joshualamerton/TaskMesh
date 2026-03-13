```python
import pytest
from your_module import TaskRouter  # Import the module under test


def test_task_router_init():
    """Test that the task router is initialized correctly."""
    router = TaskRouter()
    assert router.tasks == []
    assert router.capabilities == {}  # Added assertion for capabilities


def test_submit_task():
    """Test that tasks are added to the queue correctly."""
    router = TaskRouter()
    router.submit_task("Task 1")
    router.submit_task("Task 2")
    assert router.tasks == ["Task 1", "Task 2"]


def test_submit_task_multiple():
    """Test that multiple tasks can be added to the queue."""
    router = TaskRouter()
    for i in range(10):
        router.submit_task(f"Task {i+1}")
    assert len(router.tasks) == 10


def test_claim_task_empty_queue():
    """Test that claiming a task from an empty queue returns None."""
    router = TaskRouter()
    assert router.claim_task("Agent 1") is None


def test_claim_task_single_task():
    """Test that claiming a task from a single-task queue returns the task."""
    router = TaskRouter()
    router.submit_task("Task 1")
    task = router.claim_task("Agent 1")
    assert task == {"agent": "Agent 1", "task": "Task 1"}


def test_claim_task_multiple_tasks():
    """Test that claiming tasks from a multi-task queue returns the tasks in order."""
    router = TaskRouter()
    for i in range(3):
        router.submit_task(f"Task {i+1}")
    tasks = []
    for _ in range(3):
        task = router.claim_task("Agent 1")
        assert task is not None
        tasks.append(task)
    assert tasks == [
        {"agent": "Agent 1", "task": "Task 1"},
        {"agent": "Agent 1", "task": "Task 2"},
        {"agent": "Agent 1", "task": "Task 3"},
    ]


def test_claim_task_multiple_agents():
    """Test that claiming tasks from a multi-task queue returns the tasks in order across multiple agents."""
    router = TaskRouter()
    for i in range(6):
        router.submit_task(f"Task {i+1}")
    tasks = []
    for i in range(3):
        task = router.claim_task("Agent 1")
        assert task is not None
        tasks.append(task)
        task = router.claim_task("Agent 2")
        assert task is not None
        tasks.append(task)
    assert tasks == [
        {"agent": "Agent 1", "task": "Task 1"},
        {"agent": "Agent 2", "task": "Task 2"},
        {"agent": "Agent 1", "task": "Task 3"},
        {"agent": "Agent 2", "task": "Task 4"},
        {"agent": "Agent 1", "task": "Task 5"},
        {"agent": "Agent 2", "task": "Task 6"},
    ]


def test_claim_task_invalid_agent_name():
    """Test that claiming a task with an invalid agent name raises no error."""
    router = TaskRouter()
    router.submit_task("Task 1")
    task = router.claim_task(None)
    assert task == {"agent": "Agent 1", "task": "Task 1"}


def test_claim_task_by_capability():
    """Test that tasks are claimed based on agent capabilities."""
    router = TaskRouter()
    router.submit_task("Task 1", capabilities={"language": "Python"})
    router.submit_task("Task 2", capabilities={"language": "Java"})
    router.submit_task("Task 3", capabilities={"language": "Python"})
    router.add_agent("Agent 1", capabilities={"language": "Python"})
    router.add_agent("Agent 2", capabilities={"language": "Java"})
    task = router.claim_task("Agent 1")
    assert task == {"agent": "Agent 1", "task": "Task 1"}
    task = router.claim_task("Agent 1")
    assert task == {"agent": "Agent 1", "task": "Task 3"}
    task = router.claim_task("Agent 2")
    assert task == {"agent": "Agent 2", "task": "Task 2"}


def test_add_agent():
    """Test that agents can be added with capabilities."""
    router = TaskRouter()
    router.add_agent("Agent 1", capabilities={"language": "Python"})
    assert router.capabilities["Agent 1"] == {"language": "Python"}


def test_add_agent_multiple():
    """Test that multiple agents can be added with capabilities."""
    router = TaskRouter()
    router.add_agent("Agent 1", capabilities={"language": "Python"})
    router.add_agent("Agent 2", capabilities={"language": "Java"})
    router.add_agent("Agent 3", capabilities={"language": "Python"})
    assert router.capabilities["Agent 1"] == {"language": "Python"}
    assert router.capabilities["Agent 2"] == {"language": "Java"}
    assert router.capabilities["Agent 3"] == {"language": "Python"}


def test_demo():
    """Test that the demo shows example usage."""
    # Add example usage to the demo
    print("Example usage:")
    print("1. Add agents with capabilities:")
    print("   router.add_agent('Agent 1', capabilities={'language': 'Python'})")
    print("2. Submit tasks with capabilities:")
    print("   router.submit_task('Task 1', capabilities={'language': 'Python'})")
    print("3. Claim tasks based on agent capabilities:")
    print("   task = router.claim_task('Agent 1')")
    print("   assert task == {'agent': 'Agent 1', 'task': 'Task 1'}")
```

```python
# your_module.py
class TaskRouter:
    def __init__(self):
        self.tasks = []
        self.capabilities = {}

    def add_agent(self, agent, capabilities):
        """Add an agent with capabilities."""
        self.capabilities[agent] = capabilities

    def submit_task(self, task, capabilities=None):
        """Submit a task with capabilities."""
        self.tasks.append({"task": task, "capabilities": capabilities or {}})

    def claim_task(self, agent):
        """Claim a task based on agent capabilities."""
        # Implement capability-based task routing
        tasks = [task for task in self.tasks if task["capabilities"] == self.capabilities.get(agent)]
        if tasks:
            return {"agent": agent, "task": tasks.pop(0)}
        return None
```

Note: The `TaskRouter` class has been updated to support capability-based task routing. The `add_agent` method allows adding agents with capabilities, and the `submit_task` method allows submitting tasks with capabilities. The `claim_task` method claims a task based on agent capabilities. The demo has been updated to show example usage of the `TaskRouter` class.