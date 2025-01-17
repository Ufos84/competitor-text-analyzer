import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

class CompetitorTextAnalyzer:
    def __init__(self, language='it'):
        self.language = language
        if language == 'it':
            self.nlp = spacy.load("it_core_news_sm")
        else:
            raise ValueError("Lingua non supportata. Usa 'it' per italiano.")

    def analyze_text(self, text):
        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
        keywords = Counter(tokens).most_common(10)

        blob = TextBlob(text)
        sentiment = blob.sentiment

        return {
            "main_keywords": [word for word, _ in keywords[:5]],
            "secondary_keywords": [word for word, _ in keywords[5:]],
            "entities": [(ent.text, ent.label_) for ent in doc.ents],
            "key_points": {
                "polarity": sentiment.polarity,
                "subjectivity": sentiment.subjectivity,
            },
        }

    def generate_report(self, results):
        report = "Report dell'Analisi:\n"
        report += "Keywords principali: " + ", ".join(results["main_keywords"]) + "\n"
        report += "Keywords secondarie: " + ", ".join(results["secondary_keywords"]) + "\n"
        report += "Entità trovate:\n"
        for entity, label in results["entities"]:
            report += f"  - {entity} ({label})\n"
        report += "Punti salienti:\n"
        report += f"  - Polarità: {results['key_points']['polarity']}\n"
        report += f"  - Soggettività: {results['key_points']['subjectivity']}\n"
        return report
