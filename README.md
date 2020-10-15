# MS342_SunEater
The official repo of the team SunEater for SIH2020 PS:MS342. Problem statement: App based Portrait building system.

### Data Preprocessing
The folder Data-Preprocessing contains the code of various preprocessing layers we applied in order to increase the accuracy.
The techniques used are : 
* Face-Alignment - Straightening the faces in the dataset
* Extracting feature points from the face
* Extracting the co-ordinates of all the features from the face(i.e Eyes,Nose,Lips,Eyebrows,etc)
* Extracting the shapes of the features to be used for clustering
* Generating a portrait to be used in the backend

### Front-End
The Front-End of this project was build using React.js
This Directory contains the code of the UI that was designed by the team and integrated with backend

### Back-End
The Back-End API was build using flask that was called from the react-app.
The API generates a dynamic image based on the selection of the user from the front end

### Deep Learning Code
This directory contains the code that was used to cluster teh dataset into various clusters.
Detailed analysis can be found in the jupyter notebook



