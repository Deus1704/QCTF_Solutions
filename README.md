# QCTF_Solutions
This Contains the solutions to the CTF problems solved during the QCTF challenge period.

| Challenge Name    | Points | Flag   |
| -------- | --- | ------------ |
| Flag Finder    | 10  | CTF{6006l35_f0r_fl46_n4m35}     |
| Video      | 20  | CTF{r1ck_r0ll1n6_h45_607_0ld}     |
| What does the server say?  | 25  | CTF{m0r3_7r0ubl3_7h4n_175_w0r7h}    |
| Binary Bounty  | 30  | CTF{1mm4_h4ck3rm4nn_n0w}    |
| Hide Your Secrets  | 30  | CTF{w31rd_flag}    |
| Conversion  | 35  | CTF{dumb_audio_flag}    |
| Spectral_Secret  | 50  | CTF{m3_1z_pr0}    |
| Really Simple Algorithm  | 50  | CTF{d3cipher_m3_if_y0u_can}    |

<br>
<br>

1. ### **Flag Finder (10 Points):**<br>
   Firstly from observation the given cipher appears to be encoded in Hexadecimal format. Using the ```echo``` and ```xxd``` command on Bash, I decrypted the given cipher. This
   gave out another cipher that was encrytped in Base64 format. Using the ```Base64 -d``` decoding syntax in the bash I was able to decode the cipher and finally found the flag.
   ![image](https://github.com/Deus1704/QCTF_Solutions/assets/117574289/49763edc-62ab-4861-9d24-3b0256d906b6)

   **Flag: &nbsp;&nbsp;CTF{6006l35_f0r_fl46_n4m35}**

