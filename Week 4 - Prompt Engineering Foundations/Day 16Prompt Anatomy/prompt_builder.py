def build_prompt(role, task, context, constraints, output_format):

    prompt = f"""
Role:
{role}

Task:
{task}

Context:
{context}

Constraints:
{constraints}

Output Format:
{output_format}
"""

    return prompt