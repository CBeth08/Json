import ujson

#conf={'a list': [1, 42, 3.141, 1337, 'help', u'€'],
 #     'a string': 'bla',
  #    'another dict': {'foo': 'bar','key': 'value','the answer': 42}
   #   }

# Al principio, se inicializa un diccionario vacío llamado conf.
#Luego, se agrega una clave "ssid" con un valor que es otro diccionario: {"foo": "bar"}.
#Además, se agrega una clave "pass" con el valor de la cadena "esp1"
conf={}                        
conf["ssid"]={"foo":"bar"}
conf["pass"]="esp1"
# Después de crear el diccionario, se imprime su contenido en la consola utilizando print(conf).
print(conf)
#Finalmente, el diccionario conf se guarda en un archivo llamado “conf.json” utilizando la biblioteca ujson.
with open('conf.json', 'w') as outfile:
    ujson.dump(conf, outfile)