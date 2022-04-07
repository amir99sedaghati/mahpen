def convert_english_number_to_persian_number(english_numbers):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    number = str(english_numbers)
    return ''.join(devanagari_nums[int(digit)] for digit in number)