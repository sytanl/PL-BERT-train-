# # Định nghĩa các nguyên âm với thanh điệu sang ký hiệu IPA
# tones = {
#     # Thanh ngang (không dấu)
#     'a': 'a˧', 'ă': 'ă˧', 'â': 'ə̆˧', 'e': 'e˧', 'ê': 'e˧', 'i': 'i˧',
#     'o': 'o˧', 'ô': 'o˧', 'ơ': 'ə˧', 'u': 'u˧', 'ư': 'ɨ˧', 'y': 'i˧',
    
#     # Thanh sắc
#     'á': 'a˧˥', 'ắ': 'ă˧˥', 'ấ': 'ə̆˧˥', 'é': 'e˧˥', 'ế': 'e˧˥', 'í': 'i˧˥',
#     'ó': 'o˧˥', 'ố': 'o˧˥', 'ớ': 'ə˧˥', 'ú': 'u˧˥', 'ứ': 'ɨ˧˥', 'ý': 'i˧˥',
    
#     # Thanh huyền
#     'à': 'a˧˩', 'ằ': 'ă˧˩', 'ầ': 'ə̆˧˩', 'è': 'e˧˩', 'ề': 'e˧˩', 'ì': 'i˧˩',
#     'ò': 'o˧˩', 'ồ': 'o˧˩', 'ờ': 'ə˧˩', 'ù': 'u˧˩', 'ừ': 'ɨ˧˩', 'ỳ': 'i˧˩',
    
#     # Thanh hỏi
#     'ả': 'a˧˩˧', 'ẳ': 'ă˧˩˧', 'ẩ': 'ə̆˧˩˧', 'ẻ': 'e˧˩˧', 'ể': 'e˧˩˧', 'ỉ': 'i˧˩˧',
#     'ỏ': 'o˧˩˧', 'ổ': 'o˧˩˧', 'ở': 'ə˧˩˧', 'ủ': 'u˧˩˧', 'ử': 'ɨ˧˩˧', 'ỷ': 'i˧˩˧',
    
#     # Thanh ngã
#     'ã': 'a˧˥˧', 'ẵ': 'ă˧˥˧', 'ẫ': 'ə̆˧˥˧', 'ẽ': 'e˧˥˧', 'ễ': 'e˧˥˧', 'ĩ': 'i˧˥˧',
#     'õ': 'o˧˥˧', 'ỗ': 'o˧˥˧', 'ỡ': 'ə˧˥˧', 'ũ': 'u˧˥˧', 'ữ': 'ɨ˧˥˧', 'ỹ': 'i˧˥˧',
    
#     # Thanh nặng
#     'ạ': 'a˧˨', 'ặ': 'ă˧˨', 'ậ': 'ə̆˧˨', 'ẹ': 'e˧˨', 'ệ': 'e˧˨', 'ị': 'i˧˨',
#     'ọ': 'o˧˨', 'ộ': 'o˧˨', 'ợ': 'ə˧˨', 'ụ': 'u˧˨', 'ự': 'ɨ˧˨', 'ỵ': 'i˧˨'
# }

# # Định nghĩa các phụ âm tiếng Việt sang ký hiệu IPA
# consonants = {
#     'b': 'ɓ', 'c': 'k', 'd': 'z', 'đ': 'ɗ', 'g': 'ɣ', 'h': 'h', 'k': 'k',
#     'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'q': 'kw', 'r': 'r', 's': 's',
#     't': 't', 'v': 'v', 'x': 's'
# }

# # Hàm để chuyển đổi từ tiếng Việt sang ký hiệu IPA
# def vietnamese_pronunciation(word):
#     result = ""
    
#     for char in word:
#         # Kiểm tra và xử lý nguyên âm có thanh điệu
#         if char in tones:
#             result += tones[char]
#         # Kiểm tra và xử lý phụ âm
#         elif char in consonants:
#             result += consonants[char]
#         # Nếu không phải nguyên âm hoặc phụ âm đặc biệt, giữ nguyên
#         else:
#             result += char
    
#     return result
def replace_tonemark(result: str):
    for cha in result:
        if cha in "àáảãạ":
            result = result.replace(cha, 'a')
        elif cha in "ầấẩẫậ":
            result = result.replace(cha, 'â')
        elif cha in "ằắẳẵặ":
            result = result.replace(cha, 'ă')
        elif cha in "èéẻẽẹ":
            result = result.replace(cha, 'e')
        elif cha in "ềếểễệ":
            result = result.replace(cha, 'ê')
        elif cha in "ìíỉĩị":
            result = result.replace(cha, 'i')
        elif cha in "òóỏõọ":
            result = result.replace(cha, 'o')
        elif cha in "ồốổỗộ":
            result = result.replace(cha, 'ô')
        elif cha in "ờớởỡợ":
            result = result.replace(cha, 'ơ')
        elif cha in "ùúủũụ":
            result = result.replace(cha, 'u')
        elif cha in "ừứửữự":
            result = result.replace(cha, 'ư')
        elif cha in "ỳýỷỹỵ":
            result = result.replace(cha, 'y')

    return result

