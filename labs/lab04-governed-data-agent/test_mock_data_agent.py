from dataclasses import replace
import unittest

from mock_data_agent import approve, clarify, execute, interpret, propose


class GovernedDataAgentTest(unittest.TestCase):
    def test_ambiguous_metric_cannot_execute(self):
        state = interpret("统计去年各科室检验量")
        with self.assertRaisesRegex(ValueError, "clarified"):
            propose(state)

    def test_clarified_plan_executes_once(self):
        state = clarify(interpret("统计检验量"), "inspection_item_count")
        plan = propose(state)
        approval = approve("u-1", plan)
        result = execute("u-1", plan, approval)
        self.assertEqual(result["value"], 42)
        with self.assertRaisesRegex(PermissionError, "consumed"):
            execute("u-1", plan, approval)

    def test_changed_plan_invalidates_approval(self):
        state = clarify(interpret("统计检验量"), "sample_count")
        plan = propose(state)
        approval = approve("u-1", plan)
        changed = replace(plan, filters={"patient_type": "outpatient"})
        with self.assertRaisesRegex(PermissionError, "not bound"):
            execute("u-1", changed, approval)


if __name__ == "__main__":
    unittest.main()
