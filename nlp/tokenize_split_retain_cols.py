import re
from datasets import load_dataset
from transformers import AutoTokenizer

data = load_dataset("harryph/viwiki")
tokenizer = AutoTokenizer.from_pretrained('harryph/viwiki')
print(data)

"""
If remove all others columns when tokenizing, see https://huggingface.co/learn/nlp-course/en/chapter7/6#preparing-the-dataset
This code keep all columns by repeating the same value for each tokenized sample come from a raw sample.
"""


context_length = 128
def tokenize(element):
    # assert isinstance(element, list), 'hi'
    # processed_text = [re.sub('\n+', '\n', element["text"])]
    outputs = tokenizer(
        element['text'],
        truncation=True,
        max_length=context_length,
        return_overflowing_tokens=True,
        return_length=True,
    )

    sample_map = outputs.pop("overflow_to_sample_mapping")

    for key, values in element.items():
        outputs[key] = [values[i] for i in sample_map]

    return outputs


tokenized_datasets = data.map(
    tokenize, batched=True
)

print(tokenized_datasets)
tokenized_datasets.push_to_hub("harryph/viwiki", revision="tokenized")