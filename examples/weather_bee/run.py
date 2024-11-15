from swarm.repl import run_demo_loop
from bees import weather_bee

if __name__ == "__main__":
    run_demo_loop(weather_bee, stream=True)
