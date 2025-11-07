import unittest
# Import the function from the package you created
from EmotionDetection.emotion_detection import emotion_detector 

class TestEmotionDetection(unittest.TestCase):
    """
    Unit test class for the emotion_detector function.
    """

    def test_emotion_detector(self):
        """
        Tests the emotion_detector function against the required statements and 
        expected dominant emotions.
        """
        # Test Case 1: joy
        text_1 = "I am glad this happened"
        result_1 = emotion_detector(text_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy', 
                         f"Test 1 failed for: {text_1}. Got: {result_1['dominant_emotion']}")

        # Test Case 2: anger
        text_2 = "I am really mad about this"
        result_2 = emotion_detector(text_2)
        self.assertEqual(result_2['dominant_emotion'], 'anger', 
                         f"Test 2 failed for: {text_2}. Got: {result_2['dominant_emotion']}")

        # Test Case 3: disgust
        text_3 = "I feel disgusted just hearing about this"
        result_3 = emotion_detector(text_3)
        self.assertEqual(result_3['dominant_emotion'], 'disgust', 
                         f"Test 3 failed for: {text_3}. Got: {result_3['dominant_emotion']}")

        # Test Case 4: sadness
        text_4 = "I am so sad about this"
        result_4 = emotion_detector(text_4)
        self.assertEqual(result_4['dominant_emotion'], 'sadness', 
                         f"Test 4 failed for: {text_4}. Got: {result_4['dominant_emotion']}")

        # Test Case 5: fear
        text_5 = "I am really afraid that this will happen"
        result_5 = emotion_detector(text_5)
        self.assertEqual(result_5['dominant_emotion'], 'fear', 
                         f"Test 5 failed for: {text_5}. Got: {result_5['dominant_emotion']}")
        
        # Optional: Test for non-empty output structure and valid scores
        self.assertIn('anger', result_1, "Result missing 'anger' key")
        self.assertIsInstance(result_1['joy'], float, "Joy score is not a float")

# Standard way to run the tests when executing the file
if __name__ == '__main__':
    unittest.main()