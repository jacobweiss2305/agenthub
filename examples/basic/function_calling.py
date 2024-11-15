from swarm import Swarm, Bee

swarm = Swarm()

def get_weather(location) -> str:
    return "{'temp':67, 'unit':'F'}"

weather_bee = Bee(
    name="Weather Bee",
    instructions="You are a helpful bee.",
    functions=[get_weather],
)

messages = [{"role": "user", "content": "What's the weather in NYC?"}]

response = swarm.run(bee=weather_bee, messages=messages)
print(response.messages[-1]["content"])
