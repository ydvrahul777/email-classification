{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59a3fcd2-7513-4eb1-bfa4-cace1ab95fbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "import re\n",
    "\n",
    "def mask_pii(text):\n",
    "    patterns = {\n",
    "        r'\\b(?:\\w+\\s){1,3}\\w+\\b': '[full_name]',\n",
    "        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.\\w+': '[email]',\n",
    "        r'\\b\\d{10}\\b': '[phone_number]',\n",
    "        r'\\b\\d{4}-\\d{2}-\\d{2}\\b': '[dob]',\n",
    "        r'\\b\\d{12}\\b': '[aadhar_num]',\n",
    "        r'\\b(?:\\d{4}[-\\s]?){4}\\b': '[credit_debit_no]',\n",
    "        r'\\b\\d{3}\\b': '[cvv_no]',\n",
    "        r'(0[1-9]|1[0-2])\\/?([0-9]{2})': '[expiry_no]',\n",
    "    }\n",
    "    for pattern, replacement in patterns.items():\n",
    "        text = re.sub(pattern, replacement, text)\n",
    "    return text\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
