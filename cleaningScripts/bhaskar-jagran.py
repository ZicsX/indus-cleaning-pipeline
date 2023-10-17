from indusnlp.cleaner import TextCleaner


config = [
("remove_line_with_pattern", [r"^- .*"]),
("remove_line_with_keyword",["यह भी पढ़ें"],),
("handle_whitespace", None),
("remove_single_word_lines", None),
("remove_redundant_lines", None),
("remove_blank_lines", None),
]

txt = '''
- Hindi News
- Kundalpur panchkalyanak
- World's Largest Jain Temple, 189 Feet High On A 500 Feet High Hill, Has Been Carved On The Lines Of Delwara And Khajuraho On Stones
कुण्डलपुर में बन रहा सबसे बड़ा जैन मंदिर:कारीगरी ऐसी कि देखने वाले देखते रह जाएं, 500 फीट ऊंची पहाड़ी पर 189 फीट ऊंचा मंदिर
- कॉपी लिंक
कुण्डलपुर धाम के धार्मिक महत्व को देखते हुए यहां विश्व का सबसे ऊंचा जैन मंदिर बन रहा है। जो अपनी दिव्यता और भव्यता के चलते अभी से लाखों भक्तों की श्रद्धा का केंद्र बनता जा रहा है। 500 फीट ऊंची पहाड़ी पर निर्मित 189 फीट ऊंचे इस जैन मंदिर के निर्माण पर लगभग 600 करोड़ रुपए खर्च होने हैं। जिसमें से करीब 400 करोड़ रुपए अबतक खर्च भी हो चुके हैं। पत्थरों से बने इस मंदिर पर दिलवाड़ा और खजुराहो की तर्ज पर शानदार नक्काशी की गई है।
कुण्डलपुर के इस भव्य जैन मंदिर का कार्य पिछले 16 वर्षों से जारी है। इस मंदिर में 12 लाख घन मीटर पत्थरों का उपयोग किया जा चुका है। इन पत्थरों को सीमेंट और लोहे का इस्तेमाल किए बिना जोड़ा गया है। राजस्थान के तीन प्रकार के पत्थरों से नागर शैली में बड़े बाबा भगवान आदिनाथ के मंदिर का निर्माण किया गया है। इस मंदिर में मुख्य शिखर, गुड मंडप, नृत्य मंडप, रंग मंडप सहित अनेक प्रकार के भव्य स्थल का निर्माण हुआ है।
पत्थरों पर भी उकेरी गई हैं प्रतिमाएं
जैसलमेर के मूल सागर पत्थरों से बनाए गए गुण मंडप में देवी-देवताओं व नृत्यांगना आदि की मूर्तियों को बड़े ही गजब तरीके से उकेरा गया है। इस नक्काशी को देखने वाले भी लोग कारीगरों की प्रशंसा करने से खुद को रोक नहीं पाते हैं। मंदिर निर्माण में लगे सभी पत्थरों पर शानदार नक्काशी इसकी सुंदरता और भव्यता को और बढ़ाती हैं। प्रतिदिन यहां हजारों की संख्या में लोग इस दिव्य मंदिर के दर्शन करने पहुंच रहे हैं।
कल से शुरू हो रहा पंच कल्याणक महामहोत्सव
प्रसिद्ध जैन तीर्थ स्थल कुण्डलपुर में अनौपचारिक रूप से तो पंचकल्याणक महोत्सव का शुभारंभ हो चुका है। लेकिन मुख्य समारोह 16 फरवरी से शुरू होगा। पंचकल्याणक महामहोत्सव के लिए देश-विदेश से मेहमानों के आने की संभावना जताई जा रही हैं। विदेशों से भी पंचकल्याणक में शामिल होने प्रतिमाएं पहुंच रही हैं। इन प्रतिमाओं की यहां पर प्राण प्रतिष्ठा की जाएगी इसके बाद उन प्रतिमाओं को संबंधित देशों में ले जाकर स्थापित किया जाएगा।
दो हजार साल बाद इतना दिव्य आयोजन
कुण्डलपुर सिद्धक्षेत्र समिति के मुताबिक दो हजार सालों के बाद इतना बड़ा पंच कल्याणक हो रहा है। इस महामहोत्सव में आचार्य विद्यासागरजी महाराज के साथ उनके सभी 200 से अधिक जैनमुनि शिष्य और 250 से अधिक माताएं (आर्यिकाएं) शामिल हो रही हैं। यही कारण है कि यहां देश और विदेशों से मुख्य प्रतिमाएं प्राण प्रतिष्ठा के लिए पहुंची हैं। प्रतिमाओं की प्राण प्रतिष्ठा आचार्यश्री और मुनि संघ द्वारा सूर्य मंत्र के साथ की जाएगी। इसमें करीब 11 सौ प्रतिमाएं कुण्डलपुर मंदिर में और लगभग 400 प्रतिमाएं घरों एवं देश-विदेश के अन्य जैन मंदिरों में स्थापित होंगी।
16 फरवरी से 23 फरवरी तक ये होंगे कार्यक्रम
16 व 17 फरवरी को गर्भ कल्याणक, 18 फरवरी को जन्म कल्याणक, 19 व 20 फरवरी को तप कल्याणक, 21 व 22 फरवरी को ज्ञान कल्याणक और 23 फरवरी को मोक्ष कल्याणक के साथ गजरथ फेरी होगी। इसके बाद 24 फरवरी से महामस्तकाभिषेक प्रारंभ होगा, जो अगले एक महीने तक चलता रहेगा। विश्व में अब तक हुए तमाम पंचकल्याणकों से ये अलग है। अभी तक पंचकल्याणक में केवल एक इंद्र, एक सौधर्म इंद्र-इंद्राणी तथा 1-1 माता-पिता बनते हैं। जबकि इस आयोजन में 24 तीर्थंकरों के लिए 24-24 इंद्र-इंद्राणी तथा उन सभी के 1-1 माता-पिता बनाए गए हैं।
मंदिर के सामने सहस्त्रकूट में 1008 मूर्तियां स्थापित होंगी
बड़े बाबा मंदिर और मूर्ति व्यवस्था के प्रभारी राजेश जैन के मुताबिक मुख्य मंदिर के सामने सहस्त्रकूट में 1008 मूर्तियां स्थापित होगी। ये 21 से 27 इंच की हैं। इसी तरह त्रिकाल चौबीसी, वर्तमान चौबीसी, पूर्व चौबीसी और भविष्य चौबीसी में मूर्ति स्थापित हो रही है। पंच बालयति की 5-5 प्रतिमाएं स्थापित हो रही है। ये 45 और 26 इंच की पद्मासन मुद्रा में हैं। इसी प्रकार 724 प्रतिमाएं पद्मासन की 15 इंच की, 220 प्रतिमाएं खड्गासन में 25 इंच की, 12 प्रतिमाएं खड्गासन में 39 इंच की स्थापित हो रही है।
बड़े बाबा के भव्य मंदिर की झलकियां
कुण्डलपुर महामहोत्सव को लेकर नियमित खबरें और वीडियो के लिए दैनिक भास्कर ऐप पर राज्य-शहर में जाकर 'कुण्डलपुर' सिलेक्ट करें।
MP में 4.49 लाख लोगों को हाइपरटेंशन: गांवों में भी बढ़ रहे हाई बीपी और शुगर जैसी बीमारियों के मरीज, 92% मरीजों का चल रहा इलाज
शेयर
- कॉपी लिंक
MP में मिशन 2023 के लिए दलित वोटरों पर फोकस: संत रविदास जयंती पर BJP सत्ता-संगठन के साथ पंचायत स्तर तक झोंक रही ताकत; कल से कार्यक्रम
शेयर
- कॉपी लिंक
MP बोर्ड 10वीं में मैथ्स की तैयारी का मंत्र: ज्यादा नंबर के प्रश्न पहले करें; प्रश्नों को बार-बार पढ़ें; दो पार्ट के आंसर आपस में न मिलाएं
शेयर
- कॉपी लिंक
MP का स्टूडेंट यूक्रेन में फंसा: रीवा के प्रज्जवल तिवारी मेडिकल यूनिवर्सिटी से कर रहे MBBS; बोले- कल क्या होगा, नहीं पता
शेयर
- कॉपी लिंक
'''

textcleaner = TextCleaner(config)

cleaned_text = textcleaner.run(txt)
print(cleaned_text)
