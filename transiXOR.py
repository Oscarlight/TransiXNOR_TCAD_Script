
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

label_size = 12
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['ytick.labelsize'] = label_size 
mpl.rcParams['figure.figsize'] = 12, 12

def sqResize(image, outwidth):
    # ny, nx = image.shape
    # print("width: %i, and length: %i" %(ny, nx))
    # tmp_min = np.min(image)
    # tmp_max = np.max(image)
    # print(image)
    # image = 2*(image - tmp_min)/(tmp_max - tmp_min + 1e-16)-1
    # print(image)
    log_image = np.log10(np.abs(image))
    abs_image = np.abs(image)
    out_image = resize(log_image, [outwidth, outwidth])
    # print(outimage)
    # outimage = (outimage + 1)/2*(tmp_max - tmp_min) + tmp_min
    # print(outimage)
    # ny, nx = outimage.shape
    # print("width: %i, and length: %i" %(ny, nx))
    return out_image

# data = np.float32(np.load('vds_vbg_vtg_id_D2.npy'))
data = np.load('vds_vbg_vtg_id_D2.npy')
numVds, numVbg, numVtg = data.shape
# print(numVds)
# print(numVbg)
# print(numVtg)
nRow = 3; nCol = 3; figsize = 8
# vds as z
#
## test plot
# idx = 35
# I = sqResize(data[idx, :, :], 41)
# fig, ax = plt.subplots(figsize=(6,6))
# # # idx/40 scale for Vds (see genData)
# # ax.imshow(I, vmin=0, vmax=255*(idx/40), origin='lower', interpolation = 'gaussian')
# ax.imshow(I, origin='lower', interpolation = 'gaussian')
# plt.show()


##
# ax = plt.subplot(nRow, nCol, 1)
# img = sqResize(data[, :, :], 41)
# plt.imshow(img, vmin = 0, vmax = 255*(i/90.), origin='lower', interpolation = 'gaussian')
# plt.title('Vds = {0:.2f} V'.format(vds), fontsize = label_size)
# plt.ylabel('Vbg (V)', fontsize = label_size)
# plt.xlabel('Vtg (V)', fontsize = label_size)
# plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
# ax.set_xticklabels([0.0, 0.0, 0.2, 0.4])
# ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])

# for i, vds in enumerate(np.linspace(0.24, 0.4, 9)):
#     ax = plt.subplot(nRow, nCol, i + 1)
#     i = 2 * i + 24
#     # print(i)
#     img = sqResize(data[i, :, :], 41)
#     # plt.imshow(img, vmin = 0, vmax = 255*(i/41.), origin='lower', interpolation = 'gaussian')
#     plt.imshow(img, origin='lower', interpolation='gaussian')
#     plt.title(r'$V_{DS}$' + ' = {0:.2f} V'.format(vds), fontsize = label_size)
#     plt.ylabel(r'$V_{BG}$ (V)', fontsize = label_size)
#     plt.xlabel(r'$V_{TG}$ (V)', fontsize = label_size)
#     plt.subplots_adjust(wspace = 0.0, hspace = 0.35)
#     ax.set_xticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])
#     ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])
#
# plt.savefig('figure_log.pdf')
# plt.show()

# for i, vds in enumerate(np.linspace(0.24, 0.4, 9)):
index = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 38, 40]
voltage = [0.00, 0.04, 0.08, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36, 0.38, 0.40]
i = 0
for index, vds in zip(index, voltage):
    # ax = plt.subplot(nRow, nCol, i + 1)
    # i = 2 * i + 24
    ax = plt.subplot(4, 3, i+1)
    i += 1
    # print(i)
    img = sqResize(data[index, :, :], 41)
    cax = plt.imshow(img, vmin = -13, vmax = -9, origin='lower', interpolation = 'gaussian')
    # plt.imshow(img, origin='lower', interpolation='gaussian')
    plt.title(r'$V_{DS}$' + ' = {0:.2f} V'.format(vds), fontsize = label_size)
    plt.ylabel(r'$V_{BG}$ (V)', fontsize = label_size)
    plt.xlabel(r'$V_{TG}$ (V)', fontsize = label_size)
    cbar = plt.colorbar(cax, ticks=[-13.0, -12.0, -11.0, -10.0, -9.0])
    cbar.ax.set_yticklabels([r'$10^{-7}$', r'$10^{-6}$', r'$10^{-5}$', r'$10^{-4}$', r'$10^{-3}$'], fontsize = label_size)
    plt.subplots_adjust(wspace = 0.3, hspace = 0.55)
    ax.set_xticklabels([0.0, 0.0, 0.2, 0.4])
    ax.set_yticklabels([0.0, 0.0, 0.2, 0.4])

plt.savefig('figure_log_original.pdf')
plt.show()
# for i, vds in enumerate(np.linspace(0, 0.4, numVds)):
#   ax = plt.subplot(nRow, nCol, i + 1)
#   img = sqResize(data[:, i, :], 41)
#   plt.imshow(img, vmin = 0, vmax = 255, origin='lower',interpolation = 'gaussian')
#   plt.title('Vbg = {0:.2f} V'.format(vds), fontsize = label_size)
#   plt.ylabel('Vds (V)', fontsize = label_size)
#   plt.xlabel('Vtg (V)', fontsize = label_size)
#   plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
#   ax.set_xticklabels([0.0, 0.0, 0.2, 0.4])
#   ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])

# plt.savefig('figure2.pdf')
