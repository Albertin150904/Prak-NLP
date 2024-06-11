import streamlit as st
import requests
from bs4 import BeautifulSoup

# Fungsi untuk melakukan web scraping
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memastikan tidak ada kesalahan dalam permintaan HTTP
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Contoh sederhana: Mengambil semua teks dalam tag <p>
        paragraphs = soup.find_all('p')
        content = [p.get_text() for p in paragraphs]
        
        return content
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Fungsi utama Streamlit
def main():
    st.title("Web Scraping App")
    st.write("Masukkan URL untuk melakukan scraping:")
    
    url = st.text_input("URL", "https://www.example.com")
    
    if st.button("Scrape"):
        with st.spinner('Scraping...'):
            data = scrape_website(url)
            if isinstance(data, list):
                for paragraph in data:
                    st.write(paragraph)
            else:
                st.error(data)

if __name__ == "__main__":
    main()
