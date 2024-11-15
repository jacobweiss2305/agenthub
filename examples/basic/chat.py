from hive import Nest, Worker

nest = Nest()

worker_agent = Worker(
    name="Sophisticated writer",
    instructions="You write about honey bees.",
)

response = nest.run(
    agent=worker_agent,
    messages=[{"role": "user", "content": "Create a motivational haiku to inspire beekeepers."}],
)

print(response.messages[-1]["content"])