import streamlit as st
import clipboard

st.markdown(
    f"""
        <div style="text-align: center;">
            <h2 style="text-align: center;">미드저니 프롬프트 생성기</h2>
        </div>
        """,
    unsafe_allow_html=True
)

topics = ['화면비율','화풍','2D그림체','카메라타입','화질','각도','빛','테마색','배경','시대','인물표현','감정','기타디테일']
subtopics = {
    '화면비율': {'4:3':'--ar 4:3', '16:9':'--ar 16:9', '1:1':'--ar 1:1', '9:16':'--ar 9:16', '5:4':'--ar 5:4'},
    '화풍': {'사진':'photography','심플&화려':'art nouveau style','건축적인':'bauhaus art style', '미니멀리스트':'minimalism art style', '초현실아트':'photorealism art style'},
    '2D그림체': {'영화포스터':'movie poster', '3D':'3D rendering', '애니메이션':'anime', '광고판':'billboard', '브로셔':'brochure', '만화책':'comic book', '디지털아트':'digital art', '전단지':'flyer', '설명서':'IKEA guide', '귀여운스티커':'sticker', '일러스트':'illustration', '잡지':'magazine'},
    '카메라타입': {'제품샷':'product photograph', '인물사진':'portrait photograph', '배경속실루엣':'silhouette photograph', '빈티지감성':'35mm film photograph', '다큐멘터리':'kodachrome photograph', '보정이 세게 들어간':'infrared photography', '스튜디오 조명':'glamor photography', '폴라로이드':'instax photograph'},
    '화질': {'TV광고':'backlit', '빛번짐':'bokeh', '쨍하게':'vibrant colors', '대비':'high contrast(대비)', '선이뚜렷':'sharp','별빛':'night photography', '깜깜불빛':'low light', '움직임':'motion blur','부드럽게흐린':'soft focus','배경아웃포커스':'shallow depth of field'},
    '각도': {'1인칭':'first person view', '넓게':'wide angle lens', '더 넓게':'ultra-wide angle lens', '최상화질':'telephoto lens', '파노라마':'panorama', '항공샷':'aerial', '드론샷':'drone view', '우주에서':'satellite imagery'},
    '빛': {'자연스러운': 'realistic lighting',
          '밝은 자연광': 'daylight',
          '실내': 'fluorescent lighting',
          '안개낀': 'hazy lighting',
          '깨끗한': 'high-key lighting',
          '스튜디오 조명': 'studio lighting',
          '따뜻한 전구': 'incandescent lighting',
          '클럽': 'ambient lighting',
          '영화': 'cinematic lighting',
          '역광': 'backlighting',
          '촛불': 'candlelight',
          '대비 심한': 'bright-dark contrast lighting',
          '광선': 'volumetric lighting',
          '노을': 'golden hour sunlight',
          '흑백영화': 'film noir lighting'},
    '테마색': {'어둡게': 'dark',
              '밝게': 'light',
              '그라데이션': 'gradient color',
              '차가운': 'cool color',
              '파스텔': 'pastel color',
                '봄': 'spring colors',
              '여름': 'summer colors',
              '가을': 'autumn colors',
              '겨울': 'winter colors',
              '담백한': 'low contrast',
              '톤온톤': 'monochromatic color',
              '회색빛': 'faded color',
              '또렷': 'pantone color',
              '모든색': 'spectral solar',
              '아이스크림': 'vivid color',
              '사탕': 'vibrant color',
              '네온': 'neon color'},
    '배경': {'하얀 배경': 'white background',
           '검은 배경': 'black background',
           '단색 배경': 'flat background',
           '질감 있는 배경': 'textured background',
           '흐린 배경': 'hazy background'},
    '시대': {
           '앤티크': 'antique',
           '중세': 'medieval',
           '현대': 'modern',
           '레트로': 'retro',
           '빈티지': 'vintage',
            '석기시대': 'Stone Age',
           '철기시대': 'Iron Age',
           '고대 그리스': 'Ancient Greece',
           '유럽 르네상스': 'European Renaissance',
            '산업혁명': 'Industrial Revolution',
           '빅토리아 시대': 'Victorian Era',
            '1930년대 스타일': '1930s style',
            '1950년대 스타일': '1950s style',
            '1960년대 스타일': '1960s style',
            '1970년대 스타일': '1970s style',
            '1980년대 스타일': '1980s style',
            '1990년대 스타일': '1990s style',
            },
    '인물표현': {'매력적인': 'attractive',
                 '아름다운': 'beautiful',
                 '젊은': 'young',
                 '아이': 'child',
                 '귀여운': 'cute',
                 '뚱뚱한': 'fat',
                 '여성': 'female',
                 '남성': 'male',
                 '전신 포즈': 'full body pose',
                 '잘생긴': 'handsome',
                 '어수선한': 'messy',
                 '늙은': 'old',
                 '키 작은': 'short',
                 '날씬한': 'skinny',
                 '키 큰': 'tall',
                 '못생긴': 'ugly'},
    '감정': {'행복한': 'happy',
           '슬픈': 'sad',
           '분노한': 'angry',
           '놀란': 'surprised',
           '무서운': 'scared',
           '지루한': 'bored',
           '흥분한': 'excited',
           '짜증나는': 'annoyed',
           '평온한': 'calm',
           '우울한': 'depressed',
           '불안한': 'anxious',
           '희망찬': 'hopeful',
           '당황한': 'confused',
           '피곤한': 'tired',
           '사랑스러운': 'lovable',
           '질투하는': 'jealous',
           '부끄러운': 'embarrassed',
           '기쁜': 'joyful',
           '화난': 'mad',
           '놀라운': 'astonishing',
           '공포': 'frightening',
           '지루한': 'tedious',
           '흥분한': 'thrilling',
           '졸린': 'sleepy',
           '스트레스 받는': 'stressed',
           '피곤한': 'tired',
            '외로운': 'lonely',
            '고급스러운': 'luxury',
            '미친': 'mad',
            '차분한': 'mellow',
            '기분 변화가 심한': 'moody',
            '신경 쓰이는': 'nervous',
            '기발한': 'whimsical',
            '걱정되는': 'worried'},
    '기타디테일': {'투명한': 'transparent',
              '텍스처': 'textured',
              '거친': 'rough',
              '매트한': 'matte',
              '얼음/유리 반사': 'lumen reflections',
              '그림자': 'screen space reflections'}}

