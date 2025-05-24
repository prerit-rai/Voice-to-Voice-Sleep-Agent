import chainlit as cl
from agent import get_response

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = get_response(user_input)
    await cl.Message(content=response).send()