* what is sign language?
    * how sign language communication works?
    * important of sign language in field of machine leanring?

* how sign language work?
    * how sign language work using deep neural network?
    ![image](img/how_sign_langauge_work.jpg)

* our challenge that we should do it to get good real-time sign langauge recognition?
    1. collecting good dataets:
        * our dataset collection containing:
            * 14,500 sign image for each class
            * 623,500 sign for all classes
            ![image](img/label_count.png)

    2. cleaning the dataset:
        * dataset cleaned using manuall cleaning by finding wrong sign or wrong label and removing it or correct it by moving it to the right label.
    
    3. landmark the image:
        * landmarking the hand collecting using open source tool mediapipe.
        ![iamge](img/hand_landmark.png)

    4. finding good model for our dataset:
        * our choice for training the model is CNN (Convusion Neural Network)

        * model accuracy
        ![image](img/model2_accl.png)

        * confusion matrix for my big model
        ![image](img/big_model_confusion_matrix.png)

        * confusion matrix for tflite
        ![image](img/tflite_model_confusion_matrix.png)

        * most wrong hand:
        ![image](img/wrong_hand.png)

* conclusion
    * talk about the summary of the work.

* feature work
    * talk about this idea that you have in the feature of your research
    