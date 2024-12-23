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

# ��ʼ������
init_env()
deployment_name=os.getenv("AOAI_DEPLOYMENTID")
embeddings_deployment_name=os.getenv("AOAI_EMBEDDINGS_DEPLOYMENTID")

# ����ҳ������
st.set_page_config(page_title="��7��", page_icon="robot_face")

# ������֤����
def check_password():
    if "password_correct" in st.session_state:
        correct = st.session_state.password_correct
        return correct

    def password_entered():
        """��������Ƿ���ȷ��������session_state����"""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            # ����洢����
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    # ��ʾ���������
    password = st.text_input(
        "����", 
        type="password", 
        on_change=password_entered, 
        key="password"
    )

    # ��������ѱ���֤�򷵻� True
    if st.session_state.get("password_correct", False):
        return True

    # ���������֤ʧ��
    if "password_correct" in st.session_state:
        st.error("�������")
        return False

# ����������֤����
if not check_password():
    st.stop()  # �������δͨ����֤����ִֹͣ�С�

# ����ͨ����֤���Ӧ�ó������ִ���߼�
# ��StreamlitӦ�ó����д���AI���ֵı���
st.header("��7�� - ���Լ������ݶԻ�")

# �����Ҫ����ʼ��������Ϣ��ʷ��¼
if "messages" not in st.session_state:
    st.session_state.messages = []

# ��ȡ�û����벢���浽������ʷ��¼
if query := st.chat_input("��������"):
    st.session_state.messages.append({"role": "user", "content": query})

# ��ʾ֮ǰ��������ʷ��¼
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ������һ����Ϣ�����������֣��������µ���Ӧ
if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("˼����..."):
            # ��������ǽ��������Ĵ���������LLM�����Ŀǰ���ɿհ׻ظ�
            response = ""
            # ��ʾ AI ���ɵĻش�
            st.write(response)
            message = {"role": "assistant", "content": response}
            # ����Ӧ��ӵ���Ϣ��ʷ��¼��
            st.session_state.messages.append(message)