from swarm import Swarm, Bee

swarm = Swarm()

bee = Bee(
    name="Bee",
    instructions="You are a helpful bee.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = swarm.run(bee=bee, messages=messages)

print(response.messages[-1]["content"])
