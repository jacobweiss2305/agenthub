from swarm import Swarm, Bee

swarm = Swarm()


def instructions(context_variables):
    name = context_variables.get("name", "User")
    return f"You are a helpful bee. Greet the user by name ({name})."


def print_account_details(context_variables: dict):
    user_id = context_variables.get("user_id", None)
    name = context_variables.get("name", None)
    print(f"Account Details: {name} {user_id}")
    return "Success"


customer_support_bee = Bee(
    name="Customer Support Bee",
    instructions=instructions,
    functions=[print_account_details],
)

context_variables = {"name": "James", "user_id": 123}

response = swarm.run(
    messages=[{"role": "user", "content": "Hi!"}],
    bee=customer_support_bee,
    context_variables=context_variables,
)

print(response.messages[-1]["content"])

response = swarm.run(
    messages=[{"role": "user", "content": "Print my account details!"}],
    bee=customer_support_bee,
    context_variables=context_variables,
)

print(response.messages[-1]["content"])
