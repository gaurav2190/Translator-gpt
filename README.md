# Translator-gpt

This is basic example of using Open AI APIs to translate the text submit into a language using prompt.

The solution is based on Flask and Jquery.

To run the application, follow the steps below

1. Clone the repository.

2. Create and add the private key created on OpenAI https://platform.openai.com/account/api-keys to the .env file.

3. Run command -> pip install -r requirements.txt

4. Run command -> flask run

This opens up an app with a text where you can enter the text and press key. On pressing enter, jquery sends a request to the API which in turn call open ai API and returns a response.
