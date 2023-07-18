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


