**Only 4 steps to run this Agent:**<br>
1. Clone ``git clone https://github.com/fuyuantan/gemini-backend-langgraph-quickstart``<br>
2. Install dependencies ``pip install google-generativeai langchain-google-genai langgraph``<br>
3. Set your **GEMINI_API_KEY** in ``.env`` file.<br>
4. Run `python run.py`.<br>

**News/Differences:**<br>
1. `run.py` is newly created for starting this agent.<br>
2. Fixed bug: In `configuration.py``,
   ```
   reasoning_model: str = Field(
        default="gemini-2.5-flash-preview-04-17",
        metadata={
            "description": "The name of the language model to use for the agent's reasoning."
        },
    )
   ```
   is added for solving the error of ``AttributeError: 'Configuration' object has no attribute 'reasoning_model'``<br>
3. Fixed bug: In ``graph.py``, ``llm = ChatGoogleGenerativeAI(...)`` are added a new param ``transport="rest"`` for solving the error of gRPC connection timeout.<br>

**Outputs:**<br>
You can see, `run.py` visualize the contents of  **Node**, **State**.
![1](https://github.com/user-attachments/assets/45e20e3b-1a22-4531-ab04-d7fcf298840c)

![2](https://github.com/user-attachments/assets/50489f6b-a54e-4340-a2ca-8b6315dcbd99)

![3](https://github.com/user-attachments/assets/935bf097-5100-44a7-9594-6bb1e5b20e07)

Refer/Origin: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/tree/main
