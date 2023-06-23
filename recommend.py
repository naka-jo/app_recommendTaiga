class Recommend:
    def __init__(self):
        self.kimi = 0 # 光る君へ
        self.kiyo = 0 # 平清盛
        self.dono = 0 # 鎌倉殿の13人
        self.kirin = 0 # 麒麟がくる
        self.tora = 0 # おんな城主直虎
        self.maru = 0 # 真田丸
        self.ie = 0 # どうする家康
        self.bera = 0 # べらぼう
        self.ryoma = 0 # 龍馬伝
        self.kumi = 0 # 新選組!
        self.tuke = 0 # 青天を衝け
        self.idaten = 0 # いだてん

    def era_choice(self, answer11, answer12):
        '''
        平安, 平安末期〜鎌倉前期, 戦国,
        江戸中期, 幕末〜明治, 大正〜昭和
        強くこだわる, ややこだわる, こだわらない
        '''
        if answer11 == '強くこだわる':
            if answer12 == '平安':
                self.kimi += 5
            if answer12 == '平安末期〜鎌倉前期':
                self.kiyo += 5
                self.dono += 5
            if answer12 == '戦国':
                self.kirin += 5
                self.tora += 5
                self.maru += 5
                self.ie += 5
            if answer12 == '江戸中期':
                self.bera += 5
            if answer12 == '幕末〜明治':
                self.ryoma += 5
                self.kumi += 5
                self.tuke += 5
            if answer12 == '大正〜昭和':
                self.idaten += 5
        elif answer11 == 'ややこだわる':
            if answer12 == '平安':
                self.kimi += 2
            if answer12 == '平安末期〜鎌倉前期':
                self.kiyo += 2
                self.dono += 2
            if answer12 == '戦国':
                self.kirin += 2
                self.tora += 2
                self.maru += 2
                self.ie += 2
            if answer12 == '江戸中期':
                self.bera += 2
            if answer12 == '幕末〜明治':
                self.ryoma += 2
                self.kumi += 2
                self.tuke += 2
            if answer12 == '大正〜昭和':
                self.idaten += 2
        else:
            pass
    
    def acter1_choice(self, a):
        '''
        吉高由里子、柄本佑、松山ケンイチ、深田恭子、玉木宏: 
        小栗旬、小池栄子、坂口健太郎、大泉洋、中川大志、山本耕史
        長谷川博己、染谷将太、川口春奈、柴咲コウ、高橋一生
        堺雅人、草刈正雄、長澤まさみ、松本潤、有村架純、山田裕貴
        横浜流星、福山雅治、香取慎吾、吉沢亮、草彅剛
        六代目中村勘九郎、阿部サダヲ、役所広司
        '''
        if a in ['吉高由里子', '柄本佑']:
            self.kimi += 5
        if a in ['松山ケンイチ', '深田恭子', '玉木宏']:
            self.kiyo += 5
        if a in ['小栗旬', '小池栄子', '坂口健太郎', '大泉洋', '中川大志', '山本耕史']:
            self.dono += 5
        if a in ['長谷川博己', '染谷将太', '川口春奈']:
            self.kirin += 5
        if a in ['柴咲コウ', '高橋一生']:
            self.tora += 5
        if a in ['堺雅人', '草刈正雄', '長澤まさみ', '大泉洋']:
            self.maru += 5
        if a in ['松本潤', '有村架純', '山田裕貴']:
            self.ie += 5
        if a in ['横浜流星']:
            self.bera += 5
        if a in ['福山雅治']:
            self.ryoma += 5
        if a in ['香取慎吾', '山本耕史']:
            self.kumi += 5
        if a in ['吉沢亮', '草薙剛']:
            self.tuke += 5
        if a in ['六代目中村勘九郎', '阿部サダヲ', '役所広司']:
            self.idaten += 5

    def acter2_choice(self, a):
        '''
        吉高由里子、柄本佑、松山ケンイチ、深田恭子、玉木宏: 
        小栗旬、小池栄子、坂口健太郎、大泉洋、中川大志、山本耕史
        長谷川博己、染谷将太、川口春奈、柴咲コウ、高橋一生
        堺雅人、草刈正雄、長澤まさみ、松本潤、有村架純、山田裕貴
        横浜流星、福山雅治、香取慎吾、吉沢亮、草彅剛
        六代目中村勘九郎、阿部サダヲ、役所広司
        '''
        if a in ['吉高由里子', '柄本佑']:
            self.kimi += 3
        if a in ['松山ケンイチ', '深田恭子', '玉木宏']:
            self.kiyo += 3
        if a in ['小栗旬', '小池栄子', '坂口健太郎', '大泉洋', '中川大志', '山本耕史']:
            self.dono += 3
        if a in ['長谷川博己', '染谷将太', '川口春奈']:
            self.kirin += 3
        if a in ['柴咲コウ', '高橋一生']:
            self.tora += 3
        if a in ['堺雅人', '草刈正雄', '長澤まさみ', '大泉洋']:
            self.maru += 3
        if a in ['松本潤', '有村架純', '山田裕貴']:
            self.ie += 3
        if a in ['横浜流星']:
            self.bera += 3
        if a in ['福山雅治']:
            self.ryoma += 3
        if a in ['香取慎吾', '山本耕史']:
            self.kumi += 3
        if a in ['吉沢亮', '草薙剛']:
            self.tuke += 3
        if a in ['六代目中村勘九郎', '阿部サダヲ', '役所広司']:
            self.idaten += 3
            
    def acter3_choice(self, a):
        '''
        吉高由里子、柄本佑、松山ケンイチ、深田恭子、玉木宏: 
        小栗旬、小池栄子、坂口健太郎、大泉洋、中川大志、山本耕史
        長谷川博己、染谷将太、川口春奈、柴咲コウ、高橋一生
        堺雅人、草刈正雄、長澤まさみ、松本潤、有村架純、山田裕貴
        横浜流星、福山雅治、香取慎吾、吉沢亮、草彅剛
        六代目中村勘九郎、阿部サダヲ、役所広司
        '''
        if a in ['吉高由里子', '柄本佑']:
            self.kimi += 1
        if a in ['松山ケンイチ', '深田恭子', '玉木宏']:
            self.kiyo += 1
        if a in ['小栗旬', '小池栄子', '坂口健太郎', '大泉洋', '中川大志', '山本耕史']:
            self.dono += 1
        if a in ['長谷川博己', '染谷将太', '川口春奈']:
            self.kirin += 1
        if a in ['柴咲コウ', '高橋一生']:
            self.tora += 1
        if a in ['堺雅人', '草刈正雄', '長澤まさみ', '大泉洋']:
            self.maru += 1
        if a in ['松本潤', '有村架純', '山田裕貴']:
            self.ie += 1
        if a in ['横浜流星']:
            self.bera += 1
        if a in ['福山雅治']:
            self.ryoma += 1
        if a in ['香取慎吾', '山本耕史']:
            self.kumi += 1
        if a in ['吉沢亮', '草薙剛']:
            self.tuke += 1
        if a in ['六代目中村勘九郎', '阿部サダヲ', '役所広司']:
            self.idaten += 1
            
    def writer_choice(self, a):
        '''
        大石静, 藤本有紀, 三谷幸喜, 森下佳子, 宮藤官九郎,
        池端俊策, 大森美香, 古沢良太, いない
        '''
        if a == '大石静':
            self.kimi += 5
        elif a == '藤本有紀':
            self.kiyo += 5
        elif a == '三谷幸喜':
            self.dono += 5
            self.maru += 5
            self.kumi += 5
        elif a == '森下佳子':
            self.tora += 5
            self.bera += 5
        elif a == '宮藤官九郎':
            self.idaten += 5
        elif a == '池端俊策':
            self.kimi += 5
        elif a == '大森美香':
            self.tuke += 5
        elif a == '古沢良太':
            self.ie += 5
            
    def result(self):
        point = {'光る君へ': self.kimi, '平清盛': self.kiyo, '鎌倉殿の13人': self.dono,
                '麒麟がくる': self.kirin, 'おんな城主直虎': self.tora, 'どうする家康': self.ie,
                '真田丸': self.maru, 'べらぼう': self.bera, '龍馬伝': self.ryoma, '新選組!': self.kumi,
                '青天を衝け': self.tuke, 'いだてん': self.idaten}
        point_sorted = sorted(point.items(), key = lambda x:x[1], reverse = True)
        final_result = [point_sorted[i][0] for i in range(len(point_sorted))]
        return final_result

# recommend = Recommend()

# a_11 = int(input('時代にこだわりますか？'))
# if a_11 != 2:
#     a_12 = int(input('好きな時代を選んでください'))
#     recommend.era_choice(a_11, a_12)
# a_21 = int(input('この中で1番好きな俳優を選んでください'))
# a_22 = int(input('この中で2番好きな俳優を選んでください'))
# a_23 = int(input('この中で3番好きな俳優を選んでください'))
# recommend.acter1_choice(a_21)
# recommend.acter2_choice(a_22)
# recommend.acter3_choice(a_23)
# a_31 = int(input('この中で好きな脚本家を選んでください'))
# recommend.writer_choice(a_31)
# final_result = recommend.result()
# print(final_result)
