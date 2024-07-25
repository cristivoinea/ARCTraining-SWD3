#import pytest
import hypot.source as source
def test_sqrt():
    input = 4
    expected_output = 2.0
    output = source.sqrt(input)
    assert output == expected_output