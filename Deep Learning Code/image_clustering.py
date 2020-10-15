# Imports
import random, cv2, os, sys, shutil
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import keras
import matplotlib.pyplot as plt
import pickle
import tensorflow as tf
import math

class image_clustering:

	def __init__(self, folder_path="data", n_clusters=4, max_examples=None, use_imagenets=False, use_pca=False, feature=None):
		paths = os.listdir(folder_path)

		if feature==None:
			print('Choose a feature!!!')
		else:
			self.feature = feature
		if max_examples == None:
			self.max_examples = len(paths)
		else:
			if max_examples > len(paths):
				self.max_examples = len(paths)
			else:
				self.max_examples = max_examples
		self.n_clusters = n_clusters
		self.folder_path = folder_path
		random.shuffle(paths)
		self.image_paths = paths[:self.max_examples]
		self.use_imagenets = use_imagenets
		self.use_pca = use_pca
		del paths 
		
		for i in range(self.n_clusters):
			os.makedirs(self.feature+"\\Output\\cluster" + str(i))
		os.makedirs(self.feature+"\\Output\\centers")
		print("\n Object of class \"image_clustering\" has been initialized.")

	def load_images(self):
		self.images = []
		for image in self.image_paths:
			self.images.append(cv2.cvtColor(cv2.resize(cv2.imread(self.folder_path + "\\" + image), (224,224)), cv2.COLOR_BGR2RGB))
		self.images = np.float32(self.images)
		self.images /= 255
		print("\n " + str(self.max_examples) + " images from the \"" + self.folder_path + "\" folder have been loaded in a random order.")

	def get_new_imagevectors(self):
		if self.use_imagenets == False:
			self.images_new = self.images
		else:
			if use_imagenets.lower() == "vgg16":
				model1 = keras.applications.vgg19.vgg19(include_top=False, weights="imagenet", input_shape=(224,224,3))
			elif use_imagenets.lower() == "vgg19":
				model1 = tf.keras.applications.vgg19.vgg19(include_top=False, weights="imagenet", input_shape=(224,224,3))
			elif use_imagenets.lower() == "resnet50":
				model1 = keras.applications.resnet50.ResNet50(include_top=False, weights="imagenet", input_shape=(224,224,3))
			elif use_imagenets.lower() == "xception":
				model1 = keras.applications.xception.Xception(include_top=False, weights='imagenet',input_shape=(224,224,3))
			elif use_imagenets.lower() == "inceptionv3":
				keras.applications.inception_v3.InceptionV3(include_top=False, weights='imagenet', input_shape=(224,224,3))
			elif use_imagenets.lower() == "inceptionresnetv2":
				model1 = keras.applications.inception_resnet_v2.InceptionResNetV2(include_top=False, weights='imagenet', input_shape=(224,224,3))
			elif use_imagenets.lower() == "densenet":
				model1 = keras.applications.densenet.DenseNet201(include_top=False, weights='imagenet', input_shape=(224,224,3))
			elif use_imagenets.lower() == "mobilenetv2":
				model1 = keras.applications.mobilenetv2.MobileNetV2(input_shape=(224,224,3), alpha=1.0, depth_multiplier=1, include_top=False, weights='imagenet', pooling=None)
			else:
				print("\n\n Please use one of the following keras applications only [ \"vgg16\", \"vgg19\", \"resnet50\", \"xception\", \"inceptionv3\", \"inceptionresnetv2\", \"densenet\", \"mobilenetv2\" ] or False")
				sys.exit()

			pred = model1.predict(self.images)
			images_temp = pred.reshape(self.images.shape[0], -1)
			if self.use_pca == False: 
				self.images_new = images_temp
			else: 
				model2 = PCA(n_components=None, random_state=728)
				model2.fit(images_temp)
				self.images_new = model2
			with open(self.feature + "\\im_"+self.feature+".txt", "wb") as fp:   # Unpickling
				pickle.dump(self.images_new, fr, protocol=4)

	def clustering(self):
			clusters=[]
			with open(self.feature + "\\im_"+self.feature+".txt", "rb") as fp:   # Unpickling
				self.images_new = pickle.load(fp)

			if self.use_pca == True:  
				model2 = PCA(n_components=2, random_state=728)
				self.images_new = model2.fit_transform(self.images_new)
				#self.images_new = model2
			model = KMeans(n_clusters=self.n_clusters, n_jobs=-1, random_state=728)
			model.fit(self.images_new)
			im=self.images_new
			predictions = model.predict(self.images_new)
			centers=model.cluster_centers_


			with open(self.feature + "\\pred_"+str(self.n_clusters)+".txt", "wb") as fr:   #Pickling
				pickle.dump(predictions, fr, protocol=4)

			with open(self.feature + "\\center_"+str(self.n_clusters)+".txt", "wb") as fq:   #Pickling
				pickle.dump(centers, fq, protocol=4)

			print(centers)

			print('Clustering...')
			print('FFF')        
			
			
			#plt.scatter(pca_centers[:,0], pca_centers[:,1], c='black', s=100)
			
			ind=0
			
			for i in range(self.n_clusters):
				clusters.append(im[predictions == i,:])	
			print(len(clusters))
			cent=[0]*self.n_clusters
			minn=[10000]*self.n_clusters
			for i in range(len(clusters)):
				for j in self.images_new:
					dist = math.sqrt((j[0]-centers[i][0])**2 + (j[1]-centers[i][1])**2 )
					if dist<minn[i]:
						minn[i]=dist
						cent[i]=tuple(j)
						
				#shutil.copy2(r'C:\Users\tapan\Downloads\sih\FACE_Resized\FACE_Resized'+"\\"+self.image_paths[ind], self.feature + '\\output\\centers')
				#os.rename(self.feature + "\\output\\centers\\"+self.image_paths[ind], self.feature + '\\output\\centers\\center_'+str(i)+'.jpg')

			print(len(cent))
			cs=[]
			for i in range(self.max_examples):
				if tuple(self.images_new[i]) in cent and predictions[i] not in cs:
					cs.append(predictions[i])
					print(i)
					print('cntr')
					print(self.images_new[i])
					print(cent.index(tuple(self.images_new[i])))
					shutil.copy2(r'sih\FACE_Resized\FACE_Resized'+"\\"+self.image_paths[i], self.feature + '\\output\\centers')
					os.rename(self.feature + "\\output\\centers\\"+self.image_paths[i], self.feature + '\\output\\centers\\center_'+str(cent.index(tuple(self.images_new[i])))+'_'+self.image_paths[i]+'.jpg')
				shutil.copy2(r'sih\FACE_Resized\FACE_Resized'+"\\"+self.image_paths[i],  self.feature + "\\Output\\cluster"+str(predictions[i])+'\\')
                


if __name__ == "__main__":

	print("\n\n \t\t START\n\n")

	feature= 'eye_brows' 	# choose from: 'eyes','eye_brows','nose','lips','face'

	number_of_clusters = 5 

	data_path = r"sih\BlackBackgroundEyebrows\BlackBackgroundEyebrows" 

	max_examples = None # number of examples to use, if "None" all of the images will be taken into consideration for the clustering
	

	use_imagenets = "DenseNet"
	# choose from: "Xception", "VGG16", "VGG19", "ResNet50", "InceptionV3", "InceptionResNetV2", "DenseNet", "MobileNetV2" and "False", Default is: False
	

	if use_imagenets == False:
		use_pca = False
	else:
		use_pca = True 

	temp = image_clustering(data_path, number_of_clusters, max_examples, use_imagenets, use_pca, feature)
	temp.load_images()
	temp.get_new_imagevectors()
	temp.clustering()

	print("\n\n\t\t END\n\n")