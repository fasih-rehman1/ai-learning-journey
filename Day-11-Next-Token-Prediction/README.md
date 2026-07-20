# Next Token Prediction Notes

An LLM generates text by predicting one token at a time.

It receives previous tokens as context and predicts the most probable next token.

This process repeats until a complete answer is generated.

Example:

Input:
The capital of France is

Prediction:
Paris

Final Output:
The capital of France is Paris.

Predictable prompts produce more consistent outputs.

Ambiguous prompts allow multiple valid continuations, leading to different responses.

In RAG systems, retrieved documents guide the model toward more accurate next-token predictions.

| Prompt                   | Expected Next Token | Why?                                      |
| ------------------------ | ------------------- | ----------------------------------------- |
| The capital of France is | Paris               | It is a well-known fact.                  |
| 2 + 2 =                  | 4                   | Basic mathematics has one correct answer. |
| The sun rises in the     | east                | Scientific fact.                          |
| HTML starts with         | `<html>`            | Standard HTML syntax.                     |
| Python uses the keyword  | for                 | Common programming syntax.                |


Write Five Ambiguous Prompts
Prompt	Possible Outputs
I love	--------pizza, coding, football, music
Today is	---------hot, rainy, Monday, beautiful
She is	--------reading, cooking, happy, working
Let's go	------------home, outside, shopping
Can you	-------------help, explain, translate, code