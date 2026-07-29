# Product Requirement Document

### 1. 프로젝트 개요

**프로젝트명 : DW Data Validator**

**목적 :** DW(Data Warehouse) 환경에서 Source와 Target 데이터의 정합성을 자동으로 검증하여 데이터 품질을 향상시키고, 반복적인 검증 작업을 효율화하는 Validation Tool을 개발한다.

**개발 환경**

| 구분 | 내용 |
| --- | --- |
| Language | Python 3.11+ |
| Database | PostgreSQL |
| Library | pandas, psycopg[binary], openpyxl |
| IDE | Visual Studio Code |

### 2. 프로젝트 배경

DW(Data Warehouse) 구축 및 운영 과정에서는 Source 데이터와 Target 데이터의 정합성을 확인하기 위해 다양한 검증 작업이 수행된다.

기존에는 SQL을 직접 작성하여 Count, Sum, Group By, Row Compare 등을 수행하였으며, 반복 작업으로 인해 검증 시간이 증가하고 휴먼 에러가 발생할 가능성이 있었다.

이를 개선하기 위해 **Excel 기반 설정파일을 이용하여 데이터 검증을 자동화하고, 검증 결과를 Report 및 History 형태로 관리할 수 있는 프로그램을 개발**한다.

### 3. 문제 정의

| As-Is | To-Be |
| --- | --- |
| 검증 SQL 직접 작성 | Excel 설정파일 기반 자동 Validation |
| 반복적인 수작업 수행 | Validation 자동 실행 |
| 검증 결과 관리 어려움 | Excel Report 자동 생성 |
| Validation 이력 없음 | DB History 자동 저장 |
| 프로젝트별 SQL 재작성 | Config 변경만으로 재사용 |

### 4. 개발 목표

- Excel 설정파일 기반 Validation 수행
- Source와 Target 데이터 자동 비교
- 데이터 정합성 검증 자동화
- 검증 결과 Report 생성
- Validation 수행 이력 관리
- 다양한 DW 프로젝트에서 재사용 가능한 Validation Framework 제공

### 5. 서비스 흐름

```
┌──────────────────────────────┐
│  Validation Config (Excel)   │
└──────────────┬───────────────┘
               │
               ▼
      Config 정보 읽기
 (Validation Name, Table 정보,
  Compare Column, PK 등)
               │
               ▼
      Source / Target 조회
        (PostgreSQL)
               │
               ▼
     Validation 수행
 ┌────────────────────────────┐
 │ • Count Validation         │
 │ • Sum Validation           │
 │ • Group By Validation      │
 │ • Row Compare Validation   │
 └─────────────┬──────────────┘
               │
               ▼
      Validation 결과 생성
               │
      ┌────────┴────────┐
      ▼                 ▼
 Excel Report      Validation History
   생성                 저장
      │                 │
      └────────┬────────┘
               ▼
          Validation 완료
```

### 6. 기대 효과

**업무 효율성 향상**

- 반복적인 SQL 작성 최소화
- Validation 수행 시간 단축

**데이터 품질 향상**

- Source와 Target 데이터 정합성 검증 표준화
- 휴먼 에러 감소

**운영 편의성 향상**

- Validation 결과 Report 자동 생성
- Validation History 기반 이력 관리

**재사용성 확보**

- Config 변경만으로 다양한 테이블에 적용 가능
- 프로젝트별 Validation Tool로 활용 가능