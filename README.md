# Not-Vada-Pav
Deep image Classification for Vada Pav or Not with LesNet:

1.Data Collection
* Images of Vada pav are being searched in Google Images and scrolled through the desired number of images.
* The Google_img_url_extractor.js is run on the console of the browser which extracts a urls.txt from the browser for image urls.
* The Vada pav images are downloaded with a python script(down_img.py) with urllib.request module.
* The negative images are taken from VOC2012 dataset. 

2.Data Augmentation
* The Vada Pav images are stored under images/VadaPav folder
* The not Vada Pav images are stored under images/Not_VadaPav folder

3.Training the Model
* The model is trained using the images dataset created with two folders.
* The model is saved as vadapav_not_vadapav.model
* The train network script (train_network.py) trains the model with the data split with 25% of test data.
* The losses and accuracy of the epoches are saved in plot.png as a graph.
* The test_network.py is used to evaluate the model by using images in the example folder and providing a output with "_result" at the end of the filename at the same folder.
