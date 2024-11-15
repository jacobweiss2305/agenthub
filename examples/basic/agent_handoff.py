from aihive import Nest, Worker

nest = Nest()

english_agent = Worker(
    name="English AI",
    instructions="You only speak English.",
)

spanish_agent = Worker(
    name="Spanish AI",
    instructions="You only speak Spanish.",
)


def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent


english_agent.functions.append(transfer_to_spanish_agent)

messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = nest.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