class VietnameseMapper:
    def __init__(self):
        # Vowels mapping
        self.vowels = {
            'a': 'aː',
            'ă': 'a',
            'â': 'ə',
            'e': 'ɛ',
            'ê': 'e',
            'i': 'i',
            'o': 'ɔ',
            'ô': 'o',
            'ơ': 'ə:',
            'u': 'u',
            'ư': 'ɨ',
            'y': 'i'
        }

        # Consonants mapping
        self.consonants = {
            'b': 'ɓ',
            'c': 'k',
            'd': 'j',
            'đ': 'ɗ',
            'g': 'g',
            'h': 'h',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'p': 'p',
            'q': 'k',
            'r': 'r',
            's': '∫',
            't': 't',
            'v': 'v',
            'x': 's',
            'ch': 'c',
            'gh': 'g',
            'gi': 'j',
            'kh': 'x',
            'ng': 'ŋ',
            'ngh': 'ŋ',
            'nh': 'ɲ',
            'ph': 'f',
            'th': 'tʰ',
            'tr': 'ʈʂ'
        }

        # Diphthongs and triphthongs
        # self.compounds = {
        #     'ia': 'iə',
        #     'iê': 'iə',
        #     'yê': 'iə',
        #     'ua': 'uə',
        #     'uô': 'uə',
        #     'ưa': 'ɯə',
        #     'ươ': 'ɯə',
        #     'ai': 'aj',
        #     'ao': 'aw',
        #     'eo': 'ew',
        #     'iu': 'iw',
        #     'oi': 'ɔj',
        #     'ôi': 'oj',
        #     'ơi': 'ɤj',
        #     'ui': 'uj',
        #     'ưi': 'ɯj',
        #     'ay': 'aj',
        #     'ây': 'əj',
        #     'âu': 'əw',
        #     'uy': 'uj'
        # }

        # Tone number mapping (1-6)
        self.tone_numbers = {
            'a': '1', 'à': '2', 'á': '3', 'ả': '4', 'ã': '5', 'ạ': '6',
            'ă': '1', 'ằ': '2', 'ắ': '3', 'ẳ': '4', 'ẵ': '5', 'ặ': '6',
            'â': '1', 'ầ': '2', 'ấ': '3', 'ẩ': '4', 'ẫ': '5', 'ậ': '6',
            'e': '1', 'è': '2', 'é': '3', 'ẻ': '4', 'ẽ': '5', 'ẹ': '6',
            'ê': '1', 'ề': '2', 'ế': '3', 'ể': '4', 'ễ': '5', 'ệ': '6',
            'i': '1', 'ì': '2', 'í': '3', 'ỉ': '4', 'ĩ': '5', 'ị': '6',
            'o': '1', 'ò': '2', 'ó': '3', 'ỏ': '4', 'õ': '5', 'ọ': '6',
            'ô': '1', 'ồ': '2', 'ố': '3', 'ổ': '4', 'ỗ': '5', 'ộ': '6',
            'ơ': '1', 'ờ': '2', 'ớ': '3', 'ở': '4', 'ỡ': '5', 'ợ': '6',
            'u': '1', 'ù': '2', 'ú': '3', 'ủ': '4', 'ũ': '5', 'ụ': '6',
            'ư': '1', 'ừ': '2', 'ứ': '3', 'ử': '4', 'ữ': '5', 'ự': '6',
            'y': '1', 'ỳ': '2', 'ý': '3', 'ỷ': '4', 'ỹ': '5', 'ỵ': '6'
        }

        # Base vowels for tone detection
        self.base_vowels = 'aăâeêioôơuưyàáảãạầấẩẫậằắẳẵặèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ'
    
    def get_tone_number(self, syllable):
        """Get the tone number for a syllable."""
        numbers: list[int] = [] 
        for vowel in self.base_vowels:
            if vowel in syllable:
                for tone_mark, number in self.tone_numbers.items():
                    if vowel in syllable and tone_mark in syllable:
                        numbers.append(int(number))

        return max(numbers) if len(numbers) != 0 else 1

    def replace_consonants(self, result: str) -> str:
        length = len(result)
        output = ""
        skip = False  # Cờ để bỏ qua ký tự khi đã thay thế cặp ký tự

        for i in range(length):
            if skip:
                skip = False
                continue

            # Kiểm tra cặp ký tự
            if i + 1 < length and result[i:i+2] in self.consonants:
                output += self.consonants[result[i:i+2]]
                skip = True  # Bỏ qua ký tự tiếp theo vì đã xử lý cặp
            elif result[i] in self.consonants:
                output += self.consonants[result[i]]
            else:
                output += result[i]

        return output


    def to_ipa_and_tone(self, text):
        """Convert Vietnamese text to IPA and tone numbers."""
        words = text.lower().split()
        ipa_result = []
        repeated_tones = []
        
        for word in words:
            # Get tone number first
            tone_num = self.get_tone_number(word)
            
            # Convert to IPA
            result = word
            # # Convert compounds first (to avoid single letter conflicts)
            # for viet, ipa in self.compounds.items():
            #     result = result.replace(viet, ipa)

            # Remove any remaining tone marks
            result = replace_tonemark(result)
            
            # Convert consonants
            result = self.replace_consonants(result)
            
            # Convert vowels
            for viet, ipa in self.vowels.items():
                result = result.replace(viet, ipa)
            
            # Count phonemes (approximately by counting characters in IPA)
            phoneme_count = len(result)
            
            # Create repeated tone number string
            repeated_tone = str(tone_num) * phoneme_count
            
            ipa_result.append(result)
            repeated_tones.append(repeated_tone)
        
        return {
            'ipa': ipa_result,
            'tone_numbers': repeated_tones
        }

# # Example usage:
# if __name__ == "__main__":
#     mapper = VietnameseMapper()
    
#     # Test cases
#     test_phrases = [
#         "xin chào",
#         "tiếng việt",
#         "học sinh",
#         "người ta",
#         "trường học"
#     ]
    
#     for phrase in test_phrases:
#         result = mapper.to_ipa_and_tone(phrase)
#         print(f"\nPhrase: {phrase}")
#         print(f"IPA: {' '.join(result['ipa'])}")
#         print(f"Tone numbers: {' '.join(result['tone_numbers'])}")
def vietnamese_pronunciation(word):
    mapper = VietnameseMapper()
    result = mapper.to_ipa_and_tone(word)
    return ' '.join(result['ipa']).strip()
