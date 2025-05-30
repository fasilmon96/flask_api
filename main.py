from  flask  import Flask, jsonify

from waitress import serve

class QuestionsData :
      def __init__(self,question_id,question,option,answer):
        self.question_id = question_id
        self.question = question
        self.option = option
        self.answer = answer

questionData = [
QuestionsData(
    question_id=1,
    question="ഇന്ത്യയില്‍ ഏറ്റവും കൂടുതല്‍ കാണപ്പെടുന്ന മണ്ണ് ?",
    option=["ലാറ്ററൈറ്റ് മണ്ണ്", "മുഴങ്ങിയ മണ്ണ്", "വളമുള്ള മണ്ണ്", "കറുത്ത മണ്ണ്"],
    answer="കറുത്ത മണ്ണ്"
),
QuestionsData(
    question_id=2,
    question=" സസ്യ ലോകത്തിലെ ‘മാംസ്യ സംരഭകർ’ എന്നറിയപ്പെടുന്ന സസ്യ വർഗം ഏത് ?",
    option=["കിഴങ്ങു വർഗം", "പഴ വർഗം", "പയറു വർഗം", "ധാന്യ വർഗം"],
    answer="പയറു വർഗം"
),
QuestionsData(
    question_id=3,
    question="പ്രഗത്ഭരായ കുതിരസവാരി ഉൾപ്പെടുന്ന ഒരു ______ കായിക വിനോദമാണ് ചറേരിയ",
    option=["മെക്സിക്കൻ", "ഇറ്റാലിയൻ", "ഇന്ത്യൻ", "ചൈനീസ്"],
    answer="മെക്സിക്കൻ"),
QuestionsData(
    question_id=4,
    question="പപടയണിയിൽ ഉപയോഗിക്കുന്ന വാദ്യങ്ങൾ ഏതാണ്?",
    option=["തപ്പും ചെണ്ടയും", "മൃദംഗവും തപ്പുവും", "കുഴലും ചെണ്ടയും", "മിഴാവും മദ്ദളവും"],
    answer="തപ്പും ചെണ്ടയും"
),
QuestionsData(
    question_id=5,
    question=" ഇന്ത്യയിലെ ഏറ്റവും ഉയരം കൂടിയ കൊടുമുടി?",
    option=["മൗണ്ട് എവറസ്റ്റ്", "കാഞ്ചൻജംഗ", "നന്ദാദേവി", "മൗണ്ട് K2"],
    answer="മൗണ്ട് K2"
),
QuestionsData(
    question_id=6,
    question="കേരളത്തിന്റെ ഔദ്യോഗിക പുഷ്പം ഏതാണ്?",
    option=["തകില", "ചേന", "കണിക്കൊന്ന", "തുളസി"],
    answer="കണിക്കൊന്ന"
),
QuestionsData(
    question_id=7,
    question="താരാപ്പൂർ ആണവോർജ്ജനിലയം സ്ഥിതി ചെയ്യുന്ന സംസ്ഥാനം എവിടെയാണ്?",
    option=["മഹാരാഷ്ട്ര", "കർണ്ണാടകം", "തമിഴ്‌നാട്", "ആന്ധ്രാപ്രദേശ്"],
    answer="മഹാരാഷ്ട്ര"
),
QuestionsData(
    question_id=8,
    question="ഭാരതത്തിലെ ആദ്യ ഉപഗ്രഹം ഏതാണ്?",
    option=["ആപ്സാര", "ഭാസ്കര", "അര്യഭട്ട", "ഇൻസാറ്റ്-1A"],
    answer="അര്യഭട്ട"
),
QuestionsData(
    question_id=9,
    question="കുന്ദറൻ എന്നറിയപ്പെടുന്നത് ഏത് നദിയെയാണ്?",
    option=["കാവേരി", "കൃഷ്ണ", "യമുന", "ഗോദാവരി"],
    answer="കാവേരി"
),
QuestionsData(
    question_id=10,
    question="ഇന്ത്യയുടെ രാഷ്ട്രപിതാവെന്ന് കണക്കാക്കപ്പെടുന്ന വ്യക്തി?",
    option=["ജവാഹർലാൽ നെഹ്രു", "മഹാത്മാഗാന്ധി", "സർദാർ പട്ടേൽ", "ഭഗത് സിംഗ്"],
    answer="മഹാത്മാഗാന്ധി"
),
QuestionsData(
    question_id=11,
    question="ഭാരതത്തിലെ ഏറ്റവും നീളമുള്ള നദി ഏതാണ്?",
    option=["യമുന", "നർമദ", "ഗംഗ", "സത്ലെജ്"],
    answer="ഗംഗ"
),
QuestionsData(
    question_id=12,
    question="കേരളത്തിലെ പ്രധാന കായലുകൾ തമ്മിൽ ബന്ധിപ്പിക്കുന്ന ജലപാതി ഏത്?",
    option=["പെരിയാർ", "വെമ്പനാട്", "വെള്ളായണി", "പഠിരാമണാൽ"],
    answer="വെമ്പനാട്"
),
QuestionsData(
    question_id=13,
    question="വാതകാവസ്ഥയിലുള്ള ലോഹം ഏതാണ്?",
    option=["സോഡിയം", "മെർക്കുറി", "ക്ലോറിൻ", "ഹെലിയം"],
    answer="ഹെലിയം"
),
QuestionsData(
    question_id=14,
    question="ജലത്തിൽ രാസപരമായി ചേർന്നിരിക്കുന്ന മൂലകങ്ങളാണ്?",
    option=["ഹൈഡ്രജനും ഓക്സിജനും", "ഹൈഡ്രജനും നൈറ്റ്രജനും", "കാർബണും ഓക്സിജനും", "സോഡിയവും ക്ലോറിനും"],
    answer="ഹൈഡ്രജനും ഓക്സിജനും"
),
QuestionsData(
    question_id=15,
    question="ദൃഢമായ പഞ്ചഭൗതിക വസ്തുക്കളിൽ ഏറ്റവും കഠിനതയുള്ളത് ഏത്?",
    option=["ഇരുമ്പ്", "വജ്രം", "സിൽവർ", "അലുമിനിയം"],
    answer="വജ്രം"
),
QuestionsData(
    question_id=16,
    question="പഞ്ചഭൂതങ്ങളിൽ ‘വായു’യെ പ്രധാന ഘടകമായി കാണുന്ന ഇന്ദ്രിയം ഏത്?",
    option=["നാകം", "ചർമ്മം", "ശ്രവണം", "നാസിക"],
    answer="ശ്രവണം"
),
QuestionsData(
    question_id=17,
    question="ഭാരതത്തിന്റെ ദേശീയ പക്ഷി ഏതാണ്?",
    option=["മുരളി", "മയില", "കാക്ക", "കിളി"],
    answer="മയില"
),
QuestionsData(
    question_id=18,
    question="ഇന്ത്യയിലെ ഏറ്റവും വലിയ സംസ്ഥാനം ഏത്?",
    option=["രാജസ്ഥാൻ", "ഉത്തർപ്രദേശ്", "മധ്യപ്രദേശ്", "ബിഹാർ"],
    answer="രാജസ്ഥാൻ"
),
QuestionsData(
    question_id=19,
    question="ഭൂമിയിലെ ഏറ്റവും വലിയ വന്യപ്രദേശമായ ആമസോൺ കാടുകൾ ഏവിടെ സ്ഥിതിചെയ്യുന്നു?",
    option=["ബ്രസീൽ", "കാനഡ", "റഷ്യ", "ആസ്റ്റ്രേലിയ"],
    answer="ബ്രസീൽ"
),
QuestionsData(
    question_id=20,
    question="ഒളിമ്പിക്‌സിൽ ഏറ്റവും കൂടുതൽ സ്വർണം നേടിയ രാജ്യം ഏതാണ്?",
    option=["അമേരിക്ക", "ചൈന", "റഷ്യ", "ജർമ്മനി"],
    answer="അമേരിക്ക"
),
QuestionsData(
    question_id=21,
    question="യൂറോ നാണയം ഔദ്യോഗികമായി ഉപയോഗിക്കുന്ന പ്രദേശം ഏതാണ്?",
    option=["ഫ്രാൻസ്", "ജർമ്മനി", "ഇറ്റലി", "യൂറോപ്യൻ യൂണിയൻ"],
    answer="യൂറോപ്യൻ യൂണിയൻ"
),
QuestionsData(
    question_id=22,
    question="കേരളത്തിലെ ആദ്യ വനിതാ മുഖ്യമന്ത്രി ആര്?",
    option=["പിണറായി വിജയൻ", "വൈഷ്ണവി", "കുമാരി ജയന്തി", "വിനീത കൃഷ്ണൻ"],
    answer="കുമാരി ജയന്തി"
),
QuestionsData(
    question_id=23,
    question="കേരളത്തിൽ ആദ്യമായി കർഷകസഖ്യങ്ങൽ ആരംഭിച്ചത് എവിടെ ആണ്?",
    option=["തൃശൂർ", "കൊച്ചി", "കാസർകോട്", "കോട്ടയം"],
    answer="തൃശൂർ"
),
QuestionsData(
    question_id=24,
    question="കേരളത്തിലെ ഏറ്റവും പഴക്കം ചെന്ന പത്രം ഏത്?",
    option=["മാതൃഭൂമി", "മലയാള മനോരമ", "ദീപിക", "ദിനമണി"],
    answer="ദീപിക"
),
QuestionsData(
    question_id=25,
    question="കേരളത്തിലെ ആദ്യത്തെ വനിതാ ഐ.എ.എസ് ഉദ്യോഗസ്ഥയായത് ആര്?",
    option=["മമ്മൂട്ടി", "മിനി മതി", "ബിജു ജോസഫ്", "കവിത"],
    answer="മിനി മതി"
),
QuestionsData(
    question_id=26,
    question="കേരളത്തിലെ ഏറ്റവും ഉയർന്ന മല ഏത്?",
    option=["അനമുടി", "മുക്കുടി", "എളുപ്പടി", "ചിൽക"],
    answer="അനമുടി"
),
QuestionsData(
    question_id=27,
    question="കേരളത്തിലെ ആദ്യത്തെ ദേവസ്വം ബോർഡ് സ്ഥാപിച്ചത് ഏത് വർഷം?",
    option=["1949", "1951", "1956", "1960"],
    answer="1949"
),
QuestionsData(
    question_id=28,
    question="ന്യൂട്ടന്റെ മൂന്നാം നിയമം പറയുന്നത് എന്താണ്?",
    option=[
        "പ്രതികാരം ശക്തമാണ്",
        "ഏത് പ്രക്ഷേപണത്തിനും സമാനവും എതിര്‍പ്പുള്ള ശക്തി ഉണ്ടാകും",
        "ശക്തി = ഭാരം × വേഗത",
        "ശക്തി പ്രത്യക്ഷമായി മാറും"
    ],
    answer="ഏത് പ്രക്ഷേപണത്തിനും സമാനവും എതിര്‍പ്പുള്ള ശക്തി ഉണ്ടാകും"
),
QuestionsData(
    question_id=29,
    question="വേഗതയുടെ അളവിനായി ഏത് യൂണിറ്റ് ഉപയോഗിക്കുന്നു?",
    option=["മീറ്റർ", "സെക്കൻഡ്", "മീറ്റർ/സെക്കൻഡ്", "കിലോഗ്രാം"],
    answer="മീറ്റർ/സെക്കൻഡ്"
),
QuestionsData(
    question_id=30,
    question="പ്രകാശം പ്രതിഫലിക്കുന്ന നിയമം ഏതാണ്?",
    option=["ഓംസ് നിയമം", "സ്നെൽസ് നിയമം", "റഫ്ലക്ഷൻ നിയമം", "റെഫ്രാക്ഷൻ നിയമം"],
    answer="റഫ്ലക്ഷൻ നിയമം"
),
QuestionsData(
    question_id=31,
    question="കേരള സർക്കാർ നിലവിൽ നടത്തുന്നത് 'ഹരിത കേരളം മിഷൻ' എന്ന പദ്ധതി ലക്ഷ്യം എന്താണ്?",
    option=["വനസംരക്ഷണം", "വെള്ളച്ചാട്ട സംരക്ഷണം", "കൃഷി വികസനം", "ജലസംരക്ഷണം"],
    answer="വനസംരക്ഷണം"
),
QuestionsData(
    question_id=32,
    question="2024-ലെ കേരള ബജറ്റ് അവതരിപ്പിച്ച Finance Minister ആരാണ്?",
    option=["കെ. എൻ. ബാലഗോപാൽ", "എച്ച്. ഹരീഷ്", "വി. ശിവൻകുട്ടി", "പി. എ. മുഹമ്മദ് റിയാസ്"],
    answer="എച്ച്. ഹരീഷ്"
),
QuestionsData(
    question_id=33,
    question="2024-ൽ ലോക സാമ്പത്തിക ഫോറം (World Economic Forum) നടക്കുന്ന സ്ഥലമാകുന്നത് ഏതാണ്?",
    option=["ദാവോസ്", "ജെനിവ", "സിംഗപ്പൂർ", "ന്യൂയോർക്ക്"],
    answer="ദാവോസ്"
),
QuestionsData(
    question_id=34,
    question="2023-ൽ ഇന്ത്യയിലെ ആദ്യ വനിതാ ചീഫ് ഇലക്ട്രിക്കൽ എൻജിനീയറായും സ്ഥാനമേറ്റെടുത്തത് ഏത് രാജ്യത്തെ വനിതയാണ്?",
    option=["ഇന്ത്യ", "ജപ്പാൻ", "അമേരിക്ക", "ജർമനി"],
    answer="ഇന്ത്യ"
),
QuestionsData(
    question_id=35,
    question="2024-ൽ ഇന്ത്യയുടെ ആദ്യ ജൈവ ഇന്ധന വിമാന സർവീസ് ആരംഭിച്ചത് ഏത് സംസ്ഥാനത്താണ്?",
    option=["കർണാടക", "മഹാരാഷ്ട്ര", "തമിഴ്‌നാട്", "കേരളം"],
    answer="കർണാടക"
),
QuestionsData(
    question_id=36,
    question="2023-ലെ ‘ഇന്ത്യൻ ഓർഗനൈസേഷൻ ഓഫ് സയൻസ്സ്’ (IOS) പ്രസിഡന്റായി തിരഞ്ഞെടുക്കപ്പെട്ട ശാസ്ത്രജ്ഞൻ ആര്?",
    option=["എം. വിജയൻ", "ഡി. രാമചന്ദ്രൻ", "പി. എസ്. മുരളീധരൻ", "കെ. എസ്. രമേഷ്"],
    answer="എം. വിജയൻ"
),
QuestionsData(
    question_id=37,
    question="ഒരു സംഖ്യയുടെ 25% 50 ആണെങ്കിൽ ആ സംഖ്യ എത്രയാണ്?",
    option=["100", "150", "200", "250"],
    answer="200"
),
QuestionsData(
    question_id=38,
    question="3x - 7 = 11 ആയപ്പോൾ x-ന്റെ മൂല്യം എത്ര?",
    option=["6", "7", "5", "4"],
    answer="6"
),
QuestionsData(
    question_id=39,
    question="ആകാശത്ത് ഏറ്റവും കൂടുതൽ ഓക്സിജൻ ഉത്പാദിപ്പിക്കുന്നത് ഏത് സസ്യമാണ്?",
    option=["ആല", "മരം", "ഫോട്ടോസിന്റസിസ് ചെയ്യുന്ന സസ്യങ്ങൾ", "കടൽശൈവ"],
    answer="ഫോട്ടോസിന്റസിസ് ചെയ്യുന്ന സസ്യങ്ങൾ"
),
QuestionsData(
    question_id=40,
    question="കേരളത്തിലെ പ്രാചീനകാല സംസ്കാരങ്ങളുടെ പ്രധാന സാക്ഷ്യം നൽകുന്ന സൈറ്റാണ്?",
    option=["മോഹൻജോ-ദാരോ", "ഇല്ലവൂർ", "ചേരമണ്‍പുരം", "പാറൂർ"],
    answer="ഇല്ലവൂർ"
),
QuestionsData(
    question_id=41,
    question="ചെറുവഴിയിൽ നിന്നുള്ള വിജയത്തിന്റെ വഴി ആരാണ് നിർമ്മിച്ചത്?",
    option=["മഹാത്മാ ഗാന്ധി", "ശിവജി മിത്ര", "ചെറുവഴി രാജാവ്", "കുട്ടിശ്ശേരി രാജാവ്"],
    answer="മഹാത്മാ ഗാന്ധി"
),
QuestionsData(
    question_id=42,
    question="കേരളത്തിലെ ആദ്യ വനിതാ സാന്നിധ്യം ഏത് വർഷമാണ് രേഖപ്പെടുത്തിയിരിക്കുന്നത്?",
    option=["1920", "1935", "1947", "1956"],
    answer="1935"
),
QuestionsData(
    question_id=43,
    question="ചെങ്ങന്നൂർ മദ്ധ്യകാല ചരിത്രത്തിൽ പ്രശസ്തമായത് എന്തിനാൽ?",
    option=["സാമൂഹിക സന്ധി", "വ്യാപാരം", "മത്സ്യബന്ധനം", "കലയൊന്ന്"],
    answer="വ്യാപാരം"
),
QuestionsData(
    question_id=44,
    question="‘കണ്ടത് കല്യാണമല്ല’ എന്ന കാവ്യരചനയുടെ കർത്താവ് ആര്?",
    option=["വൈക്കം മുഹമ്മദ് ബഷീർ", "ഒ. എന്‍. വി. കുറുപ്പ്", "സുഗതകുമാരി", "മുലൂർ"],
    answer="ഒ. എന്‍. വി. കുറുപ്പ്"
),
QuestionsData(
    question_id=45,
    question="‘രാമചരിതം’ എന്ന പ്രാചീന കാവ്യം ഏത് ഭാഷയിൽ എഴുതപ്പെട്ടതാണ്?",
    option=["സംസ്കൃതം", "തമിഴ്", "മലയാളം", "പാലി"],
    answer="മലയാളം"
),
QuestionsData(
    question_id=46,
    question="സ്വാതന്ത്ര്യ സമരകാലത്ത് 'ഇന്ത്യൻ റിപ്പബ്ലിക്കൻ ആർമി' എന്ന സംഘടന രൂപപ്പെടുത്തിയ വ്യക്തി ആര്?",
    option=["സുഭാഷ് ചന്ദ്രബോസ്", "ഭഗത് സിംഗ്", "ചന്ദ്രശേഖർ ആസാദ്", "സൂര്യസേന"],
    answer="ചന്ദ്രശേഖർ ആസാദ്"
),
QuestionsData(
    question_id=47,
    question="മലയാളത്തിലെ ആദ്യകാല കവിതയായ ‘രാമചരിതം’യെ എഴുതിയത് ഏത് പ്രദേശവാസിയാണ് എന്ന് കരുതപ്പെടുന്നു?",
    option=["തിരുവിതാംകൂർ", "തെക്കൻ മലബാർ", "നേമത്ത്", "മധുര"],
    answer="തെക്കൻ മലബാർ"
),
QuestionsData(
    question_id=48,
    question="2024-ലെ രാജ്യസഭാ ഡെപ്യൂട്ടി ചെയർമാനായി തിരഞ്ഞെടുക്കപ്പെട്ടത് ആര്?",
    option=["ജഗദീപ് ധൻഖഡ്", "ഹർഷ വർദ്ധൻ", "കെ. കെ. വേണുഗോപാൽ", "ഹരി വംശ്"],
    answer="ഹരി വംശ്"
),
QuestionsData(
    question_id=49,
    question="കേരളത്തിൽ ആദ്യമായി വോട്ട് ചെയ്യാനായി ഇലക്‌ട്രോണിക് വോട്ടിംഗ് മെഷീൻ ഉപയോഗിച്ച മണ്ഡലം ഏത്?",
    option=["വട്ടിയൂർക്കാവ്", "പാർശ്ശാല", "ആലത്തൂർ", "പാർലിക്കര"],
    answer="ആലത്തൂർ"
),
QuestionsData(
    question_id=50,
    question="കേരള സംസ്ഥാന വനിതാ കമ്മീഷന്റെ ആദ്യ അധ്യക്ഷയായത് ആരാണ്?",
    option=["ജസ്റ്റിസ് കെ. ആർ. ഉമാദേവി", "സുധാ നായർ", "സരസു പാറേക്", "സുധാ മാധവൻ"],
    answer="ജസ്റ്റിസ് കെ. ആർ. ഉമാദേവി"
),
]

def questionToJson(questions: QuestionsData):
    return {
        "question_id": questions.question_id,
        "question":    questions.question,
        "option": questions.option,
        "answer": questions.answer,
    }

app = Flask("Api Application")

@app.route("/allQuestion", methods=["GET"])
def getAllQuestions():
     print("called getAllQuestions")
     questionlist = []
     for questionValue in questionData:
         questionlist.append(questionToJson(questionValue))
     return  jsonify({"questions"  : questionlist})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

