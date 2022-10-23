from transformers import pipeline

qa = pipeline("question-answering", model="mrm8488/bert-multi-cased-finetuned-xquadv1",
              tokenizer="mrm8488/bert-multi-cased-finetuned-xquadv1")
context = """2010年，黄晓明离开华谊兄弟文化经纪公司与经纪人共同创办个人工作室。
黄晓明开始担任起影视投资人及出品人。[4]2012年，黄晓明个人蜡像进驻香港杜莎夫人蜡像馆。
2013年，黄晓明回归电视剧，主演《精忠岳飞》。2014年5月，黄晓明获评为第20届山东省十大杰出青年之一。
[5]福布斯发布2014年中国名人榜，黄晓明综合排名第四。
在历史的福布斯中国名人榜上，直至2015年福布斯中国名人榜停办之前，他已连续十年登榜福布斯中国名人榜，其中七次位居中国小生之首，是中国最具商业价值的男星之一。
[6]黄晓明亦深受各大时尚圈青睐，身兼多个知名国际品牌代言人身份。
除片约不断外，黄晓明也投资生意，包括饭店餐厅、红酒、高尔夫球场、医院等；积极参与慈善，
更曾任联合国儿童基金会形象大使、中国儿童少年基金会形象大使、中国保护大熊猫研究中心爱心大使。
据《每日经济新闻》报道，黄晓明名下拥有48家公司，其中投资类公司有14家[7]。"""
question = "黄晓明是哪年被评为山东省十大杰出青年之一？"
result = qa(question=question, context=context)
print("Answer:", result['answer'])
print("Score:", result['score'])