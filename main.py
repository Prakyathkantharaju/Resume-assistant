from langchain.chat_models import ChatOpenAI
import json

import gradio as gr

from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.document_loaders import PyPDFLoader

def load_description(html: str):
    loader = UnstructuredHTMLLoader(html)
    return loader.load()[0].dict()['page_content']

def load_resume(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()[0].dict()['page_content']


def main():
    inputs  =[gr.Markdown("""
                          ## Resume Assistant
                          Upload the resume, job description and get the resume edits, rating and cover letter using GPT-3.
                          """),
        gr.UploadButton(label="Resume (pdf)", file_types = ['.pdf'], live=True, file_count = "single"),
    gr.Textbox("Job Description (text)", lines=15, placeholder="Paste the job description here"),
    gr.UploadButton(label="job description (html) - optional input", file_types = ['.html'], live=True, file_count = "multiple")]
    interface = gr.Interface(fn=chat, inputs =inputs,outputs ="text")
    interface.launch(debug=True)


def chat(markdown: str, pdf: str, text: str, html: str):

    print(html, pdf)
    if text == "":
        html_path = html[0].name
        description = load_description(html_path)
    else:
        description = text
    pdf_path = pdf.name
    chat = ChatOpenAI(temperature=0)
    template="You are a helpful assistant that vets resume, suggests the resume edits in points, rate the resume for the job decription in 1-10 and generate cover letter in a markdown format (200 Words) 'be turthfull and use only resume'. The response should be in mardown format: #rating: ; #resume_edits: ; #cover_letter: "
    system_message_prompt = SystemMessage(content=template)
    resume = load_resume(pdf_path)

    example_human = HumanMessage(content=f"Resume: {resume}; Job Description: {description}")
    messages = [system_message_prompt, example_human]
    test = chat(messages)
    content = test.dict()

    # make it a pritty
    updated = content['content'].replace('"', '').replace("{", "").replace("}", "").replace(":", "").replace(";", "")
    print(updated)

    return updated


if __name__ == "__main__":
    main()