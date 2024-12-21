import pytest
from db.file.block_id import BlockID

def test_block_id_equality():
    block = BlockID("testfile.txt", 5)
    other_block = BlockID("testfile.txt", 5)
    third_block = BlockID("otherfile.txt", 10)

    assert block == other_block, "Blocks with the same filename and block number should be equal"
    assert block != third_block, "Blocks with different filename or block number should not be equal"

def test_block_id_string_representation():
    block = BlockID("testfile.txt", 5)
    assert str(block) == "[testfile.txt, block 5]", "String representation of BlockId is incorrect"
