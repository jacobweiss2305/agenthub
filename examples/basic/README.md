# Swarm basic

This folder contains basic examples demonstrating core Swarm capabilities. These examples show the simplest implementations of Swarm, with one input message, and a corresponding output. The `simple_loop_no_helpers` has a while loop to demonstrate how to create an interactive Swarm session.

### Examples

1. **bee_handoff.py**

   - Demonstrates how to transfer a conversation from one bee to another.
   - **Usage**: Transfers Spanish-speaking users from an English bee to a Spanish bee.

2. **bare_minimum.py**

   - A bare minimum example showing the basic setup of an bee.
   - **Usage**: Sets up an bee that responds to a simple user message.

3. **context_variables.py**

   - Shows how to use context variables within an bee.
   - **Usage**: Uses context variables to greet a user by name and print account details.

4. **function_calling.py**

   - Demonstrates how to define and call functions from an bee.
   - **Usage**: Sets up an bee that can respond with weather information for a given location.

5. **simple_loop_no_helpers.py**
   - An example of a simple interaction loop without using helper functions.
   - **Usage**: Sets up a loop where the user can continuously interact with the bee, printing the conversation.

## Running the Examples

To run any of the examples, use the following command:

```shell
python3 <example_name>.py
```
