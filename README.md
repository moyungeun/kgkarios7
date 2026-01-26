# Escape from Tarkov 아이템 데이터베이스 웹

Streamlit과 CSV 기반으로 제작한 **Escape from Tarkov 아이템 검색 및 상세 정보 웹 애플리케이션**입니다.
과제 제출용으로 시작했지만, 아이템을 계속 추가·확장할 수 있는 구조를 목표로 설계되었습니다.

---

## 📌 주요 기능

* 🔍 **아이템 이름 검색**
* 🧱 **아이템 상세 정보 표시**

  * 이름
  * 무게 (weight)
  * 크기 (size)
  * 플리마켓 판매 가능 여부
* 📦 **획득처 정보**

  * 루팅 가능한 컨테이너 / 장소
  * 희귀도(rarity) 표시
* 🔄 **사용처(교환)**

  * 해당 아이템이 사용되는 교환(barter) 목록
  * 필요한 아이템 조합 및 결과 아이템
  * 상인(trader) 정보 및 해금 조건
* 🗂️ **CSV 기반 데이터 관리**

  * 코드 수정 없이 CSV 추가/수정만으로 데이터 확장 가능

---

## 🛠️ 사용 기술

* **Python 3.12**
* **Streamlit** – 웹 UI 구성
* **Pandas** – CSV 데이터 처리

---

## 📁 프로젝트 구조

```
project/
│
├─ app.py                 # Streamlit 메인 앱
├─ items.csv              # 아이템 기본 정보
├─ looting.csv            # 아이템 획득처 정보
├─ barters.csv            # 교환 결과 정보
├─ barters_items.csv      # 교환에 필요한 재료 아이템
└─ README.md
```

---

## 📄 CSV 파일 설명

### 1️⃣ items.csv (아이템 기본 정보)

| 컬럼명                  | 설명                         |
| -------------------- | -------------------------- |
| item_id              | 아이템 고유 ID                  |
| name                 | 아이템 이름                     |
| weight               | 무게 (kg)                    |
| size                 | 인벤토리 크기                    |
| flea_market_sellable | 플리마켓 판매 가능 여부 (TRUE/FALSE) |

---

### 2️⃣ looting.csv (획득처)

| 컬럼명         | 설명                    |
| ----------- | --------------------- |
| item_id     | 아이템 ID                |
| source_id   | 획득처 ID                |
| source_name | 획득처 이름 (예: Sport bag) |
| rarity      | 희귀도                   |

---

### 3️⃣ barters.csv (교환 결과)

| 컬럼명             | 설명           |
| --------------- | ------------ |
| barter_id       | 교환 ID        |
| trader_name     | 상인 이름        |
| result_item_id  | 교환 결과 아이템 ID |
| result_quantity | 결과 아이템 수량    |
| unlock_11       | 해금 조건        |

---

### 4️⃣ barters_items.csv (교환 재료)

| 컬럼명       | 설명        |
| --------- | --------- |
| barter_id | 교환 ID     |
| item_id   | 재료 아이템 ID |
| item_name | 재료 아이템 이름 |
| quantity  | 필요 수량     |

---

## ▶ 실행 방법

```bash
pip install streamlit pandas
streamlit run app.py
```

브라우저에서 자동으로 웹 페이지가 열립니다.

---

## 🎯 프로젝트 목표

* Escape from Tarkov 아이템 정보를 **한 화면에서 직관적으로 확인**
* 아이템 추가 시 **코드 수정 없이 CSV만으로 확장 가능**한 구조
* 향후 제작(Craft), 하이드아웃, 퀘스트 연계 정보까지 확장 예정

---

## 🚧 현재 한계 및 개선 예정

* 아이템 이미지 미연동 (추후 URL 기반 추가 예정)
* 상점 판매 정보 미구현
* 획득처 클릭 시 상세 페이지 전환 기능 준비 중

---

## 📎 참고

본 프로젝트는 비공식 팬 프로젝트이며,
Escape from Tarkov 및 Battlestate Games와 직접적인 관련은 없습니다.
