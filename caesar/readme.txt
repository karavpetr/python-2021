python3 cryptography.py --action=Encrypt --in_path=caesar/input.txt --out_path=caesar/encrypted.txt --cipher_name=Caesar --key_path=caesar/key.txt

python3 cryptography.py --action=Decrypt --in_path=caesar/encrypted.txt --out_path=caesar/decrypted.txt --cipher_name=Caesar --key_path=caesar/key.txt

python3 cryptography.py --action=AutoDecrypt --in_path=caesar/encrypted.txt --out_path=caesar/autodecrypted.txt --cipher_name=Caesar --key_path=caesar/key.txt
