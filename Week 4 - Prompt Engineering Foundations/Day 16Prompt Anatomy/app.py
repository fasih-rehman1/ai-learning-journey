from prompt_builder import build_prompt

print("=" * 50)
print("Production Prompt Builder")
print("=" * 50)

role = input("Role: ")
task = input("Task: ")
context = input("Context: ")
constraints = input("Constraints: ")
output_format = input("Output Format: ")

prompt = build_prompt(
    role,
    task,
    context,
    constraints,
    output_format
)

print("\nGenerated Prompt")
print("-" * 50)
print(prompt)