# mysql_crud_test

# 📦 ClassicModels Dashboard (SQLite + Streamlit)

이 프로젝트는 MySQL 데이터베이스를 SQLite로 변환한 `classicmodels.sqlite`를 기반으로,  
Streamlit을 통해 SQL 쿼리를 직접 실행하고 결과를 시각화할 수 있는 웹 대시보드를 제공합니다.

![preview](https://img.shields.io/badge/Streamlit-Running-brightgreen?logo=streamlit)

### 사용 데이터베이스
[MySQL Sample Database](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/) - **`classicmodels`** 사용

---

## 🧰 주요 기능

- SQLite 데이터베이스 쿼리 조회 (직접 SQL 입력)
- 실행된 쿼리 출력 및 결과 표 형태 표시
- 실행한 DB 경로 및 디버깅 로그 출력
- Streamlit Cloud 배포 가능

---

## 📂 프로젝트 구조
```yaml
MYSQL_CRUD_TEST/ 
├── classicmodels.sqlite    # SQLite DB 파일 (MySQL → SQLite 변환 결과) 
├── streamlit_sqlite_app.py # Streamlit 앱 메인 파일 
├── requirements.txt        # Streamlit 실행에 필요한 의존성 
└── README.md
```

---

## 🚀 실행 방법

### 🔹 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 🔹 2. Streamlit 실행
```bash
streamlit run streamlit_sqlit_app.py
```

### 🌐 Streamlit Cloud 배포 방법
1. GitHub에 이 저장소 업로드

2. https://streamlit.io/cloud 접속

3. New App → 저장소 선택 → app.py 지정

4. 파일명에 classicmodels.sqlite 포함해서 업로드

5. requirements.txt는 아래처럼 구성:
```python
streamlit
pandas
```

---
## Streamlit 배포 
![alt text](스크린샷(82)-1.png)

---

## 💡 예시 쿼리
```sql
SELECT * FROM customers LIMIT 10;
SELECT country, COUNT(*) FROM customers GROUP BY country;
```


## 📌 참고
- classicmodels.sqlite는 MySQL classicmodels DB를 변환한 SQLite 파일입니다.
- 변환 도구 예시: mysql-to-sqlite3

---

## 🧑‍💻 개발자용 참고
```python
DB_PATH = os.path.join(os.path.dirname(__file__), "classicmodels.sqlite")
conn = sqlite3.connect(DB_PATH)
```

---

> # MySQL DB를 SQLite3 DB로 변환하는 방법

1. `mysql-to-sqlite3` 파이썬 라이브러리 설치
```bash
$ pip install mysql-to-sqlite3
```
![alt text](스크린샷(65).png)

2. mysql을 sqlite로 변환
```bash
$ mysql2sqlite -f classicmodels.sqlite -d classicmodels -u root -p
```
![alt text](스크린샷(66).png)

3. Explorer 창에 `classicmodels.sqlite` 파일 생성 확인
![alt text](스크린샷(67).png)

4. `classicmodels.sqlite` 경로 복사
![alt text](스크린샷(68).png)

5. VSCode 좌측 패널 Extensions에서 **MySQL** 검색 후 **MySQL Database Client** 설치
![alt text](스크린샷(62)-1.png)

6. 좌측 패널에 Database, Service 아이콘 생성 확인, Database 아이콘 클릭 후, [+] 버튼 클릭
![alt text](스크린샷(63).png)
![alt text](스크린샷(63)-1.png)

7. connect to server 창에 `SQLite` 선택, Database Path 칸에 4번에서 복사한 경로 붙여넣기 후, [Connect] 버튼 클릭
![alt text](스크린샷(69).png)

8. 좌측 패널 Database에 `classicmodels.sqlite DB` 생성 확인
![alt text](스크린샷(71).png)

9. 쿼리 생성
![alt text](스크린샷(72).png)

10. 쿼리 실행
![alt text](스크린샷(73).png)

---