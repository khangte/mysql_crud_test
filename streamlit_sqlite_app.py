import streamlit as st
import sqlite3
import pandas as pd
import os

# SQLite DB 파일 경로
DB_PATH = os.path.join(os.path.dirname(__file__), "classicmodels.sqlite")
st.write("🔎 열리는 DB 파일 경로:", DB_PATH)

def fetch_data(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cleaned_query = query.strip().rstrip(';')
        st.write("🧪 실행 전 쿼리:", repr(cleaned_query))

        cursor.execute(cleaned_query)

        if cursor.description is None:
            st.warning("⚠️ 결과가 없는 쿼리입니다 (예: INSERT, DELETE 등)")
            return pd.DataFrame()

        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        return pd.DataFrame(rows, columns=columns)

    except Exception as e:
        st.error(f"❌ fetch_data 내부 오류: {e}")
        return pd.DataFrame()

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Streamlit UI
st.title("📦 ClassicModels Dashboard (SQLite)")

# SQL 입력창
user_query = st.text_area("📝 SQL 쿼리를 입력하세요:", "SELECT * FROM customers LIMIT 10;")

# 실행 버튼
if st.button("실행"):
    st.write("💡 실행된 쿼리:")
    st.code(user_query, language='sql')

    result_df = fetch_data(user_query)

    if not result_df.empty:
        st.success(f"✅ {len(result_df)}개 행 조회됨")
        st.dataframe(result_df)
    else:
        st.warning("⚠️ 결과가 없거나 쿼리에 오류가 있습니다.")
