import pandas as pd
import streamlit as st
st.header("Youtube Interface WIT Solapur College")
pages=["Video Playlist Search",'Video Search By Professor Details','Video Search By Title',]
st.sidebar.title('Menu')
out=st.sidebar.radio("",pages)
#====================================================================================================
def get_url_playloist(vname):
    ptid=pdf.groupby('vtitle').get_group(str(vname))['vid']
    return list("https://www.youtube.com/watch?v="+ptid)
#====================================================================================================
pdf=pd.read_csv("YChannelData.csv",index_col=False)
def search_by_playlist(title):
    try:    
        ptid=pdf.groupby('ptitle').get_group(title)['pid'].unique()[0]
        return ("https://www.youtube.com/playlist?list="+ptid)
    except:
        return ("URL Not Found")
#====================================================================================================
alldata=pd.read_csv("AllVideo.csv",index_col=False)
def search_by_Professor_name(name):
    ptid=alldata.groupby('video_description').get_group(name)['videoIDS']
    url="https://www.youtube.com/watch?v="+ptid
    title=alldata.groupby('video_description').get_group(name)['title']
    return list(title)

def get_urls(vname):
    ptid=alldata.groupby('title').get_group(str(vname))['videoIDS']
    return list("https://www.youtube.com/watch?v="+ptid)

def teacher_name(pdf,):
    for i in range(len(pdf['video_description'])):
        try:
            pdf['video_description'][i]=pdf['video_description'][i].split('\n')[0]
        except:
            pass
    ls=pdf['video_description'].unique()
    return ls
#==========================================================================================================
if out=='Video Playlist Search':
    #plist=st.selectbox('Select Name of Playlist in Drop Down Menu', pdf['ptitle'].unique())
    plist=st.selectbox('Select Name of Playlist in Drop Down Menu', pdf['ptitle'].unique())
    video_title=list(pdf.groupby('ptitle').get_group(plist)['vtitle'])
    col=st.beta_columns(len(video_title))
    for i in range(len(video_title)):
        col[i].video((get_url_playloist(video_title[i])[0]))
    
    if st.button("Show Youtube Playlist URL"):
        st.write(search_by_playlist(plist))

#===========================================================================================================
if out == 'Video Search By Professor Details':
    prof_list=st.selectbox('Select Professor Name',teacher_name(alldata))
    b=search_by_Professor_name(prof_list)
    st.video((get_urls(st.selectbox('Select Video Name',b)))[0])

#=========================================================================================================

if out=='Video Search By Title':
    alldata['title'].unique()
    st.video((get_urls(st.selectbox('Select Title Name',(alldata['title'].unique()))))[0])
    
#==========================================================================================================

if out=="Data":
    if st.button("Show Data"):
        st.dataframe(pdf)
        st.dataframe(alldata)