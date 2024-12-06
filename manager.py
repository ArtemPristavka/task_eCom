from sqlalchemy.orm import Session
from sqlalchemy import select

from typing import Dict, List, Optional

from models import Template
from engine_db import engine

import json
import re


class Manager:
    """
    Менеджер проверяет входные данные с набором шаблонов из бд,
    и возвращает имя шаблона если таковой есть
    """
    
    def __init__(self, input_data: Dict[str, str]) -> None:
        """
        Вставляем тело запроса для обработки в будущем

        Args:
            input_data (Dict[str, str]): Тело запроса
        """
        
        self.input_data = input_data
        self.all_template = self.get_templates()
        
    def get_templates(self) -> List[Template]:
        """
        Берем все шаблоны из Бд

        Returns:
            List[Template]: Список шаблонов
        """
        
        session = Session(engine)
        stmt = select(Template)
        response = session.scalars(stmt)
        
        return response # type: ignore
    
    def loads_from_json(self, data: str) -> Dict[str, str]:
        """
        Десериалиуем данные шаблоны из бд.

        Args:
            data (str): _description_

        Returns:
            Dict[str, str]: Десерилизованные данные
        """
        
        ready_data = json.loads(data)
        
        return ready_data
    
    def search_template(self) -> Optional[str]:
        """
        Поиск подходячего шаблона

        Returns:
            Optional[str]: None - если шаблон не найден,
                Строка - имя шаблона 
        """
        
        for i_elem in self.all_template:
            template = self.loads_from_json(i_elem.template)

            for i_key, i_val in template.items():
                field = self.input_data.get(i_key)
                
                if field is None:
                    break
                
                if not self.check_fields(i_val, field):
                    break
            
            else:
                return i_elem.name
        
        return None
                
    def check_fields(self, field_form: str, field_input_data: str) -> bool: # type: ignore
        """
        Проверка и валадация полей заданных в шаблоне во входящих данных 

        Args:
            field_form (str): Поле из шаблона формы
            field_input_data (str): Поле из входных данных

        Returns:
            bool: True - если есть и тип данных совпадает,
                Fasle - если тип данных не совпадает
        """
        
        match field_form: # type: ignore
            case "str":
                return isinstance(field_input_data, str) # type: ignore
            
            case "phone":
                if re.search(r'(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}', field_input_data):
                    return True
                
                return False
                
            case "date":
                if len(field_input_data) == 10:
                    
                    if re.search(r"\d{2}\.\d{2}\.\d{4}", field_input_data):
                        return True
                    elif re.search(r"\d{4}-\d{2}-\d{2}", field_input_data):
                        return True

                    return False
                    
                else:
                    return False
                
            case "email":
                if "@" in field_input_data:
                    return True

                return False
