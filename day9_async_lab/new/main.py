def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def build_prompt(question):

    return f"""
Answer professionally.

Question:{question}
"""