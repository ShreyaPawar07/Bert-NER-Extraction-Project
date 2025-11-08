import transformers

MAX_LEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS =10
BASE_MODEL_PATH = "../bert+base_uncased"
MODEL_PATH = "model.bin"
TRAINING_FILE ="''ner_dataset.csv/ner_dataset.csv"
TOKENZIER = transformers.BertTokenizer.from_pretrained(BASE_MODEL_PATH , do_lower_case = True)