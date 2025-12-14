import streamlit as st
import random

# --- ส่วนที่ 1: ตั้งค่าความจำ (Session State) ---
# เนื่องจาก Web App จะรีเฟรชใหม่ทุกครั้งที่กดปุ่ม เราต้องสั่งให้มันจำคะแนนไว้
if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'round_result' not in st.session_state:
    st.session_state.round_result = "Start the game by choosing a weapon!"

# --- ฟังก์ชัน: รีเซ็ตเกมเมื่อจบ ---
def reset_game():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.round_result = "Game Reset! Start new game."

# --- ฟังก์ชัน: ตรรกะเกม (Logic เดิมของคุณ) ---
def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # ตัดสินผล
    if player_choice == computer_choice:
        result_msg = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_msg = "You Win!"
        st.session_state.player_score += 1 # บวกคะแนนในความจำ
    else:
        result_msg = "You Lose!"
        st.session_state.computer_score += 1 # บวกคะแนนในความจำ

    # บันทึกผลลัพธ์เพื่อเอาไปโชว์
    st.session_state.round_result = f"You: {player_choice} 🆚 Com: {computer_choice} -> {result_msg}"

# ==========================================
# --- ส่วนหน้าตาเว็บไซต์ (UI Layout) ---
# ==========================================

st.title("✊✋✌️ The PYC Game (Web Version)")
st.write("First to 3 wins! (Best of 5)")

# 1. แสดงคะแนน (Scoreboard)
col1, col2 = st.columns(2)
with col1:
    st.metric("Your Score", st.session_state.player_score)
with col2:
    st.metric("Computer Score", st.session_state.computer_score)

st.divider() # เส้นขีดคั่น

# 2. เช็คว่าจบเกมหรือยัง?
if st.session_state.player_score >= 3:
    st.success("🎉 CONGRATULATIONS! YOU WON THE MATCH!")
    if st.button("Play Again"):
        reset_game()
        st.rerun() # รีเฟรชหน้าเว็บทันที

elif st.session_state.computer_score >= 3:
    st.error("💀 GAME OVER! COMPUTER WON THE MATCH!")
    if st.button("Try Again"):
        reset_game()
        st.rerun()

else:
    # 3. ถ้าเกมยังไม่จบ -> แสดงปุ่มให้กดเลือกอาวุธ
    st.write("Choose your weapon:")

    # จัดปุ่มเรียงแนวนอนสวยๆ 3 ปุ่ม
    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        if st.button("✊ Rock"):
            play_game("Rock")
            st.rerun() # สั่งรีเฟรชเพื่ออัปเดตคะแนน

    with btn_col2:
        if st.button("✋ Paper"):
            play_game("Paper")
            st.rerun()

    with btn_col3:
        if st.button("✌️ Scissors"):
            play_game("Scissors")
            st.rerun()

# 4. แสดงผลลัพธ์รอบล่าสุด
st.info(st.session_state.round_result)
