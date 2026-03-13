# TaskMesh

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![Status](https://img.shields.io/badge/build-experimental-orange)

TaskMesh is a lightweight task routing layer for AI agents.

It allows agents to publish tasks and other agents to claim them based on capability or availability.

## Quick Start

Clone the repository and run the demo.

```bash
git clone https://github.com/joshuamlamerton/taskmesh
cd taskmesh
python examples/demo.py
```

## Architecture

```mermaid
flowchart TB

A[Task Producer Agent]
B[TaskMesh Router]
C[Worker Agent 1]
D[Worker Agent 2]

A --> B
B --> C
B --> D
```

## What it does

The demo shows:

- a task being submitted
- agents claiming tasks
- the router assigning work

## Repository Structure

```text
taskmesh

README.md
LICENSE

docs
  architecture.md

core
  task_router.py

examples
  demo.py
```

## Roadmap

Phase 1  
Basic task queue

Phase 2  
Capability-based routing

Phase 3  
Priority and retry logic

Phase 4  
Multi-agent coordination features
