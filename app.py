import tensorflow as tf
import gradio as gr
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2",pad_token_id=tokenizer.eos_token_id)

def generate_text(inp):
    input_ids = tokenizer.encode(inp, return_tensors='tf')
    beam_output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    output = tokenizer.decode(beam_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return ".".join(output.split(".")[:-1]) + "."

input_text = gr.components.Textbox(lines=5, label="Input Text")
output_text = gr.components.Textbox(label="Output Text")

gr.Interface(generate_text, inputs=input_text, outputs=output_text, title="GPT-2",
             description="OpenAI's GPT-2 is an unsupervised model that can generate coherent text.\
              Go ahead and input a sentence and see what it completes it with! Takes around 20s to run").launch(share=True, inline = False)