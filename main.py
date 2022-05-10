from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%
class NFT():
	def __init__(self):

		self.background = ['Black','Purple','DarkPurple','Pink','PinkRed','Orange','LightOrange','YellowGreen','DarkBlueGreen','Gray','WhiteGray',
'WhiteBlue','Rainbow','PurpleRainbow','PinkBlue','BlueViolet','ClearYellow','PurpleYellow','ClearRed','ClearBlueYellow']
		self.background_weights = [5,12,5,12,5,12,5,8,3,6,5,3,2,2,5,5,1,2,1,1]
		self.background_files = {
		    "Black": "bg1",
		    "Purple": "bg2",
		    "DarkPurple": "bg3",
		    "Pink": "bg4",
		    "PinkRed": "bg5",
		    "Orange": "bg6",
		    "LightOrange": "bg7",
		    "YellowGreen": "bg8",
		    "DarkBlueGreen": "bg9",
		    "Gray": "bg10",
		    "WhiteGray": "bg11",
		    "WhiteBlue": "bg12",
		    "Rainbow": "bg13",
		    "PurpleRainbow": "bg14",
		    "PinkBlue": "bg15",
		    "BlueViolet": "bg16",
		    "ClearYellow": "bg17",
		    "PurpleYellow": "bg18",
		    "ClearRed": "bg19",
		    "ClearBlueYellow": "bg20"
		}
		self.background_count = {} 

		self.face = ["White", "Black"]
		self.face_weights = [60, 40]
		self.face_files = {
    		"White": "face1",
    		"Black": "face2"
		}
		self.face_count = {}


		self.ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
		self.ears_weights = [25, 30, 44, 1]
		self.ears_files = {
		    "No Earring": "ears1",
		    "Left Earring": "ears2",
		    "Right Earring": "ears3",
		    "Two Earrings": "ears4"
		}
		self.ears_count = {}


		self.eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
		self.eyes_weights = [70, 10, 5 , 1 , 14]
		self.eyes_files = {
		    "Regular": "eyes1",
		    "Small": "eyes2",
		    "Rayban": "eyes3",
		    "Hipster": "eyes4",
		    "Focused": "eyes5"     
		}
		self.eyes_count = {}


		self.hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair','Thin Hair','Bald','Blonde Hair','Caret Hair','Pony Tails']
		self.hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]
		self.hair_files = {
		    "Up Hair": "hair1",
		    "Down Hair": "hair2",
		    "Mohawk": "hair3",
		    "Red Mohawk": "hair4",
		    "Orange Hair": "hair5",
		    "Bubble Hair": "hair6",
		    "Emo Hair": "hair7",
		    "Thin Hair": "hair8",
		    "Bald": "hair9",
		    "Blonde Hair": "hair10",
		    "Caret Hair": "hair11",
		    "Pony Tails": "hair12"
		}
		self.hair_count = {}   


		self.mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
		self.mouth_weights = [10, 10,50, 10,15, 5]
		self.mouth_files = {
		    "Black Lipstick": "m1",
		    "Red Lipstick": "m2",
		    "Big Smile": "m3",
		    "Smile": "m4",
		    "Teeth Smile": "m5",
		    "Purple Lipstick": "m6"
		}
		self.mouth_count = {}


		self.nose = ['Nose', 'Nose Ring']
		self.nose_weights = [90, 10]
		self.nose_files = {
		    "Nose": "n1",
		    "Nose Ring": "n2"   
		}
		self.nose_count = {}


		self.beard = ['Nothing','GingerHipster', 'ThinBlack','BlackMustache','BlackBeard']
		self.beard_weights = [40, 5, 20, 15, 20]
		self.beard_files = {
		    "Nothing": "beard1",
		    "GingerHipster": "beard2",
		    "ThinBlack": "beard3",
		    "BlackMustache": "beard4",
			"BlackBeard": "beard5"
		}
		self.beard_count = {}
		

		self.access = ['Nothing','Cigarette', 'Pipe']
		self.access_weights = [60,20,20]
		self.access_files = {
			"Nothing": "acc1",
    		"Cigarette": "acc2",
    		"Pipe": "acc3"
		}
		self.access_count = {}


		self.all_images = [] 
		self.savePath = "./col4/"

	#def addProperty():

	def generate(self,count):
		for i in range(count):
			new_image = {} #

		    # For each trait category, select a random trait based on the weightings
			new_image ["Background"] = random.choices(self.background, self.background_weights)[0]
			new_image ["Face"] = random.choices(self.face, self.face_weights)[0]
			new_image ["Ears"] = random.choices(self.ears, self.ears_weights)[0]
			new_image ["Eyes"] = random.choices(self.eyes, self.eyes_weights)[0]
			new_image ["Hair"] = random.choices(self.hair, self.hair_weights)[0]
			new_image ["Mouth"] = random.choices(self.mouth, self.mouth_weights)[0]
			new_image ["Nose"] = random.choices(self.nose, self.nose_weights)[0]
			new_image ["Beard"] = random.choices(self.beard, self.beard_weights)[0]
			new_image ["Access"] = random.choices(self.access, self.access_weights)[0] 
		    
			if new_image in self.all_images:
				return NFT.generate(self,count)
			else:
				self.all_images.append(new_image)
				count-=1


	# Returns true if all images are unique
	def isCollectionUnique(self):
		seen = list()
		return not any(i in seen or seen.append(i) for i in self.all_images)

	def addToken(self):
		# Add token Id to each image
		i = 0
		for item in self.all_images:
		    item["tokenId"] = i
		    i = i + 1

	def getTraitCount(self):
		for item in self.background:
		    self.background_count[item] = 0

		for item in self.face:
		    self.face_count[item] = 0

		for item in self.ears:
		    self.ears_count[item] = 0

		for item in self.eyes:
		    self.eyes_count[item] = 0    
		
		for item in self.hair:
		    self.hair_count[item] = 0

		for item in self.mouth:
		    self.mouth_count[item] = 0    
		
		for item in self.nose:
		    self.nose_count[item] = 0

		for item in self.beard:
		    self.beard_count[item] = 0
		
		for item in self.access:
		    self.access_count[item] = 0


		for image in self.all_images:
			self.background_count[image["Background"]] += 1
			self.face_count[image["Face"]] += 1
			self.ears_count[image["Ears"]] += 1
			self.eyes_count[image["Eyes"]] += 1
			self.hair_count[image["Hair"]] += 1
			self.mouth_count[image["Mouth"]] += 1
			self.nose_count[image["Nose"]] += 1
			self.beard_count[image["Beard"]] += 1
			self.access_count[image["Access"]] += 1

		print(self.background_count)
		print(self.face_count)
		print(self.ears_count)
		print(self.eyes_count)
		print(self.hair_count)
		print(self.mouth_count)
		print(self.nose_count)
		print(self.beard_count)
		print(self.access_count)  

		for item in self.all_images:

			im1 = Image.open(f'./scripts/background/{self.background_files[item["Background"]]}.png').convert('RGBA')
			im2 = Image.open(f'./scripts/face_parts/face/{self.face_files[item["Face"]]}.png').convert('RGBA')
			im3 = Image.open(f'./scripts/face_parts/eyes/{self.eyes_files[item["Eyes"]]}.png').convert('RGBA')
			im4 = Image.open(f'./scripts/face_parts/ears/{self.ears_files[item["Ears"]]}.png').convert('RGBA')
			im5 = Image.open(f'./scripts/face_parts/hair/{self.hair_files[item["Hair"]]}.png').convert('RGBA')
			im6 = Image.open(f'./scripts/face_parts/mouth/{self.mouth_files[item["Mouth"]]}.png').convert('RGBA')
			im7 = Image.open(f'./scripts/face_parts/nose/{self.nose_files[item["Nose"]]}.png').convert('RGBA')
			im8 = Image.open(f'./scripts/face_parts/beard/{self.beard_files[item["Beard"]]}.png').convert('RGBA')
			im9 = Image.open(f'./scripts/face_parts/access/{self.access_files[item["Access"]]}.png').convert('RGBA')

		    #Create each composite
			com1 = Image.alpha_composite(im1, im2)
			com2 = Image.alpha_composite(com1, im3)
			com3 = Image.alpha_composite(com2, im4)
			com4 = Image.alpha_composite(com3, im5)
			com5 = Image.alpha_composite(com4, im6)
			com6 = Image.alpha_composite(com5, im7)
			com6 = Image.alpha_composite(com6, im8)                 
			com7 = Image.alpha_composite(com6, im9) 
		    #Convert to RGB
			rgb_im = com7.convert('RGB')
			file_name = str(item["tokenId"]+1) + ".png"
			rgb_im.save(self.savePath + file_name)

nft = NFT()
nft.generate(500)
nft.isCollectionUnique()
nft.addToken()
print("Are all images unique?",nft.isCollectionUnique())  
nft.getTraitCount()