import sampleModule

def test_sample_function():
    """
    Tests the toUpper function from sampleModule by converting a sample string to uppercase.

    Asserts:
        The result of sampleModule.toUpper("This is a test") should be "THIS IS A TEST".
    """
    result = sampleModule.toUpper("This is a test")
    assert result == "THIS IS A TEST", f"Expected 'THIS IS A TEST', but got '{result}'"

def test_sample_function_lower():
    """
    Tests the toLower function from sampleModule to ensure it correctly converts a string 
    to lowercase.

    Asserts:
        The result of sampleModule.toLower("This is a test") should be "this is a test".
    """
    result = sampleModule.toLower("This is a test")
    assert result == "this is a test", f"Expected 'this is a test', but got '{result}'"

def run_tests():
    """
    Runs all test functions for the module.

    This function executes the test_sample_function and test_sample_function_lower
    functions to verify their correctness. If all tests pass, it prints a confirmation message.

    Raises:
        AssertionError: If any of the test functions fail.
    """
    test_sample_function()
    test_sample_function_lower()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    print("Tests completed successfully.")
