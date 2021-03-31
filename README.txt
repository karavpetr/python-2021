Проект Караваева Петра, студента 1 курса МФТИ, предмет Практика на Python, 2021.

Проект Шифрование.
Запуск программы:
В общем случа:
python3 cryptography.py --action=<> --in_path=<> --out_path=<> --cipher_name=<> --key_path=<>

Примеры:
python3 cryptography.py --action=Encrypt --in_path=input.txt --out_path=output.txt --cipher_name=Caesar --key_path=key.txt

python3 cryptography.py --action=Decrypt --in_path=output.txt --out_path=output2.txt --cipher_name=Caesar --key_path=key.txt

Возможные значения параметров:
action: Encrypt, Decrypt, AutoDecrypt
cipher_name: Caesar, Vigenere, Vernam
