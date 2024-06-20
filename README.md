# FastAPI for interacting with langchain and GPT-3.5 based chatbot, with Redis database as the vector store-backed retriever memory.

## How to run

### Using Docker Compose:

1. Build the Docker images:
<code>make build</code>

2. Start the Docker containers:
<code>make build-up</code>

3. Install LLM Model to using Gpt4All library
<code>https://python.langchain.com/v0.2/docs/integrations/providers/gpt4all/</code>

## Add Docker container to VS Code
<code>https://www.youtube.com/watch?v=0H2miBK_gAk&ab_channel=PatrickLoeber</code>

4. After add dependancies with pip don't forget to run this command below at the current path
<code>pip freeze > requirements.txt</code>

## API Documentation

### Accessing API Documentation

For detailed documentation on how to interact with the APIs in the application, visit:
<code>localhost:8000/docs</code>


This endpoint provides comprehensive guidance on utilizing the APIs effectively.

---

You can seamlessly integrate this backend into your existing application, providing your users with access to a dedicated vector-based database chatbot. Remember to generate the repsective API keys.