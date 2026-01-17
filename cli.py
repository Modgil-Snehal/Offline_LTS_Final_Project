from translator_engine import OfflineTranslator

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Odia": "ory_Orya",
    "Assamese": "asm_Beng",
    "Urdu": "urd_Arab",
    "Nepali": "npi_Deva",
    "Sanskrit": "san_Deva",
    "Maithili": "mai_Deva"
}

def show_languages():
    print("\nSupported Languages:")
    for idx, lang in enumerate(LANGUAGES.keys(), start=1):
        print(f"{idx}. {lang}")

def get_language(prompt):
    while True:
        show_languages()
        choice = input(prompt).strip()

        # Numeric selection
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(LANGUAGES):
                lang_name = list(LANGUAGES.keys())[idx]
                return lang_name, LANGUAGES[lang_name]

        # Text selection
        for name in LANGUAGES:
            if choice.lower() == name.lower():
                return name, LANGUAGES[name]

        print("❌ Invalid choice. Try again.")


def main():
    print("\n=== Offline Indian Language Translation System ===")

    translator = OfflineTranslator()

    while True:
        src_name, src_code = get_language("\nSelect SOURCE language: ")
        tgt_name, tgt_code = get_language("Select TARGET language: ")

        if src_code == tgt_code:
            print("❌ Source and target languages cannot be the same.")
            continue

        text = input(f"\nEnter text in {src_name} (or type 'exit'): ").strip()
        if text.lower() == "exit":
            print("Exiting translator.")
            break

        try:
            output = translator.translate(text, src_code, tgt_code)
            print(f"\nTranslated ({tgt_name}):")
            print(output)
        except Exception as e:
            print("❌ Translation failed:", e)

if __name__ == "__main__":
    main()