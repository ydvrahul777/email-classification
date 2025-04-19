import re

def mask_pii(text):
    patterns = {
        r'\b(?:\w+\s){1,3}\w+\b': '[full_name]',
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.\w+': '[email]',
        r'\b\d{10}\b': '[phone_number]',
        r'\b\d{4}-\d{2}-\d{2}\b': '[dob]',
        r'\b\d{12}\b': '[aadhar_num]',
        r'\b(?:\d{4}[-\s]?){4}\b': '[credit_debit_no]',
        r'\b\d{3}\b': '[cvv_no]',
        r'(0[1-9]|1[0-2])\/?([0-9]{2})': '[expiry_no]',
    }
    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    return text
