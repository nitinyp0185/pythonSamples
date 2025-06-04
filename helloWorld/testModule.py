import sampleModule

def test_sample_function():
    result = sampleModule.toUpper("This is a test")
    assert result == "THIS IS A TEST", f"Expected 'THIS IS A TEST', but got '{result}'" 

def test_sample_function_lower():
    result = sampleModule.toLower("This is a test")
    assert result == "this is a test", f"Expected 'this is a test', but got '{result}'"

def run_tests():
    test_sample_function()
    test_sample_function_lower()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    print("Tests completed successfully.")