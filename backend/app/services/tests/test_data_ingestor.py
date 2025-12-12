import pytest
from data_ingestors import create_parser

def test_create_parser_returns_correct_instance():
    parser = create_parser("dummy.pdf")
    assert hasattr(parser, "parse")

def test_parser_parse_returns_docs(mocker):
    parser = create_parser("dummy.pdf")
    mocker.patch.object(parser, "parse", return_value=["doc1", "doc2"])

    docs = parser.parse()
    assert docs == ["doc1", "doc2"]
    
def test_parser_handels_unknown_file_format():
    with pytest.raises(ValueError):
        create_parser("dummy.txt")
