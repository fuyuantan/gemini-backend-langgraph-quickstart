**Only 4 steps to run this Agent:**<br>
1. Clone `git clone https://github.com/fuyuantan/gemini-backend-langgraph-quickstart`<br>
2. Install dependencies `pip install google-generativeai langchain-google-genai langgraph`<br>
3. Set your **GEMINI_API_KEY** in ``.env`` file.<br>
4. Run `python run.py`.<br>

**News/Differences:**<br>
1. `run.py` is newly created for starting this agent.<br>
2. Fixed bug:<br>
   In `configuration.py`,
   ```
   reasoning_model: str = Field(
        default="gemini-2.5-flash-preview-04-17",
        metadata={
            "description": "The name of the language model to use for the agent's reasoning."
        },
    )
   ```
   is added for resolving the error of ``AttributeError: 'Configuration' object has no attribute 'reasoning_model'``<br>
4. Fixed bug:<br>
   In ``graph.py``, a new parameter ``transport="rest"`` is added to ``llm = ChatGoogleGenerativeAI(...)`` to resolve the following gRPC connection timeout error:<br>
`Retrying langchain_google_genai.chat_models._chat_with_retry.<locals>._chat_with_retry in 2.0 seconds as it raised RetryError: Timeout of 600.0s exceeded, last exception: 503 failed to connect to all addresses; last error: UNKNOWN: ipv4:142.250.99.95:443: socket is null.`

**Outputs:**<br>
You can see, `run.py` visualizes the contents of  **Node**, **State**.
![1](https://github.com/user-attachments/assets/45e20e3b-1a22-4531-ab04-d7fcf298840c)

![2](https://github.com/user-attachments/assets/50489f6b-a54e-4340-a2ca-8b6315dcbd99)

![3](https://github.com/user-attachments/assets/935bf097-5100-44a7-9594-6bb1e5b20e07)

The **introductions/tutorials** of each .py file of `/Agent` is in the [README.md](https://github.com/fuyuantan/gemini-backend-langgraph-quickstart/tree/main/agent) under the `/Agent`.<br>

Find me in [小红书](https://www.xiaohongshu.com/user/profile/5ee64a640000000001001447).

Refer/Origin: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/tree/main
