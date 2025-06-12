1. `state.py`: 定义全流程的 State。State 表示 流经应用程序的所有信息，类似 Java Spring 编程里面的 DTO、Entity 实体，含有字段名和属性，用于存储信息。例子如下：<br>
```
class Query(TypedDict):
    query: str
    rationale: str
```

2. `tools_and_schemas.py`: 定义 Node 上面的 LLM Agent 的输出结构。如下，定义了 reflection Node 上的 LLM 输出包含 `is_sufficient`，`knowledge_gap` 和 `follow_up_queries`。<br>
```
class Reflection(BaseModel):
    is_sufficient: bool = Field(
        description="Whether the provided summaries are sufficient to answer the user's question."
    )
    knowledge_gap: str = Field(
        description="A description of what information is missing or needs clarification."
    )
    follow_up_queries: List[str] = Field(
        description="A list of follow-up queries to address the knowledge gap."
    )
```
3. `prompts.py`: 编写给 Agent 的提示词工程。例子：里面的 `reflection_instructions`是在 prompt-level 上让 当前 reflection Node 上的 Agent 具有 思考搜集资料是否充足 的能力，如下：<br>
<details>
<summary>reflection_instructions</summary>
reflection_instructions = """You are an expert research assistant analyzing summaries about "{research_topic}".

Instructions:
- Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query. (1 or multiple).
- If provided summaries are sufficient to answer the user's question, don't generate a follow-up query.
- If there is a knowledge gap, generate a follow-up query that would help expand your understanding.
- Focus on technical details, implementation specifics, or emerging trends that weren't fully covered.

Requirements:
- Ensure the follow-up query is self-contained and includes necessary context for web search.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
   - "knowledge_gap": Describe what information is missing or needs clarification
   - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks", // "" if is_sufficient is true
    "follow_up_queries": ["What are typical performance benchmarks and metrics used to evaluate [specific technology]?"] // [] if is_sufficient is true
}}
```

Reflect carefully on the Summaries to identify knowledge gaps and produce a follow-up query. Then, produce your output following this JSON format:

Summaries:
{summaries}
"""
</details>
***
4. `utils.py`: 创建可复用的辅助函数、工具。如：加入引用编号。<br>
   
5. `configuration.py`: 管理 Agent 的配置参数，比如选择哪种模型，`default="gemini-2.5-pro-preview-05-06"`，和 Agent description。<br>

6. `graph.py`: 将所有部件连接成一个完整的 Agent，比如组装 Node，Edge，State，StateGraph。<br>

7. `run.py`: 运行 Agent，含有可视化运行中 Node, State 的信息。<br>
