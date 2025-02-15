from abc import ABC
from typing import List

from db.plan.plan import Plan
from db.query.project_scan import ProjectScan
from db.query.scan import Scan
from db.record.schema import Schema


class ProjectPlan(Plan, ABC):

    def __init__(self, plan: Plan, field_list: List[str]) -> None:
        super().__init__()
        self.plan = plan
        self._schema = Schema()
        for field_name in field_list:
            self._schema.add(field_name, self.plan.schema())

    def open(self) -> Scan:
        scan = self.plan.open()
        field_names = self._schema.get_fields()
        return ProjectScan(scan, field_names)

    def blocks_accessed(self) -> int:
        return self.plan.blocks_accessed()

    def records_output(self) -> int:
        return self.plan.records_output()

    def distinct_values(self, field_name: str) -> int:
        return self.plan.distinct_values(field_name)

    def schema(self) -> Schema:
        return self._schema
