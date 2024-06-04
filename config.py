import tensorflow as tf
from keras import layers


class ImageLayer(layers.Layer):
    def call(self, image: tf.Tensor):
        image_rgb = tf.cast(image, tf.uint8)
        resized_image = tf.image.resize(image_rgb, (224, 224))
        gradient = self.compute_gradient(resized_image)
        noise = self.compute_noise_distribution(resized_image)
        color = self.compute_color_distribution(resized_image)
        laplacian = self.compute_laplacian(resized_image)
        return gradient, noise, color, laplacian

    def compute_gradient(self, image):
        image_gray = tf.image.rgb_to_grayscale(image)
        sobel_x = tf.image.sobel_edges(image_gray)[..., 0]
        sobel_y = tf.image.sobel_edges(image_gray)[..., 1]
        gradient = tf.sqrt(tf.square(sobel_x) + tf.square(sobel_y))
        return gradient

    def compute_noise_distribution(self, image):
        grayscale_image = tf.image.rgb_to_grayscale(image)
        kernel = tf.constant([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=tf.float32)
        kernel = tf.reshape(kernel, [3, 3, 1, 1])
        noise = tf.nn.conv2d(grayscale_image, kernel, strides=[1, 1, 1, 1], padding='SAME')
        return noise

    def get_config(self):
        config = super().get_config()
        return config

    def compute_color_distribution(self, image):
        return tf.image.rgb_to_hsv(image)

    def compute_laplacian(self, image):
        image_gray = tf.image.rgb_to_grayscale(image)
        laplacian = tf.image.sobel_edges(image_gray)[..., 1]
        return laplacian


MODEL_CUSTOM_LAYERS = {
    'ImageLayer': ImageLayer
}