import streamlit as st
from analyzer import CompetitorTextAnalyzer

def main():
    st.title("Competitor Text Analyzer")
    st.subheader("Analizza rapidamente i testi dei tuoi concorrenti!")

    # Input dell'utente
    user_input = st.text_area("Inserisci il testo del concorrente da analizzare:")
    
    if st.button("Analizza"):
        if user_input.strip():
            analyzer = CompetitorTextAnalyzer(language='it')
            results = analyzer.analyze_text(user_input)
            st.write("### Report dell'analisi")
            st.write(analyzer.generate_report(results))
        else:
            st.warning("Per favore, inserisci un testo valido.")

if __name__ == "__main__":
    main()
