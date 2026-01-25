import streamlit as st
import pandas as pd

st.set_page_config(page_title="Escape from Tarkov 아이템(item)", layout="wide")
st.title("Escape from Tarkov 아이템(item)")

# 페이지 상태 초기화
if "page" not in st.session_state:
    st.session_state["page"] = "item"   # item / source
    st.session_state["source_id"] = None
    st.session_state["source_name"] = None

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv("items.csv")

@st.cache_data
def load_looting():
    return pd.read_csv("looting.csv")

df = load_data()
looting_df = load_looting()

def show_item_page():
    pass

def show_source_page():
    pass

if st.session_state["page"] == "item":
    show_item_page()
elif st.session_state["page"] == "source":
    show_source_page()

# 획득처 초기화
if "selected_source" not in st.session_state:
    st.session_state["selected_source"] = None
    st.session_state["selected_source_name"] = None

# 검색
keyword = st.text_input("아이템 이름 검색")

if keyword:
    view_df = df[df["name"].str.contains(keyword, case=False, na=False)]
else:
    view_df = df

for _, item in view_df.iterrows():
    with st.expander(item["name"]):

        col1, col2 = st.columns([1, 5])

        with col1:
            st.markdown("🖼️")

        with col2:
            st.text(item["name"])

        st.markdown(f"""
**무게** : {item['weight']} kg  
**크기** : {item['size']}
""")

        st.divider()

        st.subheader("획득처")

        item_loot = looting_df[looting_df["item_id"] == item["item_id"]]

        if item_loot.empty:
            st.caption("데이터 없음")
        else:
            for _, loot in item_loot.iterrows():
                label = f"{loot['source_name']} ({loot['rarity']})"

                if st.button(
                    label,
                    key=f"{item['item_id']}_{loot['source_id']}"
                ):
                    st.session_state["selected_source"] = loot["source_id"]
                    st.session_state["selected_source_name"] = loot["source_name"]
           

        st.divider()

        st.subheader("사용처")
        st.caption("데이터 없음")

        st.divider()

        st.subheader("상점")
        st.caption("데이터 없음")
