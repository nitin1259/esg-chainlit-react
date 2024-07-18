# Custom React frontend with Chainlit!

## Install Chainlit and OpenAI

```shell
pip install -U chainlit openai
```

## Start the Chainlit server

Create a `./chainlit-backend/.env` file:

## create a .env and provide OPENAI API Key
```.env
OPENAI_API_KEY=YOUR_API_KEY
```

Start the server in headless mode:

```shell
cd ./chainlit-backend

chainlit run app.py -h
```

## Start the React app

```shell
cd ./frontend

npm install

npm run dev
```
