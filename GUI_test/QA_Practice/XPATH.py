"""
Поиск по содержимому атрибута

//li[@class="tab active"]
//*[@class="tab active"] - можно пропускать название аттрибута
//*[@type="hidden"]
//li[@class="tab"][1] - Если несколько элементов. указываем номер элемента [1]
//li[@class="tab"][2] - Если несколько элементов. указываем номер элемента [2]
//li[contains(@class, "tab")][3]
//*[text()="Simple button"] - поиск по тексту

//*[contains(text(), "Simple button")] - поиск по частичному совпадению текста
//li[contains(@class, "tab")]
//label[@class="form-check-label"]
//label[@class="form-check-label" and contains(text(), "One")] - поиск по частичному совпадению с ипользованием "and"
//a[starts-with(text(), "Check")] - поиск по началному фрагменту текста

//label[@class=" form-label"]/following::footer - поиск соседних элементов вниз
//label[@class=" form-label"]/following::input[@value="one"]

//*[@id="div_id_checkboxes"]/child::label - поиск внутри дочернего элемента (только первыая ступень вложенности)
//*[@id="div_id_checkboxes"]/descendant::label - поиск вниз по вложенности (по всем уровням вложенности элементов)
//*[@id="div_id_checkboxes"]/following-sibling::input - поиск "близнеца", т.е. соседа, который находится  на том же уровне
//*[@id="id_checkboxes_0"]/following-sibling::label

//*[@class=" form-label"]/ancestor::div - поиск вверх (поиск предков)
//*[@class=" form-label"]/ancestor::div[1] - можно перемещаться по div с помощью индексов, чтобы выбирать уровень предка
//*[@class=" form-label"]/parent::* - поиск ближайшего предка
//*[@class=" form-label"]/preceding::*[@data-scrollbar="true"] - поиск предшествующего элемента
//div[@class="form-check form-check-inline"]/parent::* - поиск элемента изнутри
//div[@class="form-check form-check-inline"][1]/parent::*- поиск элемента изнутри через первый (может быть любой существующий индекс) вложенный элемент











"""
