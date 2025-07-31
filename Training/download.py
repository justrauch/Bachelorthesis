# Hier werden die einzelnen Datensätze von Kaggle heruntergeladen.

import kagglehub

path = kagglehub.dataset_download("siddharthkumarsah/logo-dataset-2341-classes-and-167140-images", path="logos")

print("Path to dataset files:", path)

path = kagglehub.dataset_download("coledie/qr-codes", path="qr_codes")

print("Path to dataset files:", path)

path = kagglehub.dataset_download("volkandl/cartoon-classification", path="unrealistic")

print("Path to dataset files:", path)

path = kagglehub.dataset_download("sunedition/graphs-dataset" path="charts")

print("Path to dataset files:", path)

#For this ignore the Ai generated Images
path = kagglehub.dataset_download("kaustubhdhote/human-faces-dataset" path="portrait")

print("Path to dataset files:", path)
