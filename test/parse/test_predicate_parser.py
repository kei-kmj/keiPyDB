from unittest.mock import MagicMock

import pytest

from db.parse.lexer import Lexer
from db.parse.predicate_parser import PredicateParser


@pytest.fixture
def mock_lexer():
    """Lexerクラスのモックを作成"""
    mock = MagicMock(spec=Lexer)
    return mock


def test_フィールドをパースできる(mock_lexer):

    mock_lexer.eat_id.return_value = "field_name"
    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.field()
    assert result == "field_name", "フィールドが正しくパースできません"


def test_文字列定数をパースできる(mock_lexer):

    mock_lexer.match_string_constant.return_value = True
    mock_lexer.eat_string_constant.return_value = "string"
    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.constant()
    assert result is None, "文字列定数が正しくパースできません"


def test_整数定数をパースできる(mock_lexer):

    mock_lexer.match_string_constant.return_value = False
    mock_lexer.eat_int_constant.return_value = 123
    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.constant()
    assert result is None, "整数定数が正しくパースできません"


def test_フィールドで式をパースできる(mock_lexer):

    mock_lexer.match_id.return_value = True
    mock_lexer.eat_id.return_value = "field_name"
    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.expression()
    assert result is None, "式が正しくパースできません"


def test_定数で式をパースできる(mock_lexer):

    mock_lexer.match_id.return_value = False
    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.expression()
    assert result is None, "式が正しくパースできません"


def test_項をパースできる(mock_lexer):

    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.term()
    assert result is None, "項が正しくパースできません"


def test_条件式をパースできる(mock_lexer):

    parser = PredicateParser("")
    parser.lexer = mock_lexer

    result = parser.predicate()
    assert result is None, "条件式が正しくパースできません"