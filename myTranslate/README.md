# MyTranslate
#### Video Demo:  [MyTranslate](https://youtu.be/YI-u_MrB-BE)
#### Description:

MyTranslate is a web application built using the Flask module in python for the backend, and Jinja templating for the frontend.

It allows you to translate any words that you want to translate from one language to another. It also automatically detects languages so you don't need to even know the language of the text which you want to translate.

When you open the website you will see a field where you can input text. There you can go ahead and type whatever you need there to translate. Right below that is a dropdown menu containing the language you want to translate to. Select the language you’re going to translate into and then click the translate button. Your translated text will appear under the area.

__Files:__

The application.py file is the file for the backend. In this file, the Flask library, as well as the Bootstrap and WTForms libraries, adapted to be compatible with Flask. The WTForms library allows for the creation of secure forms inside of the Flask app without having to manually manage the template data for the form. Lastly, the Googletrans library is also imported to perform the translations. The Googletrans library is just one of many different libraries that allow for translation of text. First, a Flask app is initialized. Then, there is first a key for the WTForms selection to ensure that the forms are secure and cannot be accessed without the keys. After that, the Bootstrap app has to be configured.

The TranslateText class, which inherits the FlaskForm class(to be able to access data inside the fields) is the class that sets up the form. Then, in the index() method, the form variable is initialized to an instance of the TranslateText class. Then, when the user submits the form, if it is valid, then the translate function takes place, to translate into whatever "destination" language the user has chosen. Finally, the index() function returns a request to render the index.html template.

The index.html template is the template which shows the user the actual web application. This file uses jinja templating to get the base file as well as a basic template for WTForms. This template is then filled in with the title of MyTranslate as well as the content, which includes the form and the translated result if any. Finally it uses internal styling to style the file(since it is only one file and not multiple files.)

**Challenges:**

The most challenging aaspect of this program was to get the information from the user in a certain way that is both user-friendly, but also convenient and doesn't require too much extra polishing done to match the output. Luckily, WTForms in conjunction with Bootstrap allows to implement forms in a visually pleasing and clean manner, while also ensuring that the data stays in just a single file and doesnt need to be moved back and forth multiple times.

Another challenging aspect is to implement languages in a manner that is understandable to both the viewer and googletrans. Fortunately, list comprehension in python speeds this up quite a bit.

