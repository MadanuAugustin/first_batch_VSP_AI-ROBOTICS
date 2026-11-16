import gradio as gr



def count_letters(text):
    return "Letters: " + str(len(text))


def shout(text):
    return text.upper()


with gr.Blocks() as demo:
    box = gr.Textbox(label="Type here")
    count = gr.Textbox(label="Live count")
    loud = gr.Textbox(label="Loud (press Enter)")
    box.change(count_letters, box, count)
    box.submit(shout, box, loud)

    
demo.launch()