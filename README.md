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
   ![image](/Images/CTF1sol.png)
   
   **Flag: &nbsp;&nbsp;CTF{6006l35_f0r_fl46_n4m35}**

<br>

2. ### **Video (20 Points):**<br>
   For this challenge, I studied the methods of Steganography from the following blog https://0xrick.github.io/lists/stego/. Using the `exiftool` command in Bash, while analysing
   the output from the exiftool, I noticied the flag inside comments.<br>
   <br>
   ![image2](/Images/CTF2sol.png)

   **Flag: &nbsp;&nbsp;CTF{r1ck_r0ll1n6_h45_607_0ld}**
<br>

3. ### **What does the server say? (25 Points):**<br>
   This was one of the most problematic yet simplest challenge of the all. From the looks of it and through the general methods to solve web based CTFs, I tried to access the
   http://139.59.26.242:20632 multiple times but it refused to connect nearly everytime. Hence to dig deeper in the given port, I tried port knocking using the open ports 21, 80 and 2000. This was tracked using Wireshark on Linux VM but no response was recieved. Then I tried SSH Tunneling by setting up a localhost at port 8000 and tried to connect to port 20632, yet again refused to connect. Atlast when all hope was gone, I kept opening the site with given port and to my surprise it opened up and was able to get the flag. The end message does make sense since I had to keep looking at it but harder.
   <br>
   ![image](/Images/CTF3sol.png)

   **Flag: &nbsp;&nbsp;CTF{m0r3_7r0ubl3_7h4n_175_w0r7h}**
<br>

4. ### **Binary Bounty (30 Points):**<br>
   The given file on basic analysis usign the `file` command in Bash. This analysis cleared that the elf file was a mix of ASCII and binary values. To quickly find the flag that might be hidden, I tried the `strings` command and found out something catchy saying, "flag doesn't seem so easily obtainable". This had some repetetions like the word `easily` and `sily`. Apart from the obvious extra `H`s in the flag, the repetetions gave me a hint that some word might be repeated in the flag. Hence tried all the possible flags.
   <br>
   ![image](/Images/CTF4sol.png)

   **Flag: &nbsp;&nbsp;CTF{1mm4_h4ck3rm4nn_n0w}**
<br>

5. ### **Hide Your Secrets (30 Points):**<br>
   Analysing the file provided, I found that it contained ASCII charachters. Now using the `cat` command, I analysed the file contents and found them to be simple key logs. I read bout keylogging and the scan codes for different keyboards from https://en.wikipedia.org/wiki/Keystroke_logging .Now using these key logs to be the decimal scan codes of the keyboard used while it was being keylogged, I deciphered the keys and found the flag as VTF{w31rd_flag} but since the format was CTF{}, it had to be corrected.

   **Flag: &nbsp;&nbsp;CTF{w31rd_flag}**
<br>

6. ### **Conversion (35 Points):**<br>
   After analysing the file, I found that it was containing only ASCII values which were not comprehendable. Since it was mentioning about the file being froma audio company, I figured out that it must be converted to some audio format. While analysing its file headers, I found it to be containing ID3 tags, which showed me that the file was an mp3 earlier. In order to conver it back to mp3, I first had to convert the file into binary file. Using the `ffmpeg` tool I converted the binary file into mp3 file and then played it. <br>
   ![image](/Images/convfirststep.png)
This sounded weird. Then I realised it was in reverse. Then using the reverse command of the ffmpeg, I finally converted it and found the flag.<br>
   ![image](/Images/confrombintomp4.png)
   <br>
   **Flag: &nbsp;&nbsp;CTF{dumb_audio_flag}**
<br>

8. ### **Spectral_Secret (50 Points):**<br>
   Firstly, I analyzed the file that contained the arrays of values, and I noticed that these values were represented as complex numbers. The shape of the array was (574, 1366), indicating that it was a 2D array with 574 rows and 1366 columns. My goal was to find a way to extract meaningful information from these complex values and uncover the hidden flag. To start, I attempted an Inverse Fourier Transform (IFT) of order 1 on the complex number arrays, hoping it would reveal something useful. Unfortunately, this initial attempt didn't provide any relevant results, and I couldn't find the flag I was looking for. However, I wasn't ready to give up just yet. I decided to take a more sophisticated approach and applied the Inverse Fourier Transform of order 2 to the complex number arrays. To my delight, this time it worked like magic! "Voila!" I found the elusive flag hidden within the arrays.

```
import numpy as np
import matplotlib.pyplot as plt

# Load the .npy file
data = np.load('spectral_secret.npy')

print(data.shape)
# Apply the inverse Fourier transform
inverse_data = np.fft.ifft(data)

# Plot the real part
plt.figure()
plt.imshow(np.real(inverse_data), cmap='gray')
plt.colorbar()
plt.title('Real Part')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
<br>

   ![image](/Images/CTF7sol.png)

   <br>
   
   **Flag: &nbsp;&nbsp;CTF{m3_1z_pr0}**
<br>



10. ### **Flag Finder (10 Points):**<br>
