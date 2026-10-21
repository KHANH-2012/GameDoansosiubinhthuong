
import random
import streamlit as st

# Cau hinh trang
st.set_page_config(
    page_title="Game Doan So",
    page_icon="🎯",
    layout="centered"
)

# CSS giao dien
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #1e3a5f);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Khoi tao game
def new_game():
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.finished = False
    st.session_state.message = "Hay nhap mot so va bat dau!"
    st.session_state.history = []

if "secret" not in st.session_state:
    new_game()

# Tieu de
st.title("🎯 GAME ĐOÁN SỐ")
st.markdown("### Thử thách trí tuệ của bạn!")
st.write("Máy tính đã chọn một số từ **1 đến 100**.")
st.write("Bạn hãy đoán đúng số bí mật với ít lượt nhất nhé!")

# Hien thi thong tin
col1, col2 = st.columns(2)

with col1:
    st.metric("🔢 Số lượt đoán", st.session_state.attempts)

with col2:
    st.metric("📊 Phạm vi số", "1 - 100")

st.divider()

# Form nhap so
with st.form("guess_form", clear_on_submit=True):
    guess = st.number_input(
        "Nhập số bạn dự đoán:",
        min_value=1,
        max_value=100,
        value=50,
        step=1
    )

    submitted = st.form_submit_button(
        "🎯 KIỂM TRA",
        disabled=st.session_state.finished
    )

# Xu ly du doan
if submitted and not st.session_state.finished:
    st.session_state.attempts += 1
    number = int(guess)
    secret = st.session_state.secret

    st.session_state.history.append(number)

    if number < secret:
        st.session_state.message = "📈 Số bí mật LỚN HƠN!"
        st.info(st.session_state.message)

    elif number > secret:
        st.session_state.message = "📉 Số bí mật NHỎ HƠN!"
        st.info(st.session_state.message)

    else:
        st.session_state.finished = True
        st.session_state.message = "🎉 CHÍNH XÁC! BẠN ĐÃ CHIẾN THẮNG!"
        st.balloons()
        st.success(st.session_state.message)
        st.markdown(
            f"### Bạn đã tìm ra số {secret} "
            f"sau {st.session_state.attempts} lượt đoán!"
        )

# Hien thi thong bao sau khi rerun
if st.session_state.message and not submitted:
    if st.session_state.finished:
        st.success(st.session_state.message)
    elif st.session_state.attempts > 0:
        st.info(st.session_state.message)
    else:
        st.caption(st.session_state.message)

# Lich su du doan
if st.session_state.history:
    with st.expander("📜 Lịch sử đoán số"):
        for i, number in enumerate(st.session_state.history, start=1):
            st.write(f"Lượt {i}: {number}")

# Nut choi lai
st.divider()

if st.button("🔄 CHƠI VÁN MỚI", use_container_width=True):
    new_game()
    st.rerun()

st.caption("Made with Python 🐍 and Streamlit")
