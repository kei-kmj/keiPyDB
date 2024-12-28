from abc import ABC, abstractmethod
from typing import Union

from db.query.constant import Constant


class Scan(ABC):

    @abstractmethod
    def before_first(self) -> None:
        pass

    @abstractmethod
    def next(self) -> bool:
        pass

    @abstractmethod
    def get_int(self, field_name: str) -> int:
        pass

    @abstractmethod
    def get_string(self, field_name: str) -> str:
        pass

    @abstractmethod
    def get_val(self, field_name: str) -> Union[int, str, Constant]:
        pass

    @abstractmethod
    def has_field(self, field_name: str) -> bool:
        pass

    @abstractmethod
    def close(self) -> None:
        pass