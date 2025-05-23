from abc import ABC

from db.metadata.metadata_manager import MetadataManager
from db.plan.plan import Plan
from db.query.scan import Scan
from db.record.schema import Schema
from db.record.table_scan import TableScan
from db.transaction.transaction import Transaction


class TablePlan(Plan, ABC):

    def __init__(self, transaction: Transaction, table_name: str, metadata_manager: MetadataManager) -> None:
        super().__init__()
        self.table_name = table_name
        self.transaction = transaction
        self.layout = metadata_manager.get_layout(table_name, transaction)
        self.stat_info = metadata_manager.get_stat_info(table_name, self.layout, transaction)

    def open(self) -> Scan:
        return TableScan(self.transaction, self.table_name, self.layout)

    def blocks_accessed(self) -> int:
        return self.stat_info.blocks_accessed()

    def records_output(self) -> int:
        return self.stat_info.records_output()

    def distinct_values(self, file_name: str) -> int:
        return self.stat_info.distinct_values()

    def schema(self) -> Schema:
        return self.layout.schema
