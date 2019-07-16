import pandas ad pd

entrepreneurs_dict = {'Варбанець Є.Р. ФОП': 26009054357407, 'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': 26003054348616, 'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': 26007054340085, 'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': 26009054358622, 'ЧОС М.В. ФОП': 26007054353395, 'Яковчук А.А. ФОП': 26004054347876}
entrepreneurs=pd.Series(entrepreneurs_dict)

id_priv_dict = {'Варбанець Є.Р. ФОП': '3a574ecf-a938-47fd-8034-bd9901aa85d6', 'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': 'f5886524-377a-42d1-9fa2-a5ced0de1d9c', 'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': '68acdf17-321a-4585-8bc7-be7de2fcb163', 'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': '0e80d3f5-fe09-4445-aa2d-06037cc41465', 'ЧОС М.В. ФОП': 'bccbaa87-adc3-489d-9420-b92747154471', 'Яковчук А.А. ФОП': '20edd1d5-3b9f-4492-9807-b3c5d8146e57'}
id_priv=pd.Series(id_priv_dict)

token_priv_dict = {'Варбанець Є.Р. ФОП': 'bT8WLCvBKMXAQFVoKyg3etRGMZ7P9pfqUsN6bGpNj6FeJt9LMP9OC3KXp/VRsldL+AKIENu6MatRnTMo0K2kGYY/hAWbZv+XlaKStCENu/3KvMzs4t0cwUdV8nZca250C6VLztndzF/u+2ZA0YVSnSssyvHgpQtxDTx8vQX0bDTmGGjjXvvPrMHlkqaI6xzNAtG+bNOijFKRHeY6mVThIt5L86hlwIFATqYAsmjSLPoyXW2cIi+iOS43sNX9oUSp0g==', 
'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': '23oaUCA/NIrAil3/X7u2do6v/KDxK2oFHsU0yBBPZf0Nlw143RdSp2p/jNmVksu4F9zigKFK5JLpMHiJINsCie2g2i3IcaDPmfU5iA1KGddSsygey6Lh/1lpTgDB4VhWuN0rPNNYDXf7yvH34ZGkA50Oi88dcU2vgNxdotp34KwqUsiR6pDYsp0a8vUt4p1oQr2mdCz5NXHPW1pnaTB2k/K4sE51fySHb7wSFNwxLcd8nwL80Fjtvf65C4XFuNM=', 
'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': 'NP72msmkmglCvEdmm7iSZPCof1OgGcd/53DEPiLyHhMGZcDF0oYS7CJNwEXlW/ZA/Mh63VNQysp49drqlv1vUnhMPEwp3zYNmPep9o+GfnJrg/ZH/vB3Z/MSonqxd+QOBfaNyqS1IATcrSpJtmN0L4XuAFQ1R1gRBJK1uaX1VDKXxGK2S2vWPdmbFnPFXNbrcu3oll1+f5j8zoyVAXAlQVzfAKKiwHAnJx2JcC5RIW2yWmv4a/tXIJYMZOpEFtQ=', 
'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': '4wglXzCEVbHjndC6jAPfI3zdYfkKNeso4k3dvSDtYp6INyb0vOKODVFeQgoWdfK2WuHGOBag3HbmW/Yo5pUhEueMA2xPCku84echQUOZ8WYhyLJAv3b+UTwaKM23c2gq1r7Z7cWIj70Yq1QakoVydWE8n3M2OuKtXPNwWVk41MxJdNBfcVgWInFfyPLS1hBAayG3YLqZvm9ybmjC7hz4KtFgl8ZKCzAGkY4iVmDnYN80JDoSEk+GbtfzD6217XyFwA==', 
'ЧОС М.В. ФОП': 'AGkeljWgYJ+9YSTFY0pbwkmxbmBigCJnjPEITKnJwEtnA46YnT2vPqzSTPtNXr2jp2byvv23F9T7kzzR03dHfCnZ5ShNPVYt9owX1eVMuC6Y0rNx81FgUm75MTphiycsbXcHkzJVXFe2kURf0lh08DOwMHkmPPZbInbRXXSNmt3ZcbxEiyr+oXsAyeptFtJJy8QDzYgMVyWpq7TTcCVlz26rG9y4HMN0aowMptCx+qZgO65bxclFozcwdEIFKlkqaQ==',
'Яковчук А.А. ФОП': 'bAw8Ng6RujV1wnpjSFzaiJl/2nm2yG94Zz8YdANno7fvJyLdtKMNf3Hv7nNvYsx67p9l5xSyfX6aq4YQVmq6JS+TLKogaQ+QAP4IUu2KLbBOXsWKyCq5KahRf9KmuN6kdgehGAHVUBKq6SmkqQs6RMV2DCOtSa5luQashjz8dvBSPj/RlUzTLw+58qzcAdhNRClfb4mURKhBlEBdckSLeCknFAt10Rue8KO5wbR3B7Ma9X/LW1o3ASHoSq7EyzY='}
token_priv = pd.Series(token_priv_dict)

data = pd.DataFrame({'acc':entrepreneurs, 'id': id_priv, 'token': token_priv})

