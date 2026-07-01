from pydantic import BaseModel, Field, ValidationError, EmailStr
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class UserQuestion(BaseModel):
    user_id: int = Field(..., description="The unique identifier of the user")
    question: str = Field(...,min_length=10, max_length=500, description="The question asked by the user")
    priority: Priority


class ExtractedLead(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="The name of the lead")
    email: EmailStr
    company: str | None = None

class ClassificationResult(BaseModel):
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence score between 0 and 1")
    tags: list[str] = Field(..., min_items=1, description="At least 1 tag is required")



#------------------------------TEST CASES----------------------------------------#

print("=" * 50)
print("TESTING USER QUESTION")
print("=" * 50)

try:
    user_question = UserQuestion(user_id=1, question="What is the capital of France?", priority=Priority.HIGH)
    print(user_question, "✅ PASSED")
except ValidationError as e:
    print(f"Validation error: {e}")

try:
    user2 = UserQuestion(user_id=2, question="Hi", priority="low")
    print(user2, "✅ PASSED")
except ValidationError as e:
    print("❌ Error (Question shorter than 10 characters):", e)


print("=" * 50)
print("TESTING EXTRACTED LEAD")
print("=" * 50)

try:
    extracted_lead = ExtractedLead(name="John Doe", email="john.doe@example.com", company="Example Inc")
    print(extracted_lead, "✅ PASSED")
    print(extracted_lead)
except ValidationError as e:
    print("❌ Error (Invalid email):", e)

try:
    extracted_lead2 = ExtractedLead(name="John Doe", email="john.doe@example.", company="Example Inc")
    print(extracted_lead2, "✅ PASSED")
except ValidationError as e:
    print("❌ Error Invalid email: ", e)


print("=" * 50)
print("TESTING CLASSIFICATION RESULT")
print("=" * 50)
# correct data
try:
    result1 = ClassificationResult(confidence_score=0.95, tags=["billing", "urgent"])
    print("✅ passed result:", result1)
except ValidationError as e:
    print("❌ failed result:", e)

# wrong data (confidence 1.5 hai)
try:
    result2 = ClassificationResult(confidence_score=1.5, tags=["billing"])
except ValidationError as e:
    print("❌ Error (Confidence score out of range):", e)

# Ghalat data (tags empty)
try:
    result3 = ClassificationResult(confidence_score=0.8, tags=[])
except ValidationError as e:
    print("❌ Error (Tags empty):", e)



