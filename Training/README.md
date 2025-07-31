# Start

First, install all required libraries:
```bash
cd /bachelorthesis/Bachelorthesis/Training
pip install -r requirements.txt
```

# To download the datasets used for training the model, follow the instructions below:

To get the TableBank dataset in a WSL or Linux environment, use the following commands. These will download the dataset in multiple parts, merge them, and unzip the final archive:

```bash
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.001
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.002
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.003
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.004
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.005

cat TableBank.zip.001 TableBank.zip.002 TableBank.zip.003 TableBank.zip.004 TableBank.zip.005 > TableBank.zip
unzip TableBank.zip -d TableBank
```

# For the charts, logos, unrealistic images, and QR code datasets, run the following script:

``` python
cd bachelorthesis/Bachelorthesis/Datasets/
python3 download.py
```

# To download the infographics dataset, visit the official website of the competition:

Go to https://rrc.cvc.uab.es/?ch=17&com=downloads

Sign up or log in

Scroll down to “Task 3 – Infographics VQA”

Click the hyperlink labeled “images” to start the download

then

```bash
cd /path/to/the/folder/where/the/file/is
tar -xzf infographicsvqa_images.tar.gz -C /path/to/target/folder
```

# Finally, to download the realistic images dataset (from OpenImages), run the following script:

```python
cd bachelorthesis/Bachelorthesis/Datasets/
python3 openimages.py
```
These datasets are required for training and evaluating the model on visual content classification tasks.

# Bachelor Thesis – Vision Transformer Workflow

## Assemble the Dataset

To assemble the final dataset, use the script `split.py`:

Run it with: 
```bash 
python3 split.py <preferred_label_name> <target_folder_name> 
``` 

This script will split the images into `train`, `val`, and `test` sets. 

Run the training process for all downloaded folders or for any specific labels you want to include.
--- 

## Train the Model 

To train the model, use: 
``` 
\\bachelorthesis\\Bachelorthesis\\Training\\train.py 
``` 

It uses the data created by `split.py`. After training, a folder named `vit_output` will be created containing all model checkpoints. 

To upload the model to Hugging Face, use the script: 
``` 
\\bachelorthesis\\Bachelorthesis\\Training\\upload.py 
``` 

Make sure to: 

1. Adjust the folder name. 
2. Add your Hugging Face token to the `.env` file: 
```env 
HUGGING_FACE_TOKEN=<Your Token> 
``` 

Or use the \bachelorthesis\Bachelorthesis\Training\Jupiter_Notebook.ipynb and enter your hugging_face und wandsandbiases tokens
--- 

## Test the Model 

To test the model, run: 

``` 
\\bachelorthesis\\Bachelorthesis\\Training\\test.py
``` 

It will use the test data located in: 
``` 
\\bachelorthesis\\Bachelorthesis\\Training\\data\\test 
``` 

Make sure the model name matches the folder or your Hugging Face repo. 
--- 

## Optional Image Testing 

If you want to test the model with your own images: 

1. Use the script: 
``` 
\\bachelorthesis\\Bachelorthesis\\Training\\get_images.py 
``` 

Set the zip_path parameter to the location of your ZIP folder.
The ZIP folder should contain only PDF files.
The script will extract all images from all PDFs in the folder.

2. Then run: 
``` 
\\bachelorthesis\\Bachelorthesis\\Training\\model_sort.py 
``` 
This will create a `sample` folder and automatically sort the images into subfolders based on the model's predictions. 

