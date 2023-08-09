import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_KEY")

@st.cache_data(show_spinner=False)
def unpack_prescriptions(prescription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a screenwriter. You will develop an engaging and creative script for a Web Series that can captivate its viewers. Start with coming up with interesting ideas for the setting of the story. Keep in mind that it will indirectly conveys the efficacy of a medicine. Make sure bring it to life so readers can imagine vivid picture of what's going on in the scene. 실수하지마 and don't add unnecessary comments."},
            {
                "role": "user",
                "content": f"{prescription} 의약품의 효능효과에 대해 설명한 자료야. 일반인도 알아듣기 쉽게 150자 미만으로 비유를 들어 설명해. 창의적이면서 정확한 표현을 사용하고 반드시 한국어로 작성."
            }
        ],
        temperature=0.9,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

def unpack_prescriptions_2(prescription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a screenwriter. You will develop an engaging and creative script for a Web Series that can captivate its viewers. Start with coming up with interesting ideas for the setting of the story. Keep in mind that it will indirectly conveys the efficacy of a medicine. Make sure bring it to life so readers can imagine vivid picture of what's going on in the scene. 실수하지마 and don't add unnecessary comments."},
            {
                "role": "user",
                "content": f"{prescription} 의약품의 효능효과에 대해 설명한 자료야. 일반인도 알아듣기 쉽게 150자 미만으로 요약해. 반드시 한국어로 작성."
            }
        ],
        temperature=0.8,
        max_tokens=220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

def unpack_prescriptions_3(prescription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a screenwriter. You will develop an engaging and creative script for a Web Series that can captivate its viewers. Start with coming up with interesting ideas for the setting of the story. Keep in mind that it will indirectly conveys the efficacy of a medicine. Make sure bring it to life so readers can imagine vivid picture of what's going on in the scene. 실수하지마 and don't add unnecessary comments."},
            {
                "role": "user",
                "content": f"{prescription} 의약품의 처방명분에 대해 설명한 자료야. 네가 이해한 것을 알아듣기 쉽게 150자 내로 요약해. 반드시 한국어로 작성."
            }
        ],
        temperature=0.9,
        max_tokens=220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

def write_ideas(topic, input_story, input_characters):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a screenwriter. You will develop an engaging and creative script for either a feature length film, or a Web Series that can captivate its viewers. Start with coming up with interesting characters, the setting of the story, dialogues between the characters etc. Once your character development is complete - create an exciting storyline filled with twists and turns that keeps the viewers in suspense until the end. **write in Korean"},
            {
                "role": "user",
                "content": f"write a interesting A parodic drama that Use a famous TVshow {topic} as a reference and subvert it. ``` 1) Here are the story preferences and The character information to be parodied:{input_story} {input_characters}.``` Keep in mind that it will indirectly conveys the efficacy of a medicine. Make sure bring it to life so readers can imagine vivid picture of what's going on in the scene. 실수하지마 and don't add unnecessary comments."
            }
        ],
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

def write_scenario(topic, product, base_prescript, base_story):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I want you to act as a screenwriter. You will develop an engaging and creative script for either a feature length film, or a Web Series that can captivate its viewers. based on scenario written first, develop it decorating with interesting ideas and dialogues between the characters etc. Once your story understanding is complete - revise some lines by strenthening Prescription informations that I give you. try create an exciting storyline filled with twists and turns that keeps the viewers in suspense until the end. **write in Korean"},
            {
                "role": "user",
                "content": f"write a interesting A parodic drama that Use a famous TVshow {topic} as a reference and subvert it. ``` Here is the story preferences and The character information to be expanded:{base_story}``` Keep in mind that it will indirectly conveys the efficacy of a medicine {product}. here are the Prescription information {base_prescript} ```Make sure bring it to life so readers can imagine vivid picture of what's going on in the scene. **Avoid direct statements about the numbers or the drug's effectiveness and make sure to tell the story indirectly. 실수하지마 and don't add unnecessary comments."
            }
        ],
        temperature=0.7,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

st.markdown(
    f"""
        <div style="text-align: center;">
            <h2 style="text-align: center;">콘텐츠 기획봇 for. 닥터빌TOON</h2>
        </div>
        """,
    unsafe_allow_html=True
)
st.write("")

