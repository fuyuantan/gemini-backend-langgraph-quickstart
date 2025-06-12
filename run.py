import asyncio
from uuid import uuid4
from langchain_core.messages import HumanMessage
from agent.graph import graph


async def run_agent():
    print("--- Running Gemini LangGraph Search Agent ---")

    user_question = "Who won the euro 2024"

    # 根据 graph.py 的设计，入口 generate_query 函数需要一个 'messages' 列表作为起始点。
    inputs = {"messages": [HumanMessage(content=user_question)]}

    # 你的 Agent 使用了 `Configuration` 类，这意味着我们可以动态覆盖默认设置。
    thread_id = str(uuid4())
    config = {
        "configurable": {
            "thread_id": thread_id,
            "max_research_loops": 3,
            "initial_search_query_count": 3,
        }
    }

    # 使用 .stream() 并流式处理输出，因为它能让你实时看到 Agent 的每一步操作。
    print(f"\n User question: '{user_question}'\n")
    final_answer = None

    # .stream() 会返回一个异步生成器，其中包含每个节点执行后的状态更新
    async for event in graph.astream(inputs, config=config):
        # `event` 是一个字典，key 是节点名，value 是该节点返回的状态更新
        for key, value in event.items():
            # 可视化打印整个流转过程
            print(f"--- Node: {key} ---")
            if 'messages' in value and value['messages']:
                # 如果是最终答案，它会被放在 messages 列表里
                final_answer = value['messages'][-1].content
                print(f"  Message: {final_answer}")
            else:
                # 打印其他状态更新以供调试
                print(f"  State Update: {value}")
            print("\n")

    print("--- Agent Finish ---")
    if final_answer:
        print("\nFinal answer:")
        print(final_answer)
    else:
        print("Agent failed to  generate final answer.")


if __name__ == "__main__":
    asyncio.run(run_agent())
