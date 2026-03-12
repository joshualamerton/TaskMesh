from core.task_router import Agent, Task, TaskRouter

router = TaskRouter()

# Register agents with their capabilities
router.register_agent(Agent("analysis_agent", capabilities=["data_analysis", "statistics"]))
router.register_agent(Agent("report_agent", capabilities=["reporting", "pdf_generation"]))
router.register_agent(Agent("general_agent", capabilities=[]))

# Submit tasks with capability requirements
router.submit_task(Task("analyze_market_data", required_capabilities=["data_analysis"]))
router.submit_task(Task("generate_report", required_capabilities=["reporting"]))
router.submit_task(Task("send_notification"))  # No specific capability required

# Agents claim tasks matching their capabilities
print("Claim 1:", router.claim_task("analysis_agent"))   # gets analyze_market_data
print("Claim 2:", router.claim_task("report_agent"))     # gets generate_report
print("Claim 3:", router.claim_task("general_agent"))    # gets send_notification
print("Claim 4:", router.claim_task("analysis_agent"))   # None - queue empty
