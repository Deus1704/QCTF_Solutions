# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer

# def convert_npy_to_text(npy_file):
#     # Load the .npy file
#     data = np.load(npy_file)

#     # Reverse the TF-IDF process
#     vectorizer = TfidfVectorizer(norm=None, use_idf=True, smooth_idf=False)
#     transformed_data = vectorizer.inverse_transform(data)

#     # Convert the transformed data to text
#     text_data = []
#     for row in transformed_data:
#         text = " ".join(row)
#         text_data.append(text)

#     return text_data

# # Example usage
# npy_file_path = "spectral_secret.npy"
# text_data = convert_npy_to_text(npy_file_path)

# # Print the converted text data
# for text in text_data:
#     print(text)




# import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer

# def convert_npy_to_text(npy_file, text_data):
#     # Load the .npy file
#     data = np.load(npy_file)

#     # Create and fit the TfidfVectorizer on the original text data
#     vectorizer = TfidfVectorizer(norm=None, use_idf=True, smooth_idf=False)
#     vectorizer.fit(text_data)

#     # Reverse the TF-IDF process
#     transformed_data = vectorizer.inverse_transform(data)

#     # Convert the transformed data to text
#     text_data = []
#     for row in transformed_data:
#         text = " ".join(row)
#         text_data.append(text)

#     return text_data

# # Example usage
# npy_file_path = "spectral_secret.npy"
# original_text_data = [...]  # Provide the original text data used for conversion
# text_data = convert_npy_to_text(npy_file_path, original_text_data)

# # Print the converted text data
# for text in text_data:
#     print(text)



# import numpy as np

# data = np.load('spectral_secret.npy')

# inverse_data = np.fft.ifft(data, axis=0)
# print(inverse_data.shape)



# import numpy as np
# import matplotlib.pyplot as plt

# # Load the .npy file
# data = np.load('spectral_secret.npy')

# # Apply the inverse Fourier transform
# inverse_data = np.fft.ifft(data)

# # Plot the real part of the inverse transformed data
# plt.plot(np.imag(inverse_data))
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Inverse Fourier Transform')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Load the .npy file
# data = np.load('spectral_secret.npy')

# # Apply the inverse Fourier transform
# inverse_data = np.fft.ifftn(data)

# # Plot the real and imaginary parts together
# plt.plot(np.real(inverse_data), label='Real Part')
# plt.plot(np.imag(inverse_data), label='Imaginary Part')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Inverse Fourier Transform')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Load the .npy file
data = np.load('spectral_secret.npy')

# Apply the inverse Fourier transform
inverse_data = np.fft.ifftn(data, axes=(-2, -1))

# Plot the real part
plt.figure()
plt.imshow(np.real(inverse_data), cmap='gray')
plt.colorbar()
plt.title('Real Part')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# # Plot the imaginary part
# plt.figure()
# plt.imshow(np.imag(inverse_data), cmap='gray')
# plt.colorbar()
# plt.title('Imaginary Part')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

plt.show()
