
# Resume assistant 📝

Helping you to rate, improve and write cover letter to your resume.


**Note:** This is a prototype and not a production ready app.
TODO:
- [x] Add pdf resume support.
- [x] Add html description support.
- [x] Gradio app.
- [ ] Link the linkedin.
- [ ] Add other language models support like open-assistant, claude and palm.
- [ ] Seperate the rating and cover letter suggestions as seperate models.
- [ ] Fine tune the model using Qlora and resume datasets for more accurate rating and edits suggestions.



## Prerequisites
1. Langchain [documentation](https://python.langchain.com/en/latest/index.html)
   ```bash
    pip install langchain
    ```
2. openai api and key
   ```bash
    pip install openai
    ```
    API key is required to use the openai api. You can get it from Account -> generate api keys.
    add to your environment variable as OPENAI_API_KEY in your .bashrc or .zshrc file.
    ```bash
    export OPENAI_API_KEY="your api key"
    ```
3. python requirements
   ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the app
   ```bash
    python main.py
    ```
2. Open the browser and go to http://127.0.0.1:7860/ to use the app.
3. Upload the resume pdf file, add job description as text or local html file and click on the submit button.
4. Edit the resume based on the suggested edits.
5. Copy the cover letter and paste it in the cover letter section of the job application.
6. APPLY! ALL THE BEST!