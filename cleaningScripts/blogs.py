from indusnlp.cleaner import TextCleaner


config = [
("remove_line_and_below", ["Disclaimer","disclaimer","Comments","Comment",
                           "COMMENTs", "Facebook"]),
("remove_line_with_keyword",["केयरवैद्य", "www.carevaidya.com", "share", "comments"
                             "हमें संपर्क करें","Social media sites", "Download",
                             "available on the Internet", "Watch Online",
                              "download","डाउनलोड"],),
("handle_whitespace", None),
("remove_single_word_lines", None),
("remove_redundant_lines", None),
("remove_blank_lines", None),
]

txt = '''
क्या आपने कभी Hostgator India से hosting खरीदी है या फिर एक WordPress blog या website बनाना चाहते हैं?
यह एक step by step guide है जो आपको बताएगी कि Hostgator India की hosting पर WordPress कैसे install करें. यदि आपने अभी उनसे hosting नहीं खरीदी तो आप यहाँ से खरीद सकते हैं और Hostgator India की hosting पर WordPress blog बनाने के इस tutorial को follow कीजिये.
Hostgator.in आपके domains और hosting को manage करने के लिए custom cPanel offer करता है और hosting को manage करने के लिए standard cPanel offer करता है. मैं आपको बताऊंगा कि उनके custom cPanel के साथ कैसे शुरू करें और फिर WordPress installation के लिए उनके hosting cPanel में कैसे जाएँ.
इसके steps आसान है और कोई भी बिना किसी technical knowledge के इसे कर सकता है. तो चलिए एक coffee का कप ले आयी और अपने पहले WordPress blog को setup करने और अगले 10 minutes में शुरू करने का सफ़र शुरू कीजिये.
Hostgator India की hosting पर WordPress कैसे install करें:
मैं assume करता हूँ कि आपने Hostgator India से hosting खरीद ली है और सबसे पहली चीज़ जो आपको करनी होगी कि, अपने domain को hosting account पर point करना. मैं ये भी assume करता हूँ कि आपने Hostgator India के hosting account के साथ अपना domain name point कर लिया है.
यदि आपने ऐसा नहीं किया, तो आगे बढिए और इसे पूरा कीजिये. अब नीचे mention किये गए सभी steps follow कीजिये और कुछ ही समय में आपका WordPress blog up हो जायेगा और शुरू हो जायेगा.
- manage.hostgator.in पर जाईये और अपने credentials के साथ login कीजिये.
- Manage Orders > List/Search Orders पर click कीजिये.
Product hosting के under domain name पर click कीजिये. (नीचे दिए गए screenshot में देखिये)
अगले page पर, उस section तक scroll down कीजिये, जहाँ पर hosting India लिखा होगा, (यह multi-domain Linux hosting भी हो सकती है और single-domain Linux hosting भी) आपके package के हिसाब से.
Manage Web-hosting पर click कीजिये (नए Tab में open कीजिये) और इससे एक pop-up open होगा जोकि आपको cPanel hosting के account तक ले जायेगा. आप वहां पर admin details पर भी click कर सकते हैं, जोकि आपको आपके hosting account और login credentials का direct link देगा. (आप इसका बाद में use के लिए Google doc file में नोट बना सकते हैं).
Better clarity के लिए इस video को देखिये (English main):
आपका Hostgator.in cPanel कुछ ऐसा दिखेगा:
अब नीचे उस section तक scroll down कीजिये जहाँ पर लिखा होगा, Softaculous apps installer और यहीं से आपक WordPress blog और ऐसे बहुत से CMS जैसे कि द्रुपल, Joomla और बहुत से और install कर सकते हैं. यहाँ अपने hosting account पर WordPress install करने का quickest और fastest way है. (नीचे दिया गया screenshot देखिये)
WordPress पर click कीजिये और ये आपको उस page पर ले जायेगा, जहाँ पर आपको WordPress की इंस्टालेशन के लिए कुछ basic settings को configure करना होगा.
Install and configure the options पर click कीजिये. (यह आसान है पर patient रहें और सरे steps दुबारा check करें). मैंने सारे options already explain कर दिए हैं और यदि आपको कोई confusion है तो आप मुझे नीचे comment section के via पूछने में free feel करें.
- Protocol choose करें: यह वेह जगह है जहाँ आपको decide करना होता है कि www रखें के न रखें. जैसा कि short domain name बढ़िया होता है, मैं use बिना www के रखने का सुझाव देता हूँ. इसलिए सिर्फ http:// select कीजिये.
- Domain चुने: वह domain select कीजिये जिसपर आप WordPress install करना चाहते हैं.
- In directory: By default Hostgator wp को as directory select करेगा और मैं आपको इसे remove करने का suggest करता हूँ. यदि आप नहीं चाहते कि आपका WordPress blog किसी ऐसी directory जैसे कि domain.com/wp में install हो, मैं आपको WordPress main domain पर install करने कि सलाह देता हूँ. फॉर example, मेरे case में WordPress HGusers.in पर install होगा.
- Sitename: अपनी site को एक नाम दीजिये.
- Site Description: तीन चार शब्दों में अपनी site के लिए एक description add कीजिये. (आप अपना site name और site description बाद में कभी भी change कर सकते हैं).
Admin account section:
यह वह जगह है जहाँ आप अपने WordPress blog के लिए login details configure करेंगे. इस बात का ध्यान रखें कि आप admin के इलावा और कोई भी username select करें. इसके साथ ही एक complex password भी use करें. यदि आपने एक admin email create नहीं किया, आप use बाद में भी add कर सकते हैं और अभी के लिए एक ऐसा email add कीजिये जिसका आपके पास access हो. (आने वाले दिनों में मैं आपको बताऊंगा कि आप admin email कैसे बनायें). Settings के बाद मेरी screen कुछ ऐसी दिखती है:
Limit login plugin options में, इस feature को enable कीजिये. (आप बाद मे Jetpack WordPress plugin activate करने के बाद इस plugin को बंद कर सकते हैं).
Advanced Options:
Advanced Options पर click कीजिये और नीचे दिखाई गयी image कि तरह settings configure कीजिये. ध्यान रखें कि आपने last option “Email installation details to” में एक email address enter किया हो क्योंकि इसमें आपको installation complete होने के बाद की information आएगी. यह information बाद में helpful होगी और या फिर आपको किसी developer को WordPress में changes करने के लिए भी इन details कि जरूरत पड़ेगी.
Install पर click कीजिये और यह आपके WordPress blog कि installation complete करने के लिए लगभग एक minute लेगा.]
अपनी email check कीजिये क्योंकि आप अपने email में WordPress installations steps check करेंगे. यह एक video tutorial है (English Main):
अपने WordPress dashboard में login कीजिये, और ये कुछ ऐसा है जैसा कि आपका WordPress dashboard दिखेगा.
यहाँ पर कुछ quick changes दियें गएँ है जो आपको अपने WordPress blog के साथ blogging शुरू करने से पहले या कुछ भी और करने से पहले करने पड़ेंगे.
- Hello world post delete कीजिये.
- Pages में से sample pages delete कीजिये.
- Settings > Permalink में जाकर permalink structure को as name select कीजिये.
- Yoast SEO plugin use कीजिये.
- WP Super cache plugin install कीजिये.
- Akismet plugin install और configure कीजिये.
अगर आपने वॉर्डप्रेसस नही install करा हैं तो इस tutorial को follow करें और 10 मिनिट मैं उसे install करें. यदि आपके पास कोई प्रश्न हैं तो आप मुझसे comment द्वारा पूछ सकते हैं. और अगर आपको यह tutorial पसंद आया हो तो अपने दोस्तों के साथ share करे.
- अपने Blog के लिए अगले 5 minutes में Hosting कैसे खरीदें?
- Domain को Hostgator India की Hosting पर कैसे point करें ?
अब आप हमारे पोस्ट्स सीधे अपने मोबाइल से उपयोग कर सकते हैं. तो फिर देर किस बात की, अभी Play Store से Download कीजिये: ShoutMeHindi Android App.
COMMENTs ( 6 )
Ankit Banger says
Hello Harsh shout me hindi me ye niche ads kaise dikhai deti h hmari website me toh aisa nhi hota
vijay rana says
Hi harsh mujhe aapse ek swaal puchna h. Mera ek hindi blog h. Main manta hu ki keywords ko apni blog post me add karne par uski search ranking badti h, lekin main apne hindi blog me english keyword kaise add kar sakta hu kyonki log to english me search karte h. Please harsh solve my problem…
deepesh says
hello sir hostgator par wordpress instaal karne ke baad wordpress par login kaise kare
jo link aapne video me dikhaya hai uspar clk karne par godaddy acount login aa raha hai please help me
Gurmeet Singh says
We are soon having a Video Tutorial in Hindi for it. 🙂
Mahendra says
Hello sir godaddy ke SSL ko HostGator par keise setup karte hain
हर्ष अग्रवाल says
hello mahendra,
assuming ki aapka hostgator par shared hosting hain, aap SSL khud nahi install kar sakte. aapke pass root server access hona chahiye. aap hostgator customer care ko contact kare aur unko bole SSL install karne ke liye. Wo zaroor kar denge.
'''

textcleaner = TextCleaner(config)

cleaned_text = textcleaner.run(txt)
print(cleaned_text)
