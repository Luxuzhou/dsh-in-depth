"""A dependency-free teaching model for governed conversational analytics."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from hashlib import sha256
import json


METRICS = {
    "application_count": "按申请单计数",
    "sample_count": "按样本计数",
    "inspection_item_count": "按检验项目次数计数",
}


@dataclass(frozen=True)
class ConversationState:
    question: str
    metric_id: str | None = None
    filters: dict[str, str] = field(default_factory=dict)
    ambiguities: tuple[str, ...] = ()


@dataclass(frozen=True)
class QueryPlan:
    metric_id: str
    filters: dict[str, str]

    def digest(self) -> str:
        payload = json.dumps(
            {"metric_id": self.metric_id, "filters": self.filters},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return sha256(payload.encode("utf-8")).hexdigest()


@dataclass
class Approval:
    user_id: str
    plan_hash: str
    consumed: bool = False


def interpret(question: str) -> ConversationState:
    if "检验量" in question:
        return ConversationState(question=question, ambiguities=tuple(METRICS))
    raise ValueError("No governed metric matched the question")


def clarify(state: ConversationState, metric_id: str) -> ConversationState:
    if metric_id not in state.ambiguities:
        raise ValueError("The selected metric is not an offered candidate")
    return replace(state, metric_id=metric_id, ambiguities=())


def propose(state: ConversationState) -> QueryPlan:
    if state.ambiguities or not state.metric_id:
        raise ValueError("The business metric must be clarified before planning")
    return QueryPlan(metric_id=state.metric_id, filters=dict(state.filters))


def approve(user_id: str, plan: QueryPlan) -> Approval:
    return Approval(user_id=user_id, plan_hash=plan.digest())


def execute(user_id: str, plan: QueryPlan, approval: Approval) -> dict[str, object]:
    if approval.consumed:
        raise PermissionError("Approval has already been consumed")
    if approval.user_id != user_id or approval.plan_hash != plan.digest():
        raise PermissionError("Approval is not bound to this user and plan")
    approval.consumed = True
    return {
        "metric_id": plan.metric_id,
        "metric_definition": METRICS[plan.metric_id],
        "filters": plan.filters,
        "value": 42,
        "data_source": "teaching-fixture",
    }
