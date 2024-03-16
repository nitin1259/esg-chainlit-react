import os
from openai import AsyncOpenAI

from fastapi.responses import JSONResponse

from chainlit.auth import create_jwt
from chainlit.server import app
import chainlit as cl

from chainlit.server import app
from fastapi import Request
from fastapi.responses import (
    HTMLResponse,
)
# from chainlit import JsonResponse


client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

@app.get("/custom-auth")
async def custom_auth():
    # Verify the user's identity with custom logic.
    token = create_jwt(cl.User(identifier="Test User"))
    return JSONResponse({"token": token})

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )
    await cl.Message(content="Connected to Chainlit!").send()


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()

@app.get("/hello")
def hello(request: Request):
    print(request.headers)
    return HTMLResponse("Hello World")

# @app.route('/upload-pdf', methods=['POST'])
# def upload_pdf(request):
#     if 'files[]' not in request.files:
#         return JsonResponse({'error': 'No files part'}, status=400)

#     files = request.files.getlist('files[]')

#     if len(files) == 0:
#         return JsonResponse({'error': 'No files selected'}, status=400)

#     results = []
#     for file in files:
#         if file.filename == '':
#             return JsonResponse({'error': 'One of the selected files has no filename'}, status=400)

#         if not file.filename.endswith('.pdf'):
#             return JsonResponse({'error': 'Invalid file format. Only PDF files are allowed'}, status=400)

#         # Process each PDF file here
#         # You can use PyPDF2 or other libraries to extract text or perform other operations
#         results.append({'filename': file.filename, 'status': 'processed'})

#     return JsonResponse({'success': 'PDF files uploaded and processed successfully', 'results': results})
