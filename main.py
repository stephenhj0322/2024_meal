import streamlit as st
import pandas as pd
import datetime

# 샘플 데이터 생성
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# 공휴일 정보를 저장하는 리스트 (공휴일이 있을 경우 여기에 추가)
public_holidays = [
    datetime.date(2024, 6, 6),  # 현충일
    # 다른 공휴일 추가 가능
]

def calculate_meal_order(date, lunch_order_start, dinner_order_start):
    weekday = date.weekday()  # 날짜의 요일을 가져옴 (0: 월요일, 1: 화요일, ..., 6: 일요일)
    if weekday < 5 and date not in public_holidays:  # 평일이고 공휴일이 아닌 경우
        lunch_order = [(lunch_order_start) % 10 + 1]  # 중식 순서 계산
        dinner_order = [(dinner_order_start) % 10 + 1]  # 석식 순서 계산
        return f"{date.year}년 {date.month}월 {date.day}일 {weekday_to_string(weekday)} 중식:{ lunch_order}반 석식:{ dinner_order}반"
    else:
        return None

def weekday_to_string(weekday):
    weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return weekdays[weekday]

def generate_meal_schedule(start_date, end_date):
    meal_schedule = []
    delta = datetime.timedelta(days=1)
    current_date = start_date
    lunch_order_start = 0
    dinner_order_start = 1

    while current_date <= end_date:
        meal_order = calculate_meal_order(current_date, lunch_order_start, dinner_order_start)
        if meal_order:
            meal_schedule.append(meal_order)
            lunch_order_start = (lunch_order_start + 1) % 10
            dinner_order_start = (dinner_order_start + 1) % 10
            lunch_order_start += 1
            dinner_order_start += 1

        current_date += delta

    return meal_schedule

# Streamlit 애플리케이션 시작
st.header('1학년 급식순서')
st.subheader('오늘은 몇반 부터?')

# 동그라미 버튼 생성
if st.button('Click Me', key='circle_button', help='Click to show meal schedule'):
    # 원하는 기간 입력
    start_date = datetime.date(2024, 5, 21)
    end_date = datetime.date(2024, 6, 21)

    # 입력된 기간 동안의 급식 순서 계산
    meal_schedule = generate_meal_schedule(start_date, end_date)

    # 첫 번째 날의 급식 순서 출력
    if meal_schedule:
        st.subheader('급식 순서')
        st.write(meal_schedule[0])
    else:
        st.write("해당 기간에는 급식이 없습니다.")

# 동그라미 버튼 스타일 설정
st.markdown("""
    <style>
    div[data-testid="stButton"] > button:first-child {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# sample comment
