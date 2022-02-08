# Détection automatique de maladies de la rétine par analyse d'image 
*Astrid Nilsson, Corentin Soubeiran*

## Introduction
Les maladies de la rétine constituent une cause majeure de malvoyance. Leurs origines sont variées : elles peuvent être liées au vieillissement, comme la dégénérescence maculaire liée à l’âge (DMLA), être héréditaires, comme la rétinite pigmentaire, ou dériver d’une autre pathologie, comme des complications du diabète (ex: glaucome).
La DMLA est la première cause de malvoyance en France chez les plus de 50 ans en touchant 8% de la population française.*[1]*

Les examens classiques pour l'identification de la DMLA sont le fond de l'oeil et l'imagerie OCT *[2][3]*. Dans les dix dernières années de nombreuses recherches visent à identifier automatiquement la présence de cette maladie de manière automatique *[4][5][6]*

## Projet

Au cours de ce projet nous proposons de réaliser un algorithme d'aide au diagnostic via des images d'OCT permettant la distinction de rétines saines et atteintes de la DMLA. Pour cela nous avons accès à deux bases de données regroupant des images OCT labélisées 2D *[7]* et 3D *[8]*.

Nous tenterons dans un premier temps des approches quantitatives inspirées de *[8]* avant de tenter des approches basées sur des réseaux de neurones à convolution (CNN) comme dans *[5]*. 

Pour cela nous utiliserons la base de donnée d'OCT 3D *[8]* (qui ont l'avantage de fournir un plus grand dataset)que nous prétraiterons pour rentre ces données 2D. Après avoir entrainé et validé nos deux solutions sur ces données, nous évalurons la robustesse de notre algorithme de detection automatique sur les données de *[7]* 2D.

## Calendrier

- Semaine 1 (7/02): Détails du projet, création d'une classe de prétraitement des images, mise en place des bases de données et extraction des données.
- Semaine 2 (14/02): Implémentation de la solution 1.
- Semaine 3 (21/02): Implémentation de la solution 1.
- Semaine 4 (28/02): Implémentation de la solution 2 (CNN).
- Semaine 5 (7/02):  Implémentation de la solution 2 et validation sur second dataset.
- Semaine 6 (14/03): Evaluation orale

## Bases de données:

Voir **README.md** et les différents Jupyter notebook

## Références:

[1]: [Fondation de la recherche médicale, Comprendre les maladies de la rétine](https://www.frm.org/recherches-autres-maladies/maladies-de-la-retine#:~:text=Les%20maladies%20de%20la%20r%C3%A9tine%20constituent%20une%20cause%20majeure%20de,comme%20des%20complications%20du%20diab%C3%A8te.)

[2]: [Ophhtalmic photographers' society: Retinal OCT Imaging](https://www.opsweb.org/page/RetinalOCT)

[3]: [Stanford Medicine: Fundoscopic / Ophthalmoscopic Exam](https://stanfordmedicine25.stanford.edu/the25/fundoscopic.html)

[4]: [Z. Liang, D. W. K. Wong, J. Liu, K. L. Chan and T. Y. Wong, "Towards automatic detection of age-related macular degeneration in retinal fundus images," 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology, 2010](https://ieeexplore.ieee.org/abstract/document/5627289?casa_token=gXOoYKa8wl8AAAAA:rAshN0vRkncLP98Z92Y5rulrp7Y77ZTxxZ7-RJTM7b__sPm8TWyNqIR-zkP1RwPP9ruAAhYnip-V)

[5]: [Apostolopoulos, Stefanos & Ciller, Carlos & De Zanet, Sandro & Wolf, Sebastian & Sznitman, Raphael. (2016). RetiNet: Automatic AMD identification in OCT volumetric data. ](https://www.researchgate.net/publication/309037274_RetiNet_Automatic_AMD_identification_in_OCT_volumetric_data/citation/download)

[6]: [Wang, Yu & Zhang, Yaonan & Yao, Zhaomin & Zhao, Ruixue & Zhou, Fengfeng. (2016). Machine learning based detection of age-related macular degeneration (AMD) and diabetic macular edema (DME) from optical coherence tomography (OCT) images. Biomedical Optics Express. 7. 4928. 10.1364/BOE.7.004928. ](https://www.researchgate.net/publication/310823283_Machine_learning_based_detection_of_age-related_macular_degeneration_AMD_and_diabetic_macular_edema_DME_from_optical_coherence_tomography_OCT_images)

[7]: [Peyman Gholami, Priyanka Roy, Mohana Kuppuswamy Parthasarathy, Vasudevan Lakshminarayanan, "OCTID: Optical Coherence Tomography Image Database", arXiv preprint arXiv:1812.07056, (2018). For more information and details about the database see: https://arxiv.org/abs/1812.07056](https://dataverse.scholarsportal.info/dataverse/OCTID)

[8]: [Farsiu S, Chiu SJ, O'Connell RV, Folgar FA, Yuan E, Izatt JA, Toth CA; Age-Related Eye Disease Study 2 Ancillary Spectral Domain Optical Coherence Tomography Study Group. Quantitative classification of eyes with and without intermediate age-related macular degeneration using optical coherence tomography. Ophthalmology. 2014 Jan;121(1):162-172. doi: 10.1016/j.ophtha.2013.07.013. Epub 2013 Aug 29. PMID: 23993787; PMCID: PMC3901571.](https://pubmed.ncbi.nlm.nih.gov/23993787/)
