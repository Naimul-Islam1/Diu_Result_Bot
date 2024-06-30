<!-- # Diu_Result_Bot


## About This Bot:

**Description:**

The Daffodil International University (DIU) chatbot is an innovative tool designed to streamline information access for students, faculty, and staff. Developed by Swadhin Biswas and Naimul Islam, this chatbot leverages the power of DIU's internal servers to provide users with real-time information directly within a chat interface.

**Key Features:**

* **Centralized Information Source:** The chatbot acts as a central hub for university information, eliminating the need to navigate various departmental websites or resources.
* **Real-Time Access:** Users can access information anytime, anywhere through the chatbot's convenient chat interface.
* **Improved Efficiency:** The chatbot saves users time and effort by providing quick and easy access to frequently asked questions and other relevant university information.
* **Enhanced Communication:** The chatbot fosters improved communication between students, faculty, and staff by providing a readily available information channel.

**Benefits:**

* **Increased Accessibility:** The chatbot makes university information readily accessible to all users, regardless of their technical expertise.
* **Streamlined Communication:** The chatbot facilitates smoother communication by providing a centralized platform for information exchange.
* **Improved User Experience:** The chatbot enhances the user experience by offering a convenient and user-friendly way to access university information.

**Developed By:**

**Swadhin Biswas** and  **Naimul Islam**

----
# How To Use It

<br>









# Host Your Own Bot 

## 1.Install Requirements
 * **Clone this repo:**
 ```
  git clone https://github.com/Naimul-Islam1/Diu_Result_Bot && cd Diu_Result_Bot
```

* **For Debian Based Distros**
```
sudo apt install python3 python3-pip
```
* **For Arch and it's Child**
```
 sudo pacman -S docker python
 ```
 * **Install dependencies for running setup scripts:**
 ```pyhton3
 pip3 install -r requirements-cli.txt
 ```
 ---
 ## 2. Setting up config file
 * change sample.txt to .env
 
 * <code>BOT_TOKEN</code>:The Telegram Bot Token that you got from<a href="https://t.me/BotFather"> @BotFather</a>.<code>str</code>

 * <code>APIKEY</code> Telegram API HASH :This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org <code> str</code>

* <code>APPID</code>:Telegram API ID:This is to authenticate your Telegram account for downloading Telegram files. You can get this from https://my.telegram.org.<code>int</code> -->


## Diu_Result_Bot: Streamline Information Access at Daffodil International University

**About This Bot**

The Diu_Result_Bot is an innovative chatbot designed to empower students, faculty, and staff of Daffodil International University (DIU) with effortless access to university information. Developed by Swadhin Biswas and Naimul Islam, this chatbot leverages DIU's internal servers to deliver real-time information directly within a convenient chat interface.

**Key Features**

* **Centralized Information Hub:** Eliminate the hassle of navigating multiple departmental websites! The Diu_Result_Bot serves as a one-stop shop for all your university information needs.
* **Real-Time Access:** Get the information you need, anytime, anywhere. The chatbot's user-friendly interface allows you to access information on-demand.
* **Improved Efficiency:** Save valuable time and effort. The chatbot provides quick and easy access to frequently asked questions and other relevant university resources.
* **Enhanced Communication:** Foster better communication between students, faculty, and staff. The chatbot acts as a readily available information channel, promoting a more connected university community.

**Benefits**

* **Increased Accessibility:** The chatbot makes university information readily available to all users, regardless of their technical expertise.
* **Streamlined Communication:** The chatbot facilitates smoother communication by providing a centralized platform for information exchange.
* **Improved User Experience:** The chatbot enhances the user experience by offering a convenient and user-friendly way to access university information.

**Developed By:**

Swadhin Biswas and Naimul Islam



**How To Use It**

**Hosting Your Own Bot**

If you're interested in hosting your own instance of the Diu_Result_Bot, follow these steps:

**1. Installation Requirements**

* **Clone the repository:**

```
git clone https://github.com/Naimul-Islam1/Diu_Result_Bot && cd Diu_Result_Bot
```

* **Install dependencies:**

  * **Debian-based systems:**

    ```
    sudo apt install python3 python3-pip
    ```

  * **Arch and derivatives:**

    ```
    sudo pacman -S docker python
    ```

* **Install additional dependencies for setup scripts:**

  ```
  pip3 install -r requirements-cli.txt
  ```

**2. Setting Up the Configuration File**

* Rename the `sample.txt` file to `.env`. This file stores sensitive bot credentials.
* Update the `.env` file with the following:

    * `BOT_TOKEN`: Your Telegram Bot Token obtained from @BotFather.
    * `APIKEY`: Your Telegram API Hash for file download authentication (refer to [https://core.telegram.org/](https://core.telegram.org/)).
    * `APPID`: Your Telegram API ID for file download authentication (refer to [https://core.telegram.org/](https://core.telegram.org/)).

**Important Note:**

* **Do not share your BOT_TOKEN, APIKEY, or APPID publicly.** These credentials are essential for maintaining the security of your bot.

For detailed instructions and troubleshooting, refer to the official documentation for the Diu_Result_Bot project.
