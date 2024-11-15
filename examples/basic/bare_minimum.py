from hive import Nest, Worker

nest = Nest()

agent = Worker(
    name="AI agent",
    instructions="You are a helpful AI assistant.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = nest.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
