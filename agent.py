from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from config import OPENAI_API_KEY, MODEL_NAME, SYSTEM_PROMPT, MAX_ITERATIONS
from tools import all_tools


def create_research_agent():


    if OPENAI_API_KEY:
        llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=OPENAI_API_KEY,
            temperature=0.1
        )

    else:
        raise ValueError(
            "API ключ не знайдено! "
            "Додай OPENAI_API_KEY у файл .env"
        )


    memory = MemorySaver()


    agent = create_react_agent(
        model=llm,
        tools=all_tools,
        checkpointer=memory,
        prompt=SYSTEM_PROMPT,
    )


    return agent


def run_agent(agent, user_input: str, thread_id: str = "default"):

    config = {
        "configurable": {
            "thread_id": thread_id
        },
        "recursion_limit": MAX_ITERATIONS
    }

    # Запускаємо агента
    result = agent.invoke(
        {"messages": [("user", user_input)]},
        config=config
    )


    last_message = result["messages"][-1]

    return last_message.content