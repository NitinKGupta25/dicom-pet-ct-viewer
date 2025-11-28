import pydicom
import numpy as np
import os

class DICOMLoader:
    def __init__(self, directory):
        self.directory = directory
        self.dataset = None

    def load_dicom_files(self):
        dicom_files = [f for f in os.listdir(self.directory) if f.endswith('.dcm')]
        if not dicom_files:
            raise FileNotFoundError('No DICOM files found in the specified directory.')
        # Load the first DICOM file to initialize the dataset
        self.dataset = pydicom.dcmread(os.path.join(self.directory, dicom_files[0]))
        return self.dataset

    def get_pixel_array(self):
        if self.dataset is None:
            raise ValueError('DICOM files not loaded. Call load_dicom_files() first.')
        return self.dataset.pixel_array

    def get_metadata(self):
        if self.dataset is None:
            raise ValueError('DICOM files not loaded. Call load_dicom_files() first.')
        return {tag: getattr(self.dataset, tag, None) for tag in self.dataset.keys()}

# Example usage:
# loader = DICOMLoader(directory='./dicom_files')
# dataset = loader.load_dicom_files()
# pixel_array = loader.get_pixel_array()
# metadata = loader.get_metadata()