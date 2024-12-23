import os
import hmac
from dotenv import load_dotenv, find_dotenv
import streamlit as st
def init_env():
    _ = load_dotenv(find_dotenv())
    os.environ["LANGCHAIN_TRACING"] = "false"
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_VERSION"] = "0301"
    os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
    os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")

# 初始化环境
init_env()
deployment_name=os.getenv("AOAI_DEPLOYMENTID")
embeddings_deployment_name=os.getenv("AOAI_EMBEDDINGS_DEPLOYMENTID")

# 设置页面配置
st.set_page_config(page_title="第7章", page_icon="robot_face")

# 密码验证函数
def check_password():
    if "password_correct" in st.session_state:
        correct = st.session_state.password_correct
        return correct

    def password_entered():
        """检查密码是否正确，并设置session_state变量"""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            # 无需存储密码
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    # 显示密码输入框
    password = st.text_input(
        "密码", 
        type="password", 
        on_change=password_entered, 
        key="password"
    )

    # 如果密码已被验证则返回 True
    if st.session_state.get("password_correct", False):
        return True

    # 如果密码验证失败
    if "password_correct" in st.session_state:
        st.error("密码错误")
        return False

# 调用密码验证函数
if not check_password():
    st.stop()  # 如果密码未通过验证，则停止执行。

# 密码通过验证后的应用程序后续执行逻辑
# 在Streamlit应用程序中创建AI助手的标题
st.header("第7章 - 与自己的数据对话")

# 如果需要，初始化聊天消息历史记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 获取用户输入并保存到聊天历史记录
if query := st.chat_input("您的问题"):
    st.session_state.messages.append({"role": "user", "content": query})

# 显示之前的聊天历史记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 如果最后一条消息不是来自助手，则生成新的响应
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            # 在这里，我们将添加所需的代码来生成LLM输出，目前生成空白回复
            response = ""
            # 显示 AI 生成的回答
            st.write(response)
            message = {"role": "assistant", "content": response}
            # 将响应添加到消息历史记录中
            st.session_state.messages.append(message)