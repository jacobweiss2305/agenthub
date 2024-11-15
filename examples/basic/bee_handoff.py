from swarm import Swarm, Bee

swarm = Swarm()

english_bee = Bee(
    name="English Bee",
    instructions="You only speak English.",
)

spanish_bee = Bee(
    name="Spanish Bee",
    instructions="You only speak Spanish.",
)


def transfer_to_spanish_bee():
    """Transfer spanish speaking users immediately."""
    return spanish_bee


english_bee.functions.append(transfer_to_spanish_bee)

messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = swarm.run(bee=english_bee, messages=messages)

print(response.messages[-1]["content"])
