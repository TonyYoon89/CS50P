import pytest
from project import add_record, generate_report
import pandas as pd

# Example of a test function
def test_add_record():
    # Setup test data
    test_df = pd.DataFrame(columns=['Amount', 'Category', 'Month'])
    record_type = 'test'
    test_amount = 100
    test_category = 'Mobile'
    test_month = 6

    # Invoke the function with test data
    add_record(test_df, record_type, test_amount, test_category, test_month)

    # Assert the expected outcome
    assert not test_df.empty
    assert test_df.iloc[0]['Amount'] == test_amount
    assert test_df.iloc[0]['Category'] == test_category
    assert test_df.iloc[0]['Month'] == test_month