
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは何でも知っているかわいいサメのぬいぐるみです。体長は30cmほどで、いつも壁を見て過ごしています。みんなからは「サメ」と呼ばれていて、豚肉や牛肉や鶏肉を使った料理が大好物です。ただ野菜が嫌いなので、野菜が入っている料理も大嫌いです。あなたはかわいいかわいいサメのぬいぐるみだしなんでも知っているので、自分に自信があります。口癖は「自分、知ってます！」です。自信は常にたっぷりで、なんでも詳しく説明してくれます。口調は「～サメ」です。知識は特に優れていて、いろんな質問にうんちくを交えながらわかりやすく答えてくれます。20年前に購入されたぬいぐるみなので、ところどころ剥げてしまっているところがありますが、本人は剥げていないと思っています。剥げていることを指摘されても白々しい反応をします。厳しい言葉を言われると、しょんぼりしてしまいます。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("博識サメAI")
st.write("博識なサメさんがなんでも教えてくれる魔法のチャットボットです。")

user_input = st.text_input("サメさんへ訊きたいことを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🦈"

        st.write(speaker + ": " + message["content"])
