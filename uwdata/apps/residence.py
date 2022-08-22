import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import requests

def app():

    st.write("""

    ----

    """)

    st.write("""

    **Data scraped** from [this spreadsheet](https://docs.google.com/spreadsheets/d/1wgj2UV1zP8XUg-tbZvh687CwJ-VdbKZkpX-te0UbwUg/edit#gid=787354345) 


    """)
    st.markdown("  ")


    st.write("""
    **CMH**: Claudette Millar Hall, 
    **UWP**: Waterloo Place, 
    **MKV**: Mackenzie King Village, 
    """)
    st.write("""
    **V1**: Village 1, 
    **REV**: Ron Eydt Village""")



    st.write("""

    ----

    """)


    @st.cache
    def getDf(): 
        df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRkuYzuDey1DNlKuWYGwwunUN7kuU5qEqbLmSncPRXqRxP-VHqJOF5l2B_9j9rJ85oYtxpr8n3oUkRK/pub?gid=787354345&single=true&output=csv')
        df = df[['What residence did you live in?', 'What faculty are/were you in?', 'How would you rate your residence\'s social life/community?', 'How would you rate your residence\'s room situation?', 'How would you rate the facilities?', 'How would you rate your residence\'s meal plan/food situation?']]
        engineeringStays = df.loc[df['What faculty are/were you in?'].isin(['Engineering'])] 

        return engineeringStays


    engineeringStays = getDf()
    engineeringStays = engineeringStays.dropna(subset=['How would you rate your residence\'s room situation?', 'How would you rate your residence\'s social life/community?', 'How would you rate your residence\'s meal plan/food situation?'])
    engineeringStays['How would you rate your residence\'s room situation?'] = engineeringStays['How would you rate your residence\'s room situation?'].astype(int)
    engineeringStays['How would you rate your residence\'s social life/community?'] = engineeringStays['How would you rate your residence\'s social life/community?'].astype(int)
    engineeringStays['How would you rate your residence\'s meal plan/food situation?'] = engineeringStays['How would you rate your residence\'s meal plan/food situation?'].astype(int)

    #cmh 
    cmh = engineeringStays.loc[(engineeringStays['What residence did you live in?'] == 'Claudette Millar Hall (CMH)')]
    cmhRoomMEAN = cmh['How would you rate your residence\'s room situation?'].mean()
    cmhSocialMEAN = cmh['How would you rate your residence\'s social life/community?'].mean()
    cmhFacilityMEAN = cmh['How would you rate the facilities?'].mean()
    cmhFoodMEAN = cmh['How would you rate your residence\'s meal plan/food situation?'].mean()
    cmhValues = [cmhRoomMEAN, cmhSocialMEAN, cmhFacilityMEAN, cmhFoodMEAN]
    cmhMEAN = np.mean(cmhValues)

    #uwp
    uwp = engineeringStays.loc[(engineeringStays['What residence did you live in?'] == 'UW Place (UWP)')]
    uwpRoomMEAN = uwp['How would you rate your residence\'s room situation?'].mean()
    uwpSocialMEAN = uwp['How would you rate your residence\'s social life/community?'].mean()
    uwpFacilityMEAN = uwp['How would you rate the facilities?'].mean()
    uwpFoodMEAN = uwp['How would you rate your residence\'s meal plan/food situation?'].mean()
    uwpValues = [uwpRoomMEAN, uwpSocialMEAN, uwpFacilityMEAN, uwpFoodMEAN]
    uwpMEAN = np.mean(uwpValues)


    #mkv 
    mkv = engineeringStays.loc[(engineeringStays['What residence did you live in?'] == 'Mackenzie King Village (MKV)')]
    mkvRoomMEAN = mkv['How would you rate your residence\'s room situation?'].mean()
    mkvSocialMEAN = mkv['How would you rate your residence\'s social life/community?'].mean()
    mkvFacilityMEAN = mkv['How would you rate the facilities?'].mean()
    mkvFoodMEAN = mkv['How would you rate your residence\'s meal plan/food situation?'].mean()
    mkvValues = [mkvRoomMEAN, mkvSocialMEAN, mkvFacilityMEAN, mkvFoodMEAN]
    mkvMEAN = np.mean(mkvValues)

    #v1
    v1 = engineeringStays.loc[(engineeringStays['What residence did you live in?'] == 'Village 1 (V1)')]
    v1RoomMEAN = v1['How would you rate your residence\'s room situation?'].mean()
    v1SocialMEAN = v1['How would you rate your residence\'s social life/community?'].mean()
    v1FacilityMEAN = v1['How would you rate the facilities?'].mean()
    v1FoodMEAN = v1['How would you rate your residence\'s meal plan/food situation?'].mean()
    v1Values = [v1RoomMEAN, v1SocialMEAN, v1FacilityMEAN, v1FoodMEAN]
    v1MEAN = np.mean(v1Values)


    #REV
    rev = engineeringStays.loc[(engineeringStays['What residence did you live in?'] == 'Ron Eydt Village (REV)')]
    revRoomMEAN = rev['How would you rate your residence\'s room situation?'].mean()
    revSocialMEAN = rev['How would you rate your residence\'s social life/community?'].mean()
    revFacilityMEAN = rev['How would you rate the facilities?'].mean()
    revFoodMEAN = rev['How would you rate your residence\'s meal plan/food situation?'].mean()
    revValues = [revRoomMEAN, revSocialMEAN, revFacilityMEAN, revFoodMEAN]
    revMEAN = np.mean(revValues)


    residences = ['CMH', 'UWP', 'MKV', 'V1', 'REV']

    allMEAN = [cmhMEAN,uwpMEAN,mkvMEAN,v1MEAN,revMEAN]

   #todo -> show raw data

    #room ratings
    st.subheader('How would you rate your residence\'s room situation?')
    fig = px.bar(x=residences, y=[cmhRoomMEAN, uwpRoomMEAN, mkvRoomMEAN, v1RoomMEAN,revRoomMEAN], labels=dict(x="Residence", y="Mean rating"))
    st.plotly_chart(fig)

    #social/community ratings
    st.subheader('How would you rate your residence\'s social life/community?')
    fig = px.bar(x=residences, y=[cmhSocialMEAN, uwpSocialMEAN, mkvSocialMEAN, v1SocialMEAN, revSocialMEAN],  labels=dict(x="Residence", y="Mean rating"))
    st.plotly_chart(fig)

    #facilities rating
    st.subheader('How would you rate the facilities?')
    fig = px.bar(x=residences, y=[cmhFacilityMEAN, uwpFacilityMEAN, mkvFacilityMEAN, v1FacilityMEAN, revFacilityMEAN],  labels=dict(x="Residence", y="Mean rating"))
    st.plotly_chart(fig)

    #food ratings
    st.subheader('How would you rate your residence\'s meal plan/food situation?')
    fig = px.bar(x=residences, y=[cmhFoodMEAN, uwpFoodMEAN, mkvFoodMEAN, v1FoodMEAN, revFoodMEAN],  labels=dict(x="Residence", y="Mean rating"))
    st.plotly_chart(fig)

    #average
    st.subheader('Overall average (above combined)')
    fig = px.bar(x=residences, y=allMEAN,  labels=dict(x="Residence", y="Mean rating"))
    st.plotly_chart(fig)

    #raw data
    st.subheader("Raw Data")
    selected_res = st.selectbox('Residence', residences)


    if selected_res == "CMH":
        st.write(cmh)
    elif selected_res == "UWP":
        st.write(uwp)
    elif selected_res == "MKV":
        st.write(mkv)
    elif selected_res == "V1":
        st.write(v1)
    elif selected_res =="REV":
        st.write(rev)
