import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy_emotion(self):
        sentence = "I am glad this happened"
        dominant_emotion = "joy"
        self.assertEqual(emotion_detector(sentence)['dominant_emotion'], dominant_emotion)

    def test_anger_emotion(self):
        sentence = "I am really mad about this"
        dominant_emotion = "anger"
        self.assertEqual(emotion_detector(sentence)['dominant_emotion'], dominant_emotion)

    def test_disgust_emotion(self):
        sentence = "I feel disgusted just hearing about this"
        dominant_emotion = "disgust"
        self.assertEqual(emotion_detector(sentence)['dominant_emotion'], dominant_emotion)

    def test_sadness_emotion(self):
        sentence = "I am so sad about this"
        dominant_emotion = "sadness"
        self.assertEqual(emotion_detector(sentence)['dominant_emotion'], dominant_emotion)

    def test_fear_emotion(self):
        sentence = "I am really afraid that this will happen"
        dominant_emotion = "fear"
        self.assertEqual(emotion_detector(sentence)['dominant_emotion'], dominant_emotion)

    
if __name__ == '__main__':
    unittest.main()
