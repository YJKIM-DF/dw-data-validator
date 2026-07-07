## 개발 진행 현황

- [x] 개발환경 구축
- [x] GitHub Repository 생성
- [x] PostgreSQL 환경 구성
- [ ] DB 연결
- [ ] Excel 설정파일 읽기
- [ ] Count 검증
- [ ] Sum 검증
- [ ] Row Compare
- [ ] Excel Report 생성
- [ ] 검증 이력 관리
- [ ] 통합 테스트


# DW Data Validator

## 프로젝트 소개

DW(Data Warehouse) 프로젝트에서 Source 데이터와 Target 데이터를 자동으로 검증하기 위한 Python 기반 데이터 검증 프레임워크입니다.

기존에는 SQL을 직접 작성하거나 Excel(VLOOKUP 등)을 이용하여 데이터를 비교하였으나,
본 프로젝트는 Excel 설정파일을 기반으로 데이터 검증을 자동 수행하고 결과를 Excel 형태의 리포트로 생성하는 것을 목표로 합니다.

본 프로젝트는 PostgreSQL 환경을 대상으로 개발하며, 향후 Oracle 등 다른 DBMS로도 확장 가능하도록 설계합니다.

---

## 개발 목적

DW/ETL 프로젝트에서는 데이터 적재 이후 다음과 같은 검증 작업을 반복적으로 수행합니다.

- Source / Target 건수 비교
- 집계(SUM) 데이터 비교
- PK 기준 Row 데이터 비교
- 누락 데이터 확인
- 검증 결과 정리 및 보고

현재 대부분의 프로젝트에서는

- SQL 직접 작성
- Excel 복사
- VLOOKUP
- 수동 비교

등의 방식으로 검증을 수행하고 있어 많은 시간이 소요됩니다.

본 프로젝트에서는 이러한 반복 작업을 자동화하여
검증 시간을 단축하고 정확성을 향상시키는 것을 목표로 합니다.

---

## 개발 환경

| 구분 | 내용 |
|------|------|
| Language | Python 3.x |
| DBMS | PostgreSQL |
| IDE | Visual Studio Code |
| Version Control | Git / GitHub |
| OS | Windows 11 |

---

## 사용 라이브러리

- pandas
- openpyxl
- psycopg
- python-dotenv

---

## 프로젝트 구조

```
dw-data-validator
│
├── config                 # 설정파일(Excel)
├── docs                   # 프로젝트 문서(PRD, 기능명세서)
├── sample                 # 샘플 파일
├── sql                    # DB 생성 SQL
│
├── src
│   ├── db                 # DB Connection
│   ├── validators         # 검증 로직
│   ├── reports            # Excel Report 생성
│   ├── history            # 검증 이력 관리
│   ├── utils              # 공통 함수
│   └── main.py
│
├── tests                  # 테스트 코드
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 주요 기능

### 1. Excel 설정파일 기반 검증

설정파일만 변경하면 별도의 프로그램 수정 없이 다양한 테이블을 검증할 수 있습니다.

예시

|SOURCE_TABLE|TARGET_TABLE|PK|GROUP_BY|SUM_COLUMN|
|------------|------------|--|--------|----------|
|valid.ods_sales|valid.fact_sales|sale_id|sale_dt|sale_amt|

---

### 2. 데이터 검증

지원 예정 기능

- Row Count 비교
- SUM 비교
- GROUP BY SUM 비교
- PK 기준 Row Compare
- Difference Data 추출

---

### 3. Excel 결과 리포트 생성

검증 결과를 Excel 파일로 자동 생성합니다.

예정 Sheet

- Summary
- Count Result
- Sum Result
- Row Compare
- Difference

---

### 4. 검증 이력 관리

검증 수행 이력을 저장하여
실행일, 결과, 실패 건수 등을 관리합니다.

---

## 개발 진행 일정

|일정|내용|
|------|------|
|7/7|개발환경 구축 및 프로젝트 생성|
|7/8|DB 연결 및 Excel 설정파일 구현|
|7/9|Count / Sum 검증 구현|
|7/10|Row Compare 구현|
|7/13|Excel Report 생성|
|7/14|검증 이력 관리|
|7/15|리팩토링 및 예외처리|
|7/16|통합 테스트 및 버그 수정|
|7/17|개발 완료|

---

## 향후 개선 사항

- Oracle DB 지원
- AI 기반 검증 결과 분석
- 검증 대상 자동 추천
- CLI(Command Line Interface) 지원

---

## Git Commit Rule

```
feat    : 기능 추가
fix     : 버그 수정
refactor: 코드 개선
docs    : 문서 수정
style   : 코드 스타일 수정
chore   : 환경 설정 및 기타 작업
```

예시

```
feat: add PostgreSQL connection
feat: implement count validator
feat: implement Excel report generator
fix: correct row comparison logic
docs: update README
```

---

## 개발자

R&D Project

DW Data Validation Framework

2026