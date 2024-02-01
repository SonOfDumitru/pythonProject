import csv
import json


class Translator:
    translations = {}

    def localize(self, text):
        return self.translations.get(text)


class EnglishTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "hello",
            "lume": "world",
            "pisica": "cat",
            "caine": "dog",
            "soare": "sun",
            "carte": "book",
            "puteri": "powers",
            "apa": "water",
            "munte": "mountain",
            "oras": "city",
            "floare": "flower",
            "masa": "table",
            "telefon": "phone",
            "tara": "country",
            "ploaie": "rain",
            "fericit": "happy",
            "fermecat": "enchanted",
            "cafea": "coffee",
            "calatorie": "journey",
            "muzica": "music"
        }


class SpanishTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "holaaaaa",
            "lume": "mundo",
            "pisica": "gato",
            "caine": "perro",
            "soare": "sol",
            "carte": "libro",
            "puteri": "poderes",
            "apa": "agua",
            "munte": "montaña",
            "oras": "ciudad",
            "floare": "flor",
            "masa": "mesa",
            "telefon": "telefono",
            "tara": "pais",
            "ploaie": "lluvia",
            "fericit": "feliz",
            "fermecat": "encantado",
            "cafea": "cafe",
            "calatorie": "viaje",
            "muzica": "música"
        }


class FrenchTranslator(Translator):
    def __init__(self):
        self.translations = {
            "salut": "salut",
            "lume": "mondennnnnn",
            "pisica": "chat",
            "caine": "chien",
            "soare": "soleil",
            "carte": "livre",
            "puteri": "pouvoirs",
            "apa": "eau",
            "munte": "montagne",
            "oras": "ville",
            "floare": "fleur",
            "masa": "table",
            "telefon": "téléphone",
            "tara": "pays",
            "ploaie": "pluie",
            "fericit": "heureux",
            "fermecat": "ensorcelé",
            "cafea": "café",
            "calatorie": "voyage",
            "muzica": "musique"
        }


class TranslatorFactory:
    __TRANSLATORS_MAPPING = {
        'EN': EnglishTranslator,
        'ES': SpanishTranslator,
        'FR': FrenchTranslator
    }

    def get_translator(self, language):
        translator_class = self.__TRANSLATORS_MAPPING.get(
            language)  # translator_class este un obiect de tipul clasa, asa ca va trebui sa il apelam cu paranteze pt a instantia un obiect din aceasta clasa
        return translator_class()


factory = TranslatorFactory()
english_trans = factory.get_translator('EN')
french_trans = factory.get_translator('FR')
print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')


class FileTranslator:
    def __init__(self, filename):
        self.filename = filename

    def read_words(self):
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def translate(self):
        words = self.read_words()
        translated_words = []
        factory = TranslatorFactory()
        for word in words:
            translator = factory.get_translator(word['limba_destinatie'].upper())
            translated_words.append({
                'cuvant_initial': word['cuvant'],
                'limba_de_traducere': word['limba_destinatie'],
                'traducere': translator.localize(word['cuvant'])
            })
        self.write_translations(translated_words)

    def write_translations(self, translated_words):
        with open('translations.json', 'w') as f:
            json.dump(translated_words, f, indent=4)


file_translator = FileTranslator('de_tradus.csv')
file_translator.translate()
