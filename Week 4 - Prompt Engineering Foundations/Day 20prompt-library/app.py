from pathlib import Path

# Load template
template = Path("prompts/rag_answer.md").read_text()

# Replace variables
prompt = template.replace(
    "{{question}}",
    "What is Django ORM?"
)

prompt = prompt.replace(
    "{{context}}",
    "Django ORM is an Object Relational Mapper."
)

print(prompt)