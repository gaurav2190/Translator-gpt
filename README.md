# Translator-gpt

This is basic example of using Open AI APIs to translate the text submit into a language using prompt.

The solution is based on Flask and Jquery.

To run the application, follow the steps below

1. Clone the repository.

2. Create and add the private key created on OpenAI https://platform.openai.com/account/api-keys to the .env file.

3. Run command -> pip install -r requirements.txt

4. Run command -> flask run

This opens up an app with a textbox where you can enter text and press Enter key. On pressing enter, jquery sends a request to the API which in turn call open ai API and returns a response.

![image](https://user-images.githubusercontent.com/2959075/227758588-e3862554-5317-4d8b-b56b-ec436cd9fa90.png)