tabs = st.tabs(topics)

if "selected_subtopics" not in st.session_state:
    st.session_state["selected_subtopics"] = {}

for i, topic in enumerate(topics):
    with tabs[i]:
        selected_subtopics = st.multiselect("", options=subtopics[topic].keys(), key=f"tab-{topic}")
        st.session_state["selected_subtopics"][topic] = selected_subtopics

selected = st.session_state['selected_subtopics']
selected = {topic: subtopics for topic, subtopics in selected.items() if subtopics}
selected_subtopics = {subtopic: subtopics[topic][subtopic] for topic, subtopic_list in selected.items() for subtopic in subtopic_list}

selected_str = ' '.join(selected_subtopics.keys())
st.text(selected_str)

def generate_midjourney_prompt(selected_subtopics):
    prompts = []
    for selected_subtopic, selected_subtopic_val in selected_subtopics.items():
        for topic, subtopic_dict in subtopics.items():
            for subtopic_key, subtopic_val in subtopic_dict.items():
                if subtopic_key == selected_subtopic:
                    prompts.append(subtopic_val)
    return prompts

generated_prompts = []

col1, col2 = st.columns(2)
if col1.button('프롬프트 생성하기'):
    generated_prompts.clear()
    generated_prompts.extend(generate_midjourney_prompt(selected_subtopics))
    promptout = ", ".join(generated_prompts)
    st.write(promptout)

if col2.button('복사하기'):
    if generated_prompts:
        clipboard.copy("\n".join(generated_prompts))
        st.success("클립보드에 복사되었습니다.")