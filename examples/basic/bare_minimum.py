from swarm import Swarm, AI

swarm = Swarm()

agent = AI(
    name="AI agent",
    instructions="You are a helpful AI assistant.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = swarm.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
