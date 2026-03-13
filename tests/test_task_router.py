import pytest
from your_module import TaskRouter  # Import the module under test


def test_task_router_init():
    """Test that the task router is initialized correctly."""
    router = TaskRouter()
    assert router.tasks == []


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
