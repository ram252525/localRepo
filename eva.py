import streamlit as st
from API.WikipediaApi import wiki
from API.Wallframealpha import shortAlpha, longAlpha, conversationBot
from API.YoutubeTranscriptApi import transcript
from API.OMDBApi import movieDetailes
from API.OpenWeatherApi import weather
from API.googleAnswerApi import googleShortAnswer
import time

#page config
st.set_page_config(page_title="Eva",
                   page_icon=r"c:\Users\HP Probook\OneDrive\Desktop\eva.png",
                   layout="centered")

#logo
st.logo(r"c:\Users\HP Probook\OneDrive\Desktop\eva.png", link=None, icon_image=None)


#bots
Bots = st.sidebar.selectbox('Bots', ['GoogleBot', 'WikipediaBot', 'ShortAnswerBot', 'LongAnswerBot', 'ConversationBot', 'YouTubeTransciptBot', 'MovieBot', 'WeatherBot'], index=0)

#clear chat history
def clear_chat_history():
      st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]


#google bot(google api)
if Bots == 'GoogleBot':
    
    #title
    st.title("Google Bot")

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Say something ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                response = googleShortAnswer(prompt)

            def output_stream():
                for word in response.split(" "):
                    yield word + " "
                    time.sleep(0.02)
                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : response})


#wikipedia bot(wikipedia api)
if Bots == 'WikipediaBot':
    
    #title
    st.title("Wikipedia Bot")

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Say something ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                response = wiki(prompt)
            
            def output_stream():
                for word in response.split(" "):
                    yield word + " "
                    time.sleep(0.02)

        def input_st():
            for i in only.streamseyetem.io not in ():

                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : response})

#short answer bot (wallframe alpha)
elif Bots == 'ShortAnswerBot':

    #title
    st.title("Short Answer Bot")

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Say something ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):

                response = shortAlpha(prompt)
                
                # Convert bytes literal to a string
                string_literal = response.decode('utf-8')
                string_literal = response.encode('utf-8')

                # Remove single quotes
                cleaned_string = string_literal.replace("'", "")

            def output_stream():
                for word in  cleaned_string.split(" "):
                    yield word + " "
                    time.sleep(0.02)
                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : cleaned_string})


#long answer bot (wallframe alpha)
elif Bots == 'LongAnswerBot':

    #title
    st.title("Long Answer Bot")

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Say something ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                response = longAlpha(prompt)
                
            def output_stream():
                for word in  response.split(" "):
                    yield word + " "
                    time.sleep(0.02)
                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : response})

#conversation bot (wallframe alpha)
elif Bots == 'ConversationBot':

    #title
    st.title("Conversation Bot")

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Say something ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                response = conversationBot(prompt)
                
            def output_stream():
                for word in  response.split(" "):
                    yield word + " "
                    time.sleep(0.02)
                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : response})

#LLM bot (wallframe alpha)
elif Bots == 'YouTubeTransciptBot':

    #title
    st.title("YouTube Transcript")

    lang = st.sidebar._selectbox("Translation Language", ['en', 'hi', 'de'])

    #set default message
    if "message" not in st.session_state.keys():
        st.session_state['message'] = [{"role" : "assistant", "content" : "How may I help you?"}]

    #show all message
    for message in st.session_state['message']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    #uset input
    if prompt := st.chat_input("Type a URL ..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        #add to session
        st.session_state.message.append({"role" : "user", "content" : prompt})

    #assistant reply
    if st.session_state.message[-1]['role'] != 'assistant':
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):

                if lang:
                    response = transcript(prompt, lang)
                    #print(lang)
                
                else:
                    response = transcript(prompt)

            def output_stream():
                for word in response.split(" "):
                    yield word + " "
                    time.sleep(0.02)
                
            st.write_stream(output_stream)

        #add to session
        st.session_state.message.append({"role" : "assistant", "content" : response})

#Movie Bot(OMDB api)
elif Bots == 'MovieBot':

    #title
    st.title("MovieBot")

    prompt = st.chat_input("Enter movie name...")
    
    if prompt:

        Details, Actors, Awards, BoxOfficeCollection, Director, Country, Genre, Language, Rated,  RottenTomatoesRating,  IMDB, ReleasedDate, Runtime, Writer, Plot, Title, Poster = movieDetailes(prompt)

        #heading
        st.header(f''':blue[{Title}]''')

        st.image(Poster, Title)

        st.markdown(f'''
                :blue[Actrors:]  {Actors}\n
                :blue[Awards:]  {Awards}\n
                :blue[BoxOffice Collection:]  {BoxOfficeCollection}\n
                :blue[Director:]  {Director}\n
                :blue[Country:]  {Country}\n
                :blue[Genre:]  {Genre}\n
                :blue[Language:]  {Language}\n
                :blue[Rated:]  {Rated}\n
                :blue[Rotten Tomatoes Rating:]  {RottenTomatoesRating}\n
                :blue[IMDB Rating:]  {IMDB}\n
                :blue[Released Date:]  {ReleasedDate}\n
                :blue[Runtime:]  {Runtime}\n
                :blue[Writer:]  {Writer}\n
                :blue[Plot:]  {Plot}
                ''', True)
        
#Weather Bot(Opean weather api api)
elif Bots == 'WeatherBot':

    #title
    st.title("WeatherBot")

    prompt = st.chat_input("Enter movie city name...")
    
    if prompt:

        city, temperature, min_temperature, max_temperature, sea_level, pressure, humidity, description, wind_speed, sunrise, sunset = weather('jaipur')
        
        #heading
        st.header(f''':blue[{city}]''')
 
        st.markdown(f'''
                :blue[Temperature:]  {temperature} °C\n
                :blue[Min Temperature:]  {min_temperature} °C\n
                :blue[Man Temperature:]  {max_temperature} °C\n
                :blue[Sea Level:]  {sea_level} feet\n
                :blue[Pressure:]  {pressure} atm\n
                :blue[Humidity:]  {humidity} %\n
                :blue[Description:]  {description}\n
                :blue[Wind Speed:]  {wind_speed} km/h\n
                :blue[Sunrise:]  {sunrise}\n
                :blue[Sunset:]  {sunset}\n
                ''', True)
   
   
#clear chat history
st.sidebar.button("Clear chat history", on_click = clear_chat_history)

#stop
if st.sidebar.button("stop"):
    st.stop()
