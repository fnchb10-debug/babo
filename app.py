import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="당신은 바보입니까?",
    page_icon="🤔",
    layout="centered"
)

st.title("🤔 당신은 바보입니까?")
st.write("진실을 선택해 주세요. 거짓말은 안 돼요!")
st.divider()

# 버튼과 도망가는 기능
components.html("""
<div style="
    text-align: center;
    height: 350px;
    position: relative;
    padding-top: 30px;
">
    <h2 style="color:#444;">당신은 바보입니까?</h2>

    <button id="yes" onclick="alert('솔직하시군요! 😂')"
    style="
        background-color:#ff4b4b;
        color:white;
        border:none;
        padding:15px 35px;
        border-radius:12px;
        font-size:20px;
        cursor:pointer;
        margin:20px;
    ">
        예
    </button>

    <button id="no"
    style="
        position:absolute;
        left:55%;
        top:190px;
        background-color:#4b91ff;
        color:white;
        border:none;
        padding:15px 35px;
        border-radius:12px;
        font-size:20px;
        cursor:pointer;
        transition:0.08s;
    ">
        아니오
    </button>
</div>

<script>
const noButton = document.getElementById("no");

function escapeButton() {
    const area = noButton.parentElement;
    const maxX = area.clientWidth - noButton.offsetWidth;
    const maxY = area.clientHeight - noButton.offsetHeight;

    const newX = Math.random() * Math.max(0, maxX);
    const newY = Math.random() * Math.max(0, maxY);

    noButton.style.left = newX + "px";
    noButton.style.top = newY + "px";
}

noButton.addEventListener("mouseenter", escapeButton);

noButton.addEventListener("click", function(event) {
    event.preventDefault();
    escapeButton();
});
</script>
""", height=400)

st.caption("※ 아니오를 선택하려는 순간 도망갑니다! 😈")
