import streamlit as st
import sqlite3

menu = st.sidebar.selectbox("MENU", ["로그인", "회원가입"])

if menu == "로그인":
    st.title("로그인")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type='password')
    login = st.button("로그인")
    if login:
        if username == "test" and password == "123":
            st.subheader(username + "님 환영합니다.")
            st.balloons()
        else:
            st.subheader("로그인 실패")
elif menu == "회원가입":
    st.title("회원가입")
    username = st.text_input("아이디를 입력하십시오:")
    password = st.text_input("비밀번호를 입력하십시오:",type='password')
    passwordChk = st.text_input("비밀번호 확인",type='password')
    if passwordChk == password:
        st.subheader("확인됐습니다")
    else:
        st.subheader("다시 입력하십시오")
    email = st.text_input("이메일을 입력하십시오")
    gender = st.text_input("성별을 입력하십시오")
    birthday = st.date_input("생일을 입력하십시오")
    age = st.number_input("나이를 입력하십시오", step = 1)
    join = st.button("join")

    if join:
        conn = sqlite3.connect('db.db')
        c = conn.cursor()

        c.execute(f'''
                insert into users(username, password, email, gender, birthday, age)
                values ('{username}', '{password}','{email}','{birthday}', {age})
                ''')
        conn.commit()
        conn.close()
