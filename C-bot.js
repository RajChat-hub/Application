const { pipeline } = require('@huggingface/transformers');
const readlineSync = require('readline-sync');

// Define translation models
const translationModels = {
    en: {
        es: 'Helsinki-NLP/opus-mt-en-es',
        de: 'Helsinki-NLP/opus-mt-en-de',
        fr: 'Helsinki-NLP/opus-mt-en-fr',
        it: 'Helsinki-NLP/opus-mt-en-it',
        ru: 'Helsinki-NLP/opus-mt-en-ru',
        zh: 'Helsinki-NLP/opus-mt-en-zh',
        ja: 'Helsinki-NLP/opus-mt-en-ja',
        ar: 'Helsinki-NLP/opus-mt-en-ar',
        hi: 'Helsinki-NLP/opus-mt-en-hi',
        bn: 'Helsinki-NLP/opus-mt-en-bn',
        sr: 'Helsinki-NLP/opus-mt-en-sr',
        el: 'Helsinki-NLP/opus-mt-en-el',
    },
    // Add other language pairs if needed
};

// Load translation models
async function loadModels() {
    const models = {};
    for (const [sourceLang, targets] of Object.entries(translationModels)) {
        models[sourceLang] = {};
        for (const [targetLang, modelName] of Object.entries(targets)) {
            models[sourceLang][targetLang] = await pipeline('translation', modelName);
        }
    }
    return models;
}

// Translate text
async function translateText(text, sourceLang, targetLang, models) {
    try {
        const translator = models[sourceLang][targetLang];
        const result = await translator(text);
        return result[0].translation_text;
    } catch (error) {
        console.error('Translation error:', error);
        return null;
    }
}

// Basic conversation responses
function getResponse(question) {
    const responses = {
        'hi': 'Hi, How can I assist you today?',
        'hello': 'Hello, How can I assist you today?',
        'how are you': 'I am doing great, What about you?',
        'what is your name': 'I am Basic-Bot, The basic structure of a Chat-Bot.',
        'who invented you': 'Rajdeep Chatterjee, whose hobby is programming.',
        'how many languages do you know': 'I know varieties of languages, like English, Hindi, Bengali, German, Spanish, Italian, French, Russian, Chinese, Japanese, Arabic, Serbian, Greek.',
        'write a script in': {
            'german': 'Hier ist das Skript, ............',
            'spanish': 'Aquí está el script, ............',
            'french': 'Voici le script, ............',
            // Add other languages as needed
        }
    };
    return responses[question.toLowerCase()] || 'Sorry, I did not understand that.';
}

// Main function
async function main() {
    console.log('Basic-Bot is ready to assist you.');
    const models = await loadModels();

    while (true) {
        const question = readlineSync.question('You: ');
        if (question.toLowerCase() === 'exit') {
            console.log('Goodbye!');
            break;
        }

        if (question.toLowerCase().startsWith('translate ')) {
            const [_, text, sourceLang, targetLang] = question.split(' ');
            const translation = await translateText(text, sourceLang, targetLang, models);
            console.log(`Translation: ${translation}`);
        } else if (question.toLowerCase().startsWith('write a script in ')) {
            const lang = question.split(' ').pop().toLowerCase();
            const response = getResponse(`write a script in ${lang}`);
            console.log(`Bot: ${response}`);
        } else {
            const response = getResponse(question);
            console.log(`Bot: ${response}`);
        }
    }
}

main();