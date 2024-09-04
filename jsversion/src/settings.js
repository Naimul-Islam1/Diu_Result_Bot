require('dotenv').config();

class Settings {
  constructor() {
    this.APIKEY = process.env.APIKEY;
    this.APPID = process.env.APPID;
    this.BOT_TOKEN = process.env.BOT_TOKEN;
  }
}

const setting = new Settings();

module.exports = setting;
