from db.constants import ByteSize, LogRecordFields
from db.file.page import Page
from db.log.log_manager import LogManager
from db.transaction.transaction import Transaction


class RollbackRecord:
    ROLLBACK = 3

    def __init__(self, page: Page) -> None:
        self._tx_number = page.get_int(ByteSize.Int)

    def op(self) -> int:
        return self.ROLLBACK

    def tx_number(self) -> int:
        return self._tx_number

    def undo(self, tx: Transaction) -> None:
        pass

    def __str__(self) -> str:
        return f"<ROLLBACK {self._tx_number}>"

    @staticmethod
    def write_to_log(log_manager: LogManager, tx_number: int) -> int:
        """ログにロールバックレコードを書き込む"""
        rec = bytearray(LogRecordFields.Two_Fields * ByteSize.Int)
        page = Page(rec)
        page.set_int(0, RollbackRecord.ROLLBACK)
        page.set_int(ByteSize.Int, tx_number)

        return log_manager.append(page.get_contents())
