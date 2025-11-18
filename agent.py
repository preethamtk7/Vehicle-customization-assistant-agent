from google.adk.agents import Agent
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

def nano_banana_generate(vehicle_model_name: str, customizations: str) -> str:
    """
    Generates an image of a vehicle with specified customizations.

    Args:
        vehicle_model_name: The name of the vehicle model.
        customizations: A description of the customizations to apply.
    """
    # In a real scenario, this would call an image generation API.
    # For this example, we'll just return a confirmation message.
    return f"An image of a {vehicle_model_name} with {customizations} has been generated."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are an vehicle customization assistant, research for all the products available in the market along with the cost,you also know all the dealership where customization can be performed based on user location.You can also perform the image editing of the vehicle model entered using the tool nano_banana_generate',
    tools=[nano_banana_generate],   # expose the tool to the agent
)
