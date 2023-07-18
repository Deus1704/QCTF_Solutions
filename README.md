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
   ![image](https://raw.githubusercontent.com/Deus1704/QCTF_Solutions/main/Images/CTF1sol.png?token=GHSAT0AAAAAACA34FX3U3BYIZLXQDWTBJSMZFWUESA)

   **Flag: &nbsp;&nbsp;CTF{6006l35_f0r_fl46_n4m35}**

<br>

2. ### **Video (20 Points):**<br>
   For this challenge, I studied the methods of Steganography from the following blog https://0xrick.github.io/lists/stego/. Using the `exiftool` command in Bash, while analysing
   the output from the exiftool, I noticied the flag inside comments. 
   ![image2](https://raw.githubusercontent.com/Deus1704/QCTF_Solutions/main/Images/CTF2sol.png?token=GHSAT0AAAAAACA34FX3VRXAV6WJ6JKBSFX6ZFWUNHA)



4. ### **Flag Finder (10 Points):**<br>







5. ### **Flag Finder (10 Points):**<br>







6. ### **Flag Finder (10 Points):**<br>





7. ### **Flag Finder (10 Points):**<br>




8. ### **Flag Finder (10 Points):**<br>




9. ### **Flag Finder (10 Points):**<br>
