These are the experiments for bias measurement for Switch Transformer.
```bash
##For running base Switch Transformer model on SEAT: 
python3 experiments/seat.py --model "SwitchModel" --model_name_or_path="switch-base-8"
##For creating checkpoint for gender bias for Bert Model  for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "gender" 
##For creating checkpoint for race bias for Bert Model  for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "race" 
##For creating checkpoint for religion bias for Bert Model  for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "religion"
##For running sentence debiased Bert model on SEAT, change the bias direction flag depending  on the debiased model, you want to use (this is an examaple of religion debias):
python3 experiments/seat_debias.py --model "SentenceDebiasSwitchModel" --model_name_or_path "switch-base-8" --bias_direction "results/subspace/subspace_m-SwitchModel_c-switch-base-8_t-religion.pt"
##For creating checkpoint for gender bias for Switch Transformer Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "gender"
##For creating checkpoint for race bias for Switch Transformer Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "race"
##For creating checkpoint for religion bias for Switch Transformer Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "SwitchModel" --model_name_or_path "switch-base-8" --bias_type "religion"
##For running INLP debiased Switch Transformer model on SEAT, change the bias direction flag depending  on the debiased model, you want to use (This is an example of gender debias):
python3 experiments/seat_debias.py --model "INLPSwitchModel" --model_name_or_path "switch-base-8" --projection_matrix "/home/lightkhan/bias-bench/results/projection_matrix/projection_m-SwitchModel_c-switch-base-8_t-gender_s-0.pt"
```
These are the experiments for bias measurement for Bert.
```bash
##For running base Bert model on SEAT: 
python3 experiments/seat.py --model "BertModel" --model_name_or_path "bert-base-uncased"
##For creating checkpoint for race bias for Bert Model for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "race" 
##For creating checkpoint for gender bias for Bert Model  for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "gender" 
##For creating checkpoint for religion bias for Bert Model  for SentenceDebias technqiue:
python3 experiments/sentence_debias_subspace.py --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "religion" 
##For running sentence debiased Bert model on SEAT, change the bias direction flag depending  on the debiased model, you want to use (this is an examaple of religion debias):
python3 experiments/seat_debias.py --model "SentenceDebiasBertModel" --model_name_or_path "bert-base-uncased" --bias_direction "results/subspace/subspace_m-BertModel_c-bert-base-uncased_t-religion.pt" 
##For creating checkpoint for gender bias for Bert Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "gender"
##For creating checkpoint for religion bias for Bert Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "religion"
##For creating checkpoint for race bias for Bert Model for INLP technqiue:
python3 experiments/inlp_projection_matrix.py --persistent_dir "." --model "BertModel" --model_name_or_path "bert-base-uncased" --bias_type "race"
##For running INLP debiased Bert model on SEAT, change the bias direction flag depending  on the debiased model, you want to use (This is an example of gender debias):
python3 experiments/seat_debias.py --model "INLPBertModel" --model_name_or_path "bert-base-uncased" --projection_matrix "/results/projection_matrix/projection_m-BertModel_c-bert-base-uncased_t-gender_s-0.pt"
```
These are the experiments for switch transformer running on glue
```bash
##For running switch model on mnli task (change the task for running another task) of glue for Switch Transformer
python3 experiments/run_switch_glue.py --model  "SentenceDebiasBertForSequenceClassification" --model_name_or_path "switch-base-8" --task_name "mnli" --do_train  --do_eval --max_seq_length 128 --learning_rate 2e-5 --num_train_epochs 1 --seed 42 --output_dir "results_sent" --save_strategy  "epoch"
##For running gender debiased switch model on mnli task (change the task for running another task) of glue for Switch Transformer using Sentence Debias technique
python3 experiments/run_switch_glue.py --model  "SentenceDebiasSwitchModel" --model_name_or_path "switch-base-8" --task_name "mnli" --do_train  --do_eval --max_seq_length 1024 --learning_rate 2e-5 --num_train_epochs 1 --seed 42 --output_dir "results_sent" --save_strategy  "epoch" --bias_direction "results/subspace/subspace_m-SwitchModel_c-switch-base-8_t-gender.pt"
```