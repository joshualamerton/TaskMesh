from core.task_router import TaskRouter

router = TaskRouter()

router.submit_task("analyze_market_data")
router.submit_task("generate_report")

print("Agent claim 1:", router.claim_task("analysis_agent"))
print("Agent claim 2:", router.claim_task("report_agent"))
print("Agent claim 3:", router.claim_task("idle_agent"))
