from django.shortcuts import render
from django.http import JsonResponse
from .utils import translate_text


def translate(request):
    languages = [
        # Most commonly used languages on top
        ('en', 'English'),
        ('es', 'Spanish'),
        ('zh-cn', 'Chinese (Simplified)'),
        ('hi', 'Hindi'),
        ('ar', 'Arabic'),
        ('fr', 'French'),
        ('de', 'German'),
        ('ru', 'Russian'),
        ('pt', 'Portuguese'),
        ('ja', 'Japanese'),
        ('bn', 'Bengali'),
        ('pa', 'Punjabi'),
        ('ur', 'Urdu'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('ko', 'Korean'),
        ('vi', 'Vietnamese'),

        # Other supported languages
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('am', 'Amharic'),
        ('hy', 'Armenian'),
        ('az', 'Azerbaijani'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bs', 'Bosnian'),
        ('bg', 'Bulgarian'),
        ('ca', 'Catalan'),
        ('ceb', 'Cebuano'),
        ('ny', 'Chichewa'),
        ('zh-tw', 'Chinese (Traditional)'),
        ('co', 'Corsican'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('nl', 'Dutch'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('tl', 'Filipino'),
        ('fi', 'Finnish'),
        ('fy', 'Frisian'),
        ('gl', 'Galician'),
        ('ka', 'Georgian'),
        ('el', 'Greek'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian Creole'),
        ('ha', 'Hausa'),
        ('haw', 'Hawaiian'),
        ('he', 'Hebrew'),
        ('hmn', 'Hmong'),
        ('hu', 'Hungarian'),
        ('is', 'Icelandic'),
        ('ig', 'Igbo'),
        ('id', 'Indonesian'),
        ('ga', 'Irish'),
        ('it', 'Italian'),
        ('jw', 'Javanese'),
        ('kn', 'Kannada'),
        ('kk', 'Kazakh'),
        ('km', 'Khmer'),
        ('ku', 'Kurdish (Kurmanji)'),
        ('ky', 'Kyrgyz'),
        ('lo', 'Lao'),
        ('la', 'Latin'),
        ('lv', 'Latvian'),
        ('lt', 'Lithuanian'),
        ('lb', 'Luxembourgish'),
        ('mk', 'Macedonian'),
        ('mg', 'Malagasy'),
        ('ms', 'Malay'),
        ('ml', 'Malayalam'),
        ('mt', 'Maltese'),
        ('mi', 'Maori'),
        ('mr', 'Marathi'),
        ('mn', 'Mongolian'),
        ('my', 'Myanmar (Burmese)'),
        ('ne', 'Nepali'),
        ('no', 'Norwegian'),
        ('or', 'Odia'),
        ('ps', 'Pashto'),
        ('fa', 'Persian'),
        ('pl', 'Polish'),
        ('ro', 'Romanian'),
        ('sm', 'Samoan'),
        ('gd', 'Scots Gaelic'),
        ('sr', 'Serbian'),
        ('st', 'Sesotho'),
        ('sn', 'Shona'),
        ('sd', 'Sindhi'),
        ('si', 'Sinhala'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('so', 'Somali'),
        ('su', 'Sundanese'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('tg', 'Tajik'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('ug', 'Uyghur'),
        ('uz', 'Uzbek'),
        ('cy', 'Welsh'),
        ('xh', 'Xhosa'),
        ('yi', 'Yiddish'),
        ('yo', 'Yoruba'),
        ('zu', 'Zulu'),
    ]


    if request.method == 'POST':
        source_text = request.POST.get('source_text')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')

        translated_text = translate_text(source_text, source_language, target_language)

        if translated_text is None:
            return JsonResponse({'error': 'Translation failed'}, status=500)
        else:
            print(translated_text)
            return JsonResponse({'translated_text': translated_text})

    return render(request, 'translator/index.html', {'languages': languages})
