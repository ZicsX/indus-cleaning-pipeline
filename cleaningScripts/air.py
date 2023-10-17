from indusnlp.cleaner import TextCleaner


config = [
("remove_line_with_pattern", [r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-3]?[0-9], \d{4} ,\s+([1-9]|1[0-2]):[0-5][0-9](AM|PM)"]),
("remove_line_with_pattern", [r"@\w+"]),
("remove_line_with_pattern", [r"(?i)^.*\b(pic|air|tweeted|logo)\b.*\n?"]),
("remove_line_and_below", ["Next Article"]),
("remove_line_with_keyword",["newsonair"],),
("handle_whitespace", None),
("remove_single_word_lines", None),
("remove_redundant_lines", None),
("remove_blank_lines", None),
]


txt = '''
Jun 27, 2019 ,  8:51PM 
                 
                 प्रधानमंत्री नरेन्‍द्र मोदी ने कहा कि अगले पांच वर्षों में भारत की अर्थव्यवस्था पचास खरब डॉलर होने पर जापान के साथ संबंध और सुदृढ़ होंगे। 
                
                FILE PIC: PTI 
                Pic tweeted by AIR 
                AIR PIC 
                AIR
                TWEETED BY
                newsonair
                 
                 @MEAIndia asdasd
                 
              
                प्रधानमंत्री नरेन्‍द्र मोदी ने आज सुबह जापान के ओसाका शहर में आयोजित होने वाले 20 देशों के समूह के शिखर सम्‍मेलन से पहले जापान के प्रधानमंत्री शिंजो आबे के साथ बातचीत की। चर्चा के दौरान प्रधानमंत्री ने भारतीय शिष्‍टमंडल के सभी सदस्‍यों का गर्मजोशी से स्‍वागत करने के लिए शिंजो आबे और जापान सरकार के प्रति आभार व्‍यक्‍त किया। 
  
 नरेन्‍द्र मोदी ने कहा कि आबे उनके पहले मित्र हैं जिन्‍होंने हाल के लोकसभा चुनाव में पार्टी की जीत के लिए उन्‍हें शुभकामनाएं दी।  
  
 बाद में संवाददाताओं से बातचीत में विदेश सचिव विजय गोखले ने कहा कि भारत और जापान दोनों देशों के बीच नीतिगत संबंधों का विस्‍तार करने को सहमत हुए हैं। उन्‍होंने कहा कि दोनों नेताओं ने भारत-जापान संबंधों के विभिन्‍न पहलुओं पर चर्चा की।  
  
 गोखले ने बताया कि प्रधानमंत्री ने कहा है कि वे इस साल भारत में होने वाले दोनों देशों के वार्षिक शिखर सम्‍मेलन के सिलसिले में शिंजो आबे की भारत यात्रा की उत्‍सुकता से प्रतीक्षा कर रहे हैं।
'''

textcleaner = TextCleaner(config)

cleaned_text = textcleaner.run(txt)
print(cleaned_text)
