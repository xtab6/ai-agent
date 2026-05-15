const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

const client = new Client({
    puppeteer: {
        headless: true,
        args: ['--no-sandbox']
    }
});

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('WhatsApp AI Bot Ready!');
});

client.on('message', async message => {

    if (message.fromMe) return;

    try {

        const response = await axios.post(
            'https://APPKAMU.up.railway.app/chat',
            {
                message: message.body
            }
        );

        const reply = response.data.reply;

        await message.reply(reply);

    } catch (err) {
        console.log(err);
        await message.reply('AI error');
    }

});

client.initialize();
