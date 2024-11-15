from aihive import Nest, Worker
nest = Nest()

def calculator(operation: str, a: float, b: float) -> float:
    """
    A comprehensive calculator function that performs basic arithmetic operations.
    
    Args:
        operation: The arithmetic operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number
        
    Returns:
        float: Result of the arithmetic operation
        
    Raises:
        ValueError: If invalid operation or division by zero
    """
    operation = operation.lower()
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b 
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Invalid operation: {operation}")

def search_internet(query: str) -> str:
    return "This is a test"

worker_agent = Worker(
    name="Sophisticated writer",
    instructions="an agent that uses tools to answer questions",
    functions=[calculator],
)

response = nest.run(
    agent=worker_agent,
    messages=[{"role": "user", "content": "What is 100 * 100?"}],
    debug=True,
)

print(response.messages[-1]["content"])