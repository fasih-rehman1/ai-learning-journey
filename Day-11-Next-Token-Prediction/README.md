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