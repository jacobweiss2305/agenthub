from swarm import Swarm, AI

swarm = Swarm()

english_agent = AI(
    name="English AI",
    instructions="You only speak English.",
)

spanish_agent = AI(
    name="Spanish AI",
    instructions="You only speak Spanish.",
)


def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent


english_agent.functions.append(transfer_to_spanish_agent)

messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = swarm.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
