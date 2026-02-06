def analyze_string(raw_data):
    clean_data = raw_data.strip().lower()
    print(f"The raw data is '{raw_data}'")
    print(f"The clean data is '{clean_data}'")

    vowels = 0
    consonant = 0  
    digits = 0
    others = 0     
    vowel_set = "aeiou"

    for char in clean_data:
       
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonant += 1
                
        elif char.isdigit():
            digits += 1

        else:
            others += 1

    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonant}")
    print(f"Number of digits: {digits}")
    print(f"Number of others: {others}")

string = input("Enter the sentence: ")
analyze_string(string)
