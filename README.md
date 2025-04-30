# mysql_crud_test

### [MySQL Sample Database](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/) - **`classicmodels`** 사용


>## 1. MySQL DB를 SQLite3 DB로 변환
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

5. `VSCode` 좌측 패널 `Extensions`에서 **MySQL** 검색 후 **MySQL Database Client** 설치
![alt text](스크린샷(62)-1.png)

6. 좌측 패널에 Database, Service 아이콘 생성 확인, Database 아이콘 클릭 후, `+` 버튼 클릭
![alt text](스크린샷(63).png)
![alt text](스크린샷(63)-1.png)

8. connect to server 창에 `SQLite` 선택, Database Path 칸에 4번에서 복사한 경로 붙여넣기 후, [Connect] 버튼 클릭
![alt text](스크린샷(69).png)

9. 좌측 패널 Database에 `classicmodels.sqlite DB` 생성 확인
![alt text](스크린샷(71).png)

10. `Query`를 추가, 실행하여 테이블 생성과 데이터 불러오기 확인
![alt text](스크린샷(72).png)
![alt text](스크린샷(73).png)

---

> ## 2. streamlit 대시보드 개발 및 테스트
1. `streamlit_sqlit_app.py` 파일 생성 후, 실행
```bash 
$ streamlit run streamlit_sqlit_app.py
```
![alt text](스크린샷(80).png)

2. streamlit 확인
![alt text](스크린샷(81).png)

---

> ## 3. GitHub push
```bash
$ ./git-push-all.sh
```

> ## 4. streamlit 웹사이트 배포
![alt text](스크린샷(82).png)

---
