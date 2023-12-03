import matplotlib.pyplot as plt

def read_image(filename):
    """
    Membaca berkas gambar dan mengembalikan array tiga dimensi.

    Parameters:
    - filename (str): Nama gambar:

    Returns:
    - image_array (numpy.ndarray): Array tiga dimensi yang mewakili gambar.
    
    """
    image_array = plt.imread(filename)
    return image_array

def image_to_ascii(filename):
    """
    Mengambil salah satu channel dari gambar, misalnya channel merah.
    nilai dalam channel tersebut diubah ke skala nilai antara 0 dan 1,
    dengan membaginya dengan 225
    """
    arr_moai = read_image(filename)

    arr_moai_red_channel = arr_moai[1, 1, 0]
    arr_moai_red_channel = arr_moai_red_channel / 225.0

    return arr_moai_red_channel

filename = "images.jpeg"
red_channel_array = image_to_ascii(filename)

print("Ukuran array channel merah:", red_channel_array.shape)