from vi_cleaner.vi_cleaner import ViCleaner

def normalize_text(text):
    cleaner = ViCleaner(text)
    return cleaner.clean()
