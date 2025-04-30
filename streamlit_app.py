import streamlit as st
import pandas as pd
from pool import connection_pool

# 쿼리 실행 함수
def fetch_data(query):
    try:
        conn = connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        return pd.DataFrame(rows, columns=columns)
    except Exception as e:
        st.error(f"❌ 쿼리 실행 중 오류 발생: {e}")
        return pd.DataFrame()
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

# Streamlit UI
st.title("📊 ClassicModels Dashboard")

# 쿼리 입력창
user_query = st.text_area("📝 SQL 쿼리를 입력하세요:", "SELECT * FROM customers LIMIT 10;")

# 실행 버튼
if st.button("실행"):
    st.write("💡 실행된 쿼리:")
    st.code(user_query, language='sql')

    # 쿼리 실행 및 결과 출력
    result_df = fetch_data(user_query)
    
    if not result_df.empty:
        st.success(f"✅ {len(result_df)}개 행이 조회되었습니다.")
        st.dataframe(result_df)
    else:
        st.warning("⚠️ 결과가 비어 있거나 쿼리에 오류가 있습니다.")
