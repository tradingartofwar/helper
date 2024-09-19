Step-by-Step Instructions for Beginners using Windows.  If you are using MAC, just paste all of this into GPT4o and ask it to change it over to MAC.  In fact, I would encourage you Windows users to do the same, because this is about working with AI.   If you do this, it will give you code snippets you can copy, rather than interpreting everything I wrote below.  Follow step by step.  Let me know if you have any questions, in the WhatsApp group. If your native language is not English, use GPT for that, too.  If you don't understand anything, ask GPT to explain.

You need to install Python.  Go to Python's official website and download the latest version.  https://www.python.org/downloads/

Follow the installation instructions for your operating system.
Make sure to check the box that says Add Python to PATH during installation (VERY IMPORTANT)

You will need to do 3 main things to make this work.  1.  Run commands in a terminal (mostly copy and paste)  2.  Get an API key from Openai.  3.  Clone the app from my repository (really just a command in the terminal, in this case).

Keep in mind how I did this.  I was looking at the assignment 2.4, and that took a minute or two.  Then I thought.  Well, why don't I just build a very basic version.  And it is basic.  The customer service agent can pull two questions from the database.  The sales agent can access 3 or 4.  I created the databases as csv files, which are in the same root folder (helper).  If you have never coded or done something like this, I assure you that 1. anyone can do it  2.  It's a pretty good feeling when you do.  After you finish, you could say to GPT4o, how can we improve this?  You can ask it to change it so that you can hit "enter" in addition to the send button.  You can add more inventory, order tracking, more agents, and so on.  Just explore. Okay let's begin.

1. Set Up a Projects Folder
Open File Explorer.
Navigate to your C: drive and create a new folder called "Projects."  (no quotes, no period)

2. Open a Command Prompt
Press Win + R, type cmd, and hit Enter.
Change to your Projects folder:

in your terminal, paste this and click enter
"cd C:\Projects"  (no quotes)        You should now see it pointed to that folder.

Go ahead and copy and paste this to make sure you are good with Python    "python --version"  (no quotes)

3. Clone the Repository
In the terminal, clone the repository:

paste this into your terminal
"git clone https://github.com/tradingartofwar/helper.git"  (no quotes)

Navigate to the project folder:
now change your command prompt to that folder by pasting the follow and hitting enter
"cd helper" (no quotes)

4. Set Up a Virtual Environment  (be sure you do this)
Create a virtual environment to manage dependencies: 

copy and paste the following
"python -m venv venv"  (no quotes)

Activate the virtual environment:
"venv\Scripts\activate"  (no quotes)
you should see a little venv in parenthesis in front for your path on the terminal
(venv) PS C:\Projects\helper>

5. Install Dependencies
Install the required librarie - copy and paste the following into your terminal
"pip install -r requirements.txt"  (no quotes)

6. Get an OpenAI API Key
Go to OpenAI and sign up or log in.  You will need GPT plus.  Under "products"  choose API Login  Then choose API.  Then click Dashboard on the top right.  Then click API keys on the left side column.  The click + Create new secret key on the top right, green button.  give it a name, like helper.  copy the key.   You have one more step to make the API key work.  ON the right side of the screen, click "vidw user API keys (gray button)  Then on the left column, click on billing.  Then setup a payment method.   Then add $10 to create a usable balance.  This will last for a while since we are using the 4o mini model.

7. Set Up Environment Variables
In your project folder (helper), create a .env file:
that is the entire name.  I use notepad  Open a notepad, then file save, then choose helper folder, put .env as the name, and save.

Now in that .env file, put the following  OPENAI_API_KEY=sk-proj-qQW (actual key is long)
I cut off part of my key.  But delete starting with the sk.   So it should be OPENAI_API_KEY=  then your key gets pasted right after the = sign.  Make sure you click save.

8. Run the Flask Application
Start the app:
in the terminal, copy and paste the following: "flask run"  (no quotes)

Go to http://127.0.0.1:5000/ in your browser to interact with the bot.

ask "what is your return policy," click send

as "how much is the premium mattress?"  click send.

If it says 30 days and $999, you have it all working.  If there are errors in your terminal log (just look).  Copy and paste those into GPT4o and have it help you solve it.  Feel free to ask me questions, too.  

Good luck!

Note:  if you were able to make that work, I can show you some pretty cool things you can make work from GitHub.  For example, an agent program called Maestro, where you can watch agents work together to answer a question.  But you don't need me.  GPT4o can help you do all of that.