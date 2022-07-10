class Solution: 
    def numberToWords(self, num: int) -> str:
        digits = {
            0: '', 
            1: 'One',
            2: 'Two',
            3: 'Three', 
            4: 'Four',
            5: 'Five', 
            6: 'Six', 
            7: 'Seven', 
            8: 'Eight', 
            9: 'Nine'
        }

        tens_place = {
            9: 'Ninety', 
            8: 'Eighty', 
            7: 'Seventy',
            6: 'Sixty',
            5: 'Fifty',
            4: 'Forty',
            3: 'Thirty',
            2: 'Twenty',
            0: ''
        }
        teens = {
            10: 'Ten', 
            11: 'Eleven', 
            12: 'Twelve', 
            13: 'Thirteen', 
            14: 'Fourteen',
            15: 'Fifteen', 
            16: 'Sixteen', 
            17: 'Seventeen', 
            18: 'Eighteen', 
            19: 'Nineteen'
        }
        
        def prepend_space(existing_string, string_to_add):
            if (len(existing_string) > 0) and (len(string_to_add) > 0) : 
                existing_string += ' '
            return existing_string + string_to_add
        
        def three_digit_words(num):
            string = ""
            hundreds = num // 100
            if hundreds > 0: 
                string += digits[hundreds] + " Hundred"

            remainder = num % 100
            if remainder < 20 and remainder >= 10:
                string = prepend_space(string, teens[remainder])
            elif remainder < 10:
                string = prepend_space(string, digits[remainder])
            else:
                tens = remainder // 10
                ones = remainder % 10
                string = prepend_space(string, tens_place[tens])
                string = prepend_space(string, digits[ones])
            return string
        
        if num == 0:
            return "Zero"
        
        full_string = ""
        
        bilions = num // 10**9
        bilions = bilions % 10**3
        if bilions > 0:
            full_string += three_digit_words(bilions) + " Billion"
        
        millions = num // 10**6
        millions = millions % 10**3
        if millions > 0:
            millions_string = three_digit_words(millions) + " Million"
            full_string = prepend_space(full_string, millions_string)
            
        thousands = num // 10**3
        thousands = thousands % 10**3
        if thousands > 0:
            thousands_string = three_digit_words(thousands) + " Thousand"
            full_string = prepend_space(full_string, thousands_string)

        
        full_string = prepend_space(full_string, three_digit_words(num % 1000))
        
        #print(full_string)
        return full_string