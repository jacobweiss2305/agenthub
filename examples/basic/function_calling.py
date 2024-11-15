from hive import Hive, AI

swarm = Hive()

def get_weather(location) -> str:
    return "{'temp':67, 'unit':'F'}"

weather_agent = AI(
    name="Weather AI",
    instructions="You are a helpful agent.",
    functions=[get_weather],
)

messages = [{"role": "user", "content": "What's the weather in NYC?"}]

response = swarm.run(agent=weather_agent, messages=messages)
print(response.messages[-1]["content"])
