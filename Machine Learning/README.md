# Machine Learning
- Our team collect the images dataset from Kaggle for making the model of machine learning and create the dataset for daily skincare recommendation.

- preporcessing the datasets, starts from manual reorganizing images for increasing the accuracy of training model machine learning, reshape, augment, until splitting the images to train_dataset and test_dataset.

- Our team use the sequential model MobileNet for creating the Machine Learning model. MobileNet is one of CNN architecture consists of depthwise separable convolutions, which are lightweight alternatives to standard convolutions. The addional of GlobalAveragePoolid2D to perform spatial pooling over the entire spatial dimensions then reduces the spatial dimensions to a fixed size while preserving important spatial information of the images.

 - To compile the model we use Adam's optimizer for the updated based on the computed gradients during training, categorical_crossentropy's loss for measures the model's performance during training and provides a quantifiable measure of how well the predictions match the actual labels, and accuracy's metric for easures the proportion of correctly predicted samples to the total number of samples.

- In our training we used 100 epocs for reaching the great results. The results we obtained for accuracy is 0.9812, 0.0549 for loss, 0.7817 for validation accuracy and 0.6775. For making sure our results, we evaluated the results and obtained 0.9751983880996704 for training accuracy and 0.07171811163425446 for training loss.

## Model Machine Learning
- Architecture of Mobile Net
  <br><br>
![Contoh Gambar](https://drive.google.com/uc?export=view&id=1e38-1kmkxCaHNcqNK155h627XqWarFqN)
- Model of MobileNet
  <br><br>
![Contoh Gambar]( https://drive.google.com/uc?export=view&id=18QDrM0nN0tx46O0frSok2TjZYgwik5yl)
- Accuracy results of MobileNet
  <br><br>
![Contoh Gambar](https://drive.google.com/uc?id=1xI5gKYc91lxVhq59UR8RPttYsgdfR8NZ)
- Loss results of MobileNet
  <br><br>
![Contoh Gambar](https://drive.google.com/uc?id=17fyRxV0lMtrUvqe3Lw06yggu_G3503Bt)



