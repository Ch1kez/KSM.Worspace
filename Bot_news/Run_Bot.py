import asyncio
from AgricultureCom import main_AgricultureCom
from InterfaxRu import main_InterfaxRu
from IzRu import main_IzRu
from OilWorldRu import main_OilWorldRu
from RbkRu import main_RbkRu
from RgRu import main_RgRu
from RiaRu import main_RiaRu
from SpGlobalCom import main_SpGlobalCom
from ZernoRu import main_ZernoRu
from ZolRu import main_ZolRu
from PrimeRu import main_PrimeRu
from VedomostiRu import main_VedomostiRu
# from GazetaRu import main_GazetaRu
# from ForbesRu import main_ForbesRu
# from KommersantRu import main_KommersantRu          # То что в комментах - не работает
# from TassRu import main_TassRu                        # Проблемы со структурой данных
# from LentaRu import main_LentaRu                         # Нужно переписать под новую структуру и разделы сайта
# from NasdaqCom import main_NasdaqCom

    
async def check_news_update():
    print('kek')
    while True:
        try:
            # main_InterfaxRu()
            # main_IzRu()
            main_OilWorldRu()
            main_RbkRu()
            main_RgRu()
            main_SpGlobalCom()
            main_ZernoRu()
            main_ZolRu()
            main_PrimeRu()
            main_VedomostiRu()
            main_AgricultureCom()  # Нужна ли херня на английском?
            main_RiaRu()  # Попадаются одинаковые новости - исправить
            # main_LentaRu()
            # main_NasdaqCom()
            # main_ForbesRu()                       # То что в комментах - не работает
            # main_KommersantRu()
            # main_TassRu() # Кусок говна
            # main_GazetaRu()
            print('##################################################################################################')
            print('__________________________________________________________________')
            await asyncio.sleep(60)
        except Exception:
            print(Exception)
            continue



if __name__ == '__main__':
    asyncio.run(check_news_update())
