
'''
https://www.qa-practice.com/elements/input/simple

Search by class: .tab.active

Search by id: #id_text_string

Search by attribute:
[for]
[type='hidden']
[type*='idde']
[type^='hidde']
[type$='idden']
[class|="form"] - class name begins with 'form-...'
[class~="requiredField"] - to find one of class attributes. Ex: class="form-label requiredField". Simple ex: contains

Search by nested elements:
#div_id_text_string input - find element in div
form[method="post"] label
form[method="post"] > input - ">" search just inside current element (form)
form[method="post"] ~ a - find element 'a' next to <form method="post"> on the same level
form[method="post"] + a - find first element 'a' next to <form method="post"> on the same level
'''