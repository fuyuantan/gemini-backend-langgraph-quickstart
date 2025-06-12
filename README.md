**Only 4 steps to run this Agent:**<br>
1. ``git clone https://github.com/fuyuantan/gemini-backend-langgraph-quickstart``<br>
2. Install dependencies ``pip install google-generativeai langchain-google-genai langgraph``<br>
3. Set your **GEMINI_API_KEY** in ``.env`` file.<br>
4. Run `python run.py`.<br>

**News/Differences:**<br>
1. A new .py file, `run.py`, is created for start this agent.<br>
2. Fix bug: ``AttributeError: 'Configuration' object has no attribute 'reasoning_model'``<br>
3. In ``graph.py``, ``llm = ChatGoogleGenerativeAI(...)`` are added a new param ``transport="rest"`` for solving the problem of gRPC connection timeout.<br>

Outputs:<br>
You can see, `run.py` visualize the contents of  **Node**, **State**.
![1](https://github.com/user-attachments/assets/45e20e3b-1a22-4531-ab04-d7fcf298840c)

![2](https://github.com/user-attachments/assets/50489f6b-a54e-4340-a2ca-8b6315dcbd99)

![3](https://github.com/user-attachments/assets/935bf097-5100-44a7-9594-6bb1e5b20e07)

Refer/Origin: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart/tree/main
