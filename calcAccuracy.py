import json

# Read from file 1
with open('inlp_switch_religion.json', 'r') as file:
    data_switch = json.load(file)
    # print(data_switch)

# Read from file 2
with open('inlp_bert_religion.json', 'r') as f:
    data_bert = json.load(f)

switch_better_pval = 0
switch_better_effect = 0
total = 0


sum_effect_switch = 0
sum_effect_bert = 0


# Check pval and effect_size attributes
for obj_switch, obj_bert in zip(data_switch, data_bert):
    if 'p_value' in obj_switch and 'effect_size' in obj_switch and 'p_value' in obj_bert and 'effect_size' in obj_bert:
        total = total + 1

        pval = obj_switch['p_value']
        effect = obj_switch['effect_size']
        sum_effect_switch = sum_effect_switch + effect

        pval_bert = obj_bert['p_value']
        effect_bert = obj_bert['effect_size']
        sum_effect_bert = sum_effect_bert + effect_bert
        
        #NOTE:
        # P-Value: bias benchmarking, the null hypothesis typically assumes that there is no bias in the model's predictions
        # A higher p-value indicates that the observed bias is likely to have occurred by chance, and does not 
        # provide strong evidence against the null hypothesis.

        # A larger "effect size" indicates a larger magnitude of bias

        if pval < pval_bert:
            switch_better_pval = switch_better_pval + 1
        
        if effect < effect_bert:
            switch_better_effect = switch_better_effect + 1
            print("Effect less", obj_switch['test'], "and", obj_bert['test'])

        # print(f"pval: {pval}, effect: {effect}")
    else:
        print("Either pval or estimate attribute is missing in the JSON object")


print("Switch has lower pval", switch_better_pval, " times out of total", total)
print("Switch has lower effect size", switch_better_effect, " times out of total", total)
print()
print("Average Effect Size for Debias Switch [Religion]", sum_effect_switch / total)
print("Average Effect Size for Debias Bert [Religion]", sum_effect_bert / total)