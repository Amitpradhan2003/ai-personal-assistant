from agent.assistant_agent import create_agent

agent = create_agent()

print("🧠 AI Personal Assistant is ready!")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    response = agent.run(query)
    print("\nAssistant:", response, "\n")
