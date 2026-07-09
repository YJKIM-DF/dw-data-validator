# DW Data Validator

Python 기반 데이터 검증 프레임워크

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

현재 대부분의 프로젝트에서는 SQL 직접 작성, Excel 복사, VLOOKUP, 수동 비교 등의 방식으로 검증을 수행하고 있어 많은 시간이 소요됩니다.

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

|라이브러리|용도|
|---|---|
|pandas|Excel 읽기 및 데이터 처리|
|openpyxl|Excel 파일 처리|
|psycopg[binary]|PostgreSQL 연결|
|python-dotenv|환경변수(.env) 관리|

---

## 프로젝트 구조

```text
dw-data-validator
│
├── config
│   └── validation_config.xlsx
│
├── sql
│   ├── 01_create_schema.sql
│   ├── 02_create_tables.sql
│   ├── 03_insert_sample_data.sql
│   ├── 04_drop_objects.sql
│   └── README.md
│
├── src
│   ├── db
│   │   ├── connection.py
│   │   └── query_executor.py
│   │
│   ├── utils
│   │   └── config_reader.py
│   │
│   ├── validator
│   │   ├── __init__.py
│   │   ├── base_validator.py
│   │   └── count_validator.py
│   │   └── sum_validator.py
│   │   └── groupby_validator.py
│   │
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```


---

## 주요 기능

- PostgreSQL 데이터베이스 연결
- Excel 설정파일(Config) 읽기
- 설정파일 기반 Source / Target 테이블 조회
- 조회 결과를 Pandas DataFrame으로 변환
- Count Validation
- Sum Validation
- Group By Validation
- SQL Script 버전 관리


### DB 연결

- `.env` 파일 기반 PostgreSQL 연결 지원
- DB 접속 정보를 코드와 분리하여 관리

---

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

## 검증 대상

현재 테스트 데이터는 다음과 같은 검증 시나리오를 포함합니다.

|검증 항목|예상 결과|설명|
|---|---|---|
|Count Validation|PASS|ODS와 FACT의 Row 수가 동일|
|Sum Validation (qty)|FAIL|합계 수량 불일치|
|Sum Validation (sale_amt)|FAIL|합계 금액 불일치|
|Row Compare Validation|FAIL|sale_id=3의 sale_amt 변경|
|PK Compare Validation|FAIL|sale_id=4 누락, sale_id=6 추가|

---


## 향후 개선 사항

- Validation 결과 Excel 자동 생성
- AI 기반 검증 결과 분석 기능 검토
- 다양한 검증 Rule 추가


---


## 개발 진행 현황

- [x] 프로젝트 환경 구축
- [x] GitHub Repository 구성
- [x] PostgreSQL 데이터베이스 연결
- [x] SQL Script 관리
- [x] 테스트 테이블 생성
- [x] 샘플 데이터 생성
- [x] Excel 설정파일(Config) 생성
- [x] Config Reader 구현
- [x] Query Executor 구현
- [x] Count Validation
- [x] Sum Validation
- [x] Group By Validation
- [ ] Row Compare Validation
- [ ] Validation History 저장
- [ ] Excel Report 생성


---


## 개발자

DFOCUS R&D Project

DW Data Validation Framework

Data Biz.본부 BDP팀 김예지 선임

2026