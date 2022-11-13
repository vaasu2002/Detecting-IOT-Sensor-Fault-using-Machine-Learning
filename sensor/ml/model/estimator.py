# importing dependencies

#from sensor.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import os



class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        """
        Returns:
            dict: {'neg': 0, 'pos': 1}
        """
        return self.__dict__ 

    def reverse_mapping(self):
        """
        Returns:
            dict: {0: 'neg', 1: 'pos'}
        """
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


class SensorModel:
    """
    Will be used to evaluate model
    """
    pass