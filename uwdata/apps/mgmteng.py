import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app ():
    #HEADER ------------------------------------------------------------------>
    st.write("""

    ----

    """)

    st.subheader('Waterloo MGTE Class of 27 Admission Averages')

    st.write("**Data scraped** from [this spreadsheet](https://docs.google.com/spreadsheets/d/19oz1SRmYCxZoTpypkgZwuFb-xzKVibhm03Zv0s3q6bk/edit#gid=989067333) and [excel sheet #2](https://docs.google.com/spreadsheets/d/1E_gAVTyeNHIYRgnzR_D7gPsbLoZDTXk59saUYPcLV3Q/edit#gid=953122208)" )
    st.write("Languages/libraries used: *Python*, *Streamlit*, *Pandas*, *Plotly*   ")
    st.markdown("  ")
    st.markdown("**Disclaimer:** these averages are ovnly the ones that are *voluntarily submitted* by applicants and may not be representative of the actual admission pool.")




    # BODY -------------------------------------------------------------------> 

    #ontario admissions df

    st.write("""

    ----

    """)
    @st.cache
    def getDataFrame():
        df1 = pd.read_csv('https://docs.google.com/spreadsheets/d/1ZafspjnRJuDjLRKotQ8awLTGcf3RLxrBEh2JtqRGh0Y/export?format=csv', index_col=0)
        df2 =  pd.read_csv('https://docs.google.com/spreadsheets/d/1A-6z5Fe30C266rK-6TnQm6CNOGCOnjK6s4hwfRIDMhQ/export?format=csv', index_col=0)
        df3 = pd.concat([df1, df2])
        #drop unneeded columns
        df = df3.drop(columns=['Discord', 'Other', 'Date Accepted']).reset_index(drop=True)


        #make sure avgs are all in pure decimal format
        df['Average'] = df['Average'].str.replace('%', '')
        df['Average'] = df['Average'].str.replace('~', '')
        df['Average'] = df['Average'].str.replace(',', '')
        df['Average'] = df['Average'].str.replace('+', '')
        #drop missing values
        df = df.dropna(how = 'any', subset=['Average'])

        #replace error data
        erase = {'99.75 (gr.12 data, adv func, bio, chem)': '99.75',
                            'Top6 98, 5 in AP CS and 7 in both IB Math and Physics': '98',
                            '96ish': '96',
                            '94-95': '94.5',
                            '98.5-99ish': '98.5',
                            'sub 90’s': '97.5',
                            '4.0/4.66': '98',
                            '96.6 g11': '96.3',
                            '94.7 gr12 sem 1 96.6 gr11': '96.3',
                            'probably 97.5': '97.5',
                            '39/42(IB)': '97',
                            '97-98ish': '97.5',
                            '99 (based on g11 final and g12 midterm, not likely to maintain)' : '99',
                            '99.75 (gr.12 data adv func bio chem)': '99.75',
                            'Top6 98 5 in AP CS and 7 in both IB Math and Physics': '98',
                            'sub 90’s or somethin': '97.5',
                            'around 95 idk what they look at': '95',
                            '99 (based on g11 final and g12 midterm not likely to maintain)': '99',
                            'around 95 idk': '95',
                            '94 ish I think': '94',
                            '99 20 adjustment factor': '94',
                            }

        for i in range(15):
            df['Average'] = df['Average'].replace(erase)

    

        return df



    #mgmt eng df
    def mgmt101(df):
        uwMgmt = df.loc[(df.Program.isin(['Management Engineering', 'Management engineering', 'management engineering', 'Mgmt Eng', 'Mgmt eng', 'mgmt eng', 'Mgmt Engineering']))].reset_index(drop=True)
        dfMgmt101 = uwMgmt.loc[uwMgmt['Type (101/105)'] == '101'].reset_index(drop=True)
        dfMgmt101Acc = dfMgmt101.loc[dfMgmt101['Type (101/105)'] == '101'].reset_index(drop=True)
        dfMgmt101Acc['Average'] = dfMgmt101Acc['Average'].astype(float)
        
        return dfMgmt101Acc

    #ece df
    def ece101(df):
        ECE = df.loc[(df.Program.isin(['Computer Engineering', 'Computer engineering', 'computer engineering', 'CE', 'Comp Eng', 'comp eng', 'Comp eng','EE', 'ee', 'Electrical Engineering', 'electrical engineering', 'Electrical Eng', 'Electrical eng', 'electrical eng']))].reset_index(drop=True)
        uwECE = ECE.loc[(ECE.School.isin(['UW', 'Waterloo', 'University of Waterloo', 'waterloo', 'university of waterloo', 'uw', 'University Of Waterloo', 'uWaterloo','UWaterloo']))].reset_index(drop=True)
        dfECE101Acc = uwECE.loc[uwECE['Type (101/105)'] == '101'].reset_index(drop=True)
        dfECE101Acc['Average'] = dfECE101Acc['Average'].astype(float)

        return dfECE101Acc

    #se df
    def se101(df):
        SE = df.loc[(df.Program.isin(['Software Engineering', 'Software engineering', 'software engineering', 'SE', 'Soft Eng', 'soft eng', 'Soft eng','se']))].reset_index(drop=True)
        uwSE = SE.loc[(SE.School.isin(['UW', 'Waterloo', 'University of Waterloo', 'waterloo', 'university of waterloo', 'uw', 'University Of Waterloo', 'uWaterloo','UWaterloo']))].reset_index(drop=True)
        dfSE101 = uwSE.loc[uwSE['Type (101/105)'] == '101'].reset_index(drop=True)
        dfSE101Acc = dfSE101.loc[dfSE101['Type (101/105)'] == '101'].reset_index(drop=True)
        dfSE101Acc['Average'] = dfSE101Acc['Average'].astype(float)
        
        return dfSE101Acc

    def syde101(df):
        SYDE = df.loc[(df.Program.isin(['SYDE', 'Systems Design Engineering', 'Systems Design', 'syde', 'Systems Design Eng', 'systems design eng', 'systems design engineering']))].reset_index(drop=True)
        uwSYDE = SYDE.loc[(SYDE.School.isin(['UW', 'Waterloo', 'University of Waterloo', 'waterloo', 'university of waterloo', 'uw', 'University Of Waterloo', 'uWaterloo','UWaterloo']))].reset_index(drop=True)
        dfSYDE101Acc = uwSYDE.loc[uwSYDE['Type (101/105)'] == '101'].reset_index(drop=True)
        dfSYDE101Acc['Average'] = dfSYDE101Acc['Average'].astype(float)

        return dfSYDE101Acc

    def mecha101(df):
        TRON = df.loc[(df.Program.isin(['Mechatronics Engineering', 'Mechatronic Engineering', 'mechatronics engineering', 'mechatronic engineering','TRON','Tron','tron','Mecha','mecha','Mechatronics','mechatronics']))].reset_index(drop=True)
        uwTRON = TRON.loc[(TRON.School.isin(['UW', 'Waterloo', 'University of Waterloo', 'waterloo', 'university of waterloo', 'uw', 'University Of Waterloo', 'uWaterloo','UWaterloo']))].reset_index(drop=True)
        dfTRON101Acc = uwTRON.loc[uwTRON['Type (101/105)'] == '101'].reset_index(drop=True)
        dfTRON101Acc['Average'] = dfTRON101Acc['Average'].astype(float)

        return dfTRON101Acc



    #number of applicants 95+
    def over95(df):
        over95 = df.loc[df['Average'] > 95.0]
        return len(over95.index)

    #entries of a pgm 
    def pgmEntries(df):
        return len(df.index)

    #percent of entries over 95
    def over95Percent(df, entries):
        return int((over95(df)/entries)*100)

    #average admission %
    def average(df):
        return round((df['Average'].mean()),2)


    #box plot comparsion 
    def plotBoxComparsion (df1,df2,abb):
        fig = go.Figure()
        fig.add_trace(go.Box(y=df1, name='Mgmt', marker_color = 'indianred'))
        fig.add_trace(go.Box(y=df2, name = f'{abb}', marker_color = 'lightseagreen'))
        return fig


    #store mgmt df
    mgmtStats = mgmt101(getDataFrame())

    #over 95 mgmt
    over95MGMT = over95(mgmtStats)

    #misc mgmt stats 
    mgmtAvg = average(mgmtStats)
    mgmtEntries = pgmEntries(mgmtStats)
    over95MGMTPercent = over95Percent(mgmtStats, mgmtEntries)

    #widget showing basic stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Admission Average", f'{mgmtAvg} %')
    col2.metric("Entries", mgmtEntries)
    col3.metric("Percent of entries over 95 %", f'{over95MGMTPercent} %')


    #histogram of mgmt avgs
    mgmtPgmStats = mgmtStats.sort_values(by=['Average'], ascending=False)
    fig = px.histogram(mgmtPgmStats, x="Average")
    fig.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 93,
            dtick = 1,
        )
    )
    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig)


    #mgmt box chart
    fig2 = px.box(mgmtStats, y="Average")
    fig2.update_layout(
        yaxis = dict(
            tickmode = 'linear',
            tick0 = 93,
            dtick = 0.5
        )
    )
    st.plotly_chart(fig2)
    

    #compare vs other eng pgms --------------------->

    st.subheader("MGTE compared to other tech-heavy programs")

    #selector box to pick which program to compare tiwth 
    programs = ('Software', 'Computer & Electrical', 'Systems Design', 'Mechatronics')
    selected_pgm = st.selectbox('Program', programs)

    #SE selected
    if (selected_pgm == 'Software'):
        uwEngSelected = se101(getDataFrame())
        abb = 'SE'
        
    #ECE selected
    elif (selected_pgm == 'Computer & Electrical'):
        uwEngSelected = ece101(getDataFrame())
        abb = 'ECE'
        
    #SYDE selected
    elif (selected_pgm == 'Systems Design'):
        uwEngSelected = syde101(getDataFrame())
        abb = 'SYDE'
    
    #Mecha selected
    elif (selected_pgm == 'Mechatronics'):
        uwEngSelected = mecha101(getDataFrame())
        abb = 'TRON'
    
    #misc stats of selected pgm
    selectedAvg = average(uwEngSelected)
    over95Selected = over95(uwEngSelected)
    selectedEntries = pgmEntries(uwEngSelected)
    selectedOver95Percent = over95Percent(uwEngSelected, selectedEntries)

    #calculate differences between chosen pgm and mgmt
    avgDifference = selectedAvg - mgmtAvg
    entriesDifference = selectedEntries - mgmtEntries
    over95PercentDifference = selectedOver95Percent - over95MGMTPercent


    #misc stats comparing the two (+- avg,entries,% over 95)
    col4, col5, col6 = st.columns(3)
    col4.metric("Admission Average", f'{selectedAvg} %', f'{round(avgDifference,2)} %' )
    col5.metric("Entries", selectedEntries, entriesDifference)
    col6.metric("Percent of entries over 95", selectedOver95Percent, over95PercentDifference)

    #plot the side by side box plots
    compare = plotBoxComparsion(mgmtStats['Average'],uwEngSelected['Average'],abb)
    st.plotly_chart(compare)



        

