import streamlit as st
import random
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 운세는?", page_icon="🃏")

# 2. 제목 설정
st.title("🔮 오늘의 운세는?")
st.write(f"반가워요! 오늘은 **{date.today().strftime('%Y년 %m월 %d일')}**입니다.")

# 3. 데이터 준비 (운세 리스트)
if 'selected_fortune' not in st.session_state:
    fortunes = [
        "✨ 오늘은 생각지도 못한 행운이 넝쿨째 굴러들어올 날입니다!",
        "🏃 적극적으로 움직이세요. 가만히 있으면 기회를 놓칠 수 있습니다.",
        "🎁 소중한 사람에게 작은 선물을 해보세요. 배가 되어 돌아옵니다.",
        "🧘 마음의 여유가 필요한 날입니다. 따뜻한 차 한 잔 어떠세요?",
        "💰 금전운이 상승하고 있습니다! 계획했던 소비를 해도 좋은 날입니다.",
        "🤫 비밀을 잘 지켜야 합니다. 구설수에 오를 수 있으니 조심하세요.",
        "🌈 고민하던 문제가 말끔히 해결될 징조가 보입니다.",
        "🍀 파란색 아이템이 행운을 가져다줄 거예요.",
        "💡 새로운 아이디어가 샘솟는 날입니다. 메모를 잊지 마세요!",
        "🍎 건강을 위해 가벼운 산책을 추천합니다. 몸이 가벼워질 거예요."
    ]
    st.session_state.selected_fortune = random.choice(fortunes)
    st.session_state.flipped = False

# 4. 입력 섹션
st.divider()
col1, col2 = st.columns(2)
with col1:
    user_zodiac = st.selectbox("🌠 별자리 선택", 
        ["양자리", "황소자리", "쌍둥이자리", "게자리", "사자자리", "처녀자리", "천칭자리", "전갈자리", "사수자리", "염소자리", "물병자리", "물고기자리"])
with col2:
    user_animal = st.selectbox("🐾 띠 선택", 
        ["쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠", "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"])

st.divider()

# 5. 카드 클릭 UI
st.write("### 🃏 아래의 카드 이모지를 클릭하세요!")

# 카드가 뒤집히지 않은 상태
if not st.session_state.flipped:
    # 큰 이모지 버튼 생성
    if st.button("🧧\n\n클릭해서 확인", use_container_width=True):
        st.session_state.flipped = True
        st.rerun()
    
    st.caption("카드를 클릭하면 운세가 공개됩니다.")

# 카드가 뒤집힌 상태 (결과 화면)
else:
    st.balloons() # 축하 효과
    
    # 결과 박스 디자인
    st.markdown(f"""
        <div style="
            background-color: #ffffff;
            border: 4px solid #FF4B4B;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        ">
            <h2 style="color: #FF4B4B; margin-bottom: 10px;">🃏 복채는 구독과 좋아요?</h2>
            <p style="font-size: 1.1rem; color: #555;">{user_zodiac} {user_animal} 운세</p>
            <hr style="border: 0.5px solid #eee;">
            <h1 style="font-size: 1.6rem; color: #31333F; line-height: 1.5;">
                {st.session_state.selected_fortune}
            </h1>
        </div>
    """, unsafe_allow_html=True)

    # 다시 뽑기 버튼
    if st.button("🔄 다시 뽑기", use_container_width=True):
        st.session_state.flipped = False
        # 새로운 운세 미리 선정
        st.session_state.selected_fortune = random.choice([
            "✨ 새로운 기운이 솟아납니다!", "🍀 운이 따르는 하루입니다.", "🤫 말을 아끼면 복이 옵니다.", "🏃 오늘 바로 실천하세요!"
        ]) 
        st.rerun()

st.divider()
st.caption("재미로 보는 운세입니다. 행복한 하루 되세요! 😊")
