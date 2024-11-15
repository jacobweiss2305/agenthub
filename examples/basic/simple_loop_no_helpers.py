from agenthub import Team, Agent

team = Team()

my_agent = Agent(
    name="AI agent",
    instructions="You are a helpful agent.",
)

def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


messages = []
agent = my_agent
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})
    response = team.run(agent=agent, messages=messages)
    messages = response.messages
    agent = response.agent
    pretty_print_messages(messages)
