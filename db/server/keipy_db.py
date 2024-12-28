from typing import Optional

from db.buffer.buffer_manager import BufferManager
from db.file.file_manager import FileManager
from db.log.log_manager import LogManager
from db.metadata.metadata_manager import MetadataManager
from db.transaction.transaction import Transaction


class KeiPyDB:
    BLOCK_SIZE = 400
    BUFFER_SIZE = 8
    LOG_FILE = "simpledb.log"

    def __init__(self, dir_name: str, block_size: int = BLOCK_SIZE, buffer_size: int = BUFFER_SIZE) -> None:

        self.file_manager = FileManager(dir_name, block_size)
        self.log_manager = LogManager(self.file_manager, KeiPyDB.LOG_FILE)
        self.buffer_manager = BufferManager(self.file_manager, self.log_manager, buffer_size)

        is_new = self.file_manager.is_new
        self.metadata_manager = None
        self.planner = None

        if is_new:
            print("creating new database")
        else:
            print("recovering existing database")

        transaction = self.new_transaction()
        if not is_new:
            transaction.recover()

        self.metadata_manager = MetadataManager(is_new, transaction)

        # TODO: QueryPlannerクラスを実装
        # query_planner = None
        # update_planner = None
        #
        # self.planner = Planner(query_planner, update_planner)
        #
        transaction.commit()

    def new_transaction(self) -> Transaction:
        return Transaction(self.file_manager, self.log_manager, self.buffer_manager)

    def get_metadata_manager(self) -> Optional[MetadataManager]:
        return self.metadata_manager

    # TODO: Plannerクラスを実装
    # def get_planner(self) -> Planner:
    #     return self.planner

    def get_file_manager(self) -> FileManager:
        return self.file_manager

    def get_log_manager(self) -> LogManager:
        return self.log_manager

    def get_buffer_manager(self) -> BufferManager:
        return self.buffer_manager