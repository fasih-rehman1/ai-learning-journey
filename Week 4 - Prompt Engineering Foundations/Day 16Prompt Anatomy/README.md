# Prompt Builder

## Description

This project builds production-grade AI prompts using five components:

- Role
- Task
- Context
- Constraints
- Output Format

## Run

```bash
python app.py
```

## Example

Role: Senior Python Developer

Task: Build Login API

Context: Django REST Framework

Constraints: Use Class Based Views

Output Format: Python Code Only

=-============================================
"""
ROLE:
You are an expert AI assistant.

TASK:
Perform the following task:
{user_prompt}

CONTEXT:
Use the information provided by the user only.
If context is missing, clearly mention assumptions.

CONSTRAINTS:
- Do not invent facts.
- Explain step by step.
- Use simple language.
- If code is required, provide working examples.
- Mention limitations if needed.

OUTPUT FORMAT:
1. Summary
2. Detailed Explanation
3. Examples
4. Code (if needed)
5. Final Notes
"""