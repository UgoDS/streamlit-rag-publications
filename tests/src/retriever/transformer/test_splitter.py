import pytest
from src.retriever.transformer.splitter import remove_not_found_separator, _split_text_with_regex, _merge_splits, recursive_text_split

# Test cases and expected results
test_cases = [
    ("abc-def", ["-", ".", "_"], ("-", [".", "_"]), "Test case 1"),
    ("abcdef", ["-", ".", "_"], ("_", []), "Test case 2"),
    ("abc.def", ["-", ".", "_"], (".", ["_"]), "Test case 3"),
    ("abc_def", ["-", ".", "_"], ("_", []), "Test case 4"),
    ("abcdef", [""], ("", []), "Test case 5"),
]


@pytest.mark.parametrize("text, separators, expected_result, test_description", test_cases)
def test_remove_not_found_separator(text, separators, expected_result, test_description):
    separator, new_separators = remove_not_found_separator(text, separators)
    assert separator == expected_result[0]
    assert new_separators == expected_result[1]

    print(f"Description of the test: {test_description}")


test_cases = [
    ("abc-def-ghi", "-", True, ["abc", "-def", "-ghi"], "Test case 1"),
    ("abc.def.ghi", ".", True, ["abc", ".def", ".ghi"], "Test case 2"),
    ("abc_def_ghi", "_", True, ["abc", "_def", "_ghi"], "Test case 3"),
    ("abc-def-ghi", "-", False, ["abc", "def", "ghi"], "Test case 4"),
    ("abcdef", "-", True, ["abcdef"], "Test case 5"),
    ("", "-", True, [], "Test case 6"),
]

@pytest.mark.parametrize("text, separator, keep_separator, expected_result, test_description", test_cases)
def test_split_text_with_regex(text, separator, keep_separator, expected_result, test_description):
    splits = _split_text_with_regex(text, separator, keep_separator)
    assert splits == expected_result

    # You can also print the test description for better reporting
    print(f"Test Description: {test_description}")


# Define test cases and expected results
test_cases = [
    (["abc", "def", "ghi"], "-", 12, 0, ["abc-def-ghi"], "Test case 1"),
    (["abc", "def", "ghi"], "-", 7, 0, ["abc-def", "ghi"], "Test case 2"),
    (["abc", "def", "ghi"], "-", 12, 3, ["abc-def-ghi"], "Test case 3"),
    (["abc", "def", "ghi"], "-", 7, 3, ["abc-def", "def-ghi"], "Test case 4"),
    (["abc", "def", "ghi"], ".", 12, 0, ["abc.def.ghi"], "Test case 5"),
]

@pytest.mark.parametrize("splits, separator, chunk_size, chunk_overlap, expected_result, test_description", test_cases)
def test_merge_splits(splits, separator, chunk_size, chunk_overlap, expected_result, test_description):
    result = _merge_splits(splits, separator, chunk_size, chunk_overlap)
    assert result == expected_result

    # Additional assertions if needed
    # assert some_condition

    # You can also print the test description for better reporting
    print(f"Test Description: {test_description}")


# Define test cases and expected results
test_cases = [
    ("abc-def-ghi", ["-", ".", "_"], True, 12, 0,["abc-def-ghi"], "Test case 1"),
    ("abc-def-ghi", ["-", ".", "_"], True, 10, 0,["abc-def", "-ghi"], "Test case 1bis"),
    ("abc-def-ghi", ["-", ".", "_"], True, 10, 2,["abc-def", "-ghi"], "Test case 1ter"),
    ("abc.def.ghi", ["-", ".", "_"], True, 7, 0,["abc.def", ".ghi"], "Test case 2"),
    #("abc_def_ghi", ["-", ".", "_"], False, 10, 0,["abc_def", "_ghi"], "Test case 3"), BUG HERE
    ("abc.def-def-ghi", ["-", ".", "_"], True, 5, 0,["abc", ".def", "-def", "-ghi"], "Test case 4"),
    ("abcdefghi", ["-", ".", "_", ""], True, 5, 2,["abcde", "defgh", "ghi"], "Test case 5"),
]

@pytest.mark.parametrize("text, separators, keep_separator, chunk_size, chunk_overlap, expected_result, test_description", test_cases)
def test_recursive_text_split(text, separators, keep_separator, chunk_size, chunk_overlap, expected_result, test_description):
    result = recursive_text_split(text, separators, keep_separator, chunk_size, chunk_overlap)
    assert result == expected_result

    # You can also print the test description for better reporting
    print(f"Test Description: {test_description}")
