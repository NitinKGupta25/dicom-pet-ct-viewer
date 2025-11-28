import numpy as np
import matplotlib.pyplot as plt

class VolumeRenderer:
    def __init__(self, volume_data):
        self.volume_data = volume_data

    def render(self, angle=0):
        # Set up the rendering parameters
        depth = self.volume_data.shape[0]
        height = self.volume_data.shape[1]
        width = self.volume_data.shape[2]
        # Create an image to render the volume
        image = np.zeros((height, width))

        for h in range(height):
            for w in range(width):
                # Perform ray casting
                ray_intensity = 0
                for d in range(depth):
                    intensity = self.volume_data[d, h, w]
                    ray_intensity += intensity
                image[h, w] = ray_intensity

        plt.imshow(image, cmap='gray')
        plt.title('3D Volume Rendering using Ray Casting')
        plt.axis('off')
        plt.show()

# Example usage
if __name__ == '__main__':
    # Assuming volume_data is a 3D numpy array containing the volume
    volume_data = np.random.rand(100, 256, 256)  # Dummy data for demonstration
    renderer = VolumeRenderer(volume_data)
    renderer.render()