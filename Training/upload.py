# Hier kannst du das trainierte Modell in deinen Huggingface-Account hochladen.
# Du musst dafür deinen HUGGING_FACE_TOKEN angeben.
# Ändere 'repo_id' auf den gewünschten Namen deines Modells,
# und passe 'best_model_folder' an, falls du das Modell in einem anderen Verzeichnis gespeichert hast.

from huggingface_hub import login
from transformers import ViTForImageClassification, ViTImageProcessor

login(token=os.getenv("HUGGING_FACE_TOKEN"))

best_model_folder = "./vit_output/best_model"

model = ViTForImageClassification.from_pretrained(best_model_folder)
processor = ViTImageProcessor.from_pretrained(best_model_folder)

repo_id = "JustinStrauch/vit_fit_v3"

model.push_to_hub(repo_id)
processor.push_to_hub(repo_id)