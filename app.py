
import streamlit as st
import datetime
import pytz
from PIL import Image
import pandas as pd

# Initialize voice assistant

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to display Sehri and Iftari timings
def display_sehri_iftari_timings():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Sehri Timings")
        city = st.selectbox("Select City", ["Karachi", "Lahore", "Islamabad"])
        if city == "Karachi":
            sehri_timing = "4:30 AM"
            st.write("Sehri Timing:", sehri_timing)
            # speak(f"Sehri timing in {city} is {sehri_timing}")
        elif city == "Lahore":
            sehri_timing = "4:15 AM"
            st.write("Sehri Timing:", sehri_timing)
            # speak(f"Sehri timing in {city} is {sehri_timing}")
        elif city == "Islamabad":
            sehri_timing = "4:20 AM"
            st.write("Sehri Timing:", sehri_timing)
            # speak(f"Sehri timing in {city} is {sehri_timing}")
    with col2:
        st.write("Iftari Timings")
        city = st.selectbox("Select City", ["Karachi", "Lahore", "Islamabad"])
        if city == "Karachi":
            iftari_timing = "6:30 PM"
            st.write("Iftari Timing:", iftari_timing)
            # speak(f"Iftari timing in {city} is {iftari_timing}")
        elif city == "Lahore":
            iftari_timing = "6:15 PM"
            st.write("Iftari Timing:", iftari_timing)
            # speak(f"Iftari timing in {city} is {iftari_timing}")
        elif city == "Islamabad":
            iftari_timing = "6:20 PM"
            st.write("Iftari Timing:", iftari_timing)
            # speak(f"Iftari timing in {city} is {iftari_timing}")

# Function to display Quran Tilawat tracker
def display_quran_tilawat_tracker():
    st.write("Quran Tilawat Tracker")
    surah = st.selectbox("Select Surah", ["Al-Fatihah", "Al-Baqarah", "Al-Imran"])
    ayah = st.number_input("Enter Ayah Number", min_value=1)
    st.write("You have read Surah", surah, "Ayah", ayah)
    # speak(f"You have read Surah {surah} Ayah {ayah}")

# Function to display Tasbih counter
def display_tasbih_counter():
    st.write("Tasbih Counter")
    tasbih = st.button("Tasbih")
    if tasbih:
        count = st.session_state.get("count", 0) + 1
        st.session_state["count"] = count
        st.write("Tasbih Count:", count)
        # speak(f"Tasbih count is {count}")

# Function to display Salah tracker
def display_salah_tracker():
    st.write("Salah Tracker")
    salah = st.selectbox("Select Salah", ["Fajr", "Zuhr", "Asr", "Maghrib", "Isha"])
    performed = st.checkbox("Performed")
    if performed:
        st.write("You have performed", salah, "Salah")
        # speak(f"You have performed {salah} Salah")

# Function to display Zakat calculator
def display_zakat_calculator():
    st.write("Zakat Calculator")
    wealth = st.number_input("Enter your wealth", min_value=0)
    zakat = wealth * 0.025
    st.write("Your Zakat is:", zakat)
    # speak(f"Your Zakat is {zakat}")

# Function to display Masnoon dua collections
def display_masnoon_dua_collections():
    st.write("Masnoon Dua Collections")
    dua = st.selectbox("Select Dua", ["Dua for Ramadan", "Dua for Eid", "Dua for Protection"])
    if dua == "Dua for Ramadan":
        st.write("Dua for Ramadan: Allahumma innaka 'afuwwun tuhibbul 'afwa fa'fu 'anni")
        # speak("Dua for Ramadan: Allahumma innaka 'afuwwun tuhibbul 'afwa fa'fu 'anni")
    elif dua == "Dua for Eid":
        st.write("Dua for Eid: Takbirat of Tashriq")
    elif dua == "Dua for Protection":
        st.write("Dua for Protection: A'uzu billahi minash-shaytanir-rajim")
        # speak("Dua for Protection: A'uzu billahi minash-shaytanir-rajim")

# Function to display 40 Hadith from Sahih Bukhari
def display_40_hadith():
    st.write("40 Hadith from Sahih Bukhari")
    hadith = st.selectbox("Select Hadith", ["Hadith 1", "Hadith 2", "Hadith 3"])
    if hadith == "Hadith 1":
        st.write("Hadith 1: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Whoever says 'La ilaha illallah' ...'")
        # speak("Hadith 1: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Whoever says 'La ilaha illallah' ...'")
    elif hadith == "Hadith 2":
        st.write("Hadith 2: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Do not wish for death ...'")
        # speak("Hadith 2: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Do not wish for death ...'")
    elif hadith == "Hadith 3":
        st.write("Hadith 3: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Whoever believes in Allah and the Last Day ...'")
        # speak("Hadith 3: Narrated by Abu Hurairah, The Prophet (peace be upon him) said: 'Whoever believes in Allah and the Last Day ...'")

# Main app
def main():
    st.title("Ramzan Companion")
    tabs = ["Sehri and Iftari Timings", "Quran Tilawat Tracker", "Tasbih Counter", "Salah Tracker", "Zakat Calculator", "Masnoon Dua Collections", "40 Hadith from Sahih Bukhari"]
    tab = st.selectbox("Select Tab", tabs)

    if tab == "Sehri and Iftari Timings":
        display_sehri_iftari_timings()
    elif tab == "Quran Tilawat Tracker":
        display_quran_tilawat_tracker()
    elif tab == "Tasbih Counter":
        display_tasbih_counter()
    elif tab == "Salah Tracker":
        display_salah_tracker()
    elif tab == "Zakat Calculator":
        display_zakat_calculator()
    elif tab == "Masnoon Dua Collections":
        display_masnoon_dua_collections()
    elif tab == "40 Hadith from Sahih Bukhari":
        display_40_hadith()

if __name__ == "__main__":
    main()
