from swarm import Swarm, Bee

client = Swarm()

my_bee = Bee(
    name="Bee",
    instructions="You are a helpful bee.",
)


def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


messages = []
bee = my_bee
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(bee=bee, messages=messages)
    messages = response.messages
    bee = response.bee
    pretty_print_messages(messages)
