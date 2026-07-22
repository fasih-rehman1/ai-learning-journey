from test_cases import TEST_CASES

print("=== Prompt Regression Test Sheet ===\n")

for test_type, prompt in TEST_CASES:
    print(f"Test Type : {test_type}")
    print(f"Prompt    : {prompt}")
    print("-" * 40)