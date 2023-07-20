# hello-flask

```shell
pip install Flask
```

## Quick Start

```shell
# hello.py
flask --app main run
# app.py or wsgi.py
flask run
# listen to public network
flask run --host=0.0.0.0
# enable debug mode
flask run --debug
```

### Variable Rules

```url
/path/<variable_name>
/path/<int:post_id>
/path/<path:subpath>
```

|Type|Description|
|----|-----------|
|`string`|(default)accepts any text without slash|
|`int`|accepts positive integers|
|`float`|accepts positive floating point values|
|`path`|like string but also accepts slashes|
|`uuid`|accepts UUID strings|

### Static Files

`static`目录默认通过`/static`可被访问到

### Rendering Templates

Flask会在`templates`目录下匹配模板文件

### About Response

如果是string，则以text/html格式返回该string，状态码为200 OK
如果是dict/list，则以用jsonify()返回，即json格式返回

- 如果是response对象，则直接返回
- 如果是string，则用这个string构建一个response对象，绑定默认的参数
- 如果是iterator/generator返回string/bytes，将被认为是一个流
- 如果是dict/list，则调用jsonify()的返回值构建response对象来返回
- 如果是tuple，则按照如下方式解析：
  - (response, status)
  - (response, headers)
  - (response, status, headers)
  - headers可以是list/dict
- If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a response object.