with st.expander("주제와 품목 지정"):
    product = st.text_input("품목명을 입력해주세요(ex. 펙수클루)") #["엔블로", "펙수클루", "스타틴", "리토바젯", "크레젯"]
    selected_topic = st.text_input("주제를 입력해주세요")
    if st.button('추천보기'):
        st.write(
            f'<iframe src="https://m.kinolights.com/ranking/kino" width="700" height="600"></iframe>',
            unsafe_allow_html=True,
        )

st.text(f"✔︎ 선택된 품목: {product}")
st.text(f"✔︎ 선택된 주제: {selected_topic}")

# Steps as tabs
steps = ["Step 1: 브레인스토밍-스토리 설정하기", "Step 2: 성공모델-처방명분 이해시키기", "Step 3: 시나리오-장면만들기"]
tabs = st.tabs(steps)

with tabs[0]:
    st.write("**레퍼런스 대상 주제(ex.인기 드라마 패러디)로 전개할 스토리의 전반적인 설정을 만들게 됩니다.**")
    input_story = st.text_input("선택하신 주제와 관련된 최소 정보(ex.위키백과 작품 줄거리)를 AI가 참고할 수 있도록 넣어주세요.")
    input_characters = st.text_input("등장인물 정보를 넣어주세요.")

    if st.button('아이디어 구상하기'):
        if input_story and input_characters:
            with st.spinner('생각중...'):
                ideas = write_ideas(selected_topic, input_story, input_characters)
            st.session_state['ideas'] = ideas
            st.write(ideas)
        else:
            st.error('Please enter both story and character information')

    if 'ideas' in st.session_state and st.button('보내기'):
        st.session_state['sent_ideas'] = st.session_state['ideas']
        st.success('보냈습니다! 다음 단계에서 계속 진행해주세요')

with tabs[1]:
    st.write(f"**이 단계에서는 선택하신 품목의 처방명분을 AI에게 이해시킵니다.**")
    prescription = st.text_input(f"{product} 처방명분 한 항목을 입력해주세요", key='prescription_input')

    if st.button('이해해라', key='send_button'):
        with st.spinner('생성중...'):
            st.session_state['unpacked_prescription_2'] = unpack_prescriptions(prescription)
            st.session_state['unpacked_prescription_3'] = unpack_prescriptions_3(prescription)
            st.session_state['unpacked_prescription'] = unpack_prescriptions_2(prescription)

    options = [
        st.session_state.get('unpacked_prescription_2', 'Option 1'),
        st.session_state.get('unpacked_prescription_3', 'Option 2'),
        st.session_state.get('unpacked_prescription', 'Option 3'),
    ]
    selected_option = st.radio("처방명분 설명으로 적합한 것을 선택해주세요. AI가 이를 기반으로 시나리오를 작성하게 됩니다.", options)
    st.session_state['selected_option'] = selected_option

    edited_prescript = st.text_area('여기에서 잘못된 부분을 수정해주세요', st.session_state['selected_option'], height=80)
    st.session_state['edited_prescript'] = edited_prescript
    st.session_state['sent_prescript'] = st.session_state['edited_prescript']
    if st.button('완료'):
        st.success('반영 되었습니다! 다음 단계에서 계속 진행해주세요')

with tabs[2]:
    st.write("**앞에서 정한 재료들을 바탕으로 AI가 1차 생성하고, 편집을 통해 최종 시나리오를 만들게 됩니다.**")
    if 'sent_prescript' in st.session_state:
        st.write(f"**[{product}처방명분]** {st.session_state['sent_prescript']}")
    else:
        st.session_state['sent_prescript'] = ' '
    if 'sent_ideas' not in st.session_state:
        st.session_state['sent_ideas'] = ' '
    st.markdown(
        f"""
                <div>
                    <h8><b>[시나리오]</b>👇여기에서 1편의 시나리오로 생성할 스토리 분량만을 남겨 편집해주세요.</h8>
                </div>
                """,
        unsafe_allow_html=True
    )
    edited_ideas = st.text_area('(의도와 다른 맥락은 오류를 발생시키므로 잘못된 부분은 수정해주세요.)', st.session_state['sent_ideas'], height=600)
    st.session_state['base_story'] = edited_ideas
    st.session_state['final_output'] = ' '
    if st.button("run"):
        st.session_state['final_output']  = write_scenario(selected_topic, product, st.session_state['sent_prescript'], st.session_state['base_story'])
    st.text(st.session_state['final_output'])