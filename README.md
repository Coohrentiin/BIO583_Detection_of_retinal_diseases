# BIO583_Detection_of_retinal_diseases
*Retinal fundoscopy or OCT image processing for early detection of retinal diseases such as  diabetic retinopathy or AMD. Project by Astrid Nilsson and Corentin Soubeiran* 

## Project: 

2 idées principales:
- Travailler sur des données OCT pour distinguer les cornée pathologique atteinte de DMLA (AMD) et les cornées saines. Deux approches peuvent être envisagées:
	- Quantitative, en travaillant sur des mesures géométriques et statistiques 
	- Par "IA" utiliser par exemple des CNN comme classificateurs

	Deux dataset suite à nos recherches semblent propices:
	- OCTID, 2DOCT: assez leger en terme de volume avec des images OCT en 2D.
	- Duke 3DOCT: plus lourd avec des images en volume qui demandera sans doute un pré-traitement mais dont les données sont plus "brute"
	
	Quelques image de ces bases de données sont donné dans le dossier *data* et des jupiter_nootbook d'exemple de donnée se trouvent dans le dossier principal.
- Travailler sur des images de fond de l'oeil (fundus). Ce travail permettrait également de concevoir un classificateur pour distinguer les cornées saines et pathologique comme cataract et glaucome. Pour cela suite à nos recherche la base de donnée la plus propice semble être Kaggle Fundus. Encore une fois plusieurs approches possibles
	- Quantitatif avec un analyse de texture 
	- Via IA et CNN
	Quelques images sont donnée à titre d'exemple dans le dossier *data* et un jupiter_nootbook d'exemple de donnée se trouvent dans le dossier principal.

## Dataset research
*Motivations:* https://retinatoday.com/articles/2007-nov/1107_03-php

*Exemples of studies:* 
- Based on CNN with fundus images: https://www.degruyter.com/document/doi/10.1515/comp-2020-0177/html
- Based on VGG16 with OCT images https://pubmed.ncbi.nlm.nih.gov/30610422/

*DATASET:*
a lot of them from: https://www.thelancet.com/journals/landig/article/PIIS2589-7500(20)30240-5/fulltext

- Fundus: 15 images of healthy patients, 15 images of patients with diabetic retinopathy and 15 images of glaucomatous patients.
https://www5.cs.fau.de/research/data/fundus-images/

- Fundus: 3200 images captured using three different fundus cameras with 46 conditions annotated through adjudicated consensus of two senior retinal experts.
https://ieee-dataport.org/open-access/retinal-fundus-multi-disease-image-dataset-rfmid
https://www.kaggle.com/c/aptos2019-blindness-detection/data

- **Kaggle Fundus**: 300 healthy, 100 cataract, 100 glaucoma, 100 other retinal diseases.
https://www.kaggle.com/jr2ngb/cataractdataset
	> See example

- Fundus and 3D-OCT: 22 images from random patient
https://sites.google.com/site/hosseinrabbanikhorasgani/datasets-1/vessel-reg-oct-fundus

- 3D-OCT: 800 images : normal vs glaucoma
https://zenodo.org/record/1481223#.Xr06Q2gzbIU

- **TaeKeun** Fundus and OCT: 59 normal eyes, 26 drusens, and 98 AMD eyes including both OCT and matched fundus images were obtained.
https://data.mendeley.com/datasets/2wxnrd832j/1
	> See dataset: images not adapted for a study

- **Duke** 3DOCT: Individual SDOCT images and marking: 38400 BScans from 269 AMD patients and 115 normal subjects
https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm
	> See example

- **OCTID, 2DOCT**: 470 images: age-related macular degeneration (57), macular hole (104), central serous retinopathy (109), healthy eyes (208)
https://dataverse.scholarsportal.info/dataverse/OCTID
	> See example


## Documentation

- Clinical OCT for retina imaging: https://www.opsweb.org/page/RetinalOCT
- Fundoscopy: https://stanfordmedicine25.stanford.edu/the25/fundoscopic.html
