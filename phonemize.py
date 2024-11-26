import string
from text_normalize import normalize_text
from get_phonemes import vietnamese_pronunciation
from underthesea import word_tokenize

def phonemize(text, tokenizer):
    text = normalize_text((text))
    words = word_tokenize(text)

    input_ids = []
    phonemes = []  

    for word in words:
        phoneme = vietnamese_pronunciation(word)

        input_ids.append(tokenizer.encode(word)[1])  # replace 0 by 1
        phonemes.append(phoneme)
    
    assert len(input_ids) == len(phonemes)
    return {'input_ids' : input_ids, 'phonemes': phonemes}