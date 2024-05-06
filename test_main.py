import os
import pytest
from unittest.mock import patch
from app import get_completion

@pytest.mark.parametrize("prompt", ["This is a test prompt.", "Another test prompt."])
def test_get_completion(prompt):
    response = get_completion(prompt)
    assert isinstance(response, str)
    assert response != ""

@patch("builtins.open")
@patch("main.fitz")
def test_summary_generation(mock_fitz, mock_open):
    mock_pdf = mock_fitz.open.return_value.__enter__.return_value
    mock_page = mock_pdf.load_page.return_value
    mock_page.get_text.return_value = "Sample text from PDF file."

    summary = get_summary_from_pdf("test.pdf")
    assert isinstance(summary, str)
    assert summary != ""

def test_summary_file_created():
    assert os.path.exists("summary.txt")

def test_summary_content():
    with open("summary.txt", "r") as file:
        summary = file.read()
    assert isinstance(summary, str)
    assert summary != ""
