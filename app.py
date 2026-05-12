import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 데이터베이스 확인
st.set_page_config(page_title="예술의전당 데이터 대시보드", layout="wide")

DB_PATH = "예술의전당.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

# 데이터베이스 파일 존재 여부 확인
if not os.path.exists(DB_PATH):
    st.error(f"❌ '{DB_PATH}' 파일을 찾을 수 없습니다. 데이터베이스 파일이 같은 폴더에 있는지 확인해주세요!")
    st.stop()

st.title("🎭 예술의전당 공공데이터 분석 대시보드")
st.markdown("예술의전당 공연 운영 전략 설정을 위해 데이터를 시각화한 대시보드")

# --- 차트 1) 회원 성별 비율 (픽토그램 스타일) ---
st.divider()
st.header("1. 회원 성별 비율")

sql1 = """
select 성별, 
count (*) as 인원수,
round(count(*) *100.0 / (select count(*) from 회원), 2) || '%' AS 비율
from 회원
group by 성별;
"""

df1 = pd.read_sql(sql1, get_connection())

# 픽토그램 느낌을 위해 Plotly의 가로 막대와 이모지 활용
col1, col2 = st.columns([2, 1])
with col1:
    fig1 = px.bar(df1, x='인원수', y='성별', orientation='h',
                 color='성별', color_discrete_map={'여': '#ff4b4b', '남': '#1c83e1'},
                 text='비율')
    fig1.update_layout(showlegend=False, height=300)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.info("💡 **SQL 쿼리**\n" + f"```sql\n{sql1}\n```")
    st.success("**인사이트**\n1. 회원 성별의 비중을 통해 마케팅 타겟을 설정할 수 있습니다.\n2. 여성과 남성의 비율 차이가 크지 않으므로 성별에 관계없이 즐길 수 있는 공연을 기획해야 합니다.")


# --- 차트 2) 회원 나이 분포 (세로 막대) ---
st.divider()
st.header("2. 회원 연령대 분포")

sql2 = """
select 
(나이/10)*10 || '대' as 연령대,
count(*) as 인원수
from 회원
group by (나이/10)
order by 연령대;
"""
df2 = pd.read_sql(sql2, get_connection())

col1, col2 = st.columns([2, 1])
with col1:
    fig2 = px.bar(df2, x='연령대', y='인원수', color='연령대', title="연령별 회원수")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.info("💡 **SQL 쿼리**\n" + f"```sql\n{sql2}\n```")
    st.success("**인사이트**\n1. 어떤 연령대가 예술의전당을 가장 많이 이용하는지 한눈에 알 수 있습니다.\n2. 상대적으로 낮은 비율의 연령대인 10대 미만 아이들을 위한 참여 프로그램 개발이 필요합니다.")


# --- 차트 3) 2025년 작품 입장객 순위 및 장르 (가로 막대) ---
st.divider()
st.header("3. 2025년 관객수 TOP 10 작품")

sql3 = """
select 
A. 작품명, 
B. 장르,
SUM(A. 합계) as 총_입장객수
from 입장객 A
join 안내 B ON B.제목 like '%' || A.작품명 || '%'
where A.일자 LIKE '2025%'
Group by A.작품명, B.장르
order by 총_입장객수 DESC
limit 10;
"""
df3 = pd.read_sql(sql3, get_connection())

col1, col2 = st.columns([2, 1])
with col1:
    fig3 = px.bar(df3, x='총_입장객수', y='작품명', color='장르', orientation='h',
                 title="2025년 작품별 총 관객수 (TOP 10)")
    fig3.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.info("💡 **SQL 쿼리**\n" + f"```sql\n{sql3}\n```")
    st.success("**인사이트**\n1. 2025년 가장 흥행한 작품과 해당 작품의 장르를 파악할 수 있습니다.\n2. 상위권 작품의 성공 요인 분석이 필요함을 확인할 수 있습니다.")


# --- 차트 4) 2025년 인기 작품 TOP 100의 장르 비율 (원형 차트) ---
st.divider()
st.header("4. 2025년 인기 TOP 100 작품의 장르 비중")

sql4 = """
select top_works.장르, 
count(*) as 작품_수
from (
    select A.작품명, B.장르, SUM(A.합계) as 총_입장객수
    from 입장객 A
    JOIN 안내 B ON B.제목 LIKE '%' || A.작품명 || '%'
    WHERE A.일자 LIKE '2025%'
    GROUP BY A.작품명, B.장르
    ORDER BY 총_입장객수 DESC
    LIMIT 100
) AS TOP_WORKS 
GROUP BY TOP_WORKS.장르
ORDER BY 작품_수 DESC;
"""
df4 = pd.read_sql(sql4, get_connection())

col1, col2 = st.columns([2, 1])
with col1:
    fig4 = px.pie(df4, values='작품_수', names='장르', title="TOP 100 작품의 장르 분포",
                 hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.info("💡 **SQL 쿼리**\n" + f"```sql\n{sql4}\n```")
    st.success("**인사이트**\n1. 인기 있는 100개 작품 중 특정 장르가 차지하는 비중을 알 수 있습니다.\n2. 관객들이 선호하는 장르의 편중도를 확인하여 공연 라인업의 다양성을 검토할 수 있습니다.")

st.sidebar.info("👋 **안내**\n예술의전당 데이터를 SQLite와 Streamlit으로 분석하는 실습 화면입니다.")
