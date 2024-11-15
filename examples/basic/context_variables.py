from agenthub import Team, Agent

team = Team()


def instructions(context_variables):
    name = context_variables.get("name", "User")
    return f"You are a helpful agent. Greet the user by name ({name})."


def print_account_details(context_variables: dict):
    user_id = context_variables.get("user_id", None)
    name = context_variables.get("name", None)
    print(f"Account Details: {name} {user_id}")
    return "Success"


customer_support_agent = Agent(
    name="Customer Support AI",
    instructions=instructions,
    functions=[print_account_details],
)

context_variables = {"name": "James", "user_id": 123}

response = team.run(
    messages=[{"role": "user", "content": "Hi!"}],
    agent=customer_support_agent,
    context_variables=context_variables,
)

print(response.messages[-1]["content"])

response = team.run(
    messages=[{"role": "user", "content": "Print my account details!"}],
    agent=customer_support_agent,
    context_variables=context_variables,
)

print(response.messages[-1]["content"])
