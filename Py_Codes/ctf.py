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
