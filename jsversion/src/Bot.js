const TelegramBot = require('node-telegram-bot-api');
const settings = require('./settings');
const messagex = require('./Messages');
const getResult = require('./result').get_result;
const getFormattedResult = require('./Getresult').get_formatted_result;

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(settings.BOT_TOKEN, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, messagex.get_startmessage());
});

bot.onText(/\/help/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, messagex.get_helpmessage());
});

bot.onText(/\/result/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, messagex.get_resultmessage());
});

bot.onText(/\/about/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, messagex.about());
});

bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  // Ignore commands like /start, /help, /result, etc.
  if (text.startsWith('/')) return;

  try {
    const [semester_id, student_id] = text.split(' ');
    const result = await getResult(semester_id, student_id);
    if (result) {
      const formattedResult = getFormattedResult(result);
      bot.sendMessage(chatId, formattedResult);
    } else {
      bot.sendMessage(chatId, "Could not fetch results. Please check the semester ID and student ID.");
    }
  } catch (error) {
    bot.sendMessage(chatId, `Invalid format. Please provide the semester ID and student ID in the format: semesterId studentId
Example: 241 191-15-2639
${messagex.getResultMessage()}`);
  }
});
