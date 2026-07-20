from router import select_model
from tasks import TASKS

print("=" * 60)
print("          AI MODEL ROUTING SYSTEM")
print("=" * 60)

while True:

    print("\nAvailable Tasks:\n")

    for task in TASKS:
        print("-", task)

    print("\nType 'exit' to quit the program.")

    user_task = input("\nEnter Task Name: ").strip().lower()

    # Exit condition
    if user_task == "exit":
        print("\nThank you for using AI Model Routing System.")
        print("Program Closed Successfully!")
        break

    result = select_model(user_task)

    if result:

        print("\nTask Information")
        print("-" * 40)

        print("Required Quality      :", result["required_quality"])
        print("Latency Sensitivity   :", result["latency_sensitivity"])
        print("Cost Sensitivity      :", result["cost_sensitivity"])
        print("Recommended Model     :", result["recommended_model"])

    else:
        print("\n❌ Task Not Found!")
        print("Please enter one of the available tasks.")